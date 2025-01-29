# Real-Time Stock Market Analysis and Prediction System

This project is a real-time stock market analysis and prediction system that leverages AI agents to fetch financial news, analyze market sentiment, and generate short-term trading signals. The system is built using the `crewai` framework and integrates with OpenAI's GPT-4 model for natural language processing and decision-making.

## Features

- **Real-time News Aggregation**: Fetches the latest financial news from trusted sources to identify market-moving events.
- **Sentiment Analysis**: Analyzes the sentiment of news articles and assesses their immediate impact on specific stocks.
- **Stock Price Prediction**: Predicts short-term stock movements based on real-time news, market conditions, and technical indicators.
- **Sequential Workflow**: Utilizes a sequential process where each agent's output is used as input for the next agent, ensuring a coherent analysis pipeline.

## Project Structure

- **`.env.example`**: Template for environment variables. Rename to `.env` and fill in the required API keys.
- **`.gitignore`**: Specifies files and directories to be ignored by Git, including `.env` and `.txt` files.
- **`agents.py`**: Defines the AI agents responsible for news fetching, sentiment analysis, and stock prediction.
- **`crew.py`**: Sets up the crew of agents, defines the workflow, and kicks off the analysis process.
- **`tasks.py`**: Contains the tasks assigned to each agent, including descriptions and expected outputs.
- **`tools/`**: Contains the tools used by the agents, including:
  - **`finance_tools.py`**: Tools for fetching historical stock prices and predictions.
  - **`search_tools.py`**: Tools for searching the internet for real-time financial news.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/Stock-Agent.git
   cd Stock-Agent
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.10+ installed. Then, install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   - Rename `.env.example` to `.env`.
   - Fill in the required API keys:
     ```plaintext
     OPENAI_API_KEY=your_openai_api_key
     SERPER_API_KEY=your_serper_api_key
     ALPHAVANTAGE_API_KEY=your_alphavantage_api_key
     FINNHUB_API_KEY=your_finnhub_api_key
     ```

4. **Run the System**:
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
   - **Role**: Real-time Market Analyst
   - **Goal**: Analyze news sentiment and immediate market impact.
   - **Tools**: `SearchTools.search_internet`, `FinanceTools.fetch_historical_prices`
   - **Output**: JSON array with sentiment scores, urgency scores, and expected impact for affected stocks.

### 3. **Stock Predictor**
   - **Role**: Algorithmic Trading Strategist
   - **Goal**: Predict short-term stock movements based on real-time news and market conditions.
   - **Tools**: `SearchTools.search_internet`, `FinanceTools.fetch_historical_prices`, `FinanceTools.fetch_predictions`
   - **Output**: JSON array of trading signals with predictions, confidence levels, and price targets.

## Tasks Overview

### 1. **News Fetcher Task**
   - Collects real-time financial news from the past 60 minutes.
   - Prioritizes news with high market impact (earnings releases, M&A activity, regulatory decisions, etc.).
   - **Expected Output**: JSON array of news articles with fields: `timestamp`, `source`, `headline`, `summary`, `affected_tickers`.

### 2. **News Stocks Analyzer Task**
   - Analyzes news sentiment and calculates urgency scores.
   - Identifies affected stocks and estimates potential price movements.
   - **Expected Output**: JSON array with fields: `ticker`, `sentiment_score`, `urgency_score`, `expected_impact`, `confidence`, `historical_data`, `predictions`.

### 3. **Stock Predictor Task**
   - Generates immediate trading signals valid for the next 2 hours.
   - Combines real-time news analysis with technical indicators to predict price direction.
   - **Expected Output**: JSON array of predictions with fields: `timestamp`, `ticker`, `company_name`, `prediction`, `confidence`, `time_horizon`, `price_target`, `rationale`.

## Output

The system outputs real-time market predictions in JSON format, including:
- **Ticker**: The stock symbol.
- **Prediction**: The predicted price direction (up/down).
- **Confidence**: The confidence level of the prediction.
- **Price Target**: The expected price range.
- **Rationale**: The reasoning behind the prediction.

## Example Output

```json
{
  "timestamp": "2023-10-05 14:30",
  "ticker": "AAPL",
  "company_name": "Apple Inc.",
  "prediction": "up",
  "confidence": 0.87,
  "time_horizon": "2 hours",
  "price_target": "180.50 - 182.00",
  "rationale": "Positive earnings surprise and strong technical indicators suggest upward momentum."
}
```

## Dependencies

- `crewai`: Framework for managing AI agents and tasks.
- `langchain_openai`: Integration with OpenAI's GPT-4 model.
- `python-dotenv`: Loads environment variables from `.env` file.
- `langchain`: For creating specific tools.
- `requests`: For making HTTP requests to external APIs.
- `pandas`: For handling and manipulating data.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenAI for providing the GPT-4o model.
- Serper API for enabling real-time news search capabilities.
- FinnHub For real-time perdiction and recommendation in stocks.