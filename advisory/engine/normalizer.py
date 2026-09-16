import re


def normalize_query(query):
    """
    Normalize a student's natural-language query
    before further processing by the advisory engine.
    """

    if not isinstance(query, str):
        return ""

    # Convert to lowercase
    text = query.lower()

    # Replace punctuation with spaces
    text = re.sub(r"[^\w\s]", " ", text)

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text

