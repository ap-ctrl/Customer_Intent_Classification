import pandas as pd
import os


def read_excel_file(file_path):
    """
    Reads a single Excel file and returns a DataFrame.
    """

    df = pd.read_excel(file_path)
    df.columns = df.columns.str.strip()

    return df
def get_excel_files(input_folder):
    excel_files = []

    for file_name in os.listdir(input_folder):
        if file_name.endswith(".xlsx"):
            excel_files.append(file_name)

    return excel_files