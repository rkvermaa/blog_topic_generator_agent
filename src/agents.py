from textwrap import dedent
from crewai import Agent

from tools import TrendSearchToolset, ContentAnalysisToolset, SEOOptimizationToolset

class BlogContentAgents():
    def research_agent(self):
        return Agent(
            role="Trend Research Specialist",
            goal="Conduct thorough research on trending topics in data science, AI, deep learning, NLP, and related fields.",
            tools=TrendSearchToolset.tools(),
            backstory=dedent("""\
                As a Trend Research Specialist, your mission is to uncover the most trending
                and relevant topics in the field of data science. Your insights will guide the 
                content creation process by identifying topics that will attract readers and 
                generate revenue."""),
            verbose=True
        )
      
    def trend_analysis_agent(self):
        return Agent(
            role='Trend Analysis Expert',
            goal='Analyze collected data to identify the most promising topics for blog content.',
            tools=ContentAnalysisToolset.tools(),
            backstory=dedent("""\
                As a Trend Analysis Expert, your role is to analyze the collected data
                from various sources, identify the most trending and engaging topics,
                and predict which topics will perform well in terms of readership and revenue."""),
            verbose=True
        )
      
    def content_ideation_agent(self):
        return Agent(
            role='Content Ideation Specialist',
            goal='Generate blog post ideas, titles, and outlines based on identified trends.',
            tools=SEOOptimizationToolset.tools(),
            backstory=dedent("""\
                As a Content Ideation Specialist, your expertise in content creation will guide
                the development of blog post ideas, compelling titles, and detailed outlines.
                You will ensure that each post is optimized for maximum visibility and engagement."""),
            verbose=True
        )
      
    def competitor_analysis_agent(self): 
        return Agent(
            role='Competitor Analysis Specialist',
            goal='Analyze competitors’ content strategies and identify gaps and opportunities.',
            tools=ContentAnalysisToolset.tools(),
            backstory=dedent("""\
                As a Competitor Analysis Specialist, your role is to examine competitors’ content,
                assess their performance, and identify gaps or opportunities that can be
                leveraged to create more compelling and unique content for the blog."""),
            verbose=True
        )

    def summary_and_planning_agent(self): 
        return Agent(
            role='Content Strategy Coordinator',
            goal='Compile all research and analysis into a detailed content strategy plan.',
            backstory=dedent("""\
                As the Content Strategy Coordinator, your mission is to consolidate all the research,
                analysis, and content ideas into a coherent and actionable content strategy
                plan that will guide the blog’s content creation process."""),
            verbose=True
        )
