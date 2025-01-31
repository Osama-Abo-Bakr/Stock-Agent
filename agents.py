from crewai import Agent
from tools.search_tools import SearchTools
from tools.finance_tools import FinanceTools
from crewai import LLM

llm = LLM(
    model="groq/deepseek-r1-distill-llama-70b",
)

class StocksAgents():
    def news_fetcher(self):
        """
        Creates an Agent that specializes in identifying breaking news with market impact potential.

        The `news_fetcher` Agent is responsible for monitoring news sources in real-time to identify
        market-moving events such as earnings surprises, M&A activity, regulatory changes, and
        macroeconomic shifts. The Agent has access to the `search_internet` tool, which it uses to
        search the internet for relevant news articles.

        The Agent is verbose, meaning it will print out information about its actions and decisions.
        The Agent has memory, meaning it can remember its past actions and decisions.
        The Agent has a backstory, which is a description of its personality and expertise.

        :return: An Agent that specializes in identifying breaking news with market impact potential.
        """
        return Agent(
            role='Financial News Radar',
            goal='Identify breaking news with market impact potential',
            tools=[SearchTools.search_internet],
            verbose=True,
            memory=True,
            llm=llm,
            backstory=(
                "A veteran news analyst with 15 years experience tracking market-moving events. "
                "Specializes in real-time identification of earnings surprises, M&A activity, "
                "regulatory changes, and macroeconomic shifts using advanced news monitoring tools."
            )
        )
        
    def news_stocks_analyzer(self):
        """
        Creates an Agent that specializes in analyzing the impact of news events on stock markets.

        The `news_stocks_analyzer` Agent utilizes a combination of natural language processing and
        technical analysis to provide insights into how news events correlate with market movements.
        Equipped with tools for analyzing historical prices, technical indicators, and stock predictions,
        this Agent generates quantitative assessments of news impact.

        The Agent is verbose, meaning it will print out information about its actions and decisions.
        The Agent has memory, meaning it can remember its past actions and decisions.
        The Agent has a backstory, which describes its expertise as a former hedge fund analyst focused
        on sentiment analysis and technical indicator divergence.

        :return: An Agent that quantifies and correlates news events with market movements.
        """
        return Agent(
            role='Quantitative Impact Analyst',
            goal='Correlate news events with market movements',
            tools=[
                SearchTools.search_internet,
                FinanceTools.fetch_historical_prices,
                FinanceTools.analyze_technical,
                FinanceTools.fetch_predictions
                ],
            
            verbose=True,
            memory=True,
            llm=llm,
            backstory=(
                "Former hedge fund analyst combining NLP sentiment analysis with technical "
                "indicators to quantify news impact. Creates urgency scores using SMA/RSI "
                "divergence and trading volume analysis."
            )
        )
        
    def stock_predictor(self):
        """
        Creates an Agent that specializes in generating executable trading signals based on
        real-time news sentiment, technical indicators, and historical price data.

        The `stock_predictor` Agent utilizes a combination of natural language processing and
        technical analysis to generate quantitative assessments of market conditions and
        generate executable trading signals. Equipped with tools for analyzing historical prices,
        technical indicators, and stock predictions, this Agent provides actionable insights into
        short-term price movements.

        The Agent is verbose, meaning it will print out information about its actions and decisions.
        The Agent has memory, meaning it can remember its past actions and decisions.
        The Agent has a backstory, which describes its expertise as a former high-frequency trading
        developer focused on event-driven strategies.

        :return: An Agent that generates executable trading signals based on real-time news
        sentiment and technical indicators.
        """
        return Agent(
            role='Algorithmic Trading Strategist',
            goal='Generate executable trading signals',
            tools=[
                FinanceTools.fetch_historical_prices,
                FinanceTools.fetch_realtime_quote,
                FinanceTools.analyze_technical,
                FinanceTools.fetch_predictions
            ],
            verbose=True,
            memory=True,
            llm=llm,
            backstory=(
                "Ex-high frequency trading developer specializing in event-driven strategies. "
                "Combines MACD crossovers, RSI extremes, and news sentiment to predict "
                "short-term price movements with quantified risk parameters."
            )
        )