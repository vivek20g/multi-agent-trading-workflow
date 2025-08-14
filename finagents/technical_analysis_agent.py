from agents import Agent, ModelSettings, Runner
from tools import get_stock_technical_signals

class TechnicalAnalysisAgent:
    def __init__(self):
        SAMPLE_PROMPT = (
            "You are a technical analyst of stocks based on stock's historical prices."
            "You are currently analyzing technical indicators for the stock whose ticker/symbol is passed in the input query."
            "Perform the follwing tasks in the order: "
            "1. Calculate technical indicatos like  bollinger bands, RSI, MACD, EMA, ADX using get_stock_technical_signals function." 
            "2. Analyze the technical indicators thus calculated based on stock's price data calculated in the previous step. "
            "3. Based on the analysis of these technical indicators for the stock, reason & recommend a  buy or sell signal for the stock."    
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