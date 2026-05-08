def calculate(query):
    try:
        expression = query.replace("calculate", "").strip()
        result = eval(expression)
        return f"Result: {result}"
    except Exception:
        return "Error: Invalid mathematical expression"
