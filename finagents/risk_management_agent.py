from agents import Agent, ModelSettings, Runner
from tools import get_stock_risk_metrics, get_customer_risk_tolerance

class RiskManagementAgent:
    def __init__(self):
        SAMPLE_PROMPT = (
            "You are a risk management agent. Given a stockname and customer_id, assess the stock's risk and recommend a buy/sell action."
            "Use the following tools in order:"

            "get_stock_risk_metrics – fetch VaR, CVaR, and Max Drawdown."
            "get_customer_risk_tolerance – retrieve customer's risk limits."
            "Compare stock risk metrics with customer tolerance (loss limits, stop-loss triggers)."
            "Incorporate MetaAgent’s buy/sell signal and rationale (based on technical, fundamental, sentiment analysis)."
            "If any risk metric exceeds tolerance, reject the trade."
            "Recommend buy/sell only if risk is acceptable."
            "Clearly explain your reasoning behind the decision."

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