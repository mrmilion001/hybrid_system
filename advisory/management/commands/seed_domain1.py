from advisory.models import PolicyClause, Rule
from django.core.management.base import BaseCommand


class Command(BaseCommand):
  help = (
      "Seeds Academic Status and Domain 1 (Academic Grievances) clauses and"
      " rules"
  )

  def handle(self, *args, **kwargs):

    # ==========================================================
    # 1. SUPPORTING DOMAIN: ACADEMIC STATUS
    # ==========================================================
    status_clauses = [
        {
            "clause_id": "KB_AS_001",
            "domain": "Academic Status",
            "topic": "Good Academic Standing",
            "title": "Good Academic Standing Threshold",
            "provision": (
                "A cumulative grade point average (CGPA) of at least 1.00 places"
                " a student in good academic standing."
            ),
            "source_title": (
                "Nnamdi Azikiwe University General and Academic Regulations,"
                " Seventh Edition 2021"
            ),
            "source_reference": "§4.7.1",
            "keywords": ["cgpa", "academic standing", "good standing"],
            "clause_type": "deterministic",
        },
        {
            "clause_id": "KB_AS_002",
            "domain": "Academic Status",
            "topic": "Academic Probation",
            "title": "Academic Probation Threshold",
            "provision": (
                "A student whose CGPA lies between 0.60 and 0.99 is placed on"
                " academic probation in the following session."
            ),
            "source_title": (
                "Nnamdi Azikiwe University General and Academic Regulations,"
                " Seventh Edition 2021"
            ),
            "source_reference": "§4.7.2",
            "keywords": [
                "cgpa",
                "probation",
                "academic probation",
                "repeat course",
            ],
            "clause_type": "deterministic",
        },
    ]

    status_rules = [
        {
            "rule_id": "RULE_AS_001",
            "domain": "Academic Status",
            "name": "Good Standing Evaluation Rule",
            "description": "Evaluates if CGPA is greater than or equal to 1.00",
            "conditions": {"domain": "academic_status", "cgpa_min": 1.00},
            "actions": {
                "retrieve": ["KB_AS_001"],
                "response_type": "advisory",
                "message": "Student is in Good Academic Standing.",
            },
            "clause_ids": ["KB_AS_001"],
            "stop_processing": True,
        },
        {
            "rule_id": "RULE_AS_002",
            "domain": "Academic Status",
            "name": "Academic Probation Evaluation Rule",
            "description": "Evaluates if CGPA lies between 0.60 and 0.99",
            "conditions": {
                "domain": "academic_status",
                "cgpa_min": 0.60,
                "cgpa_max": 0.99,
            },
            "actions": {
                "retrieve": ["KB_AS_002"],
                "response_type": "advisory",
                "message": "Student is placed on Academic Probation.",
            },
            "clause_ids": ["KB_AS_002"],
            "stop_processing": True,
        },
    ]

    # ==========================================================
    # 2. DOMAIN 1: ACADEMIC GRIEVANCES
    # ==========================================================
    academic_grievance_clauses = [
        {
            "clause_id": "KB_AG_001",
            "domain": "academic_grievances",
            "topic": "remark_petition",
            "title": "Right to Seek Re-marking",
            "provision": (
                "A student who is aggrieved at the mark awarded at the end of"
                " an examination has the right, and not merely a privilege, to"
                " seek re-marking of the answer script."
            ),
            "source_title": (
                "Nnamdi Azikiwe University General and Academic Regulations,"
                " Seventh Edition 2021"
            ),
            "source_reference": "§5.9.1(i)",
            "source_url": (
                "https://unizik.edu.ng/wp-content/uploads/2023/09/GENERALAND-ACADEMICREGULATIONS.pdf"
            ),
            "keywords": [
                "remark",
                "re-mark",
                "remarking",
                "mark",
                "examination result",
                "petition",
                "answer script",
            ],
            "clause_type": "deterministic",
        },
        {
            "clause_id": "KB_AG_002",
            "domain": "academic_grievances",
            "topic": "remark_petition",
            "title": "Time Limit for Re-marking Petition",
            "provision": (
                "A student seeking re-marking must make the request not later"
                " than the end of the semester following the examination."
            ),
            "source_title": (
                "Nnamdi Azikiwe University General and Academic Regulations,"
                " Seventh Edition 2021"
            ),
            "source_reference": "§5.9.1(i)",
            "source_url": (
                "https://unizik.edu.ng/wp-content/uploads/2023/09/GENERALAND-ACADEMICREGULATIONS.pdf"
            ),
            "keywords": [
                "remark",
                "deadline",
                "time limit",
                "semester",
                "petition",
                "examination",
            ],
            "clause_type": "deterministic",
        },
        {
            "clause_id": "KB_AG_003",
            "domain": "academic_grievances",
            "topic": "remark_petition",
            "title": "OMR and CBT Exclusion",
            "provision": (
                "No petition for re-marking shall be entertained in respect of"
                " examinations where Optical Mark Reader (OMR) or Computer"
                " Based Test (CBT) is used."
            ),
            "source_title": (
                "Nnamdi Azikiwe University General and Academic Regulations,"
                " Seventh Edition 2021"
            ),
            "source_reference": "§5.9.1(ii)",
            "source_url": (
                "https://unizik.edu.ng/wp-content/uploads/2023/09/GENERALAND-ACADEMICREGULATIONS.pdf"
            ),
            "keywords": [
                "OMR",
                "CBT",
                "computer based test",
                "optical mark reader",
                "remark",
                "re-mark",
                "petition",
            ],
            "clause_type": "deterministic",
        },
        {
            "clause_id": "KB_AG_004",
            "domain": "academic_grievances",
            "topic": "remark_petition",
            "title": "Petition Fee and Submission",
            "provision": (
                "To initiate the re-marking exercise, the student shall pay the"
                " prescribed fee of N50,000 for non-professional examinations"
                " and N100,000 for specified professional examinations at the"
                " Bursary. A copy of the payment receipt shall be attached to"
                " a petition addressed to the Vice-Chancellor requesting that"
                " the scripts be re-marked."
            ),
            "source_title": (
                "Nnamdi Azikiwe University General and Academic Regulations,"
                " Seventh Edition 2021"
            ),
            "source_reference": "§5.9.1(iii)",
            "source_url": (
                "https://unizik.edu.ng/wp-content/uploads/2023/09/GENERALAND-ACADEMICREGULATIONS.pdf"
            ),
            "keywords": [
                "N50000",
                "N100000",
                "fee",
                "Bursary",
                "receipt",
                "petition",
                "Vice-Chancellor",
                "professional examination",
                "non-professional examination",
            ],
            "clause_type": "procedural",
        },
        {
            "clause_id": "KB_AG_005",
            "domain": "academic_grievances",
            "topic": "remark_petition",
            "title": "Materials Requested for Re-marking",
            "provision": (
                "The Vice-Chancellor shall request from the Dean of the"
                " Faculty concerned the materials relevant to the course,"
                " including the question paper, the marking scheme, the class"
                " score sheet, selected scripts, and other relevant scripts"
                " specified by the regulation."
            ),
            "source_title": (
                "Nnamdi Azikiwe University General and Academic Regulations,"
                " Seventh Edition 2021"
            ),
            "source_reference": "§5.9.1(iv)",
            "source_url": (
                "https://unizik.edu.ng/wp-content/uploads/2023/09/GENERALAND-ACADEMICREGULATIONS.pdf"
            ),
            "keywords": [
                "question paper",
                "marking scheme",
                "score sheet",
                "scripts",
                "Dean",
                "Vice-Chancellor",
                "remark",
            ],
            "clause_type": "procedural",
        },
        {
            "clause_id": "KB_AG_006",
            "domain": "academic_grievances",
            "topic": "remark_petition",
            "title": "External Assessor",
            "provision": (
                "The Vice-Chancellor shall arrange for the selected scripts to"
                " be re-marked using an external assessor."
            ),
            "source_title": (
                "Nnamdi Azikiwe University General and Academic Regulations,"
                " Seventh Edition 2021"
            ),
            "source_reference": "§5.9.1(vi)",
            "source_url": (
                "https://unizik.edu.ng/wp-content/uploads/2023/09/GENERALAND-ACADEMICREGULATIONS.pdf"
            ),
            "keywords": [
                "external assessor",
                "remark",
                "re-mark",
                "scripts",
                "Vice-Chancellor",
            ],
            "clause_type": "procedural",
        },
        {
            "clause_id": "KB_AG_007",
            "domain": "academic_grievances",
            "topic": "remark_outcome",
            "title": (
                "Re-marking Outcome Where Differences Are Below Five Percent"
            ),
            "provision": (
                "If the differences in marks for all the re-marked scripts are"
                " less than 5%, the petition fails and the case is closed."
            ),
            "source_title": (
                "Nnamdi Azikiwe University General and Academic Regulations,"
                " Seventh Edition 2021"
            ),
            "source_reference": "§5.9.1(vii)",
            "source_url": (
                "https://unizik.edu.ng/wp-content/uploads/2023/09/GENERALAND-ACADEMICREGULATIONS.pdf"
            ),
            "keywords": [
                "5%",
                "difference in marks",
                "remark",
                "petition fails",
                "case closed",
            ],
            "clause_type": "deterministic",
        },
        {
            "clause_id": "KB_AG_008",
            "domain": "academic_grievances",
            "topic": "remark_outcome",
            "title": (
                "Re-marking Outcome Where Petitioner Alone Has a Five Percent"
                " Increase"
            ),
            "provision": (
                "If the difference in marks is plus 5% or more for only the"
                " petitioner, the petition succeeds; the petitioner is awarded"
                " the new mark and the petition fee is refunded. A possible"
                " case of victimization shall be investigated and, if"
                " established, appropriate disciplinary measures are applied."
            ),
            "source_title": (
                "Nnamdi Azikiwe University General and Academic Regulations,"
                " Seventh Edition 2021"
            ),
            "source_reference": "§5.9.1(ix)",
            "source_url": (
                "https://unizik.edu.ng/wp-content/uploads/2023/09/GENERALAND-ACADEMICREGULATIONS.pdf"
            ),
            "keywords": [
                "5%",
                "petitioner",
                "new mark",
                "fee refund",
                "victimization",
                "petition succeeds",
            ],
            "clause_type": "deterministic",
        },
        {
            "clause_id": "KB_AG_009",
            "domain": "academic_grievances",
            "topic": "remark_outcome",
            "title": (
                "Re-marking Outcome Where Two or More Scripts Differ by Five"
                " Percent or More"
            ),
            "provision": (
                "If the differences in marks are 5% or more for two or more of"
                " the marked scripts, all the scripts shall be re-marked. If the"
                " petitioner is one of the affected cases, the petition"
                " succeeds, the petitioner is awarded the new mark and the"
                " petition fee is refunded. If the petitioner is not one of the"
                " affected cases, the petition fails and the case is closed."
            ),
            "source_title": (
                "Nnamdi Azikiwe University General and Academic Regulations,"
                " Seventh Edition 2021"
            ),
            "source_reference": "§5.9.1(x)",
            "source_url": (
                "https://unizik.edu.ng/wp-content/uploads/2023/09/GENERALAND-ACADEMICREGULATIONS.pdf"
            ),
            "keywords": [
                "5%",
                "two or more scripts",
                "re-marked",
                "new mark",
                "fee refund",
                "petition succeeds",
                "petition fails",
            ],
            "clause_type": "deterministic",
        },
        {
            "clause_id": "KB_AG_010",
            "domain": "academic_grievances",
            "topic": "remark_outcome",
            "title": "Unmarked Scripts or Failure to Follow Marking Scheme",
            "provision": (
                "A case of unmarked examination scripts or failure to adhere"
                " to the marking scheme shall be investigated and, if"
                " established, appropriate disciplinary measures are applied."
            ),
            "source_title": (
                "Nnamdi Azikiwe University General and Academic Regulations,"
                " Seventh Edition 2021"
            ),
            "source_reference": "§5.9.1",
            "source_url": (
                "https://unizik.edu.ng/wp-content/uploads/2023/09/GENERALAND-ACADEMICREGULATIONS.pdf"
            ),
            "keywords": [
                "unmarked scripts",
                "marking scheme",
                "investigation",
                "disciplinary measures",
                "examination",
            ],
            "clause_type": "procedural",
        },
    ]

    academic_grievance_rules = [
        {
            "rule_id": "RULE_AG_001",
            "domain": "academic_grievances",
            "name": "Re-marking Petition Eligibility",
            "description": (
                "Handles enquiries concerning the student's right and basic"
                " eligibility to seek re-marking."
            ),
            "conditions": {"intent": "remark_petition"},
            "actions": {
                "retrieve": [
                    "KB_AG_001",
                    "KB_AG_002",
                    "KB_AG_004",
                    "KB_AG_005",
                    "KB_AG_006",
                ],
                "response_type": "advisory",
                "human_decision_required": True,
            },
            "clause_ids": [
                "KB_AG_001",
                "KB_AG_002",
                "KB_AG_004",
                "KB_AG_005",
                "KB_AG_006",
            ],
            "stop_processing": False,
            "requires_human_review": False,
        },
        {
            "rule_id": "RULE_AG_002",
            "domain": "academic_grievances",
            "name": "OMR or CBT Re-marking Exclusion",
            "description": (
                "Blocks a re-marking pathway where the examination was"
                " conducted using OMR or CBT."
            ),
            "conditions": {
                "intent": "remark_petition",
                "exam_format": ["OMR", "CBT"],
            },
            "actions": {
                "retrieve": ["KB_AG_003"],
                "response_type": "advisory_exclusion",
                "stop_reason": (
                    "The regulation does not provide for a petition for"
                    " re-marking of examinations where OMR or CBT is used."
                ),
            },
            "clause_ids": ["KB_AG_003"],
            "stop_processing": True,
            "requires_human_review": False,
        },
        {
            "rule_id": "RULE_AG_003",
            "domain": "academic_grievances",
            "name": "Re-marking Petition Time Limit",
            "description": (
                "Checks whether the student's re-marking request falls within"
                " the regulatory time limit."
            ),
            "conditions": {
                "intent": "remark_petition",
                "deadline_status": "passed",
            },
            "actions": {
                "retrieve": ["KB_AG_002"],
                "response_type": "deadline_advisory",
                "message": (
                    "The regulation provides that a request for re-marking must"
                    " be made not later than the end of the semester following"
                    " the examination."
                ),
                "human_decision_required": True,
            },
            "clause_ids": ["KB_AG_002"],
            "stop_processing": True,
            "requires_human_review": False,
        },
        {
            "rule_id": "RULE_AG_004",
            "domain": "academic_grievances",
            "name": "Valid Re-marking Petition Pathway",
            "description": (
                "Provides the procedural pathway for a potentially eligible"
                " re-marking request where the examination is neither OMR nor"
                " CBT and the regulatory time limit has not passed."
            ),
            "conditions": {
                "intent": "remark_petition",
                "exam_format": {"not_in": ["OMR", "CBT"]},
                "deadline_status": "within_limit",
            },
            "actions": {
                "retrieve": [
                    "KB_AG_001",
                    "KB_AG_002",
                    "KB_AG_004",
                    "KB_AG_005",
                    "KB_AG_006",
                ],
                "response_type": "procedural_advisory",
                "human_decision_required": True,
            },
            "clause_ids": [
                "KB_AG_001",
                "KB_AG_002",
                "KB_AG_004",
                "KB_AG_005",
                "KB_AG_006",
            ],
            "stop_processing": False,
            "requires_human_review": False,
        },
        {
            "rule_id": "RULE_AG_005",
            "domain": "academic_grievances",
            "name": "Re-marking Outcome Assessment",
            "description": (
                "Provides the applicable regulatory outcome pathway after the"
                " required re-marking exercise has been completed."
            ),
            "conditions": {"intent": "remark_outcome", "remark_completed": True},
            "actions": {
                "retrieve": ["KB_AG_007", "KB_AG_008", "KB_AG_009", "KB_AG_010"],
                "response_type": "outcome_advisory",
                "human_decision_required": True,
            },
            "clause_ids": ["KB_AG_007", "KB_AG_008", "KB_AG_009", "KB_AG_010"],
            "stop_processing": True,
            "requires_human_review": True,
        },
    ]

    # --- EXECUTION BLOCKS ---

    # Seed Supporting Status Clauses & Rules
    for c in status_clauses:
      PolicyClause.objects.update_or_create(
          clause_id=c["clause_id"], defaults=c
      )
    for r in status_rules:
      Rule.objects.update_or_create(rule_id=r["rule_id"], defaults=r)

    # Seed Academic Grievances Clauses
    for c in academic_grievance_clauses:
      cid = c.pop("clause_id")
      PolicyClause.objects.update_or_create(clause_id=cid, defaults=c)
      self.stdout.write(self.style.SUCCESS(f"Successfully seeded clause: {cid}"))

    # Seed Academic Grievances Rules
    for r in academic_grievance_rules:
      rid = r.pop("rule_id")
      Rule.objects.update_or_create(rule_id=rid, defaults=r)
      self.stdout.write(self.style.SUCCESS(f"Successfully seeded rule: {rid}"))