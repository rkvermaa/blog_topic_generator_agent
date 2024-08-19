from dotenv import load_dotenv
from crewai import Crew
from tasks import BlogContentTasks
from agents import BlogContentAgents
from datetime import datetime


def save_to_markdown(output, filename):
    """Saves the output to a Markdown file."""
    with open(filename, 'w') as file:
        file.write(output)
        
def main():
    load_dotenv()
    
    print("## Welcome to the Data Science Blog Content Creation Crew")
    print('-------------------------------------------------------')
    niche = input("What is the niche or topic you want to write about?\n")
    specific_focus = input("What specific area of this niche are you interested in?\n")
    blog_goal = input("What is the main objective for your blog post (e.g., attract readers, SEO ranking, monetize)?\n")
    
    tasks = BlogContentTasks()
    agents = BlogContentAgents()
    
    # Create agents
    trend_research_agent = agents.research_agent()
    trend_analysis_agent = agents.trend_analysis_agent()
    content_ideation_agent = agents.content_ideation_agent()
    competitor_analysis_agent = agents.competitor_analysis_agent()
    summary_and_planning_agent = agents.summary_and_planning_agent()
    
    # Create tasks
    trend_research_task = tasks.research_task(trend_research_agent, niche, specific_focus)
    trend_analysis_task = tasks.trend_analysis_task(trend_analysis_agent, trend_research_task)
    content_ideation_task = tasks.content_ideation_task(content_ideation_agent, trend_analysis_task, blog_goal)
    competitor_analysis_task = tasks.competitor_analysis_task(competitor_analysis_agent, niche, specific_focus)
    summary_and_planning_task = tasks.summary_and_planning_task(summary_and_planning_agent, trend_research_task, content_ideation_task)
    
    # Set context for tasks
    trend_analysis_task.context = [trend_research_task]
    content_ideation_task.context = [trend_analysis_task]
    summary_and_planning_task.context = [trend_research_task, trend_analysis_task, content_ideation_task, competitor_analysis_task]
    

    # Initialize Crew with agents and tasks
    crew = Crew(
        agents=[
            trend_research_agent,
            trend_analysis_agent,
            content_ideation_agent,
            competitor_analysis_agent,
            summary_and_planning_agent
        ],
        tasks=[
            trend_research_task,
            trend_analysis_task,
            content_ideation_task,
            competitor_analysis_task,
            summary_and_planning_task
        ]
    )
    
    result = crew.kickoff()
    
    print(result)
    # Generate a timestamped filename
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'blog_content_output_{timestamp}.md'

    # Save result to a Markdown file with the timestamped filename
    save_to_markdown(result, filename)
    

if __name__ == "__main__":
    main()
