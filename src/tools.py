import os
from exa_py import Exa
from langchain.agents import tool

class TrendSearchToolset():
  
    @tool
    def search_trending_topics(query: str):
        """Search for trending topics in data science and related fields."""
        return TrendSearchToolset._exa().search(f"{query} trending topics", use_autoprompt=True, num_results=3)
    
    @tool
    def search_social_media_trends(query: str):
        """Search for trending topics on social media related to data science."""
        return TrendSearchToolset._exa().search(f"site:twitter.com {query} trends", use_autoprompt=True, num_results=3)
    
    def tools():
        return [
            TrendSearchToolset.search_trending_topics,
            TrendSearchToolset.search_social_media_trends
        ]

    def _exa():
        return Exa(api_key=os.environ.get('EXA_API_KEY'))

class ContentAnalysisToolset():
  
    @tool
    def find_similar_content(url: str):
        """Find content similar to a given URL."""
        return ContentAnalysisToolset._exa().find_similar(url, num_results=3)

    @tool
    def get_webpage_contents(ids: str):
        """Retrieve and summarize the contents of a webpage."""
        ids = eval(ids)
        contents = str(ContentAnalysisToolset._exa().get_contents(ids))
        contents = contents.split("URL:")
        contents = [content[:1000] for content in contents]
        return "\n\n".join(contents)

    @tool
    def competitor_content_analysis(query: str):
        """Analyze competitors' content strategies."""
        return ContentAnalysisToolset._exa().search(f"{query} competitor content strategy", use_autoprompt=True, num_results=3)

    def tools():
        return [
            ContentAnalysisToolset.find_similar_content,
            ContentAnalysisToolset.get_webpage_contents,
            ContentAnalysisToolset.competitor_content_analysis
        ]

    def _exa():
        return Exa(api_key=os.environ.get('EXA_API_KEY'))
    
class SEOOptimizationToolset():
  
    @tool
    def search_seo_keywords(query: str):
        """Search for SEO-optimized keywords related to a topic."""
        return SEOOptimizationToolset._exa().search(f"{query} SEO keywords", use_autoprompt=True, num_results=3)

    @tool
    def analyze_seo_performance(url: str):
        """Analyze the SEO performance of a given URL."""
        return SEOOptimizationToolset._exa().search(f"{url} SEO performance", use_autoprompt=True, num_results=3)

    @tool
    def get_competitor_seo_strategy(query: str):
        """Analyze competitors' SEO strategies."""
        return SEOOptimizationToolset._exa().search(f"{query} competitor SEO strategy", use_autoprompt=True, num_results=3)

    def tools():
        return [
            SEOOptimizationToolset.search_seo_keywords,
            SEOOptimizationToolset.analyze_seo_performance,
            SEOOptimizationToolset.get_competitor_seo_strategy
        ]

    def _exa():
        return Exa(api_key=os.environ.get('EXA_API_KEY'))
