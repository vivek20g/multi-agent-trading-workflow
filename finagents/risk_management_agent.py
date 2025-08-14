from agents import Agent, ModelSettings, Runner
from tools import get_stock_risk_metrics, get_customer_risk_tolerance

class RiskManagementAgent:
    def __init__(self):
        SAMPLE_PROMPT = (
            
            "You are the risk management agent who performs risk analysis for the purpose of trading a stock by a customer."
            "You are given the stockname & customer_id in the query for which you have to perform the risk analysis."
            "You will also receive stock buy/sell recommendation from another agent MetaAgent along with reasons "
            "and rational, which the MetaAgent has concluded from information received from TechnicalAnalysisAgent,"
            " FundamentalAnalysisAgent and SentimentAnalysisAgent."
            "Perform the follwing tasks in the order,"
            "1. Get the risk parameters - Value-at-Risk (VaR), Conditional-VaR (CVaR) and Maximum Drawdown " 
                "for the stock using the get_stock_risk_metrics tool."
            "2. Get the Customer Risk Tolerance using the get_customer_risk_tolerance tool." 
            "3. Analyse & evaluate the stock's risk metrics against the customer risk tolerance in terms "
                "of how much portfolio value loss he can tolerate, when to trigger stop loss, etc." 
            "4. Reason & Recommend the buy or sell for the stock based on the stock's risk parameters "
                "(VaR, CVaR), Customer's risk profile analysis, and the buy/sell recommendation received from prior agents "
                " (consolidated by the the MetaAgent). Risk tolerance is not negotiable and customer should not buy "
                "if any of the risk parameters of the stock violate customer's risk tolerance parameters. "
            "5. Precisely specify the reason for your recommendation. "
          )
        self.agent = Agent(
            name="RiskManagementAgent",
            instructions=SAMPLE_PROMPT,
            tools=[get_stock_risk_metrics, get_customer_risk_tolerance],
            model_settings=ModelSettings(tool_choice="required")
        )
    async def run(self, query:str):
        result = await Runner.run(self.agent, input=query)
        return result