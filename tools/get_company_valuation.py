import pandas as pd
from agents import function_tool
from utils import DataLoader

@function_tool
def get_company_valuation(stockname:str):
    data_loader = DataLoader()
    config = data_loader.load_config()
    """
        We look at company's valuation - what will be the price in 5 years, and the associated probablity.
        This will be looked at in combination with customer goals.
    """
    stockfile_dir = config['VALUATION']['stockvaluation']
    excel_file = f"{stockfile_dir}"
    sheet_name = 'CompanyValuation'
    data = data_loader.load_data(excel_file,sheet_name)
    
    data = data[data['NSE_Symbol']==stockname]
    
    estimated_price_5_Years = data['Price_In_5YR'].values[0]
    potential_upside_CAGR = data['Mean_CAGR_Est'].values[0]
    std_dev = data['Std_Dev'].values[0]
    CMP = data['CMP'].values[0]
    est_price_beyond_1_sigma_5Yr =  CMP * ((1+potential_upside_CAGR+std_dev)**5)
    
    return_dict = {
                    "Stock_Current_Market_Price":CMP,
                    "StockPrice_Growth_Prospects_In_5_Years":[
                        {
                        "estimated_price_in_5_Years":estimated_price_5_Years,
                        "potential_upside_CAGR":potential_upside_CAGR,
                        "probability_of_reaching_this_estimated_price_or_higher":"50%"
                        },
                        {
                        "estimated_price_in_5_Years":est_price_beyond_1_sigma_5Yr,
                        "potential_upside_CAGR":(potential_upside_CAGR+std_dev),
                        "probability_of_reaching_this_estimated_price_or_higher":"16%"
                        }
                    ]
                }
          
    return return_dict