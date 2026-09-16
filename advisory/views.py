import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from advisory.engine.classifier import classify_intent, classify_sub_intent
from advisory.engine.evidence import assemble_evidence
from advisory.engine.extractor import extract_parameters
from advisory.engine.normalizer import normalize_query
from advisory.engine.response_generator import generate_response
from advisory.engine.retriever import retrieve_policy_clauses
from advisory.engine.rule_engine import evaluate_rules


@csrf_exempt
def advisory_query_view(request):
  if request.method != "POST":
    return JsonResponse(
        {"error": "Only POST requests are allowed."}, status=405
    )

  try:
    data = json.loads(request.body)
    raw_query = data.get("query", "").strip()

    if not raw_query:
      return JsonResponse({"error": "Query field cannot be empty."}, status=400)

    # --- Execute the 8-Stage Engine Pipeline ---
    norm_q = normalize_query(raw_query)
    intent_data = classify_intent(norm_q)
    domain = intent_data["intent"]
    sub_intent = classify_sub_intent(norm_q, domain)
    params = extract_parameters(norm_q, domain)
    
    # 1. Get clauses via TF-IDF retriever (restrict to top 1)
    retrieved = retrieve_policy_clauses(query=norm_q, domain=domain, top_k=1)
    
    matched_rules = evaluate_rules(domain, params, sub_intent)
    evidence = assemble_evidence(domain, sub_intent, params, matched_rules)
    
    # 2. Inject ONLY the single best TF-IDF matched clause if rule-based ones are empty
    if not evidence.get("policy_evidence") and retrieved:
        best_match = retrieved[0]["clause"]
        evidence["policy_evidence"] = [{
            "clause_id": best_match.clause_id,
            "title": best_match.title,
            "provision": best_match.provision,
            "source_reference": best_match.source_reference,
        }]

    response_payload = generate_response(evidence)

    response_payload["metadata"] = {
        "domain": domain,
        "sub_intent": sub_intent,
        "extracted_parameters": params,
        "matched_rules": [r["rule_id"] for r in matched_rules],
    }

    return JsonResponse(response_payload, status=200)

  except json.JSONDecodeError:
    return JsonResponse({"error": "Invalid JSON payload."}, status=400)
  except Exception as e:
    return JsonResponse({"error": str(e)}, status=500)


def advisory_ui_view(request):
  return render(request, "advisory/advisory_chat.html")

def advisory_landing_view(request):
    return render(request, "advisory/landing.html")