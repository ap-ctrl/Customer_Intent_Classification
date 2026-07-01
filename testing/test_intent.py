from processors.intent_processor import classify_intent

note = "Inventory sufficient till July."

intent = classify_intent(note)

print("Intent:", intent)