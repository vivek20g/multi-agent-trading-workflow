import pandas as pd
from transformers import pipeline
from operator import itemgetter
from agents import function_tool
from utils import DataLoader

@function_tool
def get_stock_sentiment_signals(stockname:str):
    
    data_loader = DataLoader()
    config = data_loader.load_config()
    """
        We get 2 types of sentiment signals
        (1) analysing sentiment (bullish, neutral, bearish) in recent (previous week for example) news articles
        (2) Over time, you should have a sentiment trend in your database, so as to avoid recency bias
    """
    excel_file = config['SENTIMENT']['sentiment']
    sheet_name = 'news'
    df_news = data_loader.load_data(excel_file,sheet_name)
    df_news = df_news.sort_values(by='Date')
    df_news['Date'] = pd.to_datetime(df_news['Date'])

    week_start_date = '2025-07-20' # Recent sentiment about the stock, like last week. depend upon data availability
    
    df_specific_news = df_news.loc[(df_news.Stock.apply(lambda x: stockname in x)) & (df_news['Date']>pd.to_datetime(week_start_date))]
    
    news_articles = df_specific_news.loc[:,'News_Synopsis'].values.tolist()
    sentiment_pipeline = pipeline(model="mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis")
    sentiment_results = sentiment_pipeline(news_articles)
    positives=negatives=neutral = 0
    for sentiment in sentiment_results:
      if sentiment['label'] == 'positive':
        positives +=  1
      elif sentiment['label'] == 'negative':
        negatives += 1
      else:
        neutral += 1
    bullish_ratio = round(abs(positives-neutral)/negatives,2)
    
    # what has been the long term sentiment trend for this stock?
    df_sentiment_trend = data_loader.load_data(excel_file, sheetname='sentiment_trend')
    positives = (df_sentiment_trend['Sentiment'] == 'positive').sum()
    negatives = (df_sentiment_trend['Sentiment'] == 'negative').sum()
    neutrals = (df_sentiment_trend['Sentiment'] == 'neutral').sum()
    trend_list = [('positive',positives),('negative',negatives),('neutral',neutrals)]
    trend = max(trend_list, key=itemgetter(1))[0]
   
    return_dict = {'bullish_ratio':bullish_ratio, 'stock_sentiment_trend':trend}

    return return_dict