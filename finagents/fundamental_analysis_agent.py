from agents import Agent, ModelSettings, Runner
from tools import get_stock_fundamental_data

class FundamentalAnalysisAgent:
    def __init__(self):
        
        SAMPLE_PROMPT = (
          "You are a fundamental analysis agent. Given a stockname, use get_stock_fundamental_data to retrieve:"
          "Company fundamentals (PE, PEG, EPS Growth, etc.)"
          "Macroeconomic indicators (GDP, inflation, geopolitical risk)"
          "Industry/sector prospects and medians"
          "Management commentary from earnings reports"
          "Analyze all data and recommend buy or sell with reasoning."
        )
        self.agent = Agent(
                  name="FundamentalAnalysisAgent",
                  instructions=SAMPLE_PROMPT,
                  tools=[get_stock_fundamental_data],
                  model_settings=ModelSettings(tool_choice="required")
                )
    async def run(self, query:str):
        result = await Runner.run(self.agent, input=query)
        return result