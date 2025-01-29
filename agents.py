from crewai import Agent
from tools.search_tools import SearchTools  # New tools for Searching News In the Internet
from tools.finance_tools import FinanceTools  # New tools for financial data

class StocksAgents():
    def news_fetcher(self):
        """
        Creates an Agent that specializes in fetching real-time financial news from trusted sources to identify immediate market-moving events.
        The `news_fetcher` Agent is responsible for fetching real-time news articles from trusted sources such as news outlets and financial websites.
        The Agent's primary goal is to identify market-moving events such as breaking news, earnings surprises, and macroeconomic events that create immediate market impact.
        The Agent has access to the `search_internet` tool, which it uses to search the internet for relevant news articles.
        The Agent is verbose, meaning it will print out information about its actions and decisions.
        The Agent has memory, meaning it can remember its past actions and decisions.
        The Agent has a backstory, which is a description of its personality and expertise.

        :return: An Agent that specializes in fetching real-time financial news.
        """
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
        """
        Creates an Agent that specializes in analyzing news sentiment and immediate market impact.
        The `news_stocks_analyzer` Agent is responsible for analyzing news sentiment and immediate market impact.
        The Agent's primary goal is to connect breaking news events to specific stock movements by analyzing the sentiment of news articles and the immediate market impact.
        The Agent has access to the `search_internet` tool, which it uses to search the internet for relevant news articles.
        The Agent has access to the `fetch_historical_prices` tool, which it uses to fetch historical stock prices.
        The Agent is verbose, meaning it will print out information about its actions and decisions.
        The Agent has memory, meaning it can remember its past actions and decisions.
        The Agent has a backstory, which is a description of its personality and expertise.

        :return: An Agent that specializes in analyzing news sentiment and immediate market impact.
        """

        return Agent(
            role='Real-time Market Analyst',
            goal='Analyze news sentiment and immediate market impact',
            tools=[SearchTools.search_internet, FinanceTools.fetch_historical_prices],
            verbose=True,
            memory=True,
            backstory=(
                "Financial analyst specializing in real-time sentiment analysis and "
                "immediate impact assessment of market-moving news. Expert in connecting "
                "breaking events to specific stock movements."
            )
        )
        
    def stock_predictor(self):
        """
        Creates an Agent that specializes in predicting short-term stock movements based on real-time news and market conditions.
        The `stock_predictor` Agent is responsible for generating immediate trading signals for short-term price movements.
        The Agent has access to the `search_internet` tool, which it uses to search the internet for relevant news articles.
        The Agent has access to the `fetch_historical_prices` tool, which it uses to fetch historical stock prices.
        The Agent has access to the `fetch_predictions` tool, which it uses to fetch stock predictions.
        The Agent is verbose, meaning it will print out information about its actions and decisions.
        The Agent has memory, meaning it can remember its past actions and decisions.
        The Agent has a backstory, which is a description of its personality and expertise.

        :return: An Agent that specializes in predicting short-term stock movements based on real-time news and market conditions.
        """
        return Agent(
            role='Algorithmic Trading Strategist',
            goal='Predict short-term stock movements based on real-time news and market conditions',
            tools=[SearchTools.search_internet, FinanceTools.fetch_historical_prices, FinanceTools.fetch_predictions],
            verbose=True,
            memory=True,
            backstory=(
                "Quantitative analyst with expertise in real-time prediction models. "
                "Uses news sentiment, market data, and historical patterns to generate "
                "immediate trading signals for short-term price movements."
            )
        )