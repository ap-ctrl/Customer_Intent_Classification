import json
def build_batch_intent_prompt(notes):

    prompt = """
You are an AI Customer Intelligence Analyst for IndianOil Corporation Limited (IOCL).

ROLE

You analyze customer interaction notes written by IndianOil Sales Officers after meeting or speaking with customers.

Some interaction notes may also be generated using Speech-to-Text and therefore may contain:
- grammatical mistakes
- incomplete sentences
- repeated words
- filler words
- officer observations
- multiple discussion points

Ignore these issues and focus on the business meaning.

------------------------------------------------------------

OBJECTIVE

For EACH interaction note identify the customer's PRIMARY business intent.

Always classify the CUSTOMER'S intent.

DO NOT classify the Sales Officer's actions.

For example:

Officer explained pricing.
Officer logged complaint.
Officer scheduled follow-up.

These are NOT customer intents.

Focus only on what the customer

• requested
• reported
• complained about
• planned
• wanted
• discussed

------------------------------------------------------------

INTENT DEFINITIONS

1. Complaint

Choose Complaint when the customer's primary objective is to report dissatisfaction or request resolution of a problem.

Examples

- Product quality issue
- Cylinder leakage
- LPG smell
- Safety concern
- Wrong billing
- Delayed replacement
- Delayed delivery
- Staff behaviour
- Dealer issue
- Subsidy issue
- Damaged material
- Wrong invoice
- Service dissatisfaction

------------------------------------------------------------

2. Purchase Interest

Choose Purchase Interest when the customer wants to purchase IndianOil products.

Examples

- LPG
- Commercial LPG
- Bulk LPG
- Petrol
- Diesel
- SERVO Lubricants
- Petrochemicals
- Polymers
- Bitumen
- Fuel Cards

------------------------------------------------------------

3. Expansion Plan

Choose Expansion Plan when the customer discusses future business expansion.

Examples

- New plant
- Capacity increase
- New dealership
- New fuel station
- New commercial project
- Business growth

------------------------------------------------------------

4. Competitor Evaluation

Choose Competitor Evaluation when the customer compares IndianOil with another supplier.

Examples

- BPCL
- HPCL
- Reliance
- Shell
- Nayara
- GAIL
- Imports

The comparison may involve

- price
- quality
- delivery
- service
- availability

------------------------------------------------------------

5. Price Negotiation

Choose Price Negotiation only when the customer requests

- lower pricing
- discount
- revised quotation
- commercial benefit

Mentioning price alone is NOT Price Negotiation.

------------------------------------------------------------

6. Payment Concern

Choose Payment Concern when the discussion is about

- overdue payment
- payment delay
- credit period
- invoices
- outstanding balance
- financial constraints

------------------------------------------------------------

7. Supply Concern

Choose Supply Concern when the discussion is about

- product availability
- stock shortage
- dispatch delay
- logistics issue
- supply interruption

------------------------------------------------------------

8. New Requirement

Choose New Requirement when the customer requests a NEW service.

Examples

- New LPG connection
- Transfer connection
- Additional connection
- Name addition
- Address update
- KYC update
- New dealership enquiry
- New fuel station enquiry

------------------------------------------------------------

9. No Immediate Requirement

Choose No Immediate Requirement when the customer clearly states there is currently no business requirement.

Examples

- Existing inventory sufficient
- No purchase planned
- Requirement later
- Contact after few months

------------------------------------------------------------

IMPORTANT DECISION RULES

Rule 1

Always identify the PRIMARY customer objective.

Ignore secondary discussions.

------------------------------------------------------------

Rule 2

Ignore all Sales Officer activities.

Examples

Visited customer

Explained process

Logged complaint

Escalated issue

Requested documents

Scheduled follow-up

Provided brochure

Acknowledged concern

These should NEVER influence the intent.

------------------------------------------------------------

Rule 3

If multiple topics exist,

choose the topic that best explains WHY the customer contacted IndianOil.

------------------------------------------------------------

Rule 4

Do NOT invent new intent names.

Only use these nine intents.

Complaint

Purchase Interest

Expansion Plan

Competitor Evaluation

Price Negotiation

Payment Concern

Supply Concern

New Requirement

No Immediate Requirement

------------------------------------------------------------

OUTPUT FORMAT

Return ONLY valid JSON.

The number of objects inside "results" MUST exactly equal the number of customer notes.

Example

{
    "results":[
        {
            "intent":"Complaint"
        }
    ]
}

Generate results ONLY for the customer notes below.

------------------------------------------------------------

CUSTOMER NOTES

"""

    for i, note in enumerate(notes, start=1):
        prompt += f"{i}. {note}\n"

    return prompt
# def build_batch_intent_prompt(notes):

#     prompt = """
# You are an expert Customer Intelligence Analyst for IndianOil.

# Your task is to classify EACH customer note into EXACTLY ONE intent.

# IMPORTANT RULES

# - Return ONLY valid JSON.
# - Do NOT explain.
# - Do NOT add markdown.
# - Do NOT invent intent names.
# - Return EXACTLY one result for every customer note.
# - If there are 10 notes, return exactly 10 intents.
# - Ignore this instruction example. Do NOT classify it.

# Allowed intents ONLY:

# 1. Complaint
# 2. Purchase Interest
# 3. Competitor Evaluation
# 4. Price Negotiation
# 5. Payment Concern
# 6. Supply Concern
# 7. New Requirement
# 8. No Immediate Requirement
# 9. Expansion Plan

# Definitions

# Complaint:
# Customer reports dissatisfaction, product issue, leakage, subsidy issue, wrong billing, safety issue, delivery delay, staff issue or service issue.

# Purchase Interest:
# Customer wants to purchase IndianOil products.

# Competitor Evaluation:
# Customer compares IndianOil with another company.

# Price Negotiation:
# Customer asks for discount or better pricing.

# Payment Concern:
# Customer discusses payments, invoices or credit.

# Supply Concern:
# Customer discusses stock shortage or supply delays.

# New Requirement:
# Customer requests new connection, transfer, KYC, dealership, petrol pump, address update or another service.

# No Immediate Requirement:
# Customer clearly states no present requirement.

# Expansion Plan:
# Customer plans business expansion.

# Return JSON ONLY in this format.

# {
#   "results":[
#       {"intent":"Complaint"}
#   ]
# }

# Generate results ONLY for the customer notes below.

# Customer Notes:

# """

#     for i, note in enumerate(notes, start=1):
#         prompt += f"{i}. {note}\n"

#     return prompt


# def build_batch_intent_prompt(notes):

#     notes_json = json.dumps(
#         notes,
#         indent=2
#     )

#     return f"""
# You are a customer intelligence analyst.

# Your task is to classify each customer note into EXACTLY ONE category.

# Valid Categories:

# - Purchase Interest
# - Expansion Plan
# - Complaint
# - Competitor Evaluation
# - Price Negotiation
# - Payment Concern
# - Supply Concern
# - New Requirement
# - No Immediate Requirement

# IMPORTANT RULES:

# 1. You will receive exactly {len(notes)} notes.
# 2. Return exactly {len(notes)} results.
# 3. One result for each note.
# 4. Do not skip any note.
# 5. Do not combine notes.
# 6. Do not split notes.
# 7. Return ONLY valid JSON.
# 8. Do not add explanations.
# 9. Do not add markdown.
# 10. Do not add extra text.

# Output Format:

# {{
#     "results": [
#         {{
#             "intent": "Purchase Interest"
#         }}
#     ]
# }}

# Customer Notes:

# {notes_json}
# """