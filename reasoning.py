# backend/reasoning.py

def explain_reasoning(context):
    if not context:
        return "No prior knowledge was found for this question."

    return (
        "This answer is generated based on existing enterprise documents "
        "and previously stored knowledge relevant to the query."
    )
