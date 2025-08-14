import pandas as pd
from agents import function_tool
from utils import DataLoader

@function_tool
def get_customer_investment_portfolio(customer_id:str):
    data_loader = DataLoader()
    config = data_loader.load_config()
    """
        We get the investment portoflio for the customer,
        which gets all the equities he is invested in
        and also the current cash he holds. 
        this will help the agent to size the position for a buy/sell.
    """
    stockfile_dir = config['PORTFOLIO']['portfolio']
    excel_file = f"{stockfile_dir}"
    sheet_name = 'equity_portfolio'
    data_equity = data_loader.load_data(excel_file,sheet_name)
    
    data_equity = data_equity.loc[data_equity['CustomerId']==int(customer_id)]
    equities = data_equity.to_dict(orient='records')
    
    sheet_name = 'cash_position'
    data_cash = data_loader.load_data(excel_file,sheet_name)
    data_cash = data_cash.loc[data_cash['CustomerId']==int(customer_id)]
    cash_available = data_cash['CashAvailable'].values[0]
    
    current_invested_portfolio_val=0
    stock_position_size = securities = []
    # Calculate the current value of the portfolio and position sizes
    # for each stock in the portfolio
    for equity_data in equities:
        current_invested_portfolio_val += equity_data['NumberOfUnits']*equity_data['CurrentMarketPrice']
        securities.append(equity_data['SecuritySymbol'])
    # Calculate the position size for each stock by using the current_invested_portfolio_val
    for equity_data in equities:
        stock_pos_size = equity_data['NumberOfUnits']*equity_data['CurrentMarketPrice']/current_invested_portfolio_val
        stock_pos_dict = {"stock_name":equity_data['SecuritySymbol'],
                          "stock_postion_size":f"{stock_pos_size:.2%}"
                          }
        stock_position_size.append(stock_pos_dict)

    return_dict = {"Customer_Investment_Portfolio":{
                    "Customer_Portfolio_Total_Current_Value":f" Total Value of Customer's Investment Portfolio is Indian Rupees of {current_invested_portfolio_val:,}",
                    "Stocks_In_Customer_Portfolio":f" Customer has following stocks in his portfolio {securities}.",
                    "Position_Sizes_For_Each_Stock":stock_position_size
                    },
                  "Customer_Cash_Position":f" Customer has cash of Indian Rupees of {cash_available:,} which he can use to buy stocks."
                  
                  }
    
    
    return return_dict
