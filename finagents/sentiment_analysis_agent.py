from agents import Agent, ModelSettings, Runner
from tools import get_stock_sentiment_signals

class SentimentAnalysisAgent:
    def __init__(self):
        SAMPLE_PROMPT = (
            "You are an agent who performs sentiment analysis based on narrative set in news articles and social media."
            "You are currently performing sentiment analysis for the stock whose symbol is passed in the input query."
            "Perform the follwing tasks in the order,"
            "1. Get the sentiments (positive, negative or neutral) in the news articles for the stock "
                "using get_stock_sentiment_signals tool/function."
            "2. The get_stock_sentiment_signals function returns bullish_ratio & stock_sentiment_trend for the company." 
            "3. bullish_ratio is the ratio of positive sentiments & negative sentiments in recent news articles "
                "and social media posts. Therefore, the higher the ratio, more positive news for the company."
            "4. stock_sentiment_trend is the general trend in last week or last month or last year. "
                "If there are more positive news in the past, the trend is positive otherwise negative or neutral "
                "as the historical sentiment data might indicate to be."
            "5. Based on the sentiment analysis of the stock as in above steps, reason & recommend a buy or sell signal for the stock."
            
          )

        self.agent = Agent(
                  name="SentimentAnalysisAgent",
                  instructions=SAMPLE_PROMPT,
                  tools=[get_stock_sentiment_signals],
                  model_settings=ModelSettings(tool_choice="required")
                )
    async def run(self, query:str):
        result = await Runner.run(self.agent, input=query)
        return result