from crewai import Task
from datetime import datetime

class StocksTasks():
    def news_fetcher_task(self, agent):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return Task(
            description=(
               f"Identify market-moving news from past 4 hours ({current_time})."
                "Filter for events affecting publicly traded companies. "
                "Prioritize by source credibility and ticker mention frequency."
            ),
            agent=agent,
            expected_output=(
                "List[Dict]: Minimum 3 news items with fields - "
                "timestamp, source, headline, affected_tickers, summary"
            )
        )
        
    def news_stocks_analyzer_task(self, agent, context):
        return Task(
            description=(
                "Analyze news impact using: \n"
                "1. Sentiment polarity (-1 to 1 scale) \n"
                "2. Historical volatility (20-day) \n"
                "3. Current RSI/MACD positioning \n"
                "4. Volume spike detection"
            ),
            agent=agent,
            context=context,
            expected_output=(
                "List[Dict]: Analysis for each ticker with - "
                "sentiment_score, technical_urgency (1-5), "
                "expected_move (%), confidence (0-1)"
            )
        )
        
    def stock_predictor_task(self, agent, context):
        return Task(
            description=(
                "Generate 2-hour trading signals with: \n"
                "- Entry/exit price ranges \n"
                "- Stop-loss levels \n"
                "- Risk/reward ratios \n"
                "Prioritize setups with RSI <30/>70 and MACD crosses"
            ),
            agent=agent,
            context=context,
            expected_output=(
                "List[Dict]: Executable signals with - "
                "ticker, company_name, direction (Buy/Sell), confidence (0-1), "
                "timeframe, price_target, max_risk, rationale"
            ),
            output_file='./signals.json'
        )