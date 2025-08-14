import pandas as pd
from agents import function_tool
from utils import DataLoader

@function_tool
def get_customer_investment_constraints(customer_id:str):
    data_loader = DataLoader()
    config = data_loader.load_config()
    """
        We get the investment constraints for the customer,
       regarding maximum number of stocks in portfolio, maximum position of a stock 
       in a protfolio.
    """
    stockfile_dir = config['PORTFOLIO']['portfolio']
    excel_file = f"{stockfile_dir}"
    sheet_name = 'diversification'
    data_diversification = data_loader.load_data(excel_file,sheet_name)
    data_diversification = data_diversification.loc[data_diversification['CustomerId']==int(customer_id)]
    diversification_params = data_diversification.to_dict(orient='records')

    max_no_of_positions=max_positions_size=take_profit_at_gain = 0
      
    for parameter in diversification_params:
        
        if parameter['Parameter'] == 'MaxNumberOfPositions':
            max_no_of_positions = parameter['Value']
        elif parameter['Parameter'] == 'MaxPositionSize':
            max_positions_size = parameter['Value']
        elif parameter['Parameter'] == 'TakeProfitPricePercentage':
            take_profit_at_gain = parameter['Value']
    
    return_dict = {"Customer_Investment_Constraints":{
                    "Maximum_No_Of_Stocks":f" Customer can tolerate a maximum number of {max_no_of_positions} stocks in its portfolio ",
                    "Maximum_Position_In_Particular_Stock":f" Customer can tolerate a maximum position of total {max_positions_size:.2%} of current portfolio value in a particular stock ",
                    "Take_Profit_At":f" Book Profit by triggering a sell of stock if its current market price is {take_profit_at_gain:.2%} over and above the average buy price."
                    }
                  }
    
    return return_dict