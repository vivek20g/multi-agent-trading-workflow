from agents import Agent, ModelSettings, Runner
from tools import get_stock_price_data

class MarketDataAgent:
    def __init__(self):
        SAMPLE_PROMPT = (
            "You are a market data agent. Given a stockname, use get_stock_price_data to retrieve price and volume data."
            "Summarize trends, average highs/lows/close, and daily volume."
            "Comment on stock liquidity based on this data."
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