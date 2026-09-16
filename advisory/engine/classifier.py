import re


# More specific phrases should be checked before broader keywords.
DOMAIN_PATTERNS = {
    "academic_status": [
        r"\bcgpa\b",
        r"\bgpa\b",
        r"\bprobation\b",
        r"\bgood standing\b",
        r"\brepeat(?:ing)?\s+(?:a\s+)?course\b",
        r"\brepeat(?:ing)?\s+(?:a\s+)?(?:course|class)\b",
    ],

    "academic_grievances": [
        r"\bre[-\s]?mark(?:ing)?\b",
        r"\bremark(?:ing)?\b",
        r"\bpetition\b",
        r"\banswer\s+script\b",
        r"\bbursary\s+receipt\b",
        r"\bOMR\b",
        r"\bCBT\b",
        r"\bexternal\s+assessor\b",
    ],

    "examination_misconduct": [
        r"\bexam(?:ination)?\s+misconduct\b",
        r"\bexam(?:ination)?\s+malpractice\b",
        r"\bcheat(?:ing)?\b",
        r"\binvigilator\b",
        r"\bmisconduct\s+form\b",
        r"\bunauthorized\s+material\b",
        r"\bunauthorised\s+material\b",
        r"\bimpersonation\b",
        r"\btable\s+7\b",
        r"\bpanel\s+invitation\b",
    ],

    "plagiarism": [
        r"\bplagiarism\b",
        r"\bplagiar(?:ise|ize|ised|ized|ising|izing)\b",
        r"\bcitation\b",
        r"\backnowledg(?:e|ement|ement)\b",
        r"\bsimilarity\s+report\b",
        r"\bturnitin\b",
        r"\bunreferenced\s+work\b",
    ],

    "research_ip": [
        r"\bresearch\s+copyright\b",
        r"\bcopyright\b",
        r"\bownership\b",
        r"\bpatent\b",
        r"\binvention\b",
        r"\bthesis\b",
        r"\bdissertation\b",
        r"\bbureau\s+of\s+intellectual\s+property\b",
        r"\bBIP\b",
        r"\bsponsored\s+research\b",
        r"\bintellectual\s+property\b",
    ],

    "disciplinary": [
        r"\bdisciplinary\s+appeal\b",
        r"\bdisciplinary\s+committee\b",
        r"\bfair\s+hearing\b",
        r"\bnotice\s+period\b",
        r"\bpanel\s+quorum\b",
        r"\bstandard\s+of\s+proof\b",
        r"\bsuspension\b",
        r"\bexpulsion\b",
        r"\bdisciplinary\b",
        r"\bappeal\b",
    ],
}


def classify_intent(normalized_query):
    """
    Classify a normalized student query into one of the
    supported regulatory domains.

    Returns:
        {
            "intent": domain name,
            "matched_keywords": list of matched patterns,
            "classification_method": "keyword_rule"
        }

    If no domain can be identified, returns:
        {
            "intent": "unknown",
            "matched_keywords": [],
            "classification_method": "keyword_rule"
        }

    If multiple domains have equally strong evidence, returns:
        {
            "intent": "ambiguous",
            "matched_keywords": {...},
            "classification_method": "keyword_rule"
        }
    """

    if not isinstance(normalized_query, str):
        return {
            "intent": "unknown",
            "matched_keywords": [],
            "classification_method": "keyword_rule",
        }

    query = normalized_query.lower()

    matches = {}

    for domain, patterns in DOMAIN_PATTERNS.items():
        domain_matches = []

        for pattern in patterns:
            if re.search(pattern.lower(), query):
                domain_matches.append(pattern)

        if domain_matches:
            matches[domain] = domain_matches

    # No identifiable domain
    if not matches:
        return {
            "intent": "unknown",
            "matched_keywords": [],
            "classification_method": "keyword_rule",
        }

    # Count matched patterns for each domain
    scores = {
        domain: len(domain_matches)
        for domain, domain_matches in matches.items()
    }

    highest_score = max(scores.values())

    top_domains = [
        domain
        for domain, score in scores.items()
        if score == highest_score
    ]

    # More than one domain has the same strongest evidence
    if len(top_domains) > 1:
        return {
            "intent": "ambiguous",
            "matched_keywords": {
                domain: matches[domain]
                for domain in top_domains
            },
            "classification_method": "keyword_rule",
        }

    selected_domain = top_domains[0]

    return {
        "intent": selected_domain,
        "matched_keywords": matches[selected_domain],
        "classification_method": "keyword_rule",
    }

def classify_sub_intent(normalized_query, domain):
    """
    Identify the specific regulatory intent within a supported domain.
    """

    if domain == "academic_grievances":
        if re.search(
            r"\b(re[-\s]?mark(?:ing)?|remark(?:ing)?|petition)\b",
            normalized_query
        ):
            return "remark_petition"

    return None