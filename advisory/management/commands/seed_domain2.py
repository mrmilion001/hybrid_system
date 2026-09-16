from django.core.management.base import BaseCommand

from advisory.models import PolicyClause, Rule


SOURCE_TITLE = (
    "Nnamdi Azikiwe University General and Academic Regulations, "
    "Seventh Edition 2021"
)

SOURCE_URL = (
    "https://unizik.edu.ng/wp-content/uploads/2023/09/"
    "GENERALAND-ACADEMICREGULATIONS.pdf"
)


class Command(BaseCommand):
    help = "Seed Domain 2: Examination Misconduct"

    def handle(self, *args, **options):

        # ============================================================
        # DOMAIN 2 — EXAMINATION MISCONDUCT
        # ============================================================

        clauses = [

            # --------------------------------------------------------
            # GENERAL / PROCEDURAL CLAUSES
            # --------------------------------------------------------

            {
                "clause_id": "KB_EM_001",
                "domain": "examination_misconduct",
                "topic": "definition",
                "title": "General Definition of Examination Misconduct",
                "provision": (
                    "Any departure either by staff or student from laid down "
                    "examination regulations constitutes examination misconduct. "
                    "Examination misconduct should therefore be considered for "
                    "staff as well as for students in and outside the examination hall."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "§5.8",
                "source_url": SOURCE_URL,
                "keywords": [
                    "examination misconduct",
                    "misconduct",
                    "examination regulations",
                    "student",
                    "staff",
                    "examination hall",
                    "outside examination hall",
                ],
                "clause_type": "explanatory",
            },

            {
                "clause_id": "KB_EM_002",
                "domain": "examination_misconduct",
                "topic": "hall_procedure",
                "title": "Examination Misconduct Report Form",
                "provision": (
                    "Every alleged case of examination misconduct arising during "
                    "an examination shall be recorded on the prescribed Examination "
                    "Misconduct Report Form, filled in duplicate."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "§5.8.1(i)",
                "source_url": SOURCE_URL,
                "keywords": [
                    "alleged case",
                    "misconduct report form",
                    "examination misconduct report",
                    "report form",
                    "duplicate",
                    "examination hall",
                ],
                "clause_type": "procedural",
            },

            {
                "clause_id": "KB_EM_003",
                "domain": "examination_misconduct",
                "topic": "hall_procedure",
                "title": "Completion of Examination and No Time Extension",
                "provision": (
                    "The Examination Misconduct Report Form shall be completed "
                    "before the student involved is allowed to continue with the "
                    "examination. The student's examination time shall not be extended. "
                    "An allegation of a case of examination misconduct shall not "
                    "constitute enough grounds for a student not to be allowed to "
                    "complete writing the examination except where his/her continued "
                    "presence within the examination hall endangers peace and good order."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "§5.8.1(ii)–(iii)",
                "source_url": SOURCE_URL,
                "keywords": [
                    "report form",
                    "continue examination",
                    "no time extension",
                    "allegation",
                    "complete examination",
                    "peace",
                    "good order",
                ],
                "clause_type": "procedural",
            },

            {
                "clause_id": "KB_EM_004",
                "domain": "examination_misconduct",
                "topic": "hall_reporting_chain",
                "title": "Examination-Hall Reporting Chain",
                "provision": (
                    "The Chief Invigilator shall package the completed Examination "
                    "Misconduct Report Forms along with the relevant answer scripts "
                    "and any supporting materials for the Faculty Examinations Officer. "
                    "The Faculty Examination Officer shall collect all cases of "
                    "examination misconduct at the end of each examination, make a "
                    "record of them and promptly submit them to the Chairman of the "
                    "Examination Misconduct Panel for the Faculty through the Dean "
                    "of the Faculty."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "§5.8.1(iv)–(v)",
                "source_url": SOURCE_URL,
                "keywords": [
                    "Chief Invigilator",
                    "Faculty Examination Officer",
                    "Dean",
                    "Examination Misconduct Panel",
                    "answer scripts",
                    "supporting materials",
                    "reporting chain",
                ],
                "clause_type": "procedural",
            },

            {
                "clause_id": "KB_EM_005",
                "domain": "examination_misconduct",
                "topic": "outside_hall_procedure",
                "title": "Outside-Hall Reporting Procedure",
                "provision": (
                    "Any suspected case of examination misconduct detected outside "
                    "the examination hall shall be promptly reported in writing "
                    "through the Head of Department to the Dean of the Faculty. "
                    "The Dean shall forward the case to the Chairman of the Faculty "
                    "Examination Misconduct Panel within one working day of receipt "
                    "of the report."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "§5.8.2(i)",
                "source_url": SOURCE_URL,
                "keywords": [
                    "outside examination hall",
                    "suspected case",
                    "Head of Department",
                    "Dean",
                    "one working day",
                    "Examination Misconduct Panel",
                ],
                "clause_type": "procedural",
            },

            {
                "clause_id": "KB_EM_006",
                "domain": "examination_misconduct",
                "topic": "panel_authority",
                "title": "Panel Disposal and Authorized Officers",
                "provision": (
                    "The Examination Misconduct Panel shall dispose of such cases "
                    "before the next semester examinations. Only the Dean, the "
                    "Examination Monitor or Examination Misconduct Panel is empowered "
                    "to treat examination misconduct cases, and no other officer "
                    "shall either investigate a case or delay its forwarding process."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "§5.8.2(ii), (vii)",
                "source_url": SOURCE_URL,
                "keywords": [
                    "Examination Misconduct Panel",
                    "Dean",
                    "Examination Monitor",
                    "authorized officers",
                    "dispose cases",
                    "next semester examinations",
                ],
                "clause_type": "procedural",
            },

            {
                "clause_id": "KB_EM_007",
                "domain": "examination_misconduct",
                "topic": "reporting_deadline",
                "title": "Maximum Forwarding Delay",
                "provision": (
                    "On no account shall a report on an alleged case of examination "
                    "misconduct be delayed for more than one working day in the "
                    "custody of any forwarding officer."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "§5.8.2",
                "source_url": SOURCE_URL,
                "keywords": [
                    "one working day",
                    "delay",
                    "forwarding officer",
                    "report",
                    "alleged case",
                    "examination misconduct",
                ],
                "clause_type": "procedural",
            },

            # --------------------------------------------------------
            # TABLE 7 — OFFENCE / PENALTY CLAUSES
            # --------------------------------------------------------

            {
                "clause_id": "KB_EM_008",
                "domain": "examination_misconduct",
                "topic": "table_7_penalty",
                "title": "Table 7 — Impersonation",
                "provision": (
                    "Nature of offence: Impersonation. "
                    "Penalty: Suspension for 3 years for both students for first offenders."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "§5.8.4, Table 7, S/N 1",
                "source_url": SOURCE_URL,
                "keywords": [
                    "impersonation",
                    "impersonating",
                    "false candidate",
                    "Table 7",
                    "three years",
                    "suspension",
                ],
                "clause_type": "deterministic",
            },

            {
                "clause_id": "KB_EM_009",
                "domain": "examination_misconduct",
                "topic": "table_7_penalty",
                "title": "Table 7 — Forged Receipts/Documents",
                "provision": (
                    "Nature of offence: Forged receipts(s) documents. "
                    "Penalty: Suspension for 3 years and hand over to police."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "§5.8.4, Table 7, S/N 2",
                "source_url": SOURCE_URL,
                "keywords": [
                    "forged receipts",
                    "forged documents",
                    "false documents",
                    "Table 7",
                    "three years",
                    "police",
                ],
                "clause_type": "deterministic",
            },

            {
                "clause_id": "KB_EM_010",
                "domain": "examination_misconduct",
                "topic": "table_7_penalty",
                "title": "Table 7 — Collaborative Copying",
                "provision": (
                    "Nature of offence: Collaborative copying. "
                    "Penalty: Suspend for 1 year."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "§5.8.4, Table 7, S/N 3",
                "source_url": SOURCE_URL,
                "keywords": [
                    "collaborative copying",
                    "copying",
                    "collusion",
                    "Table 7",
                    "one year",
                    "suspension",
                ],
                "clause_type": "deterministic",
            },

            {
                "clause_id": "KB_EM_011",
                "domain": "examination_misconduct",
                "topic": "table_7_penalty",
                "title": "Table 7 — Unauthorized Materials",
                "provision": (
                    "Nature of offence: Unauthorized material(s). "
                    "Penalty: Suspend for 2 years."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "§5.8.4, Table 7, S/N 4",
                "source_url": SOURCE_URL,
                "keywords": [
                    "unauthorized material",
                    "unauthorized materials",
                    "materials",
                    "Table 7",
                    "two years",
                    "suspension",
                ],
                "clause_type": "deterministic",
            },

            {
                "clause_id": "KB_EM_012",
                "domain": "examination_misconduct",
                "topic": "table_7_penalty",
                "title": "Table 7 — Exchange of Answer Booklets or Written Materials",
                "provision": (
                    "Nature of offence: Exchange of answer booklets/written material(s). "
                    "Penalty: Suspend for 2 years."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "§5.8.4, Table 7, S/N 5",
                "source_url": SOURCE_URL,
                "keywords": [
                    "exchange answer booklets",
                    "exchange written materials",
                    "answer booklet",
                    "written materials",
                    "Table 7",
                    "two years",
                ],
                "clause_type": "deterministic",
            },

            {
                "clause_id": "KB_EM_013",
                "domain": "examination_misconduct",
                "topic": "table_7_penalty",
                "title": "Table 7 — Refusal to Hand Over Suspected Incriminating Materials",
                "provision": (
                    "Nature of offence: Refusal to hand over suspected incriminating "
                    "material(s). Penalty: Suspend for 2 years."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "§5.8.4, Table 7, S/N 6",
                "source_url": SOURCE_URL,
                "keywords": [
                    "refusal",
                    "hand over",
                    "incriminating materials",
                    "suspected materials",
                    "Table 7",
                    "two years",
                ],
                "clause_type": "deterministic",
            },

            {
                "clause_id": "KB_EM_014",
                "domain": "examination_misconduct",
                "topic": "table_7_penalty",
                "title": "Table 7 — Destruction of Suspected Incriminating Materials",
                "provision": (
                    "Nature of offence: Destruction of suspected incriminating "
                    "material(s). Penalty: Suspend for 2 years."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "§5.8.4, Table 7, S/N 7",
                "source_url": SOURCE_URL,
                "keywords": [
                    "destruction",
                    "incriminating materials",
                    "suspected materials",
                    "Table 7",
                    "two years",
                ],
                "clause_type": "deterministic",
            },

            {
                "clause_id": "KB_EM_015",
                "domain": "examination_misconduct",
                "topic": "table_7_penalty",
                "title": "Table 7 — Presentation of False Identity Card",
                "provision": (
                    "Nature of offence: Presentation of false identity card. "
                    "Penalty: Suspend for 2 years."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "§5.8.4, Table 7, S/N 8",
                "source_url": SOURCE_URL,
                "keywords": [
                    "false identity card",
                    "identity card",
                    "fake identity",
                    "Table 7",
                    "two years",
                ],
                "clause_type": "deterministic",
            },

            {
                "clause_id": "KB_EM_016",
                "domain": "examination_misconduct",
                "topic": "table_7_penalty",
                "title": "Table 7 — Possession of Unauthorized Materials Relevant to Exams",
                "provision": (
                    "Nature of offence: Possession of unauthorized materials "
                    "relevant to exams. Penalty: Suspend for 2 years."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "§5.8.4, Table 7, S/N 9",
                "source_url": SOURCE_URL,
                "keywords": [
                    "possession",
                    "unauthorized materials",
                    "exam materials",
                    "Table 7",
                    "two years",
                ],
                "clause_type": "deterministic",
            },

            {
                "clause_id": "KB_EM_017",
                "domain": "examination_misconduct",
                "topic": "table_7_penalty",
                "title": "Table 7 — Smuggling Question Paper Out of Examination Hall",
                "provision": (
                    "Nature of offence: Smuggling of question paper out of the "
                    "exam hall. Penalty: Suspend for 3 years."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "§5.8.4, Table 7, S/N 10",
                "source_url": SOURCE_URL,
                "keywords": [
                    "smuggling",
                    "question paper",
                    "exam hall",
                    "Table 7",
                    "three years",
                ],
                "clause_type": "deterministic",
            },

            {
                "clause_id": "KB_EM_018",
                "domain": "examination_misconduct",
                "topic": "table_7_penalty",
                "title": "Table 7 — Smuggling Answer Script",
                "provision": (
                    "Nature of offence: Smuggling of answer script into or out "
                    "of the exam hall. Penalty: Suspend for 3 years."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "§5.8.4, Table 7, S/N 11",
                "source_url": SOURCE_URL,
                "keywords": [
                    "smuggling",
                    "answer script",
                    "exam hall",
                    "Table 7",
                    "three years",
                ],
                "clause_type": "deterministic",
            },

            {
                "clause_id": "KB_EM_019",
                "domain": "examination_misconduct",
                "topic": "table_7_penalty",
                "title": "Table 7 — Conviction in Two or More Misconduct Offences",
                "provision": (
                    "Nature of offence: Conviction in two or more misconduct offences. "
                    "Penalty: The punishments shall be cumulative subject to maximum "
                    "of three (3) years."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "§5.8.4, Table 7, S/N 12",
                "source_url": SOURCE_URL,
                "keywords": [
                    "conviction",
                    "two offences",
                    "multiple offences",
                    "cumulative punishment",
                    "three years",
                    "Table 7",
                ],
                "clause_type": "deterministic",
            },

            {
                "clause_id": "KB_EM_020",
                "domain": "examination_misconduct",
                "topic": "table_7_penalty",
                "title": "Table 7 — Refusal to Appear Before Panel",
                "provision": (
                    "Nature of offence: Refusal to appear before the panel after "
                    "three invitations. Penalty: Apply the punishment for the "
                    "offence for which the candidate failed to appear for trial."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "§5.8.4, Table 7, S/N 13",
                "source_url": SOURCE_URL,
                "keywords": [
                    "refusal to appear",
                    "panel",
                    "three invitations",
                    "trial",
                    "Table 7",
                ],
                "clause_type": "deterministic",
            },

            {
                "clause_id": "KB_EM_021",
                "domain": "examination_misconduct",
                "topic": "table_7_penalty",
                "title": "Table 7 — Battery, Assault or Fighting an Invigilator",
                "provision": (
                    "Nature of offence: Battery/Assault occasioning harm or "
                    "fighting an invigilator. Penalty: Suspension for 3 years "
                    "and should present an apology letter."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "§5.8.4, Table 7, S/N 14",
                "source_url": SOURCE_URL,
                "keywords": [
                    "battery",
                    "assault",
                    "harm",
                    "fighting",
                    "invigilator",
                    "apology letter",
                    "three years",
                ],
                "clause_type": "deterministic",
            },

            {
                "clause_id": "KB_EM_022",
                "domain": "examination_misconduct",
                "topic": "table_7_penalty",
                "title": "Table 7 — Mutilation or Use of Fake Registration Number",
                "provision": (
                    "Nature of offence: Mutilation of or use of fake Registration "
                    "Number. Penalty: (a) Suspend for 1 year for mutilation of "
                    "Registration number; (b) Suspend for 3 years for use of "
                    "fake Registration Number."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "§5.8.4, Table 7, S/N 15",
                "source_url": SOURCE_URL,
                "keywords": [
                    "registration number",
                    "mutilation",
                    "fake registration number",
                    "one year",
                    "three years",
                    "Table 7",
                ],
                "clause_type": "deterministic",
            },

            {
                "clause_id": "KB_EM_023",
                "domain": "examination_misconduct",
                "topic": "table_7_penalty",
                "title": "Table 7 — Second Offence Attracting Three-Year Suspension",
                "provision": (
                    "A student who is found guilty of committing for a second time "
                    "any of the offences that attract 3 years suspension: Expulsion."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "§5.8.4, Table 7, S/N 16",
                "source_url": SOURCE_URL,
                "keywords": [
                    "second offence",
                    "repeat offence",
                    "three year suspension",
                    "expulsion",
                    "Table 7",
                ],
                "clause_type": "deterministic",
            },

            {
                "clause_id": "KB_EM_024",
                "domain": "examination_misconduct",
                "topic": "table_7_penalty",
                "title": "Table 7 — Second Offence Attracting One- or Two-Year Suspension",
                "provision": (
                    "A student who is found guilty of committing for a second time "
                    "any of the offences that attract 1 year or 2 years suspension: "
                    "Suspend again."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "§5.8.4, Table 7, S/N 17",
                "source_url": SOURCE_URL,
                "keywords": [
                    "second offence",
                    "repeat offence",
                    "one year",
                    "two years",
                    "suspend again",
                    "Table 7",
                ],
                "clause_type": "deterministic",
            },

            {
                "clause_id": "KB_EM_025",
                "domain": "examination_misconduct",
                "topic": "table_7_penalty",
                "title": "Table 7 — Refusal to Sign Examination Misconduct Form",
                "provision": (
                    "Nature of offence: Refusal to sign the examination misconduct "
                    "form. Penalty: Suspend for two years."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "§5.8.4, Table 7, S/N 18",
                "source_url": SOURCE_URL,
                "keywords": [
                    "refusal to sign",
                    "examination misconduct form",
                    "misconduct form",
                    "two years",
                    "Table 7",
                ],
                "clause_type": "deterministic",
            },

            {
                "clause_id": "KB_EM_026",
                "domain": "examination_misconduct",
                "topic": "table_7_penalty",
                "title": "Table 7 — Failure to Return an Answer Script",
                "provision": (
                    "Nature of offence: Failure to return an answer script. "
                    "Penalty: Repeat the Year."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "§5.8.4, Table 7, S/N 19",
                "source_url": SOURCE_URL,
                "keywords": [
                    "failure to return",
                    "answer script",
                    "repeat year",
                    "Table 7",
                ],
                "clause_type": "deterministic",
            },

            {
                "clause_id": "KB_EM_027",
                "domain": "examination_misconduct",
                "topic": "table_7_penalty",
                "title": "Table 7 — Talking to Another Student During Examination",
                "provision": (
                    "Nature of offence: Talking to another student during an "
                    "examination. Penalty: Award an “F”."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "§5.8.4, Table 7, S/N 20",
                "source_url": SOURCE_URL,
                "keywords": [
                    "talking",
                    "another student",
                    "examination",
                    "F",
                    "Table 7",
                ],
                "clause_type": "deterministic",
            },

            {
                "clause_id": "KB_EM_028",
                "domain": "examination_misconduct",
                "topic": "table_7_penalty",
                "title": "Table 7 — Looking Into Another Student's Answer Script",
                "provision": (
                    "Nature of offence: Looking into another student's answer "
                    "script. Penalty: Award an “F”."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "§5.8.4, Table 7, S/N 21",
                "source_url": SOURCE_URL,
                "keywords": [
                    "looking",
                    "another student's answer script",
                    "answer script",
                    "F",
                    "Table 7",
                ],
                "clause_type": "deterministic",
            },

            {
                "clause_id": "KB_EM_029",
                "domain": "examination_misconduct",
                "topic": "table_7_penalty",
                "title": "Table 7 — Unruly Behaviour Toward Examination Officer",
                "provision": (
                    "Nature of offence: Unruly behaviour to the invigilator or "
                    "any other examination officer. Penalty: Award an “F”."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "§5.8.4, Table 7, S/N 22",
                "source_url": SOURCE_URL,
                "keywords": [
                    "unruly behaviour",
                    "invigilator",
                    "examination officer",
                    "F",
                    "Table 7",
                ],
                "clause_type": "deterministic",
            },

            {
                "clause_id": "KB_EM_030",
                "domain": "examination_misconduct",
                "topic": "table_7_penalty",
                "title": "Table 7 — Borrowing or Lending Material",
                "provision": (
                    "Nature of offence: Borrowing or lending of any material "
                    "in the examination hall. Penalty: Award an “F”."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "§5.8.4, Table 7, S/N 23",
                "source_url": SOURCE_URL,
                "keywords": [
                    "borrowing",
                    "lending",
                    "material",
                    "examination hall",
                    "F",
                    "Table 7",
                ],
                "clause_type": "deterministic",
            },

            {
                "clause_id": "KB_EM_031",
                "domain": "examination_misconduct",
                "topic": "table_7_penalty",
                "title": "Table 7 — Writing Before Start of Examination",
                "provision": (
                    "Nature of offence: Writing before the start of the examination. "
                    "Penalty: Loss between 5 and 20 marks."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "§5.8.4, Table 7, S/N 24",
                "source_url": SOURCE_URL,
                "keywords": [
                    "writing before",
                    "start of examination",
                    "5 marks",
                    "20 marks",
                    "loss of marks",
                    "Table 7",
                ],
                "clause_type": "deterministic",
            },

            {
                "clause_id": "KB_EM_032",
                "domain": "examination_misconduct",
                "topic": "table_7_penalty",
                "title": "Table 7 — Writing After Call to Stop",
                "provision": (
                    "Nature of offence: Writing after the call for stop of examination. "
                    "Penalty: Loss between 5 and 20 marks."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "§5.8.4, Table 7, S/N 25",
                "source_url": SOURCE_URL,
                "keywords": [
                    "writing after",
                    "call to stop",
                    "stop examination",
                    "5 marks",
                    "20 marks",
                    "loss of marks",
                    "Table 7",
                ],
                "clause_type": "deterministic",
            },

            {
                "clause_id": "KB_EM_033",
                "domain": "examination_misconduct",
                "topic": "table_7_penalty",
                "title": "Table 7 — Writing Things Other Than Registration Number",
                "provision": (
                    "Nature of offence: Writing things other than the registration "
                    "number on the question paper. Penalty: Loss between 5 and 20 marks."
                ),
                "source_title": SOURCE_TITLE,
                "source_reference": "§5.8.4, Table 7, S/N 26",
                "source_url": SOURCE_URL,
                "keywords": [
                    "registration number",
                    "question paper",
                    "writing",
                    "5 marks",
                    "20 marks",
                    "loss of marks",
                    "Table 7",
                ],
                "clause_type": "deterministic",
            },
        ]

        # ============================================================
        # RULES
        # ============================================================

        rules = [

            {
                "rule_id": "RULE_EM_001",
                "domain": "examination_misconduct",
                "name": "Examination Misconduct Classification",
                "description": (
                    "Identifies an alleged examination-misconduct enquiry "
                    "and retrieves the relevant regulatory provision without "
                    "determining guilt."
                ),
                "conditions": {
                    "domain": "examination_misconduct",
                    "intent": "misconduct_inquiry",
                },
                "actions": {
                    "response_type": "non_judgmental_advisory",
                    "retrieve_matching_clause": True,
                    "determine_guilt": False,
                },
                "clause_ids": [
                    "KB_EM_001"
                ],
                "stop_processing": False,
                "requires_human_review": False,
            },

            {
                "rule_id": "RULE_EM_002",
                "domain": "examination_misconduct",
                "name": "Examination-Hall Procedure",
                "description": (
                    "Provides the regulatory reporting procedure for an alleged "
                    "examination-misconduct case arising during an examination."
                ),
                "conditions": {
                    "domain": "examination_misconduct",
                    "intent": "procedure_inquiry",
                    "incident_location": "examination_hall",
                },
                "actions": {
                    "retrieve": [
                        "KB_EM_002",
                        "KB_EM_003",
                        "KB_EM_004",
                    ],
                    "response_type": "procedural_advisory",
                    "determine_guilt": False,
                },
                "clause_ids": [
                    "KB_EM_002",
                    "KB_EM_003",
                    "KB_EM_004",
                ],
                "stop_processing": True,
                "requires_human_review": False,
            },

            {
                "rule_id": "RULE_EM_003",
                "domain": "examination_misconduct",
                "name": "Outside-Hall Procedure",
                "description": (
                    "Provides the regulatory reporting and forwarding procedure "
                    "for suspected examination misconduct detected outside "
                    "the examination hall."
                ),
                "conditions": {
                    "domain": "examination_misconduct",
                    "intent": "procedure_inquiry",
                    "incident_location": "outside_examination_hall",
                },
                "actions": {
                    "retrieve": [
                        "KB_EM_005",
                        "KB_EM_006",
                        "KB_EM_007",
                    ],
                    "response_type": "procedural_advisory",
                    "determine_guilt": False,
                },
                "clause_ids": [
                    "KB_EM_005",
                    "KB_EM_006",
                    "KB_EM_007",
                ],
                "stop_processing": True,
                "requires_human_review": False,
            },

            {
                "rule_id": "RULE_EM_004",
                "domain": "examination_misconduct",
                "name": "Table 7 Penalty Retrieval",
                "description": (
                    "Retrieves the exact Table 7 offence and corresponding "
                    "prescribed penalty when the alleged offence matches "
                    "a verified Table 7 entry."
                ),
                "conditions": {
                    "domain": "examination_misconduct",
                    "intent": "penalty_inquiry",
                    "offence_type": "verified_table_7_offence",
                },
                "actions": {
                    "retrieve": "matching_KB_EM_008_to_KB_EM_033",
                    "response_type": "penalty_advisory",
                    "present_as_prescribed_penalty": True,
                    "determine_guilt": False,
                    "impose_penalty": False,
                },
                "clause_ids": [
                    "KB_EM_008",
                    "KB_EM_009",
                    "KB_EM_010",
                    "KB_EM_011",
                    "KB_EM_012",
                    "KB_EM_013",
                    "KB_EM_014",
                    "KB_EM_015",
                    "KB_EM_016",
                    "KB_EM_017",
                    "KB_EM_018",
                    "KB_EM_019",
                    "KB_EM_020",
                    "KB_EM_021",
                    "KB_EM_022",
                    "KB_EM_023",
                    "KB_EM_024",
                    "KB_EM_025",
                    "KB_EM_026",
                    "KB_EM_027",
                    "KB_EM_028",
                    "KB_EM_029",
                    "KB_EM_030",
                    "KB_EM_031",
                    "KB_EM_032",
                    "KB_EM_033",
                ],
                "stop_processing": True,
                "requires_human_review": False,
            },

            {
                "rule_id": "RULE_EM_005",
                "domain": "examination_misconduct",
                "name": "Repeat-Offence Penalty Advisory",
                "description": (
                    "Retrieves the Table 7 provisions dealing with repeat "
                    "offences without independently determining whether the "
                    "student has previously been found guilty."
                ),
                "conditions": {
                    "domain": "examination_misconduct",
                    "intent": "repeat_offence_inquiry",
                    "repeat_status": "institutionally_verified",
                },
                "actions": {
                    "retrieve": [
                        "KB_EM_023",
                        "KB_EM_024",
                    ],
                    "response_type": "penalty_advisory",
                    "determine_guilt": False,
                    "determine_repeat_status": False,
                    "impose_penalty": False,
                },
                "clause_ids": [
                    "KB_EM_023",
                    "KB_EM_024",
                ],
                "stop_processing": True,
                "requires_human_review": True,
            },
        ]

        # ============================================================
        # SEED CLAUSES
        # ============================================================

        for data in clauses:
            clause, created = PolicyClause.objects.update_or_create(
                clause_id=data["clause_id"],
                defaults=data,
            )

            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully seeded clause: {clause.clause_id}"
                    )
                )
            else:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully updated clause: {clause.clause_id}"
                    )
                )

        # ============================================================
        # SEED RULES
        # ============================================================

        for data in rules:
            rule, created = Rule.objects.update_or_create(
                rule_id=data["rule_id"],
                defaults=data,
            )

            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully seeded rule: {rule.rule_id}"
                    )
                )
            else:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully updated rule: {rule.rule_id}"
                    )
                )

        self.stdout.write(
            self.style.SUCCESS(
                "Domain 2: Examination Misconduct seeding completed successfully."
            )
        )