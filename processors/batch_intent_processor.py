import json

from serve.groq_client import get_llm_response
from prompts.batch_intent_prompt import (
    build_batch_intent_prompt
)


def create_batches(notes, batch_size):

    for i in range(0, len(notes), batch_size):
        yield notes[i:i + batch_size]

def classify_intent_batch(notes):

    prompt = build_batch_intent_prompt(notes)

    response = get_llm_response(prompt)

    print("\nRAW RESPONSE:")
    print(response)

    # -----------------------------
    # Clean the response
    # -----------------------------
    response = response.strip()

    # Remove markdown if present
    response = response.replace("```json", "")
    response = response.replace("```", "")

    # Keep only the JSON part
    start = response.find("{")

    if start == -1:
        raise ValueError("Groq did not return valid JSON.")

    response = response[start:]

    print("\nCLEANED RESPONSE:")
    print(response)

    # Convert JSON text to Python dictionary
    data = json.loads(response)

    # Validate output length
    if "results" not in data:
        raise ValueError("JSON does not contain 'results'.")

    if len(data["results"]) != len(notes):
        raise ValueError(
            f"Groq returned {len(data['results'])} results "
            f"for {len(notes)} notes"
        )

    intents = []

    for item in data["results"]:
        intents.append(item["intent"])

    return intents
# def classify_intent_batch(notes):

#     prompt = build_batch_intent_prompt(notes)

#     response = get_llm_response(prompt)

#     print("\nRAW RESPONSE:")
#     print(response)

#     data = json.loads(response)
#     print(type(data))
#     print(data)
#     if len(data["results"]) != len(notes):

#      raise ValueError(
#         f"Groq returned "
#         f"{len(data['results'])} results "
#         f"for {len(notes)} notes"
#     )

#     intents = []

#     for item in data["results"]:
#         intents.append(item["intent"])

#     return intents
# def classify_intent_batch(notes):

#     prompt = build_batch_intent_prompt(notes)

#     response = get_llm_response(prompt)
#     data = json.loads(response)

#     print(response)

#     return response
# def create_batches(notes, batch_size):
#     """
#     Splits a list into smaller batches.
#     """

#     for i in range(0, len(notes), batch_size):
#         yield notes[i:i + batch_size]