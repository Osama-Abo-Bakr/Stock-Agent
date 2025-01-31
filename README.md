# Real-Time Stock Market Analysis and Prediction System

This project is a sophisticated real-time stock market analysis and prediction system that leverages AI agents to fetch financial news, analyze market sentiment, and generate short-term trading signals. Built using the `crewai` framework, the system integrates with advanced language models and financial APIs to provide actionable insights for traders and investors.

## Features

- **Real-time News Aggregation**: Fetches the latest financial news from trusted sources to identify market-moving events.
- **Sentiment Analysis**: Analyzes the sentiment of news articles and assesses their immediate impact on specific stocks.
- **Technical Analysis**: Utilizes technical indicators such as RSI, MACD, and moving averages to evaluate stock conditions.
- **Stock Price Prediction**: Predicts short-term stock movements based on real-time news, market conditions, and technical indicators.
- **Sequential Workflow**: Employs a sequential process where each agent's output is used as input for the next agent, ensuring a coherent and efficient analysis pipeline.

## Project Structure

- **`.env.example`**: Template for environment variables. Rename to `.env` and fill in the required API keys.
- **`.gitignore`**: Specifies files and directories to be ignored by Git, including `.env` and `.txt` files.
- **`agents.py`**: Defines the AI agents responsible for news fetching, sentiment analysis, and stock prediction.
- **`crew.py`**: Sets up the crew of agents, defines the workflow, and kicks off the analysis process.
- **`tasks.py`**: Contains the tasks assigned to each agent, including descriptions and expected outputs.
- **`tools/`**: Contains the tools used by the agents, including:
  - **`finance_tools.py`**: Tools for fetching historical stock prices, real-time quotes, and technical analysis.
  - **`search_tools.py`**: Tools for searching the internet for real-time financial news.

## Setup Instructions

1. **Install Python 3.10+**:
   - Ensure you have Python 3.10 or higher installed. You can download it from the official [Python website](https://www.python.org/downloads/).
   - Verify the installation by running:
     ```bash
     python --version
     ```
     or
     ```bash
     python3 --version
     ```

2. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/Stock-Agent.git
   cd Stock-Agent
   ```

3. **Create a Virtual Environment**:
   To isolate dependencies, create a virtual environment:
   ```bash
   python -m venv venv
   ```

4. **Activate the Virtual Environment**:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

5. **Install Dependencies**:
   Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

6. **Set Up Environment Variables**:
   - Rename `.env.example` to `.env`.
   - Fill in the required API keys:
     ```plaintext
     OPENAI_API_KEY=your_openai_api_key
     SERPER_API_KEY=your_serper_api_key
     FINNHUB_API_KEY=your_finnhub_api_key
     GROQ_API_KEY=your_groq_api_key
     ```

7. **Run the System**:
   Execute the `crew.py` script to start the analysis:
   ```bash
   python crew.py
   ```

## Agents Overview

### 1. **News Fetcher**
   - **Role**: Real-time News Aggregator
   - **Goal**: Fetch real-time financial news from trusted sources to identify immediate market-moving events.
   - **Tools**: `SearchTools.search_internet`
   - **Output**: JSON array of news articles with relevant details.

### 2. **News Stocks Analyzer**
   - **Role**: Quantitative Impact Analyst
   - **Goal**: Analyze news sentiment and immediate market impact using technical indicators.
   - **Tools**: `SearchTools.search_internet`, `FinanceTools.fetch_historical_prices`, `FinanceTools.analyze_technical`
   - **Output**: JSON array with sentiment scores, urgency scores, and expected impact for affected stocks.

### 3. **Stock Predictor**
   - **Role**: Algorithmic Trading Strategist
   - **Goal**: Predict short-term stock movements based on real-time news and market conditions.
   - **Tools**: `FinanceTools.fetch_historical_prices`, `FinanceTools.fetch_realtime_quote`, `FinanceTools.analyze_technical`, `FinanceTools.fetch_predictions`
   - **Output**: JSON array of trading signals with predictions, confidence levels, and price targets.

## Tasks Overview

### 1. **News Fetcher Task**
   - Collects real-time financial news from the past 4 hours.
   - Prioritizes news with high market impact (earnings releases, M&A activity, regulatory decisions, etc.).
   - **Expected Output**: JSON array of news articles with fields: `timestamp`, `source`, `headline`, `affected_tickers`, `summary`.

### 2. **News Stocks Analyzer Task**
   - Analyzes news sentiment and calculates urgency scores.
   - Identifies affected stocks and estimates potential price movements using technical indicators.
   - **Expected Output**: JSON array with fields: `ticker`, `sentiment_score`, `technical_urgency`, `expected_move`, `confidence`.

### 3. **Stock Predictor Task**
   - Generates immediate trading signals valid for the next 2 hours.
   - Combines real-time news analysis with technical indicators to predict price direction.
   - **Expected Output**: JSON array of predictions with fields: `ticker`, `company_name`, `direction`, `confidence`, `timeframe`, `price_target`, `max_risk`, `rationale`.

## Output

The system outputs real-time market predictions in JSON format, including:
- **Ticker**: The stock symbol.
- **Company Name**: The name of the company.
- **Direction**: The predicted price direction (Buy/Sell).
- **Confidence**: The confidence level of the prediction.
- **Timeframe**: The validity period of the prediction.
- **Price Target**: The expected price range.
- **Max Risk**: The maximum risk associated with the trade.
- **Rationale**: The reasoning behind the prediction.

## Example Output

```json
{
  "ticker": "AAPL",
  "company_name": "Apple Inc.",
  "direction": "Buy",
  "confidence": 0.87,
  "timeframe": "2 hours",
  "price_target": "180.50 - 182.00",
  "max_risk": "1.5%",
  "rationale": "Positive earnings surprise and strong technical indicators suggest upward momentum."
}
```

## Dependencies

- **`crewai`**: Framework for managing AI agents and tasks.
- **`langchain_openai`**: Integration with OpenAI's GPT-4 model.
- **`python-dotenv`**: Loads environment variables from `.env` file.
- **`langchain`**: For creating specific tools.
- **`requests`**: For making HTTP requests to external APIs.
- **`pandas`**: For handling and manipulating data.
- **`yfinance`**: For fetching historical stock prices.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **OpenAI** for providing the GPT-4 model.
- **Serper API** for enabling real-time news search capabilities.
- **Finnhub** for providing real-time stock predictions and recommendations.
- **Groq** for providing the high-performance language model used in this project.