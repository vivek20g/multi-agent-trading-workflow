import pandas as pd
from datetime import datetime

from agents import function_tool
from utils import DataLoader

@function_tool
def get_customer_risk_tolerance(customer_id:str):
    data_loader = DataLoader()
    config = data_loader.load_config()
    """
        We get the following risk tolerance params for the customer
        max account loss and stop loss for any stock.
        The agent will analyse these against stock's risk metrics for a decision on buy/sell
    """
    stockfile_dir = config['RISKPROFILE']['riskprofile']
    excel_file = f"{stockfile_dir}"
    sheet_name = 'risk_profile'
    data = data_loader.load_data(excel_file,sheet_name)
    
    data = data.loc[data['CustomerId']==int(customer_id)]
    risk_profile = data['RiskProfile'].values[0]
    risk_profile_desc = data['RiskProfileDesc'].values[0]
    max_account_loss = data['MaximumAccountRisk'].values[0]
    stoploss_percent = data['StopLossPricePercentage'].values[0]
    
    return_dict = {
                    "Customer_Risk_Profile": risk_profile,
                    "Risk_Profile_Descriptions": risk_profile_desc,
                    "Customer_Risk_Tolerance_Paraemeters":{
                        "Maximum_Account_Loss":f" Customer can tolerare a maximum portfolio loss of {max_account_loss:.2%}",
                        "Stop_Loss":f" Stop any further loss by triggering a sell of stock if its current market price falls by {stoploss_percent:.2%} of average buy price."
                    }
                  }

    return return_dict
