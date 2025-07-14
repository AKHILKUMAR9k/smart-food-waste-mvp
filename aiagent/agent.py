# aiagent/agent.py
# aiagent/agent.py
def load_agent():
    class MockAgent:
        def run(self, query):
            query = query.lower()
            # Simulated responses
            if "surplus" in query:
                return "📊 Store B has the highest surplus today: 85 units of vegetables, mostly leafy greens nearing expiry."
            elif "expiry" in query or "expiring" in query:
                return "⏳ 5 items are expiring within 2 days: Spinach, Yogurt, Lettuce, Strawberries, and Milk."
            else:
                return f"🤖 Mock AI: Received query — '{query}'"
    return MockAgent()

