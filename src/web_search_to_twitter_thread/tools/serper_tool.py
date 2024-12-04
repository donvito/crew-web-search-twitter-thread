from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import os
import json
import requests

class SerperSearchInput(BaseModel):
    """Input schema for SerperSearch."""
    query: str = Field(..., description="The search query to look up.")

class SerperSearchTool(BaseTool):
    name: str = "Serper Search"
    description: str = (
        "A tool that performs web searches using the Serper.dev API to find relevant information."
    )
    args_schema: Type[BaseModel] = SerperSearchInput

    def _run(self, query: str) -> str:
        api_key = os.getenv('SERPER_API_KEY')
        if not api_key:
            return "Error: SERPER_API_KEY environment variable is not set"

        headers = {
            'X-API-KEY': api_key,
            'Content-Type': 'application/json'
        }
        
        payload = json.dumps({
            "q": query
        })

        try:
            response = requests.post(
                'https://google.serper.dev/search',
                headers=headers,
                data=payload
            )
            response.raise_for_status()
            search_results = response.json()
            
            # Format the results
            formatted_results = []
            if 'organic' in search_results:
                for result in search_results['organic'][:5]:  # Limit to top 5 results
                    formatted_results.append(
                        f"Title: {result.get('title', 'N/A')}\n"
                        f"Link: {result.get('link', 'N/A')}\n"
                        f"Snippet: {result.get('snippet', 'N/A')}\n"
                    )
            
            return "\n\n".join(formatted_results) if formatted_results else "No results found."
            
        except Exception as e:
            return f"Error performing search: {str(e)}" 