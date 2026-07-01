from processors.batch_intent_processor import (
    classify_intent_batch
)

notes = [
    "Looking for additional 200 MT next month.",
    "Material quality issue observed."
]

intents = classify_intent_batch(notes)

print(intents)