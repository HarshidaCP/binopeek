import urllib.parse

# Mock data for various service types
MOCK_DATA = {
    "car wash": [
        {"name": "Shine & Go Car Wash", "location": "Downtown", "price": "₹250–400", "rating": 4.3},
        {"name": "QuickClean Auto Spa", "location": "Market Road", "price": "₹200–350", "rating": 4.1},
    ],
    "repair": [
        {"name": "SmartFix Electronics", "location": "City Center", "price": "₹300–600", "rating": 4.4},
        {"name": "TechDoctor Repairs", "location": "Kaloor", "price": "₹250–500", "rating": 4.2},
    ],
    "salon": [
        {"name": "StylePoint Salon", "location": "Panampilly", "price": "₹150–400", "rating": 4.5},
        {"name": "HairCraft Studio", "location": "Edappally", "price": "₹200–500", "rating": 4.3},
    ],
}

def get_suggestions(query: str):
    """
    Interpret the query and return mock suggestions.
    """
    query_lower = query.lower()
    if "car" in query_lower and "wash" in query_lower:
        return MOCK_DATA["car wash"]
    elif "repair" in query_lower or "fix" in query_lower:
        return MOCK_DATA["repair"]
    elif "salon" in query_lower or "hair" in query_lower:
        return MOCK_DATA["salon"]
    else:
        return [ ]


def generate_whatsapp_link(query: str):
    """
    Create a WhatsApp link pre-filled with the user query.
    """
    phone_number = "919800081110"  # your Bino WhatsApp number
    encoded_query = urllib.parse.quote(query)
    return f"https://wa.me/{phone_number}?text={encoded_query}"
