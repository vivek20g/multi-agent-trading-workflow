from agents import Agent, ModelSettings, Runner
from tools import get_company_valuation, get_customer_investment_constraints, get_customer_goals, get_customer_investment_portfolio

class PortfolioManagementAgent:
    def __init__(self):
        SAMPLE_PROMPT = (
            "You are a portfolio management agent. Given a stockname and customer_id, analyze the customer's investment portfolio and goals before recommending a buy/sell action."
            "Use the following tools in order:"
            
            "get_customer_investment_portfolio – fetch current holdings, position sizes, and available cash."
            "get_company_valuation – assess 5-year growth prospects and probability metrics."
            "get_customer_investment_constraints – retrieve max stock count and position limits."
            "get_customer_goals – get goal names, timelines, amounts, and required success probabilities."
            "Incorporate buy/sell signals from MetaAgent (technical, fundamental, sentiment) and RiskManagerAgent (risk-based decision)."
            "Analyze all data to ensure recommendations align with portfolio constraints and help achieve customer goals."
            "Provide a detailed rationale, position size, and a clear executive summary for the customer."
        )
        self.agent = Agent(
            name="PortfolioManagementAgent",
            instructions=SAMPLE_PROMPT,
            tools=[get_company_valuation, get_customer_investment_constraints, get_customer_goals, get_customer_investment_portfolio],
            model_settings=ModelSettings(tool_choice="required")
        )
    async def run(self, query:str):
        result = await Runner.run(self.agent, input=query)
        return result