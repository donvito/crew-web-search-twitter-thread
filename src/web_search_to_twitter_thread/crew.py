from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from web_search_to_twitter_thread.tools.serper_tool import SerperSearchTool

@CrewBase
class WebSearchToTwitterThreadCrew():
    """WebSearchToTwitterThread crew"""

    @agent
    def content_gathering_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['content_gathering_specialist'],
            tools=[SerperSearchTool()],
        )

    @agent
    def thread_formatter(self) -> Agent:
        return Agent(
            config=self.agents_config['thread_formatter'],
            tools=[],
        )


    @task
    def scrape_information_task(self) -> Task:
        return Task(
            config=self.tasks_config['scrape_information_task'],
            tools=[SerperSearchTool()],
        )

    @task
    def create_twitter_thread_task(self) -> Task:
        return Task(
            config=self.tasks_config['create_twitter_thread_task'],
            
        )


    @crew
    def crew(self) -> Crew:
        """Creates the WebSearchToTwitterThread crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
