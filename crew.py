from crewai import Crew,Process
from Agents import News_Researcher,News_Summarizer,News_Analyzer,News_Categorize,News_Drafting
from tasks import news_gathering_task,news_summarization_task,news_analysis_task,news_categorization_task,news_drafting_task

## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[News_Researcher,News_Summarizer,News_Analyzer,News_Categorize,News_Drafting],
    tasks=[news_gathering_task,news_summarization_task,news_analysis_task,news_categorization_task,news_drafting_task],
    process=Process.sequential,

)

## starting the task execution process wiht enhanced feedback

result=crew.kickoff(inputs={'topic':'AI in Accounting'})
print(result)