from crewai import Task
from datetime import datetime

class StocksTasks():
    def news_fetcher_task(self, agent):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return Task(
            description=(
                f"Collect real-time financial news from the past 60 minutes (as of {current_time}). "
                "Prioritize news with high market impact: earnings releases, M&A activity, "
                "regulatory decisions, and macroeconomic indicators. "
                "Focus on sources with real-time reporting capabilities."
            ),
            agent=agent,
            expected_output=(
                "JSON array of news articles with fields: "
                "timestamp, source, headline, summary, affected_tickers"
            )
        )
        
    def news_stocks_analyzer_task(self, agent, context):
        return Task(
            description=(
                "Analyze news sentiment and immediate market impact. "
                "Calculate urgency score based on news type and market conditions. "
                "Identify affected stocks and estimate magnitude of potential price movement."
            ),
            agent=agent,
            context=context,
            expected_output=(
                "JSON array with fields: "
                "ticker, sentiment_score, urgency_score, expected_impact, confidence"
            )
        )
        
    def stock_predictor_task(self, agent, context):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        return Task(
            description=(
                f"Generate immediate trading signals valid until {current_time}. "
                "Predict price direction (up/down) for next 2 trading hours. "
                "Combine real-time news analysis with technical indicators. "
                "Include confidence level and price target ranges."
            ),
            agent=agent,
            context=context,
            expected_output=(
                "JSON array of predictions with fields: "
                "timestamp, ticker, company_name, prediction, confidence, time_horizon, "
                "price_target, rationale. "
                "Example: {\"ticker\": \"AAPL\", \"prediction\": \"up\", \"confidence\": 0.87}"
            ),
            output_file='./predictions.json'
        )