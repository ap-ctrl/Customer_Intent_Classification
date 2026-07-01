from serve.groq_client import get_llm_response
from prompts.intent_prompt import build_intent_prompt


def classify_intent(note):
    """
    Takes a customer note and returns its intent category.
    """

    prompt = build_intent_prompt(note)

    intent = get_llm_response(prompt)

    return intent.strip()