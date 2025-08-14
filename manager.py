from finagents import MarketDataAgent
from finagents import TechnicalAnalysisAgent
from finagents import FundamentalAnalysisAgent
from finagents import SentimentAnalysisAgent
from finagents import RiskManagementAgent
from finagents import PortfolioManagementAgent
import time
import asyncio
from agents import Agent, Runner


class PortfolioTradingManager:

    def __init__(self, customer_id:str, stockname:str):
       
        self.customer_id = customer_id
        self.stockname = stockname
        self.query = "Analyse a stock with stockname/ticker-symbol as "+stockname+" for a customer whose customer_id is " +customer_id+" ."

    """
    This class Orchestrates the entire agentic-ai based process for a trading recommendation- 
    (1) MarketDataAgent gets the price history
    (2) TechnicalAnalysisAgent, FundamentalAnalysisAgent, SentimentAnalysisAgent run in parallel
    (3) RiskManagerAgent evaluates recommendation from the prior agents against customer's risk tolerance
    (4) PortfolioManagerAgent evaluates the signals and risk evaluation against customer's investment
        portofio, goals & constraints to provide final recommendation.
    """
    async def run_agent(self, agent, query=None):
        #result = await Runner.run(agent, input=self.query)
        if query is not None:
            result = await agent.run(query)  
        else:
            result = await agent.run(self.query)
        
        return result
    async def orchestrate_workflow(self):

        return
    async def run_agents(self):
        
        """
            This function 'run_agents' follows the typical portfolio trading procedure, in the order of 
            (1) stock analysis, 
            (2) risk evaluation, 
            (3) customer portfolio analysis.
            First, it creates a MetaAgent to orchestrate a sub-process of MarketDataAgent gathering market price
            followed by a group of agents (tech, fundamental, sentiment) running in parallel.
        """
        PROMPT = (
                "You are a meta agent coordinating multiple agents, and so you should show outputs according to the instructions"
                " in each agent. Follow the instructions for processing as following,"
                "1. You are given multiple stock analysis recommendations for the stock "+self.stockname+" from multiple agents,"
                " which are individually based on technical indicators such as RSI, MACD, EMA etc. "
                ",fundamental factors such as PE ratio, PEG ratio, sales and profit growth over last 5 years, "
                " macroeconomic indicators such as real GDP growth rate, inflation rate etc."
                " 2. You are also provided sentiment analysis based on the recent news articles concerning the stock "+self.stockname+" ."
                " 3. Combine these individual recommendations into a detailed & rationalized summary of the stock analysis."
                " 4. Recommend a consolidated buy or sell signal for the stock "+self.stockname+" with reasons for your recommendation."
                
        )
        
        meta_agent = Agent(
            name="MetaAgent",
            instructions=PROMPT
        )
        agent_a = MarketDataAgent()
        agent_b = TechnicalAnalysisAgent()
        agent_c = FundamentalAnalysisAgent()
        agent_d = SentimentAnalysisAgent()
        agent_e = RiskManagementAgent()
        agent_f = PortfolioManagementAgent()        
        
        # handoff from agent a to agent b for tech analysis
        agent_a.agent.handoffs.append(agent_b.agent)
        agent_a.agent.instructions += " After you are done, you must always handoff to TechnicalAnalysisAgent for technical indicators calculations such as Bollinger Bands, MACD etc."
        agent_a.agent.instructions +=" Pass input to TechnicalAnalysisAgent as "+self.query+" ."

        parallel_agents = [
            agent_a,
            agent_c,
            agent_d
        ]
        #asyncio.get_event_loop().run_until_complete(run_agents(parallel_agents, user_input,customer_id))
        
        responses = await asyncio.gather(
            *(self.run_agent(agent) for agent in parallel_agents)
        )

        labeled_summaries = [
            f"### {resp.last_agent.name}\n{resp.final_output}"
            for resp in responses
        ]
        """
        After parallel runs of tech, fundamental & sentiment analysis, 
        consolidate & summarize the outputs from them through a meta agent,
        then run the risk and portfolio analysis in sequence.
        Gather the outputs in a list to be later published as report.
        """

        output = []
        
        # MetaAgent to consolidate the outputs of stock analysis. 
        # This is not a core agent and has been created to show how parallelism can be achieved.
        collected_summaries = "\n".join(labeled_summaries)
        final_summary_meta_output = await Runner.run(meta_agent, input=collected_summaries)
        final_summary_meta = final_summary_meta_output.final_output
        
        output.append(final_summary_meta)

        #Get the risk manager in action with the meta agent output (buy/sell recommendation)
        agent_e = RiskManagementAgent()
        final_summary_meta += ". You should know that you are risk analysing a stock with ticker symbol as "+self.stockname+" for a customer whose customer_id is "+self.customer_id+" ."

        final_summary_risk_output = await self.run_agent(agent_e, final_summary_meta)
        #print('final_summary_risk_output: ',final_summary_risk_output)
        final_summary_risk = final_summary_risk_output.final_output
        output.append(final_summary_risk)

        #Get the portfolio manager in action with the clearance from risk manager on buy/sell recommendation
        agent_f = PortfolioManagementAgent()
        final_summary_risk += ". You should know that you are analysing a stock with ticker symbol as "+self.stockname+" for a customer whose customer_id is "+self.customer_id+" ."
        final_summary_portfolio_output = await self.run_agent(agent_f, final_summary_risk)
        final_summary_portfolio = final_summary_portfolio_output.final_output
        
        output.append(final_summary_portfolio)
        #print('\n')
        text = "Lets us look at the output of MetaAgent, RiskManagementAgent, PortfolioManagementAgent, followed by Exec Summary."
        for word in text.split(sep=' '):
            print(word, end=' ', flush=True)
            time.sleep(0.1)
        print('\n')
        print('Look into the output folder for analysis report')
        #print(*output, sep='\n')

        return output
