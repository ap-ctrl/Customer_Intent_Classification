from excel.reader import read_excel_file

df = read_excel_file(
    "input/customer_intelligence_50_entries.xlsx"
)

print(df.head())