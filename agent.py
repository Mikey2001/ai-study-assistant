from tools.search_tool import search
from tools.calculator import calculate


class Agent:
    def run(self, query):
        query = query.lower()

        if not query.strip():
            return "Please enter a valid question."

        if "calculate" in query:
            return calculate(query)

        return search(query)
