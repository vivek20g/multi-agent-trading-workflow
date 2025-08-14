import os
import pandas as pd

class DataWriter:
    def __init__(self, base_path="."):
        self.base_path = base_path
    
    def write_to_file(self, excelfilename:str, sheetname:str, df:pd.DataFrame):
        excel_file = f"{self.base_path}{excelfilename}"
        if not os.path.exists(excel_file):
            # If the file does not exist, create it and write the DataFrame
            df.to_excel(excel_file, sheet_name=sheetname, index=False)
            #print(f"Created new Excel file: {excel_file} and wrote to {sheet_name}")
        else:
            # If the file exists, update the specified sheet
            # Use ExcelWriter in append mode with if_sheet_exists='replace'
            with pd.ExcelWriter(
                excel_file,
                mode='a',
                engine='openpyxl',
                if_sheet_exists='replace'  # Overwrite the sheet if it exists
            ) as writer:
                df.to_excel(writer, sheet_name=sheetname, index=False)
        return