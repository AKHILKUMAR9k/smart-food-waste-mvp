# aiagent/agent.py
# aiagent/agent.py

def load_agent():
    class MockAgent:
        def run(self, query):
            query = query.lower()

            if "carrots" in query:
                return "🧺 Currently, 120 carrots are in stock. 30 units will expire in 2 days at Store A. Suggest: donation."

            elif "bread" in query:
                return "🥖 We have 25 loaves of bread available across stores. 10 are expiring tomorrow at Store C."

            elif "milk" in query:
                return "🥛 18 cartons of milk available. 5 expiring in 1 day at Store B. Recommend markdown or donation."

            elif "surplus" in query:
                return "📊 Store B has the highest surplus today: 85 units of vegetables, mostly leafy greens nearing expiry."

            elif "waste" in query or "expired" in query:
                return "♻️ Estimated waste this week: ~8.4 kg. Increase markdowns on perishables."

            elif "donate" in query:
                return "🎁 Suggested donation: 6 dairy and 12 bakery items expiring within 24 hours. NGO alert triggered."

            elif "expiry" in query or "expiring" in query:
                return "⏳ 5 items are expiring in 2 days: Spinach, Yogurt, Lettuce, Strawberries, and Milk."

            elif "ngo" in query or "food bank" in query:
                return "🤝 NGO 'Food Angels' available for pickup 5–7 PM. Suggested donation: fruits & dairy."

            elif "summary" in query or "report" in query:
                return (
                    "📋 Weekly Summary:\n"
                    "- Surplus: 215 units\n"
                    "- Donations: 3 pickups\n"
                    "- Waste prevented: 18.5 kg\n"
                    "- CO₂ saved: 22.7 kg"
                )

            else:
                return f"🤖 Mock AI: Received query — '{query}'"

    return MockAgent()



