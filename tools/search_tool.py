def search(query):
    knowledge_base = {
        "python": "Python is a high-level programming language.",
        "algorithm": "An algorithm is a step-by-step procedure for solving a problem.",
        "database": "A database is an organized collection of structured information."
    }

    query = query.lower()

    for keyword, answer in knowledge_base.items():
        if keyword in query:
            return answer

    return f"No exact match found. Searching for: {query}"
