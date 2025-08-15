from agents import Agent, ModelSettings, Runner
from tools import get_stock_sentiment_signals

class SentimentAnalysisAgent:
    def __init__(self):
        SAMPLE_PROMPT = (
            "You are a sentiment analysis agent. Given a stockname, use get_stock_sentiment_signals to retrieve:"

            "bullish_ratio (positive vs. negative sentiment)"
            "stock_sentiment_trend (weekly/monthly/yearly trend)"
            "Analyze both and recommend buy or sell with reasoning."
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