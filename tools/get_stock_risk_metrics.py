import pandas as pd
import numpy as np
from datetime import datetime

from agents import function_tool
from utils import DataLoader

@function_tool
def get_stock_risk_metrics(stockname:str):
    data_loader = DataLoader()
    config = data_loader.load_config()
    """
        We get the following risk metrics for the stock from its recent prices 
        VaR (value at risk), CVaR (conditional VaR), Max drawdown
        The agent will analyse these against customer's risk tolerance for a decision on buy/sell
    """
    stockfile_dir = config['DATA']['stockdata_dir']
    excel_file = f"{stockfile_dir}{stockname}.xlsx"
    sheet_name = 'price_history'
    data = data_loader.load_data(excel_file,sheet_name)
    data['Date'] = pd.to_datetime(data['Date'])

    # Assuming a current date for data availability.
    current_date = '2025-08-08'
    specific_date_obj = datetime.strptime(current_date,'%Y-%m-%d')
    lastyeardate = str(specific_date_obj.year-1)+ "-" + str(specific_date_obj.month)+"-"+str(specific_date_obj.day)
    data = data.loc[data['Date']>pd.to_datetime(lastyeardate)]
    data = data.round(2)
    data = data.sort_values(by='Date').reset_index()
    returns = data['Close'].pct_change().dropna()
    
    confidence_level = 0.95
    VaR = np.percentile(returns, (1 - confidence_level) * 100)
    var_threshold = np.percentile(returns, (1 - confidence_level) * 100)
    tail_losses = returns[returns < var_threshold]
    CVaR = tail_losses.mean()

    rolling_data = data['Close'].rolling(window=252,min_periods=1).max()
    daily_drawdown = data['Close']/rolling_data - 1.0
    max_daily_drawdown = daily_drawdown.rolling(window=252, min_periods = 1).min().tolist()
    value = min(max_daily_drawdown)

    return_dict = {"Stock_Risk_Metrics":
                    {
                    "VaR":f"Value at Risk (VaR) at {confidence_level*100}% confidence level is {VaR:.2%}",
                    "CVaR":f"Conditional Value at Risk (CVaR) at {confidence_level*100}% confidence level is {CVaR:.2%}",
                    "Maximum_Daily_Drawdown":f"Maximum drawdown over the last year observed as {value:.2%}"
                  }
                }
    
    return return_dict
