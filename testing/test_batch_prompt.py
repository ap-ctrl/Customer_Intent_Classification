from prompts.batch_intent_prompt import (
    build_batch_intent_prompt
)

notes = [
    "Looking for additional 200 MT next month.",
    "Material quality issue observed."
]

prompt = build_batch_intent_prompt(notes)

print(prompt)