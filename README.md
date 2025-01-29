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

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/Stock-Agent.git
   cd Stock-Agent
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.8+ installed. Then, install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   - Rename `.env.example` to `.env`.
   - Fill in the required API keys:
     ```plaintext
     OPENAI_API_KEY=your_openai_api_key
     OPENAI_MODEL_NAME=gpt-4
     SERPER_API_KEY=your_serper_api_key
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
   - **Output**: JSON array of news articles with relevant details.

### 2. **News Stocks Analyzer**
   - **Role**: Real-time Market Analyst
   - **Goal**: Analyze news sentiment and immediate market impact.
   - **Output**: JSON array with sentiment scores, urgency scores, and expected impact for affected stocks.

### 3. **Stock Predictor**
   - **Role**: Algorithmic Trading Strategist
   - **Goal**: Predict short-term stock movements based on real-time news and market conditions.
   - **Output**: JSON array of trading signals with predictions, confidence levels, and price targets.

## Tasks Overview

### 1. **News Fetcher Task**
   - Collects real-time financial news from the past 60 minutes.
   - Prioritizes news with high market impact (earnings releases, M&A activity, regulatory decisions, etc.).

### 2. **News Stocks Analyzer Task**
   - Analyzes news sentiment and calculates urgency scores.
   - Identifies affected stocks and estimates potential price movements.

### 3. **Stock Predictor Task**
   - Generates immediate trading signals valid for the next 2 hours.
   - Combines real-time news analysis with technical indicators to predict price direction.

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

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgments

- OpenAI for providing the GPT-4 model.
- Serper API for enabling real-time news search capabilities.