


from Agents import News_Researcher,News_Summarizer,News_Analyzer,News_Categorize,News_Drafting
from tools import tool



from crewai import Task

# 1. News Gathering Task
news_gathering_task = Task(
    description=(
        "Gather the latest news articles, academic papers, and other relevant sources for {topic}. "
        "Collect articles and papers from reliable sources, summarize the key information, "
        "and provide the URLs where the information was collected."
    ),
    expected_output='A collection of news articles, academic papers, their summaries, and their website URLs.',
    time_limit=15000,
    iteration_limit=800,
    async_execution=False,
    tools=[tool],
    agent=News_Researcher,
    output_file='gathered-news.json'
)

# 2. News Summarization Task
news_summarization_task = Task(
    description=(
        "Summarize the gathered news articles, academic papers, and other sources into concise summaries. "
        "Each summary should highlight the main points and key information of the respective articles and papers."
    ),
    expected_output='A list of summarized news articles, academic papers, '
                    'and other sources with their main points,key information and their URLs.',
    tools=[],
    agent=News_Summarizer,
    async_execution=False,
    time_limit=10000,
    iteration_limit=2000,
    input_file='gathered-news.json',
    output_file='summarized-news.md'
)

# 3. News Analysis Task
news_analysis_task = Task(
    description=(
        "Analyze the summarized news articles to detect sentiment and key trends. "
        "Generate a report detailing the overall sentiment and major trends observed."
    ),
    expected_output='A report on sentiment analysis and detected trends.',
    tools=[],
    agent=News_Analyzer,
    async_execution=False,
    time_limit=2000,
    iteration_limit=300,
    input_file='summarized-news.md',
    output_file='analyzed-news-report.md'
)

# 4. News Categorization Task
news_categorization_task = Task(
    description=(
        "Categorize the summarized and analyzed news articles into predefined sections like politics, "
        "technology, sports, etc. "
        "Ensure that each news item is placed in the appropriate category."
    ),
    expected_output='Categorized news articles.',
    tools=[],  # Assuming categorization is done via LLM or in-built agent capability
    agent=News_Categorize,
    time_limit=1000,
    iteration_limit=100,
    async_execution=False,
    input_files=['summarized-news.md', 'analyzed-news-report.md'],
    output_file='categorized-news.json'
)

# 5. News Drafting Task
news_drafting_task = Task(
    description=(
        "Draft the final news article or bulletin based on the gathered,categorized,analyzed and summarized news. "
        "Ensure clarity, adherence to style, and proper grammar while maintaining engagement."
    ),
    expected_output='A complete draft of the news article or bulletin in markdown format.',
    tools=[],
    agent=News_Drafting,
    time_limit=1000,
    iteration_limit=100,
    async_execution=False,
    input_file=['gathered-news.json','categorized-news.json','summarized-news.md','analyzed-news-report.md'],
    output_file='drafted-news-article.md'
)

