# Web Search To Twitter Thread Crew

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```

### Configuring Environment Variables

To configure your environment variables, create a `.env` file in the root directory of your project if it doesn't already exist. Add the following lines to the `.env` file, replacing the placeholder values with your actual API keys:

```
OPENAI_API_KEY=
SERPER_API_KEY=
```

### Customizing

- Modify `src/web_search_to_twitter_thread/config/agents.yaml` to define your agents
- Modify `src/web_search_to_twitter_thread/config/tasks.yaml` to define your tasks
- Modify `src/web_search_to_twitter_thread/crew.py` to add your own logic, tools and specific args
- Modify `src/web_search_to_twitter_thread/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the web_search_to_twitter_thread Crew, assembling the agents and assigning them tasks as defined in your configuration.

## Understanding Your Crew

The web_search_to_twitter_thread Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

