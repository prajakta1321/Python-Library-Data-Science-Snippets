import os
import pandas as pd

# 1. Update your folder path
folder_path = r"C:\Users\admin\Desktop\tommy\nom"   # CHANGE THIS

# 2. Excel file name
file_name = "test_excel.xlsx"   # your downloaded file

# Full path
file_path = os.path.join(folder_path, file_name)

# 3. Read all sheets
all_sheets = pd.read_excel(file_path, sheet_name=None)

# 4. Store filtered data
filtered_sheets = {}

# 5. Apply different conditions for each sheet
for sheet_name, df in all_sheets.items():

    if sheet_name == "Sheet1":
        # Keep rows where Color is Blue or White
        filtered_df = df[df["Color"].isin(["Blue", "White"])]

    elif sheet_name == "Sheet2":
        # Keep rows where Score > 50
        filtered_df = df[df["Score"] > 50]

    elif sheet_name == "Sheet3":
        # Keep rows where Status is Approved
        filtered_df = df[df["Status"] == "Approved"]

    else:
        # If any extra sheet exists
        filtered_df = df

    # Save with new sheet name
    filtered_sheets[f"{sheet_name}_Filtered"] = filtered_df

# 6. Save output file
output_path = os.path.join(folder_path, "filtered_output.xlsx")

with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
    for sheet_name, df in filtered_sheets.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print("Filtered Excel file created successfully!")
