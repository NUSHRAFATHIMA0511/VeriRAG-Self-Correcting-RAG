def validate_context(question, documents):

    if len(documents) >= 3:
        return 0.92

    return 0.55