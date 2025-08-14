import os
import pandas as pd
from configparser import ConfigParser

class DataLoader:
    #C:/Users/vivek/agentic-ai/multi-agent-trading-workflow
    def __init__(self,base_path="."):
        self.base_path = base_path

    def load_config(self, config_dir='/config', config_filename="filepath.ini"):
        """Load configuration from the given directory."""
        file_path = f"{self.base_path}{config_dir}"
        full_config_path = os.path.join(file_path, config_filename)
        config = ConfigParser()
        config.read(full_config_path)
        return config
        
    def load_data(self, excelfilename:str, sheetname:str):
        excel_file = f"{self.base_path}{excelfilename}"
        data = pd.read_excel(excel_file, sheet_name=sheetname)
        data = data.round(2)
        return data
