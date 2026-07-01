import os

from excel.reader import (
    read_excel_file,
    get_excel_files
)

from excel.writer import write_excel_file

from processors.batch_intent_processor import (
    create_batches,
    classify_intent_batch
)

from config import BATCH_SIZE

INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"

excel_files = get_excel_files(INPUT_FOLDER)

for file_name in excel_files:

    print(f"\nProcessing: {file_name}")

    file_path = os.path.join(
        INPUT_FOLDER,
        file_name
    )

    df = read_excel_file(file_path)

    print(f"Rows found: {len(df)}")

    notes = df["Interaction Notes"].tolist()

    intents = []

    for batch in create_batches(
        notes,
        BATCH_SIZE
    ):

        print(
            f"Processing batch of {len(batch)} notes"
        )

        batch_intents = classify_intent_batch(
            batch
        )

        print(
            f"Expected: {len(batch)} | Received: {len(batch_intents)}"
        )

        if len(batch_intents) != len(batch):

            print("\nBAD BATCH DETECTED")
            print(f"Expected: {len(batch)}")
            print(f"Received: {len(batch_intents)}")

            raise ValueError(
                "Batch size mismatch. "
                "Groq returned a different number of intents."
            )

        intents.extend(
            batch_intents
        )

    print(
        f"Generated {len(intents)} intents"
    )

    if len(intents) != len(df):

        print("\nERROR DETECTED")
        print(f"Rows in Excel     : {len(df)}")
        print(f"Generated Intents : {len(intents)}")

        raise ValueError(
            f"Mismatch! Expected {len(df)} intents "
            f"but received {len(intents)}"
        )

    df["Intent"] = intents

    output_file_name = file_name.replace(
        ".xlsx",
        "_output.xlsx"
    )

    output_path = os.path.join(
        OUTPUT_FOLDER,
        output_file_name
    )

    write_excel_file(
        df,
        output_path
    )

    print(
        f"Saved: {output_file_name}"
    )

print("\nAll files processed successfully!")



# import os

# from excel.reader import (
#     read_excel_file,
#     get_excel_files
# )

# from excel.writer import write_excel_file

# from processors.intent_processor import (
#     classify_intent
# )

# INPUT_FOLDER = "input"
# OUTPUT_FOLDER = "output"

# excel_files = get_excel_files(INPUT_FOLDER)

# for file_name in excel_files:

#     print(f"\nProcessing: {file_name}")

#     file_path = os.path.join(
#         INPUT_FOLDER,
#         file_name
#     )

#     df = read_excel_file(file_path)
#     print(f"Rows found: {len(df)}")

#     intents = []

#     for note in df["Interaction Notes"]:
#         intent = classify_intent(note)
#         intents.append(intent)

#     df["Intent"] = intents

#     output_file_name = file_name.replace(
#         ".xlsx",
#         "_output.xlsx"
#     )

#     output_path = os.path.join(
#         OUTPUT_FOLDER,
#         output_file_name
#     )

#     write_excel_file(
#         df,
#         output_path
#     )

#     print(
#         f"Saved: {output_file_name}"
#     )

# print("\nAll files processed successfully!")




# from excel.reader import read_excel_file
# from processors.intent_processor import classify_intent
# from excel.writer import write_excel_file

# df = read_excel_file(
#     "input/customer_intelligence_50_entries.xlsx"
# )

# intents = []

# for note in df["Interaction Notes"]:
#     intent = classify_intent(note)
#     intents.append(intent)

# df["Intent"] = intents
# write_excel_file(
#     df,
#     "output/customer_intelligence_output.xlsx"
# )

# print("Output file created successfully!")

# print(df[["Customer", "Intent"]].head())
# from excel.reader import read_excel_file
# from processors.intent_processor import classify_intent


# df = read_excel_file(
#     "input/customer_intelligence_50_entries.xlsx"
# )

# note = df.loc[0, "Interaction Notes"]

# print("Customer Note:")
# print(note)

# intent = classify_intent(note)

# print("\nPredicted Intent:")
# print(intent)