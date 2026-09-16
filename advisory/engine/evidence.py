from advisory.models import PolicyClause


def assemble_evidence(domain, sub_intent, parameters, matched_rules):
    """
    Assemble matched rules and their referenced policy clauses
    into a structured evidence package for response generation.
    """

    clause_ids = []

    for rule in matched_rules:
        retrieve_ids = rule.get("actions", {}).get("retrieve", [])

        for clause_id in retrieve_ids:
            if clause_id not in clause_ids:
                clause_ids.append(clause_id)

    clauses = PolicyClause.objects.filter(
        clause_id__in=clause_ids,
        active=True
    )

    clause_map = {
        clause.clause_id: clause
        for clause in clauses
    }

    policy_evidence = []

    for clause_id in clause_ids:
        clause = clause_map.get(clause_id)

        if clause:
            policy_evidence.append({
                "clause_id": clause.clause_id,
                "title": clause.title,
                "provision": clause.provision,
                "source_reference": clause.source_reference,
            })

    requires_human_review = any(
        rule.get("requires_human_review", False)
        or rule.get("actions", {}).get("human_decision_required", False)
        for rule in matched_rules
    )

    stop_processing = any(
        rule.get("stop_processing", False)
        for rule in matched_rules
    )

    return {
        "domain": domain,
        "sub_intent": sub_intent,
        "parameters": parameters,
        "matched_rules": matched_rules,
        "policy_evidence": policy_evidence,
        "requires_human_review": requires_human_review,
        "stop_processing": stop_processing,
    }