from processors.batch_intent_processor import create_batches

notes = list(range(1, 11))

for batch in create_batches(notes, 3):
    print(batch)