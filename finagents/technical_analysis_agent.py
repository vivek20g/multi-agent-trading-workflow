from agents import Agent, ModelSettings, Runner
from tools import get_stock_technical_signals

class TechnicalAnalysisAgent:
    def __init__(self):
        SAMPLE_PROMPT = (
          "You are a technical analysis agent. Given a stockname, use get_stock_technical_signals to retrieve "
          "Bollinger Bands, RSI, MACD, EMA, and ADX."
          "Analyze these indicators and recommend buy or sell with reasoning."
        )
        self.agent = Agent(
                  name="TechnicalAnalysisAgent",
                  instructions=SAMPLE_PROMPT,
                  tools=[get_stock_technical_signals],
                  model_settings=ModelSettings(tool_choice="required")
                )
    async def run(self, query:str):
        result = await Runner.run(self.agent, input=query)
        return result