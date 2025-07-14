# aiagent/agent.py

def load_agent():
    class MockAgent:
        def run(self, query):
            print("🛠 Received Query:", query)
            query = query.lower()

            if "carrot" in query:
                return "🥕 120 carrots are in stock. 30 units expiring in 2 days at Store A."

            elif "bread" in query or "milk" in query:
                return "🥖 Store C has 15 bread loaves and 10 milk cartons expiring in 1 day."

            elif "surplus" in query:
                return "📊 Store B has the highest surplus today: 85 units of vegetables."

            elif "waste" in query or "expired" in query:
                return "♻ Projected food waste: ~8.4 kg this week."

            elif "donate" in query:
                return "🎁 Donate 6 dairy items & 12 bakery products. Alerting nearby food bank."

            elif "expiry" in query or "expiring" in query:
                return "⏳ 5 items expiring soon: Spinach, Yogurt, Lettuce, Strawberries, Milk."

            elif "which store" in query or "store with most" in query:
                return "🏬 Store B has most surplus. Suggest redistribution."

            elif "ngo" in query or "food bank" in query:
                return "🤝 Nearby NGO 'Food Angels' available for pickup 5–7 PM."

            elif "summary" in query or "report" in query:
                return ("📋 Weekly Summary:\n"
                        "- Surplus: 215 units\n- Donations: 3 pickups\n"
                        "- Waste prevented: 18.5 kg\n- CO₂ saved: 22.7 kg")

            else:
                return f"🤖 Mock AI: I received your query — '{query}'"
    return MockAgent()

