# Data Science Blog Content Creation Crew

This repository contains a suite of AI-powered tools and agents designed to streamline the process of researching, analyzing, and planning content for blogs focused on data science, AI, deep learning, NLP, and related fields. The tools utilize the `CrewAI` framework and include specialized functions for trend research, content analysis, SEO optimization, and more.

## Project Overview

The project is built to assist content creators in generating high-quality blog posts that are optimized for audience engagement and search engine visibility. By using a combination of agents and tasks, this system automates the process of identifying trending topics, analyzing competitors, ideating content, and formulating a strategic content plan.

## Features

- **Trend Research:** Discover trending topics in the data science niche.
- **Content Analysis:** Analyze the content strategies of competitors and identify gaps.
- **SEO Optimization:** Find SEO-optimized keywords and assess the SEO performance of content.
- **Content Ideation:** Generate blog post ideas, titles, and outlines based on analyzed trends.
- **Content Strategy:** Compile a detailed content strategy, including a posting schedule and SEO plan.

## Project Structure

- **`agents.py`**: Defines the agents responsible for various tasks such as trend research, trend analysis, content ideation, competitor analysis, and content strategy planning.
  
- **`tasks.py`**: Contains the tasks that each agent performs, including research, analysis, content ideation, and planning.

- **`tools.py`**: Implements the toolsets used by the agents for trend searching, content analysis, and SEO optimization, utilizing the `Exa` API for data retrieval.

- **`main.py`**: The main entry point for running the project. It prompts the user for inputs, initializes agents and tasks, and executes the content creation workflow. The results are saved in a timestamped Markdown file.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/blog-content-creation-crew.git
   cd blog-content-creation-crew

## Install dependencies:

 - Ensure you have Python 3.x installed. Then, install the required packages:

```bash
  pip install -r requirements.txt
```

## Set up environment variables:

Create a .env file in the root directory and add your EXA_API_KEY:

```bash
  EXA_API_KEY=your_exa_api_key
```

## Usage:
Run the main script:

```bash
  python main.py
```

```bash
Enter the niche or topic you want to write about.
Specify the specific area of the niche.
Define the main objective for your blog post (e.g., attract readers, SEO ranking, monetize).
View the results:
```

The output will be displayed in the console and saved to a Markdown file with a timestamped filename (e.g., blog_content_output_20230819_123456.md).
