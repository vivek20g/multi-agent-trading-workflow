from agents import Agent, ModelSettings, Runner
from tools import get_stock_fundamental_data

class FundamentalAnalysisAgent:
    def __init__(self):
        SAMPLE_PROMPT = (
            
            "You are an agent who performs fundamental analysis of stocks based on stock's fundamentals such as "
            "PE Ratio, PEG Ratio, Sales Growth etc. "
            "You also take into account the macroeconomic indicators and the stock's industry/sector prospects. "
            "You are currently performing the fundamental analysis for a given stock passed in the input query."
            "Perform the follwing tasks in the order,"
            "1. Get the company fundamentals such as PE Ratio, PEG ratio, Sales Growth, EPS Growth, Price-to-Book Value, Dividend Yield etc., "
                "followed by the macroeconomic indicators such as Real GDP Growth Rate forecast, Inflation Rate, Geopolitical Risk etc., "
                "and then the prospects of the industry/sector of the stock such as sector growth prospects and industry median values for PE ratio, Sales Growth etc.,"
                "followed by the company's management commentary on latest earnings report to determine the confidence of the management in company's future prospects,"
                "using get_stock_fundamental_data function. You must use all the parameters returned from the function."
            "2. Analyse all  of the information received from the above step to understand the fundamentals of the company ,company's management perspective s from an investing point of view."
            "3. Based on the analysis of these fundamentals of the stock/company, industry medians & macroeconomic indicators, reason & recommend a  buy or sell signal for the stock."
            
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