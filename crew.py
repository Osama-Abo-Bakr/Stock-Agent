from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from agents import StocksAgents
from tasks import StocksTasks
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.3  # Lower temperature for more factual responses
)

agents = StocksAgents()
tasks = StocksTasks()

news_fetcher = agents.news_fetcher()
analyzer = agents.news_stocks_analyzer()
predictor = agents.stock_predictor()

fetch_task = tasks.news_fetcher_task(news_fetcher)
analysis_task = tasks.news_stocks_analyzer_task(analyzer, [fetch_task])
prediction_task = tasks.stock_predictor_task(predictor, [analysis_task])

crew = Crew(
    agents=[news_fetcher, analyzer, predictor],
    tasks=[fetch_task, analysis_task, prediction_task],
    verbose=True,
    process=Process.sequential,
    manager_llm=llm
)

result = crew.kickoff()
print("Real-Time Market Predictions:")
print(result)