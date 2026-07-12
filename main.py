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

from processors.batch_action_processor import (
    classify_action_batch
)

from config import (
    INTENT_BATCH_SIZE,
    ACTION_BATCH_SIZE
)

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

    # Normalize column names
    df.columns = df.columns.str.strip()

    print(f"Rows found: {len(df)}")

    notes = df["Interaction Notes"].fillna("").tolist()

    # =====================================
    # INTENT EXTRACTION
    # =====================================

    intents = []

    for batch in create_batches(
        notes,
        INTENT_BATCH_SIZE
    ):

        print(
            f"\nIntent Batch : {len(batch)} notes"
        )

        batch_intents = classify_intent_batch(
            batch
        )

        print(
            f"Intent Expected: {len(batch)} | Received: {len(batch_intents)}"
        )

        if len(batch_intents) != len(batch):

            raise ValueError(
                f"Intent mismatch! "
                f"Expected {len(batch)} "
                f"Received {len(batch_intents)}"
            )

        intents.extend(batch_intents)

    if len(intents) != len(df):

        raise ValueError(
            f"Generated {len(intents)} intents "
            f"for {len(df)} rows."
        )

    df["Intent"] = intents

    # =====================================
    # ACTION EXTRACTION
    # =====================================

    actions = []

    for batch in create_batches(
        notes,
        ACTION_BATCH_SIZE
    ):

        print(
            f"\nAction Batch : {len(batch)} notes"
        )

        batch_actions = classify_action_batch(
            batch
        )

        print(
            f"Action Expected: {len(batch)} | Received: {len(batch_actions)}"
        )

        if len(batch_actions) != len(batch):

            raise ValueError(
                f"Action mismatch! "
                f"Expected {len(batch)} "
                f"Received {len(batch_actions)}"
            )

        actions.extend(batch_actions)

    if len(actions) != len(df):

        raise ValueError(
            f"Generated {len(actions)} action rows "
            f"for {len(df)} notes."
        )

    # Convert list into comma separated string
    df["Action Items"] = [
        ", ".join(action_list)
        for action_list in actions
    ]

    # =====================================
    # SAVE OUTPUT
    # =====================================

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
        f"\nSaved: {output_file_name}"
    )

print("\nAll files processed successfully!")
# import os

# from excel.reader import (
#     read_excel_file,
#     get_excel_files
# )

# from excel.writer import write_excel_file

# from processors.batch_intent_processor import (
#     create_batches,
#     classify_intent_batch
# )


# from config import BATCH_SIZE

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

#     notes = df["Interaction Notes"].tolist()

#     intents = []

#     for batch in create_batches(
#         notes,
#         BATCH_SIZE
#     ):

#         print(
#             f"Processing batch of {len(batch)} notes"
#         )

#         batch_intents = classify_intent_batch(
#             batch
#         )

#         print(
#             f"Expected: {len(batch)} | Received: {len(batch_intents)}"
#         )

#         if len(batch_intents) != len(batch):

#             print("\nBAD BATCH DETECTED")
#             print(f"Expected: {len(batch)}")
#             print(f"Received: {len(batch_intents)}")

#             raise ValueError(
#                 "Batch size mismatch. "
#                 "Groq returned a different number of intents."
#             )

#         intents.extend(
#             batch_intents
#         )

#     print(
#         f"Generated {len(intents)} intents"
#     )

#     if len(intents) != len(df):

#         print("\nERROR DETECTED")
#         print(f"Rows in Excel     : {len(df)}")
#         print(f"Generated Intents : {len(intents)}")

#         raise ValueError(
#             f"Mismatch! Expected {len(df)} intents "
#             f"but received {len(intents)}"
#         )

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



