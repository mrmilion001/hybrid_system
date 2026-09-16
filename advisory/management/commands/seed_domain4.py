from django.core.management.base import BaseCommand

from advisory.models import PolicyClause, Rule


SOURCE_TITLE = (
    "Nnamdi Azikiwe University Intellectual Property Policy, October 2021"
)

SOURCE_URL = (
    "https://unizik.edu.ng/wp-content/uploads/2023/01/"
    "NAU_IP_Policy_Updated_Oct2021-1.pdf"
)


class Command(BaseCommand):
    help = "Seed Domain 4: Research Intellectual Property Rights"

    def handle(self, *args, **options):

        clauses = [

            {
                "clause_id": "KB_RIP_001",
                "domain": "research_ip",
                "topic": "scope",
                "title": "Students Covered by the Intellectual Property Policy",
                "provision": (
                    "The Intellectual Property Policy applies to undergraduate, "
                    "postgraduate and visiting students, whether full-time or "
                    "part-time. A student who is also an employee is treated as "
                    "staff with respect to intellectual property arising from "
                    "employment and as a student with respect to other intellectual "
                    "property created from student work."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Article 5.1(c)",
                "source_url": SOURCE_URL,
                "keywords": [
                    "student",
                    "undergraduate",
                    "postgraduate",
                    "visiting student",
                    "intellectual property",
                    "IP policy",
                ],
                "clause_type": "explanatory",
            },

            {
                "clause_id": "KB_RIP_002",
                "domain": "research_ip",
                "topic": "research_undertaking",
                "title": "Agreement Before Commencing Research",
                "provision": (
                    "Students of the University are required to sign an agreement "
                    "to be bound by the Intellectual Property Policy before "
                    "commencing research activity."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Article 6.2",
                "source_url": SOURCE_URL,
                "keywords": [
                    "research",
                    "research agreement",
                    "pre-research",
                    "IP agreement",
                    "intellectual property policy",
                ],
                "clause_type": "procedural",
            },

            {
                "clause_id": "KB_RIP_003",
                "domain": "research_ip",
                "topic": "student_ownership",
                "title": "General Ownership of Student-Created Intellectual Property",
                "provision": (
                    "Where a student generates an intellectual property asset or "
                    "work during study or research, the intellectual property "
                    "right belongs to the student unless one of the exceptions "
                    "specified in the Intellectual Property Policy applies."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Article 7.3(a)",
                "source_url": SOURCE_URL,
                "keywords": [
                    "student ownership",
                    "student IP",
                    "ownership",
                    "research ownership",
                    "intellectual property rights",
                ],
                "clause_type": "deterministic",
            },

            {
                "clause_id": "KB_RIP_004",
                "domain": "research_ip",
                "topic": "ownership_exceptions",
                "title": "Exceptions to Student Ownership",
                "provision": (
                    "Student-created intellectual property is subject to exceptions "
                    "where, among other circumstances, the student has a sponsored "
                    "studentship with a sponsor claim, makes significant use of "
                    "University resources, participates in a research programme "
                    "in which the resulting intellectual property is committed to "
                    "a sponsor, creates work building upon existing University "
                    "intellectual property or jointly invents with University "
                    "employees or associates, or is also an employee of the "
                    "University."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Article 7.3(a)(i)-(v)",
                "source_url": SOURCE_URL,
                "keywords": [
                    "ownership exception",
                    "sponsored studentship",
                    "sponsor",
                    "university resources",
                    "joint invention",
                    "university employee",
                    "existing university IP",
                ],
                "clause_type": "deterministic",
            },

            {
                "clause_id": "KB_RIP_005",
                "domain": "research_ip",
                "topic": "assignment",
                "title": "Assignment of Student Intellectual Property",
                "provision": (
                    "Where the circumstances specified in Article 7.3(a)(ii)-(iv) "
                    "apply, the student is required to assign the intellectual "
                    "property to the University. In respect of revenue generated "
                    "by that intellectual property, the student is treated on the "
                    "same basis as University employees."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Article 7.3(b)",
                "source_url": SOURCE_URL,
                "keywords": [
                    "assignment",
                    "assign IP",
                    "university ownership",
                    "student IP",
                    "revenue",
                    "intellectual property assignment",
                ],
                "clause_type": "deterministic",
            },

            {
                "clause_id": "KB_RIP_006",
                "domain": "research_ip",
                "topic": "thesis_dissertation",
                "title": "Copyright in Student Theses and Dissertations",
                "provision": (
                    "The texts of student theses and dissertations, and works "
                    "derived from them, are treated as exempted scholarly works. "
                    "Students own copyright in these scholarly works, subject "
                    "to a royalty-free licence to the University to reproduce "
                    "and publish them."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Article 7.3(c)",
                "source_url": SOURCE_URL,
                "keywords": [
                    "thesis",
                    "dissertation",
                    "copyright",
                    "student copyright",
                    "scholarly work",
                    "royalty-free licence",
                    "publication",
                ],
                "clause_type": "deterministic",
            },

            {
                "clause_id": "KB_RIP_007",
                "domain": "research_ip",
                "topic": "ip_disclosure",
                "title": "Duty to Disclose Potential Intellectual Property",
                "provision": (
                    "Persons covered by the policy are required to disclose to "
                    "the University's Bureau of Intellectual Property any research "
                    "finding, invention or creative work that is an intellectual "
                    "property asset or could potentially lead to an intellectual "
                    "property asset."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Article 9.1(a)",
                "source_url": SOURCE_URL,
                "keywords": [
                    "IP disclosure",
                    "disclosure",
                    "Bureau of Intellectual Property",
                    "invention",
                    "research finding",
                    "creative work",
                ],
                "clause_type": "procedural",
            },

            {
                "clause_id": "KB_RIP_008",
                "domain": "research_ip",
                "topic": "ip_evaluation",
                "title": "Bureau Evaluation of Reported Intellectual Property",
                "provision": (
                    "Unless there are justifiable circumstances to the contrary, "
                    "the Bureau of Intellectual Property should communicate to "
                    "the researcher as soon as possible, and not later than "
                    "sixty days after receiving the Report of Invention Form, "
                    "whether the University will pursue acquisition of rights "
                    "under the research."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Article 9.3(a)",
                "source_url": SOURCE_URL,
                "keywords": [
                    "60 days",
                    "sixty days",
                    "Bureau evaluation",
                    "Report of Invention Form",
                    "IP evaluation",
                    "acquisition of rights",
                ],
                "clause_type": "procedural",
            },

            {
                "clause_id": "KB_RIP_009",
                "domain": "research_ip",
                "topic": "dispute_resolution",
                "title": "Amicable Resolution of Intellectual Property Disputes",
                "provision": (
                    "Intellectual property disputes under the Policy are to be "
                    "resolved amicably in the spirit of supporting and furthering "
                    "the interests of the University, its staff and students, "
                    "and the public."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Article 14.1",
                "source_url": SOURCE_URL,
                "keywords": [
                    "IP dispute",
                    "dispute resolution",
                    "amicable resolution",
                    "intellectual property dispute",
                ],
                "clause_type": "procedural",
            },

            {
                "clause_id": "KB_RIP_010",
                "domain": "research_ip",
                "topic": "dispute_appeal",
                "title": "Intellectual Property Dispute Panel and Appeal",
                "provision": (
                    "Intellectual property disputes are handled by an Intellectual "
                    "Property Dispute Panel constituted by the Vice-Chancellor. "
                    "Where a dispute involves a research student, the Panel "
                    "includes a representative of the Students' Union appointed "
                    "by the Vice-Chancellor. A party dissatisfied with the "
                    "Panel's decision may appeal to the University Management "
                    "Committee, whose decision is final and binding on the parties."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Article 14.2-14.6",
                "source_url": SOURCE_URL,
                "keywords": [
                    "IP dispute panel",
                    "appeal",
                    "Students Union",
                    "research student",
                    "University Management Committee",
                    "Vice-Chancellor",
                    "intellectual property dispute",
                ],
                "clause_type": "procedural",
            },
        ]

        rules = [

            {
                "rule_id": "RULE_RIP_001",
                "domain": "research_ip",
                "name": "Student IP Ownership",
                "description": (
                    "Provides the general student-ownership position where "
                    "no identified ownership exception applies."
                ),
                "conditions": {
                    "student_context": True,
                    "sponsored_research": False,
                    "university_resource_exception": False,
                    "university_joint_ip": False,
                    "student_employee_context": False,
                },
                "actions": {
                    "state_general_student_ownership": True,
                    "cite_clause_ids": ["KB_RIP_003"],
                },
                "clause_ids": ["KB_RIP_003"],
                "stop_processing": False,
                "requires_human_review": False,
            },

            {
                "rule_id": "RULE_RIP_002",
                "domain": "research_ip",
                "name": "Student IP Ownership Exception",
                "description": (
                    "Identifies circumstances in which the ordinary student "
                    "ownership position requires consideration of an exception."
                ),
                "conditions": {
                    "student_context": True,
                    "one_or_more_ownership_exceptions": True,
                },
                "actions": {
                    "retrieve_clause_ids": [
                        "KB_RIP_004",
                        "KB_RIP_005",
                    ],
                    "state_exception_applies": True,
                    "require_institutional_determination": True,
                },
                "clause_ids": [
                    "KB_RIP_004",
                    "KB_RIP_005",
                ],
                "stop_processing": False,
                "requires_human_review": True,
            },

            {
                "rule_id": "RULE_RIP_003",
                "domain": "research_ip",
                "name": "Thesis or Dissertation Copyright",
                "description": (
                    "Handles questions concerning copyright in student theses "
                    "and dissertations."
                ),
                "conditions": {
                    "work_type": "thesis_or_dissertation",
                },
                "actions": {
                    "state_student_copyright": True,
                    "state_university_royalty_free_license": True,
                    "cite_clause_ids": ["KB_RIP_006"],
                },
                "clause_ids": ["KB_RIP_006"],
                "stop_processing": False,
                "requires_human_review": False,
            },

            {
                "rule_id": "RULE_RIP_004",
                "domain": "research_ip",
                "name": "Potential IP Disclosure",
                "description": (
                    "Provides guidance where a student or researcher asks "
                    "about disclosure of potential intellectual property."
                ),
                "conditions": {
                    "potential_ip": True,
                    "disclosure_question": True,
                },
                "actions": {
                    "recommend_ip_disclosure": True,
                    "retrieve_clause_ids": [
                        "KB_RIP_007",
                        "KB_RIP_008",
                    ],
                },
                "clause_ids": [
                    "KB_RIP_007",
                    "KB_RIP_008",
                ],
                "stop_processing": False,
                "requires_human_review": False,
            },

            {
                "rule_id": "RULE_RIP_005",
                "domain": "research_ip",
                "name": "IP Dispute and Appeal",
                "description": (
                    "Routes intellectual property disputes and appeals to "
                    "the institutional dispute-resolution process."
                ),
                "conditions": {
                    "dispute_or_appeal": True,
                },
                "actions": {
                    "retrieve_clause_ids": [
                        "KB_RIP_009",
                        "KB_RIP_010",
                    ],
                    "refer_to_ip_dispute_process": True,
                    "determine_ownership": False,
                    "determine_final_outcome": False,
                },
                "clause_ids": [
                    "KB_RIP_009",
                    "KB_RIP_010",
                ],
                "stop_processing": True,
                "requires_human_review": True,
            },
        ]

        # Seed clauses
        for data in clauses:
            PolicyClause.objects.update_or_create(
                clause_id=data["clause_id"],
                defaults=data,
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully seeded clause: {data['clause_id']}"
                )
            )

        # Seed rules
        for data in rules:
            Rule.objects.update_or_create(
                rule_id=data["rule_id"],
                defaults=data,
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully seeded rule: {data['rule_id']}"
                )
            )

        self.stdout.write(
            self.style.SUCCESS(
                "\nDomain 4: Research Intellectual Property Rights "
                "seeding completed successfully."
            )
        )