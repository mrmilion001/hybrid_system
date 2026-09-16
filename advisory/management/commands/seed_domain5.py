from django.core.management.base import BaseCommand

from advisory.models import PolicyClause, Rule


SOURCE_TITLE = (
    "Nnamdi Azikiwe University Students' Code of Ethics"
)

SOURCE_URL = (
    "https://unizik.edu.ng/wp-content/uploads/2024/03/"
    "students-code-of-Ethics.pdf"
)


class Command(BaseCommand):
    help = "Seed Domain 5: Disciplinary / Fair Hearing Procedures"

    def handle(self, *args, **options):

        clauses = [

            {
                "clause_id": "KB_DF_001",
                "domain": "disciplinary",
                "topic": "scope",
                "title": "Scope of Student Disciplinary Regulations",
                "provision": (
                    "Student conduct, whether occurring on or off campus, may "
                    "become a matter for action under the University's student "
                    "disciplinary system where it threatens or violates the "
                    "University's commitments."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Section 1",
                "source_url": SOURCE_URL,
                "keywords": [
                    "discipline",
                    "student conduct",
                    "misconduct",
                    "on campus",
                    "off campus",
                ],
                "clause_type": "explanatory",
            },

            {
                "clause_id": "KB_DF_002",
                "domain": "disciplinary",
                "topic": "fairness",
                "title": "Fair and Orderly Disciplinary Proceedings",
                "provision": (
                    "The student disciplinary system is intended to ensure "
                    "fair and orderly proceedings concerning questions of "
                    "student misconduct."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Section 1",
                "source_url": SOURCE_URL,
                "keywords": [
                    "fair hearing",
                    "fairness",
                    "orderly proceedings",
                    "disciplinary proceedings",
                    "student misconduct",
                ],
                "clause_type": "explanatory",
            },

            {
                "clause_id": "KB_DF_003",
                "domain": "disciplinary",
                "topic": "complaint",
                "title": "Submission of Misconduct Complaint",
                "provision": (
                    "A complaint of misconduct against a student will normally "
                    "be submitted to the Vice-Chancellor. The Vice-Chancellor "
                    "may determine whether the complaint should proceed under "
                    "the disciplinary procedure."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Section 13",
                "source_url": SOURCE_URL,
                "keywords": [
                    "complaint",
                    "misconduct complaint",
                    "Vice-Chancellor",
                    "disciplinary complaint",
                ],
                "clause_type": "procedural",
            },

            {
                "clause_id": "KB_DF_004",
                "domain": "disciplinary",
                "topic": "referral",
                "title": "Referral of Complaint to Disciplinary Committee",
                "provision": (
                    "Where the complaint is to proceed through the disciplinary "
                    "procedure, it may be referred to the Disciplinary Committee."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Section 13",
                "source_url": SOURCE_URL,
                "keywords": [
                    "referral",
                    "disciplinary committee",
                    "complaint",
                    "misconduct",
                ],
                "clause_type": "procedural",
            },

            {
                "clause_id": "KB_DF_005",
                "domain": "disciplinary",
                "topic": "notification",
                "title": "Notification of Alleged Misconduct",
                "provision": (
                    "Upon receipt of a misconduct complaint against a student, "
                    "the secretary of the Disciplinary Committee shall formally "
                    "notify the student through the Head of Department that the "
                    "matter is before the Committee."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Section 14(i)",
                "source_url": SOURCE_URL,
                "keywords": [
                    "notification",
                    "allegation",
                    "Head of Department",
                    "disciplinary committee",
                    "student notification",
                ],
                "clause_type": "procedural",
            },

            {
                "clause_id": "KB_DF_006",
                "domain": "disciplinary",
                "topic": "notification",
                "title": "Details of Alleged Misconduct",
                "provision": (
                    "The student shall be supplied with details of the alleged "
                    "misconduct, including the particulars alleged to constitute "
                    "a breach of the disciplinary regulations."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Section 14(ii)",
                "source_url": SOURCE_URL,
                "keywords": [
                    "allegation details",
                    "misconduct details",
                    "notification",
                    "disciplinary allegation",
                ],
                "clause_type": "procedural",
            },

            {
                "clause_id": "KB_DF_007",
                "domain": "disciplinary",
                "topic": "response",
                "title": "Submission of Student Response",
                "provision": (
                    "Documentation submitted by the student in response to "
                    "notification of the alleged offence shall be made available "
                    "to members of the Disciplinary Committee."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Section 14(iii)",
                "source_url": SOURCE_URL,
                "keywords": [
                    "student response",
                    "response document",
                    "disciplinary response",
                    "committee",
                ],
                "clause_type": "procedural",
            },

            {
                "clause_id": "KB_DF_008",
                "domain": "disciplinary",
                "topic": "hearing_notice",
                "title": "Minimum Notice of Disciplinary Hearing",
                "provision": (
                    "The Committee shall fix the time and place of the hearing "
                    "and give written notice of the meeting, giving not less "
                    "than seven days' notice to the Committee members, the "
                    "student, and relevant persons necessary for determination "
                    "of the complaint."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Section 14(iv)",
                "source_url": SOURCE_URL,
                "keywords": [
                    "seven days",
                    "7 days",
                    "hearing notice",
                    "disciplinary hearing",
                    "written notice",
                ],
                "clause_type": "procedural",
            },

            {
                "clause_id": "KB_DF_009",
                "domain": "disciplinary",
                "topic": "hearing_attendance",
                "title": "Student Attendance at Hearing",
                "provision": (
                    "A student who receives written notice is expected to attend "
                    "at the time and place appointed for the hearing."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Section 14(v)",
                "source_url": SOURCE_URL,
                "keywords": [
                    "hearing attendance",
                    "student attendance",
                    "disciplinary hearing",
                    "written notice",
                ],
                "clause_type": "procedural",
            },

            {
                "clause_id": "KB_DF_010",
                "domain": "disciplinary",
                "topic": "hearing_attendance",
                "title": "Proceeding in the Student's Absence",
                "provision": (
                    "Where a student who has received the required notice fails "
                    "to attend, the Committee may proceed with the hearing, "
                    "determine the complaint and deal with the matter in the "
                    "student's absence."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Section 14(v)",
                "source_url": SOURCE_URL,
                "keywords": [
                    "absence",
                    "hearing in absence",
                    "student absence",
                    "disciplinary hearing",
                ],
                "clause_type": "procedural",
            },

            {
                "clause_id": "KB_DF_011",
                "domain": "disciplinary",
                "topic": "witnesses",
                "title": "Witness Participation",
                "provision": (
                    "Students and staff involved as witnesses may be required "
                    "to provide formal written statements when requested by "
                    "the Committee."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Section 14(vi)",
                "source_url": SOURCE_URL,
                "keywords": [
                    "witness",
                    "witness statement",
                    "written statement",
                    "disciplinary hearing",
                ],
                "clause_type": "procedural",
            },

            {
                "clause_id": "KB_DF_012",
                "domain": "disciplinary",
                "topic": "witnesses",
                "title": "Failure to Provide Relevant Information",
                "provision": (
                    "Failure by a student or staff witness to provide relevant "
                    "information or assist an officer in determining whether a "
                    "disciplinary offence has been committed may itself constitute "
                    "a disciplinary offence."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Section 14(vi)",
                "source_url": SOURCE_URL,
                "keywords": [
                    "failure to assist",
                    "witness",
                    "relevant information",
                    "disciplinary offence",
                ],
                "clause_type": "procedural",
            },

            {
                "clause_id": "KB_DF_013",
                "domain": "disciplinary",
                "topic": "committee_authority",
                "title": "Powers of the Students Disciplinary Committee",
                "provision": (
                    "The Students Disciplinary Committee, as constituted by the "
                    "Vice-Chancellor, may receive misconduct references from the "
                    "Vice-Chancellor, hear and determine complaints of misconduct, "
                    "call witnesses and consult other authorities, and apply "
                    "sanctions specified in the Regulation."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Section 11(i)-(iv)",
                "source_url": SOURCE_URL,
                "keywords": [
                    "disciplinary committee",
                    "committee powers",
                    "hear complaints",
                    "witnesses",
                    "sanctions",
                ],
                "clause_type": "procedural",
            },

            {
                "clause_id": "KB_DF_014",
                "domain": "disciplinary",
                "topic": "committee_authority",
                "title": "Disciplinary Proceedings and Criminal Proceedings",
                "provision": (
                    "The Committee may punish a student for misconduct covered "
                    "by the Regulation even where the misconduct has also been "
                    "subject to criminal prosecution and penalty."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Section 11(v)",
                "source_url": SOURCE_URL,
                "keywords": [
                    "criminal proceedings",
                    "criminal prosecution",
                    "disciplinary proceedings",
                    "misconduct",
                ],
                "clause_type": "procedural",
            },

            {
                "clause_id": "KB_DF_015",
                "domain": "disciplinary",
                "topic": "delegation",
                "title": "Delegation of Power to Discipline",
                "provision": (
                    "The Vice-Chancellor may delegate disciplinary powers to a "
                    "disciplinary committee appointed by the Vice-Chancellor or "
                    "to another body or person."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Section 10",
                "source_url": SOURCE_URL,
                "keywords": [
                    "delegation",
                    "disciplinary powers",
                    "Vice-Chancellor",
                    "disciplinary committee",
                ],
                "clause_type": "procedural",
            },

            {
                "clause_id": "KB_DF_016",
                "domain": "disciplinary",
                "topic": "quorum",
                "title": "Disciplinary Committee Quorum",
                "provision": (
                    "The quorum for a meeting of the Disciplinary Committee shall "
                    "be half of the number of members, including the Chair; where "
                    "the number cannot be divided equally into half, the required "
                    "number is the number representing half less one."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Section 14(viii)",
                "source_url": SOURCE_URL,
                "keywords": [
                    "quorum",
                    "committee quorum",
                    "disciplinary committee",
                    "chair",
                ],
                "clause_type": "procedural",
            },

            {
                "clause_id": "KB_DF_017",
                "domain": "disciplinary",
                "topic": "hearing",
                "title": "Opening of Disciplinary Hearing",
                "provision": (
                    "At the opening of the hearing, the Chair states the complaint "
                    "and the general nature of the evidence supporting it, after "
                    "which the student is asked whether the matter complained of "
                    "is admitted."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Section 14(ix)",
                "source_url": SOURCE_URL,
                "keywords": [
                    "opening hearing",
                    "chair",
                    "complaint",
                    "evidence",
                    "admission",
                ],
                "clause_type": "procedural",
            },

            {
                "clause_id": "KB_DF_018",
                "domain": "disciplinary",
                "topic": "hearing",
                "title": "Hearing of Contested Complaint",
                "provision": (
                    "Where the student does not admit the complaint, the Committee "
                    "may call witnesses for the purpose of establishing the "
                    "complaint or otherwise determining the matter."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Section 14(ix)",
                "source_url": SOURCE_URL,
                "keywords": [
                    "contested complaint",
                    "witnesses",
                    "hearing",
                    "admission",
                    "disciplinary committee",
                ],
                "clause_type": "procedural",
            },

            {
                "clause_id": "KB_DF_019",
                "domain": "disciplinary",
                "topic": "decision",
                "title": "Dismissal of Unestablished Complaint",
                "provision": (
                    "At the conclusion of the hearing, the Committee may dismiss "
                    "the complaint where no disciplinary offence has been made "
                    "out or where the evidence does not establish that a "
                    "disciplinary offence has been committed."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Section 14(x)",
                "source_url": SOURCE_URL,
                "keywords": [
                    "dismiss complaint",
                    "unestablished complaint",
                    "evidence",
                    "disciplinary offence",
                ],
                "clause_type": "procedural",
            },

            {
                "clause_id": "KB_DF_020",
                "domain": "disciplinary",
                "topic": "decision",
                "title": "Decision Where Disciplinary Offence Is Established",
                "provision": (
                    "Where the Disciplinary Committee finds that a disciplinary "
                    "offence has been committed, it has power to impose one or "
                    "more penalties provided for in the Regulation."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Section 14(x)",
                "source_url": SOURCE_URL,
                "keywords": [
                    "disciplinary offence",
                    "penalty",
                    "committee decision",
                    "sanction",
                ],
                "clause_type": "procedural",
            },

            {
                "clause_id": "KB_DF_021",
                "domain": "disciplinary",
                "topic": "decision",
                "title": "Majority Requirement for Establishing a Complaint",
                "provision": (
                    "A complaint shall not be found established unless a majority "
                    "of members present and voting so decide. Where votes are "
                    "equal, the matter is decided in favour of the student."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Section 14(xi)",
                "source_url": SOURCE_URL,
                "keywords": [
                    "majority",
                    "vote",
                    "equal votes",
                    "complaint established",
                    "student",
                ],
                "clause_type": "procedural",
            },

            {
                "clause_id": "KB_DF_022",
                "domain": "disciplinary",
                "topic": "sanction",
                "title": "Majority Vote on Penalty",
                "provision": (
                    "Where a complaint is found to be substantiated, the penalty "
                    "to be imposed shall be determined by majority vote. Where "
                    "there is equality of votes, the Chair has a casting vote."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Section 14(xi)",
                "source_url": SOURCE_URL,
                "keywords": [
                    "penalty vote",
                    "majority vote",
                    "casting vote",
                    "Chair",
                    "sanction",
                ],
                "clause_type": "procedural",
            },

            {
                "clause_id": "KB_DF_023",
                "domain": "disciplinary",
                "topic": "decision_communication",
                "title": "Communication of Disciplinary Decision",
                "provision": (
                    "The Committee's decision is normally communicated to the "
                    "Vice-Chancellor for approval, after which the Vice-Chancellor "
                    "directs that it be communicated to the student as "
                    "expeditiously as possible and not later than two weeks "
                    "after the hearing."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Section 14(xii)",
                "source_url": SOURCE_URL,
                "keywords": [
                    "disciplinary decision",
                    "decision communication",
                    "two weeks",
                    "Vice-Chancellor",
                    "hearing decision",
                ],
                "clause_type": "procedural",
            },

            {
                "clause_id": "KB_DF_024",
                "domain": "disciplinary",
                "topic": "sanctions",
                "title": "Disciplinary Measures",
                "provision": (
                    "The Regulation provides disciplinary measures including "
                    "reprimand or apology, community service, a Good Behaviour "
                    "Agreement, restitution, suspension, fines, and expulsion. "
                    "The fine is limited to not more than fifty thousand naira."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Section 5",
                "source_url": SOURCE_URL,
                "keywords": [
                    "sanctions",
                    "disciplinary measures",
                    "reprimand",
                    "community service",
                    "restitution",
                    "suspension",
                    "fine",
                    "expulsion",
                ],
                "clause_type": "explanatory",
            },

            {
                "clause_id": "KB_DF_025",
                "domain": "disciplinary",
                "topic": "sanctions",
                "title": "Suspension",
                "provision": (
                    "Suspension may include exclusion from entering or using "
                    "University facilities or benefiting from academic or "
                    "administrative structures for the specified period. A "
                    "suspended student is not eligible for benefits, entitlements, "
                    "grants or scholarships during the suspension period and is "
                    "not entitled to remain on campus."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Section 5, Group B(viii)",
                "source_url": SOURCE_URL,
                "keywords": [
                    "suspension",
                    "suspended student",
                    "campus",
                    "University facilities",
                    "scholarship",
                ],
                "clause_type": "explanatory",
            },

            {
                "clause_id": "KB_DF_026",
                "domain": "disciplinary",
                "topic": "sanctions",
                "title": "Recall from Suspension",
                "provision": (
                    "A student may apply to the Vice-Chancellor for recall from "
                    "suspension by entering an undertaking of good behaviour."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Section 5, Group B(ix)",
                "source_url": SOURCE_URL,
                "keywords": [
                    "recall",
                    "suspension",
                    "good behaviour",
                    "Vice-Chancellor",
                ],
                "clause_type": "procedural",
            },

            {
                "clause_id": "KB_DF_027",
                "domain": "disciplinary",
                "topic": "examination_referral",
                "title": "Examination Misconduct and Disciplinary Measures",
                "provision": (
                    "Where examination misconduct requires a disciplinary measure, "
                    "the relevant Faculty Examination Misconduct Committee shall "
                    "handle the matter."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Section 6",
                "source_url": SOURCE_URL,
                "keywords": [
                    "examination misconduct",
                    "examination committee",
                    "disciplinary measure",
                    "Faculty Examination Misconduct Committee",
                ],
                "clause_type": "procedural",
            },

            {
                "clause_id": "KB_DF_028",
                "domain": "disciplinary",
                "topic": "unlisted_breach",
                "title": "Disciplinary Breaches Not Specifically Listed",
                "provision": (
                    "A disciplinary breach not specifically mentioned in the "
                    "Regulation may be punished in parallel with the closest "
                    "breach mentioned, considering the nature and influence "
                    "of the conduct. Unit-specific rules not mentioned in the "
                    "Regulation may also require measures through the "
                    "University administration."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Section 7",
                "source_url": SOURCE_URL,
                "keywords": [
                    "unlisted breach",
                    "unlisted offence",
                    "disciplinary breach",
                    "unit rules",
                    "University administration",
                ],
                "clause_type": "procedural",
            },

            {
                "clause_id": "KB_DF_029",
                "domain": "disciplinary",
                "topic": "repeat_breach",
                "title": "Repeated Disciplinary Breach",
                "provision": (
                    "Where a student violates the same or a similar rule more "
                    "than once during the period of study, the student may "
                    "receive a sanction one degree heavier."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Section 8",
                "source_url": SOURCE_URL,
                "keywords": [
                    "repeat offence",
                    "repeat breach",
                    "previous breach",
                    "heavier sanction",
                ],
                "clause_type": "procedural",
            },

            {
                "clause_id": "KB_DF_030",
                "domain": "disciplinary",
                "topic": "appeal",
                "title": "Disciplinary Appeal Procedure and Grounds",
                "provision": (
                    "A student against whom a direction or penalty has been "
                    "given may appeal to the Vice-Chancellor within the "
                    "prescribed period and manner. An appeal does not "
                    "automatically suspend the operation of the direction or "
                    "penalty. Appeals must be brought within three months. "
                    "Grounds include that the Committee acted outside the "
                    "scope of the Regulation, new evidence has become "
                    "available, the penalty was excessive, or the penalty "
                    "was not prescribed by the disciplinary procedure."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Section 15; Grounds of Appeal",
                "source_url": SOURCE_URL,
                "keywords": [
                    "appeal",
                    "three months",
                    "3 months",
                    "grounds of appeal",
                    "new evidence",
                    "excessive penalty",
                    "Vice-Chancellor",
                ],
                "clause_type": "procedural",
            },

            {
                "clause_id": "KB_DF_031",
                "domain": "disciplinary",
                "topic": "fairness_and_sanction",
                "title": "Standard of Proof and Factors in Selecting Sanctions",
                "provision": (
                    "Persons determining issues under the Regulations should "
                    "be satisfied on reasonable grounds based on the evidence "
                    "before them; proof does not have to be beyond reasonable "
                    "doubt. Proceedings should be conducted according to "
                    "principles of justice and fairness. In selecting a "
                    "sanction, the Committee considers factors including the "
                    "weight or degree of the conduct, the student's intention, "
                    "previous breaches, behaviour and attitude, remorse, "
                    "involvement of persons from outside the University, and "
                    "whether the misconduct was committed by a group whose "
                    "individual members could not be separately identified."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "Sections 16-18",
                "source_url": SOURCE_URL,
                "keywords": [
                    "standard of proof",
                    "reasonable grounds",
                    "beyond reasonable doubt",
                    "justice",
                    "fairness",
                    "sanction factors",
                    "intention",
                    "previous breaches",
                    "remorse",
                ],
                "clause_type": "procedural",
            },
        ]

        rules = [

            {
                "rule_id": "RULE_DF_001",
                "domain": "disciplinary",
                "name": "Complaint Routing",
                "description": (
                    "Provides the institutional route for a student misconduct "
                    "complaint without determining whether the complaint "
                    "should proceed."
                ),
                "conditions": {
                    "misconduct_complaint": True,
                },
                "actions": {
                    "provide_complaint_procedure": True,
                    "retrieve_clause_ids": [
                        "KB_DF_003",
                        "KB_DF_004",
                    ],
                    "refer_to_appropriate_authority": True,
                },
                "clause_ids": [
                    "KB_DF_003",
                    "KB_DF_004",
                ],
                "stop_processing": False,
                "requires_human_review": True,
            },

            {
                "rule_id": "RULE_DF_002",
                "domain": "disciplinary",
                "name": "Notification and Hearing Notice",
                "description": (
                    "Provides procedural information concerning notification "
                    "of allegations and minimum hearing notice."
                ),
                "conditions": {
                    "formal_allegation": True,
                },
                "actions": {
                    "retrieve_clause_ids": [
                        "KB_DF_005",
                        "KB_DF_006",
                        "KB_DF_007",
                        "KB_DF_008",
                    ],
                },
                "clause_ids": [
                    "KB_DF_005",
                    "KB_DF_006",
                    "KB_DF_007",
                    "KB_DF_008",
                ],
                "stop_processing": False,
                "requires_human_review": False,
            },

            {
                "rule_id": "RULE_DF_003",
                "domain": "disciplinary",
                "name": "Hearing Procedure",
                "description": (
                    "Provides information about attendance, absence, witnesses, "
                    "quorum and the opening and conduct of a disciplinary hearing."
                ),
                "conditions": {
                    "hearing_question": True,
                },
                "actions": {
                    "retrieve_clause_ids": [
                        "KB_DF_009",
                        "KB_DF_010",
                        "KB_DF_011",
                        "KB_DF_016",
                        "KB_DF_017",
                        "KB_DF_018",
                    ],
                },
                "clause_ids": [
                    "KB_DF_009",
                    "KB_DF_010",
                    "KB_DF_011",
                    "KB_DF_016",
                    "KB_DF_017",
                    "KB_DF_018",
                ],
                "stop_processing": False,
                "requires_human_review": False,
            },

            {
                "rule_id": "RULE_DF_004",
                "domain": "disciplinary",
                "name": "Committee Decision and Non-Adjudication",
                "description": (
                    "Explains the Committee's decision-making process while "
                    "preventing the advisory system from determining guilt "
                    "or selecting a student's penalty."
                ),
                "conditions": {
                    "user_requests_case_determination": True,
                },
                "actions": {
                    "explain_committee_role": True,
                    "retrieve_clause_ids": [
                        "KB_DF_019",
                        "KB_DF_020",
                        "KB_DF_021",
                        "KB_DF_022",
                    ],
                    "determine_guilt": False,
                    "select_student_penalty": False,
                    "refer_to_disciplinary_authority": True,
                },
                "clause_ids": [
                    "KB_DF_019",
                    "KB_DF_020",
                    "KB_DF_021",
                    "KB_DF_022",
                ],
                "stop_processing": True,
                "requires_human_review": True,
            },

            {
                "rule_id": "RULE_DF_005",
                "domain": "disciplinary",
                "name": "Appeal Guidance",
                "description": (
                    "Provides information about the disciplinary appeal "
                    "procedure, deadline, grounds and effect of an appeal."
                ),
                "conditions": {
                    "appeal_question": True,
                },
                "actions": {
                    "retrieve_clause_ids": [
                        "KB_DF_030",
                    ],
                    "provide_appeal_deadline": True,
                    "provide_appeal_grounds": True,
                    "state_penalty_not_automatically_suspended": True,
                    "refer_to_appeal_authority": True,
                },
                "clause_ids": [
                    "KB_DF_030",
                ],
                "stop_processing": False,
                "requires_human_review": True,
            },

            {
                "rule_id": "RULE_DF_006",
                "domain": "disciplinary",
                "name": "Examination Misconduct Referral",
                "description": (
                    "Routes examination misconduct requiring disciplinary "
                    "measures to the appropriate Faculty Examination "
                    "Misconduct Committee."
                ),
                "conditions": {
                    "examination_misconduct": True,
                    "disciplinary_measure_required": True,
                },
                "actions": {
                    "retrieve_clause_ids": [
                        "KB_DF_027",
                    ],
                    "refer_to_faculty_examination_misconduct_committee": True,
                },
                "clause_ids": [
                    "KB_DF_027",
                ],
                "stop_processing": True,
                "requires_human_review": True,
            },

            {
                "rule_id": "RULE_DF_007",
                "domain": "disciplinary",
                "name": "Procedural Fairness and Sanction Boundary",
                "description": (
                    "Explains available disciplinary measures and the factors "
                    "the Committee may consider while preventing the system "
                    "from selecting or imposing a sanction."
                ),
                "conditions": {
                    "sanction_question": True,
                },
                "actions": {
                    "retrieve_clause_ids": [
                        "KB_DF_024",
                        "KB_DF_025",
                        "KB_DF_026",
                        "KB_DF_029",
                        "KB_DF_031",
                    ],
                    "explain_sanction_factors": True,
                    "select_sanction_for_student": False,
                    "determine_guilt": False,
                    "refer_to_committee": True,
                },
                "clause_ids": [
                    "KB_DF_024",
                    "KB_DF_025",
                    "KB_DF_026",
                    "KB_DF_029",
                    "KB_DF_031",
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
                "\nDomain 5: Disciplinary / Fair Hearing Procedures "
                "seeding completed successfully."
            )
        )