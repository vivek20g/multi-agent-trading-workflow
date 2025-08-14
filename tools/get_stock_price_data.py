import yfinance as yf
import pandas as pd

from agents import function_tool
from utils import DataLoader, DataWriter

@function_tool
def get_stock_price_data(stockname:str):
    data_loader = DataLoader()
    data_writer = DataWriter()
    config = data_loader.load_config()
    stockfile_dir = config['DATA']['stockdata_dir']
    stockdata = yf.Ticker(stockname+".NS")
    data = stockdata.history(period="2Y")
    df = data.reset_index()
    df = df.sort_values(by='Date', ascending=False)
    df = df[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
    df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')

    excel_file = f"{stockfile_dir}{stockname}.xlsx"
    sheet_name = 'price_history'
    data_writer.write_to_file(excel_file,sheet_name,df)

    df_first_14 = df.head(14).round(2)
    return_dict = df_first_14.to_dict(orient='records') 

    return {"market_price_data":return_dict}
