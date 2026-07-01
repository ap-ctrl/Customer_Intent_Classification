INTENT_CATEGORIES = [
    "Purchase Interest",
    "Expansion Plan",
    "Complaint",
    "Competitor Evaluation",
    "Price Negotiation",
    "Payment Concern",
    "Supply Concern",
    "New Requirement",
    "No Immediate Requirement"
]


def build_intent_prompt(note):
    return f"""
You are a customer intelligence analyst.

Classify the customer note into EXACTLY ONE of the following categories:

Purchase Interest
Expansion Plan
Complaint
Competitor Evaluation
Price Negotiation
Payment Concern
Supply Concern
New Requirement
No Immediate Requirement

Rules:
1. Return ONLY the category name.
2. Do not explain.
3. Do not provide reasoning.
4. Output must match one category exactly.

Customer Note:
{note}
"""