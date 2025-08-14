import pandas as pd
from agents import function_tool
from utils import DataLoader

@function_tool
def get_stock_fundamental_data(stockname:str):
    
    data_loader = DataLoader()
    config = data_loader.load_config()
    """
        We get 3 sets of data
        (1) Macroeconomic indicators
        (2) Company's fundamentals
        (3) Company's latest earnings call summary
        The agent will analyse these and form a buy/sell signal opinion
    """
    return_dict = {}
    excel_file = config['FUNDAMENTAL']['fundamental']
    
    sheet_name = 'MacroIndicators'
    # get macro data
    macro_data = data_loader.load_data(excel_file,sheet_name)
    
    for row in macro_data.iterrows():
      return_dict[row[1].iloc[0]] = {'Value':row[1].iloc[1], 'Outlook':row[1].iloc[2]}
    #get company specific data
    sheet_name = 'CompanyFundamentalsData'
    company_data = data_loader.load_data(excel_file,sheet_name)
    company_data = company_data[company_data['NSE_Symbol']==stockname]
    
    keycompany = stockname+"_fundamentals"
    return_dict[keycompany] = company_data.to_dict('records')[0]
    

    sheet_name = 'CompanyEarningsCall'
    earnings_call_data = data_loader.load_data(excel_file,sheet_name)
    earnings_call_data = earnings_call_data[earnings_call_data['NSE_Symbol']==stockname]
    latest_earnings_call_summary = earnings_call_data['Latest_Earnings_Call_Summary'].values[0]
    return_dict["management_commentary_on_latest_earnings"] = latest_earnings_call_summary

    # Get the sector data
    sheet_name = 'SectorStockMapping'
    sector_data = data_loader.load_data(excel_file,sheet_name)
    sector_data = sector_data[sector_data['NSE_Symbol']==stockname]
    sector = sector_data['Sector'].values[0]

    sheet_name = 'SectorProspects'
    sector_prospects_data = data_loader.load_data(excel_file,sheet_name)
    sector_prospects_data = sector_prospects_data[sector_prospects_data['Sector']==sector]
    key_1 = stockname+' Industry/Sector'
    
    prospect_dict = {key_1:sector}
    for row in sector_prospects_data.iterrows():
      prospect_dict[row[1].iloc[1]] = {'Value':row[1].iloc[2], 'Outlook':row[1].iloc[3]}
    return_dict['Sector Prospects'] = prospect_dict
    

    sheet_name = 'SectorMedianValues'
    sector_median_data = data_loader.load_data(excel_file,sheet_name)
    sector_median_data = sector_median_data[sector_median_data['Sector']==sector]
    median_dict={key_1:sector}
    columns = sector_median_data.columns[1:]
    for column in columns:
      median_dict[column] = sector_median_data[column].values[0]
    return_dict['Sector Medians'] = median_dict
    
    return return_dict