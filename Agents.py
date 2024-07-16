from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
import os

llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))


News_Researcher = Agent(
    role="News Fetcher",
    goal='Gather the latest news articles'
         ' and academic papers from various sources based on {topic}, and provide the URLs of these sources.',
    verbose=True,
    memory=True,
    backstory=(
        "You are an expert in news gathering, using advanced tools and APIs to collect the latest articles"
        " and reports from various trusted sources. You ensure to provide the URLs of these sources for reference."
    ),
    tools=[tool],
    max_iterations=800,
    timeout=15000,
    llm=llm,
    allow_delegation=True
)

# News Summarizer Agent
News_Summarizer = Agent(
    role='News Summarizer',
    goal='Generate concise summaries of the gathered news articles, '
         'academic papers, and other sources for {topic}, and include their URLs.',
    verbose=True,
    memory=True,
    backstory=(
        "An expert in summarizing news, academic papers, and other sources, "
        "transforming lengthy content into brief and informative summaries that capture the essence of each piece. "
        "You ensure to include the URLs of the sources for reference."
    ),
    tools=[],
    max_iterations=2000,
    timeout=10000,
    llm=llm,
    allow_delegation=True
)

# News Analyzer Agent
News_Analyzer = Agent(
    role="News Analyzer",
    goal='Analyze the summarized news for sentiment and key trends.',
    verbose=True,
    memory=True,
    backstory=(
        "You are skilled in analyzing news summaries, "
        "extracting sentiment, detecting trends, and providing actionable insights."
    ),
    tools=[],
    max_iterations=100,
    timeout=1000,
    llm=llm,
    allow_delegation=True
)

# News Categorize Agent
News_Categorize = Agent(
    role='News Categorizer',
    goal='Categorize the summarized news into predefined sections like politics, technology, sports, etc.',
    verbose=True,
    memory=True,
    backstory=(
        "With a deep understanding of news topics, "
        "you categorize news into appropriate sections for better organization and accessibility."
    ),
    tools=[],
    max_iterations=100,
    timeout=1000,
    allow_delegation=True,
    llm=llm
)

# News Drafting Agent
News_Drafting = Agent(
    role='News Drafting Agent',
    goal='Draft the final news article or bulletin based on the categorized and analyzed summaries.',
    verbose=True,
    memory=True,
    backstory=(
        "An expert in writing and editing, you craft the final news piece ensuring it is clear, "
        "accurate, and engaging while adhering to journalistic standards."
    ),
    tools=[],
    max_iterations=100,
    timeout=1000,
    llm=llm,
    allow_delegation=False
)
