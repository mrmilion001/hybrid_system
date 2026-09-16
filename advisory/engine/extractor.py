import re


def extract_parameters(normalized_query, intent):
    """
    Extract structured parameters from a normalized query.

    Returns a dictionary containing the parameters
    identified in the query.
    """

    parameters = {}

    if intent == "academic_status":
        cgpa_match = re.search(
            r"\bcgpa\b\s*(?:is|of|=|:)?\s*(\d+(?:\.\d+)?)",
            normalized_query
        )

        if cgpa_match:
            parameters["cgpa"] = float(cgpa_match.group(1))

    if intent == "academic_grievances" or intent == "examination_regulations":
        if re.search(
            r"\b(cbt|computer[-\s]based(?:\s+test)?)\b",
            normalized_query
        ):
            parameters["exam_format"] = "CBT"

        elif re.search(
            r"\b(omr|optical\s+mark\s+reader)\b",
            normalized_query
        ):
            parameters["exam_format"] = "OMR"

    # Catch missing exams, absence, or failure to sit for examinations
    if re.search(
        r"\b(missing|missed|absent|absence|fail(ed)?\s+to\s+sit|skipped)\s+(an\s+)?exam\b",
        normalized_query,
        re.IGNORECASE
    ):
        parameters["inquiry_sub_type"] = "exam_absence"

    return parameters