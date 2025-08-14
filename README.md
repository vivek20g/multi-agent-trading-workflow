
# Multi-Agent Trading Workflow

This repository implements a **multi-agent trading workflow** that uses advanced AI agents to analyze stocks and provide buy/sell recommendations. The system leverages **OpenAI GPT** as the core large language model (LLM) and the **OpenAI Agents SDK** as the framework for orchestrating agent interactions. The agents collaborate to perform market data analysis, technical analysis, fundamental analysis, sentiment analysis, risk management, and portfolio evaluation.

---

## Table of Contents

1. [Setup Instructions](#setup-instructions)
2. [Business Functionality](#business-functionality)
3. [Workflow Diagram](#workflow-diagram)
4. [Technology Stack](#technology-stack)
5. [How It Works](#how-it-works)
6. [Example Usage](#example-usage)
7. [Running Tests](#running-tests)
8. [Contribution Guidelines](#contribution-guidelines)
9. [License](#license)

---

## Project Setup Instructions

This project uses both Python packages (via `pip`) and system-level dependencies (via `Homebrew`).

### Prerequisites
- Windows 11 (no Homebrew required)
- Mac with Homebrew installed
- Python 3.10 or higher
- (Optional) Linux with Python 3.10+ and pip installed

> **Note:** If you are using Linux, ensure you have Python 3.10+ and pip installed. The setup script may require adaptation for your distribution. If you encounter issues, please refer to your OS documentation for Python environment setup.

### 1. Clone the Repository
Clone the repository to your local machine:
```bash
git clone <repository-url>
cd multi-agent-trading-workflow
```

### 2. Set Up a Virtual Environment & Install Dependencies

#### For mac -
```bash
chmod +x setup.sh
./setup.sh
```
#### For windows -
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements_windows.txt
```

### 3. Add Your OpenAI API Key
Create a `.env` file in the root directory and add your AIOpen API key:
```env
OPENAI_API_KEY="your-openai-api-key"
```

### 4. Run the Application
Execute the main script to start the multi-agent trading workflow:
```bash
python main.py
```
> **Note:** You can see the analysis report in output folder.
---

## Business Functionality

This project is designed to assist traders and investors by providing actionable insights into stock performance. It uses a **multi-agent architecture** where each agent specializes in a specific aspect of stock analysis. The agents collaborate to generate a comprehensive recommendation tailored to the user's risk profile and portfolio goals.

### Key Features:
1. **Market Data Analysis**  
   The `MarketDataAgent` retrieves stock price data and analyzes trends, liquidity, and trading volume.

2. **Technical Analysis**  
   The `TechnicalAnalysisAgent` evaluates technical indicators like RSI, MACD, and Bollinger Bands to identify trading signals.

3. **Fundamental Analysis**  
   The `FundamentalAnalysisAgent` analyzes financial metrics such as P/E ratio, PEG ratio, and growth trends to assess the stock's intrinsic value.

4. **Sentiment Analysis**  
   The `SentimentAnalysisAgent` evaluates recent news articles and social media sentiment to gauge market perception of the stock.

5. **Risk Management**  
   The `RiskManagementAgent` evaluates the stock's risk parameters (e.g., VaR, CVaR) against the customer's risk tolerance.

6. **Portfolio Management**  
   The `PortfolioManagementAgent` consolidates all prior analyses and evaluates the stock recommendation against the customer's portfolio, goals, and constraints.

---

## Workflow Diagram

Below is a high-level diagram of the multi-agent workflow:

```plaintext
+-------------------+       
| MarketDataAgent   |       
| - Fetch stock data|+---------------+       
| - Analyze trends  |                |
+-------------------+                |
                                     v
+-------------------+       +-------------------+       +-------------------+
| SentimentAnalysis |       | TechnicalAnalysis |       |FundamentalAnalysis|
| Agent             |       | Agent             |       | Agent             |
| - News Sentiment  |       | - RSI, MACD, etc. |       | - P/E, PEG, etc.  |
+-------------------+       +-------------------+       +-------------------+
          |                          |                          |
          +--------------------------+--------------------------+
                                     |
                                     v
                          +-------------------+
                          | MetaAgent         |
                          | - Consolidates    |
                          |   analyses        |
                          +-------------------+
                                     |
                                     v
                          +-------------------+
                          | RiskManagement    |
                          | Agent             |
                          | - Evaluate risks  |
                          +-------------------+
                                     |
                                     v
                          +-------------------+
                          | PortfolioManager  |
                          | Agent             |
                          | - Final decision  |
                          +-------------------+
```

---

## Technology Stack

- **OpenAI GPT**: Used as the core LLM for generating insights and recommendations.
- **OpenAI Agents SDK**: Provides the framework for defining and orchestrating agent interactions.
- **Python Libraries**:  
  - `asyncio`: For asynchronous execution of agents.
  - `TA-Lib`: For technical analysis indicators.
  - `yfinance`: For fetching stock market data.
  
---

## How It Works

1. **Input**: The user provides a stock ticker symbol and customer ID.
2. **Agent Workflow**:  
   - The `MarketDataAgent` fetches stock data.
   - The `TechnicalAnalysisAgent`, `FundamentalAnalysisAgent`, and `SentimentAnalysisAgent` run in parallel to analyze the stock.
   - The `MetaAgent` consolidates the outputs from these agents.
   - The `RiskManagementAgent` evaluates the consolidated recommendation against the customer's risk profile.
   - The `PortfolioManagementAgent` provides the final buy/sell recommendation.
3. **Output**: A detailed report with a buy/sell recommendation and supporting rationale.

---

## Example Usage

To run the application with the stock "HDFCBANK" and Customer ID "1", follow these steps:

1. Run the `main.py` file:
   ```bash
   python main.py
   ```

2. When prompted, enter the following:
   ```
   Enter Stock Name> HDFCBANK
   Enter Customer Id> 123
   ```

3. The application will process the inputs through the multi-agent workflow and provide a detailed buy/sell recommendation for the stock "HDFCBANK" based on the customer's profile and market analysis.

---

## Running Tests

To test the workflow, provide inputs interactively when prompted. Ensure that your OpenAI API key is correctly set in the `.env` file and that all dependencies are installed.

---

## Contribution Guidelines

If you'd like to contribute to this project, feel free to fork the repository, make changes, and submit a pull request. Please ensure your code adheres to the existing style and includes appropriate tests.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
```