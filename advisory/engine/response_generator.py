def format_source_reference(raw_source: str) -> str:
  """Ensures source references explicitly state the governing document context."""
  if not raw_source:
    return "UNIZIK General Academic Regulations"

  # If the source already mentions the university or regulations, keep it clean
  if "regulations" in raw_source.lower() or "unizik" in raw_source.lower():
    return raw_source

  # Otherwise, prepend the official institutional document title
  return f"UNIZIK General Academic Regulations ({raw_source})"


def generate_response(evidence: dict) -> dict:
  """Takes assembled evidence and generates a deterministic,

  constrained student-facing advisory response.
  """
  stop_processing = evidence.get("stop_processing", False)
  policy_evidence = evidence.get("policy_evidence", [])
  matched_rules = evidence.get("matched_rules", [])
  params = evidence.get("parameters", {})
  domain = evidence.get("domain")

  # 1. Handle Exclusion / Terminal Rules (e.g., OMR/CBT remarking exclusion)
  if stop_processing:
    # Target the specific exclusion clause
    exclusion_clause = next(
        (
            c
            for c in policy_evidence
            if "exclusion" in c.get("clause_id", "").lower()
            or "omr" in c.get("provision", "").lower()
            or "cbt" in c.get("provision", "").lower()
        ),
        policy_evidence[0] if policy_evidence else {},
    )

    source_ref_raw = exclusion_clause.get("source_reference", "§5.9.1(ii)")
    source_ref = format_source_reference(source_ref_raw)

    provision = exclusion_clause.get("provision", "")
    exam_format = params.get("exam_format", "OMR or CBT")

    message = (
        f"Re-marking is not permitted for examinations conducted using"
        f" {exam_format} under {source_ref}. Official provision: \"{provision}\""
    )

    return {
        "response_type": "advisory_exclusion",
        "message": message,
        "sources": [source_ref],
        "requires_human_review": False,
    }

  # 2. Handle Academic Status Queries
  if domain == "academic_status":
    clause = policy_evidence[0] if policy_evidence else {}
    source_ref_raw = clause.get("source_reference", "University Regulations")
    source_ref = format_source_reference(source_ref_raw)

    title = clause.get("title", "Academic Status Regulation")
    provision = clause.get("provision", "")
    cgpa = params.get("cgpa")

    cgpa_str = f" with a CGPA of {cgpa}" if cgpa is not None else ""
    message = (
        f"Regarding your academic status{cgpa_str}, the governing provision"
        f" is **{title}** ({source_ref}): \"{provision}\""
    )

    return {
        "response_type": "status_advisory",
        "message": message,
        "sources": [source_ref],
        "requires_human_review": evidence.get("requires_human_review", False),
    }

  # 3. Handle General Procedural Pathways
  raw_sources = [
      c.get("source_reference")
      for c in policy_evidence
      if c.get("source_reference")
  ]
  unique_raw_sources = list(dict.fromkeys(raw_sources))
  sources = (
      [format_source_reference(s) for s in unique_raw_sources]
      if unique_raw_sources
      else ["UNIZIK General Academic Regulations"]
  )

  source_str = ", ".join(sources)

  # Extract provision text if available to display the actual rule content
  provisions_text = " ".join(
      f'"{c.get("provision")}"' for c in policy_evidence if c.get("provision")
  )
  
  if provisions_text:
      message = (
          f"Regarding your inquiry, the governing provision under {source_str}: "
          f"{provisions_text}"
      )
  else:
      message = (
          "Your request follows a valid procedural pathway. Please refer to the"
          f" following governing provisions: {source_str}."
      )

  return {
      "response_type": "standard_advisory",
      "message": message,
      "sources": sources,
      "requires_human_review": evidence.get("requires_human_review", False),
  }