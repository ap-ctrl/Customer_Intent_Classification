import json

from serve.groq_client import get_llm_response
from prompts.batch_customer_intelligence_prompt import (
    build_batch_customer_intelligence_prompt
)


def create_batches(notes, batch_size):
    """
    Split interaction notes into batches.
    """
    for i in range(0, len(notes), batch_size):
        yield notes[i:i + batch_size]


def classify_customer_intelligence_batch(notes):

    # ----------------------------------------
    # Build Prompt
    # ----------------------------------------

    prompt = build_batch_customer_intelligence_prompt(notes)

    # ----------------------------------------
    # Call LLM
    # ----------------------------------------

    response = get_llm_response(prompt)

    print("\n==============================")
    print("RAW CUSTOMER INTELLIGENCE RESPONSE")
    print("==============================")
    print(response)

    # ----------------------------------------
    # Parse JSON
    # ----------------------------------------

    try:
        data = json.loads(response)

    except json.JSONDecodeError as e:

        print("\nERROR: Invalid JSON returned by Groq\n")
        print(response)

        raise ValueError(
            "Groq returned invalid JSON."
        ) from e

    # ----------------------------------------
    # Validate JSON
    # ----------------------------------------

    if "results" not in data:

        raise ValueError(
            "Groq response does not contain 'results'."
        )

    print("\n==============================")
    print("CUSTOMER INTELLIGENCE SUMMARY")
    print("==============================")
    print(f"Expected Notes : {len(notes)}")
    print(f"Returned Items : {len(data['results'])}")

    if len(data["results"]) != len(notes):

        print("\nMismatch detected!\n")

        for index, item in enumerate(data["results"], start=1):

            print(f"{index}. {item}")

        raise ValueError(
            f"Groq returned {len(data['results'])} "
            f"results for {len(notes)} notes"
        )

    # ----------------------------------------
    # Extract Intent & Generated Actions
    # ----------------------------------------

    intents = []
    generated_actions = []

    for item in data["results"]:

        # -----------------------
        # Intent
        # -----------------------

        intent = item.get(
            "intent",
            "Unknown"
        )

        intents.append(intent)

        # -----------------------
        # Generated Actions
        # -----------------------

        actions = item.get(
            "generated_actions",
            []
        )

        # If model returns a single string
        if isinstance(actions, str):
            actions = [actions]

        # Remove duplicate actions
        actions = list(dict.fromkeys(actions))

        generated_actions.append(actions)

    print("\nCustomer Intelligence Extraction Successful!\n")

    return intents, generated_actions