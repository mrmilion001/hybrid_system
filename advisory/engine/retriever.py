from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from advisory.models import PolicyClause


def retrieve_policy_clauses(query, domain=None, top_k=1, threshold=0.1):
    """
    Retrieve the most relevant policy clauses for a query
    within the specified regulatory domain. Falls back to global
    search if domain-specific search yields nothing.
    """
    clauses = []
    if domain:
        clauses = list(PolicyClause.objects.filter(domain=domain, active=True))
    
    # Global fallback if domain yields nothing
    if not clauses:
        clauses = list(PolicyClause.objects.filter(active=True))

    if not clauses:
        return []

    clause_list = clauses

    documents = []
    for clause in clause_list:
        # Safely handle JSON keywords whether stored as a list or string
        keywords_raw = clause.keywords
        if isinstance(keywords_raw, list):
            kw_str = " ".join(str(k) for k in keywords_raw)
        elif isinstance(keywords_raw, str):
            kw_str = keywords_raw
        else:
            kw_str = ""
            
        doc_text = f"{clause.title or ''} {clause.provision or ''} {kw_str}"
        documents.append(doc_text)

    vectorizer = TfidfVectorizer(stop_words='english')
    document_vectors = vectorizer.fit_transform(documents)
    query_vector = vectorizer.transform([query])

    similarity_scores = cosine_similarity(
        query_vector,
        document_vectors
    )[0]

    ranked_results = sorted(
        zip(clause_list, similarity_scores),
        key=lambda item: item[1],
        reverse=True
    )

    results = []
    for clause, score in ranked_results[:top_k]:
        if score >= threshold:
            results.append({
                "clause": clause,
                "clause_id": clause.clause_id,
                "similarity_score": float(score),
            })

    # Ensure at least one result is returned if available
    if not results and ranked_results:
        clause, score = ranked_results[0]
        results.append({
            "clause": clause,
            "clause_id": clause.clause_id,
            "similarity_score": float(score),
        })

    return results