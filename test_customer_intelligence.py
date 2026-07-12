import os

from excel.reader import (
    read_excel_file,
    get_excel_files
)

from excel.writer import (
    write_excel_file
)

from processors.batch_customer_intelligence_processor import (
    create_batches,
    classify_customer_intelligence_batch
)

# ------------------------------------
# CONFIGURATION
# ------------------------------------

INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"

# Since this is only testing,
# keep batches small.
BATCH_SIZE = 5

# ------------------------------------
# READ FILES
# ------------------------------------

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

    intents = []

    generated_actions = []

    # ------------------------------------
    # PROCESS BATCHES
    # ------------------------------------

    for batch in create_batches(
        notes,
        BATCH_SIZE
    ):

        print(
            f"\nProcessing batch of {len(batch)} notes..."
        )

        batch_intents, batch_actions = (
            classify_customer_intelligence_batch(
                batch
            )
        )

        intents.extend(batch_intents)

        generated_actions.extend(batch_actions)

    # ------------------------------------
    # VALIDATION
    # ------------------------------------

    if len(intents) != len(df):

        raise ValueError(
            f"Expected {len(df)} intents "
            f"but received {len(intents)}"
        )

    if len(generated_actions) != len(df):

        raise ValueError(
            f"Expected {len(df)} generated actions "
            f"but received {len(generated_actions)}"
        )

    # ------------------------------------
    # WRITE OUTPUT
    # ------------------------------------

    df["Intent"] = intents

    df["Generated Actions"] = [

        "\n".join(action_list)

        for action_list in generated_actions
    ]

    output_file_name = file_name.replace(
        ".xlsx",
        "_customer_intelligence.xlsx"
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

print("\nCustomer Intelligence testing completed successfully!")