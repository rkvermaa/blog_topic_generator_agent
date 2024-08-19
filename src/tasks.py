from textwrap import dedent
from crewai import Task

class BlogContentTasks():
  
    def research_task(self, agent, topic, target_audience):
        return Task(
            description=dedent(f"""\
                Conduct thorough research on trending topics within the realm of data science, AI,
                deep learning, and NLP. Focus on gathering insights from various sources including
                blogs, social media, and news outlets. Pay attention to topics that resonate with
                the target audience.

                Topic Focus: {topic}
                Target Audience: {target_audience}"""),
            expected_output=dedent(f"""\
                A detailed report summarizing the most trending and relevant topics within the
                specified focus area, including the potential audience engagement."""),
            agent=agent,
            #async_execution=True
        )
    
    def trend_analysis_task(self, agent, collected_data):
        return Task(
            description=dedent(f"""\
                Analyze the collected data to identify key trends, challenges, and opportunities
                in the data science field. Consider search volume, social media engagement, and
                the potential longevity of each trend to prioritize topics.

                Collected Data: {collected_data}"""),
            expected_output=dedent("""\
                An insightful analysis that identifies which topics are currently most
                promising, ranked by their potential to attract readers and generate
                revenue."""),
            agent=agent,
            #async_execution=True
        )
    
    def content_ideation_task(self, agent, analyzed_trends, seo_keywords):
        return Task(
            description=dedent(f"""\
                Generate content ideas, including blog titles, outlines, and key talking points,
                based on the identified trends and SEO-optimized keywords. Ensure that each
                idea aligns with the interests of the target audience.

                Analyzed Trends: {analyzed_trends}
                SEO Keywords: {seo_keywords}"""),
            expected_output=dedent("""\
                A comprehensive list of blog post ideas, complete with titles, outlines, and
                recommended SEO keywords to enhance visibility and engagement."""),
            agent=agent,
            #async_execution=True
        )
    
    def competitor_analysis_task(self, agent, competitors, target_topics):
        return Task(
            description=dedent(f"""\
                Perform a detailed analysis of competitors’ content strategies on the target topics.
                Identify gaps, opportunities, and areas where you can offer unique insights or a
                different angle. Review metrics such as social engagement, shares, and comments.

                Competitors: {competitors}
                Target Topics: {target_topics}"""),
            expected_output=dedent("""\
                A report outlining competitors' strengths and weaknesses, gaps in the content
                landscape, and strategic recommendations for differentiating your blog content."""),
            agent=agent,
            #async_execution=True
        )
    
    def summary_and_planning_task(self, agent, research_results, content_ideas):
        return Task(
            description=dedent(f"""\
                Compile all research findings, trend analysis, and content ideas into a cohesive
                content strategy plan. The plan should include a schedule for blog posts, a strategy
                for SEO optimization, and an overview of the expected engagement for each topic.

                Research Results: {research_results}
                Content Ideas: {content_ideas}"""),
            expected_output=dedent("""\
                A well-structured content strategy document that provides a roadmap for blog posts,
                complete with a posting schedule, SEO strategy, and performance expectations."""),
            agent=agent,
            #async_execution=True
        )
