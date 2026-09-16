from advisory.models import PolicyClause, Rule
from django.core.management.base import BaseCommand


class Command(BaseCommand):
  help = "Seed Domain 3: Plagiarism / Academic Integrity"

  def handle(self, *args, **options):

    # ============================================================
    # DOMAIN 3 — PLAGIARISM / ACADEMIC INTEGRITY CLAUSES
    # ============================================================

    clauses = [
        {
            "clause_id": "KB_PI_001",
            "domain": "plagiarism",
            "topic": "definition",
            "title": "Definition of Plagiarism",
            "provision": (
                "The University defines plagiarism as presenting someone"
                " else’s work, in whole or in part, as one’s own. Work may"
                " include text, data, images, sound or performance. Where the"
                " work of others is used, appropriate acknowledgement should be"
                " provided."
            ),
            "source_title": "UNIZIK Plagiarism Guide",
            "source_reference": "University Plagiarism Guide",
            "source_url": "",
            "keywords": [
                "plagiarism",
                "definition",
                "work",
                "text",
                "data",
                "images",
                "sound",
                "performance",
                "acknowledgement",
            ],
            "clause_type": "explanatory",
        },
        {
            "clause_id": "KB_PI_002",
            "domain": "plagiarism",
            "topic": "similarity_review",
            "title": "Similarity Report as Diagnostic Evidence",
            "provision": (
                "A similarity report may be used to identify text or other"
                " material requiring further review, but a similarity"
                " percentage alone should not be treated by the advisory system"
                " as proof that plagiarism has been committed. The system shall"
                " not apply an arbitrary universal similarity threshold to"
                " determine guilt."
            ),
            "source_title": (
                "System Design Boundary Based on Available Institutional"
                " Evidence"
            ),
            "source_reference": "Design constraint",
            "source_url": "",
            "keywords": [
                "similarity report",
                "similarity percentage",
                "diagnostic",
                "threshold",
                "guilt",
            ],
            "clause_type": "explanatory",
        },
        {
            "clause_id": "KB_PI_003",
            "domain": "plagiarism",
            "topic": "institutional_review",
            "title": "Institutional Review of Plagiarism Allegations",
            "provision": (
                "Where plagiarism is alleged, the matter should be handled"
                " through the appropriate institutional process. The advisory"
                " system may provide information about the relevant"
                " academic-integrity requirements and indicate that formal"
                " determination and disciplinary action remain matters for the"
                " appropriate university authorities."
            ),
            "source_title": (
                "UNIZIK Plagiarism Guide and Institutional Disciplinary"
                " Framework"
            ),
            "source_reference": "Plagiarism Guide; Students' Code of Ethics",
            "source_url": "",
            "keywords": [
                "allegation",
                "institutional process",
                "disciplinary action",
                "university authorities",
            ],
            "clause_type": "procedural",
        },
    ]

    # ============================================================
    # DOMAIN 3 — PLAGIARISM / ACADEMIC INTEGRITY RULES
    # ============================================================

    rules = [
        {
            "rule_id": "RULE_PI_001",
            "domain": "plagiarism",
            "name": "Plagiarism Guidance",
            "description": (
                "Provides conceptual plagiarism guidance, citation importance,"
                " and diagnostic similarity handling without automatic guilt"
                " determination."
            ),
            "conditions": {"domain": "plagiarism"},
            "actions": {
                "provide_definition": True,
                "provide_acknowledgement_guidance": True,
                "use_similarity_as_diagnostic": True,
                "automatic_guilt_determination": False,
                "universal_similarity_threshold": False,
                "response_type": "advisory",
            },
            "clause_ids": ["KB_PI_001", "KB_PI_002"],
            "stop_processing": False,
            "requires_human_review": False,
        },
        {
            "rule_id": "RULE_PI_002",
            "domain": "plagiarism",
            "name": "Plagiarism Allegation Escalation",
            "description": (
                "Handles formal allegations or penalty inquiries by"
                " escalating to the appropriate institutional process rather"
                " than adjudicating or calculating penalties."
            ),
            "conditions": {
                "domain": "plagiarism",
                "allegation_or_penalty_request": True,
            },
            "actions": {
                "provide_general_guidance": True,
                "refer_to_institutional_process": True,
                "determine_guilt": False,
                "impose_penalty": False,
                "response_type": "institutional_escalation",
            },
            "clause_ids": ["KB_PI_001", "KB_PI_003"],
            "stop_processing": True,
            "requires_human_review": True,
        },
    ]

    # ============================================================
    # EXECUTION
    # ============================================================

    for data in clauses:
      clause, created = PolicyClause.objects.update_or_create(
          clause_id=data["clause_id"], defaults=data
      )
      action_word = "seeded" if created else "updated"
      self.stdout.write(
          self.style.SUCCESS(
              f"Successfully {action_word} clause: {clause.clause_id}"
          )
      )

    for data in rules:
      rule, created = Rule.objects.update_or_create(
          rule_id=data["rule_id"], defaults=data
      )
      action_word = "seeded" if created else "updated"
      self.stdout.write(
          self.style.SUCCESS(
              f"Successfully {action_word} rule: {rule.rule_id}"
          )
      )

    self.stdout.write(
        self.style.SUCCESS(
            "Domain 3: Plagiarism / Academic Integrity seeding completed"
            " successfully."
        )
    )