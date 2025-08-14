from agents import Agent, ModelSettings, Runner
from tools import get_stock_price_data

class MarketDataAgent:
    def __init__(self):
        SAMPLE_PROMPT = (
            "You are a stock data extractor and price analysis agent. Perform the following functions -"
            "1. Get the stock price data for stock name passed in input query using the get_stock_price_data tool." 
            "2. Analyse the data returned from get_stock_price_data function/tool and provide a concise summary of the observations "
                "from the market price data . The summary should include price trend, average highs, lows, close prices, "
                "traded volume on a day."
            "3. Comment on the liquidity of the stock based on the data."
        )
        self.agent = Agent(
            name="MarketDataAgent",
            instructions=SAMPLE_PROMPT,
            tools=[get_stock_price_data],
            model_settings=ModelSettings(tool_choice="required")
        )
    async def run(self, query:str):
        result = await Runner.run(self.agent, input=query)
        return result