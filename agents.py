from crewai import Agent
from tools.search_tools import SearchTools

class StocksAgents():
    def news_fetcher(self):
        return Agent(
            role='Real-time News Aggregator',
            goal='Fetch real-time financial news from trusted sources to identify immediate market-moving events',
            tools=[SearchTools.search_internet],
            verbose=True,
            memory=True,
            backstory=(
                "Expert in real-time news aggregation with a focus on financial markets. "
                "Specializes in identifying breaking news, earnings surprises, and macroeconomic "
                "events that create immediate market impact."
            )
        )
        
    def news_stocks_analyzer(self):
        return Agent(
            role='Real-time Market Analyst',
            goal='Analyze news sentiment and immediate market impact',
            tools=[SearchTools.search_internet],
            verbose=True,
            memory=True,
            backstory=(
                "Financial analyst specializing in real-time sentiment analysis and "
                "immediate impact assessment of market-moving news. Expert in connecting "
                "breaking events to specific stock movements."
            )
        )
        
    def stock_predictor(self):
        return Agent(
            role='Algorithmic Trading Strategist',
            goal='Predict short-term stock movements based on real-time news and market conditions',
            tools=[SearchTools.search_internet],
            verbose=True,
            memory=True,
            backstory=(
                "Quantitative analyst with expertise in real-time prediction models. "
                "Uses news sentiment, market data, and historical patterns to generate "
                "immediate trading signals for short-term price movements."
            )
        )