import talib
import pandas as pd
from agents import function_tool
from utils import DataLoader

@function_tool
def get_stock_technical_signals(stockname:str):
    print('get_stock_technical_signals stockname:',stockname)
    data_loader = DataLoader()
    config = data_loader.load_config()
    """
        We get the following technical signals from recent stock prices 
        BollingerBands, RelativeStrengthIndex, MACD, Exp Moving Avg, ADX
        The agent will analyse these and form a buy/sell signal opinion
    """
    stockfile_dir = config['DATA']['stockdata_dir']

    excel_file = f"{stockfile_dir}{stockname}.xlsx"
    
    sheet_name = 'price_history'
    data = data_loader.load_data(excel_file,sheet_name)

    data = data.head(50)
    
    close_price_series = data['Close']
    prices = close_price_series.to_numpy()
    high_price_series = data['High']
    high = high_price_series.to_numpy()
    low_price_series = data['Low']
    low = low_price_series.to_numpy()
    

    upper,middle,lower = talib.BBANDS(prices,timeperiod=14)
    macd, signal,hist = talib.MACD(prices)
    
    return_dict =  {
        'bollinger':{'upper': upper,'middle': middle,'lower': lower},
        'rsi': talib.RSI(prices,timeperiod=14),
        'macd': {'macd': macd, 'signal': signal, 'hist': hist}, 
        'ema': talib.EMA(prices,timeperiod=20),
        'adx': talib.ADX(high,low,prices,timeperiod=14)
    }
    
    return return_dict