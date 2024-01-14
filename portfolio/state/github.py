from __future__ import annotations

import reflex as rx
import httpx
import os
from datetime import datetime
from typing import Literal, Union, List, Dict
from ..constants import GITHUB_API_URL, GITHUB_API_TOKEN, REPOSITORIES

project_about: Dict[str, str] = {
    "cloudy": "Local storage application with NextJS and FastAPI involves utilizing both frameworks to handle client-side and server-side functionalities, respectively.",
    "sqly": "Local storage application with NextJS and FastAPI involves utilizing both frameworks to handle client-side and server-side functionalities, respectively.",
    "myhomecloud": "Local storage application with NextJS and FastAPI involves utilizing both frameworks to handle client-side and server-side functionalities, respectively.",
    "portfolio": "Local storage application with NextJS and FastAPI involves utilizing both frameworks to handle client-side and server-side functionalities, respectively.",
    "portfolio-reflex": "Local storage application with NextJS and FastAPI involves utilizing both frameworks to handle client-side and server-side functionalities, respectively."
}

# Define a custom key function to extract the 'updated_at' value as a datetime object
def get_updated_at(repo):
    return datetime.strptime(repo["updated_at"], "%Y-%m-%dT%H:%M:%SZ")

class Github(rx.State):
    """GitHub Repositories"""

    response: Union[list, Literal[False]] = False
    repositories_to_show: list[str] = REPOSITORIES
    topics: list[str] = []
    is_processing: bool = False
    is_finished: bool = False
    
    # Call github REST API to get user repositories
    @rx.background
    async def call_user_repos(self) -> None:
        """Get repository JSON from Github API
        """
        REAT_API = GITHUB_API_URL
        TOKEN = GITHUB_API_TOKEN
        try:
            async with self:
                self.is_processing = True
            
            with httpx.Client() as client:
                res = client.get(
                    REAT_API,
                    headers={
                        "Accept": "application/vnd.github+json",
                        "Authorization": f"Bearer {TOKEN}",
                        "X-GitHub-Api-Version": "2022-11-28"
                    }
                )
                if res.status_code == 200:
                    async with self:
                        self.response = sorted(res.json(), key=get_updated_at)
        except:
            async with self:
                self.response = False
                self.is_processing = False
        finally:
            async with self:
                self.is_processing = False
    
    @rx.cached_var
    def get_repositories(self) -> List[Dict[str, List[str]]]:
        """Get information of user public repositories

        Args:
            None

        Returns List[Dict[str, List[str]]]:
            List of dictionary:
                name: str
                description: str
                repo_url: str
                created_at: str
                year: str
                month_day: str
                topics: List[str]
        """
        user_repos: List[Dict[str, List[str]]] = []
        try:
            if self.response:
                user_repos = [{
                    "name": str(repo["name"]).lower(),
                    "description": repo["description"],
                    "repo_url": repo["html_url"],
                    "created_at": repo["created_at"],
                    "year": str(datetime.strptime(repo["created_at"], "%Y-%m-%dT%H:%M:%SZ").year),
                    "month_day": str(datetime.strptime(repo["created_at"], "%Y-%m-%dT%H:%M:%SZ").strftime("%b %d")),
                    "topics": [topic for topic in repo["topics"]],
                    "about": project_about[str(repo["name"]).lower()],
                    "homepage": repo["homepage"] if repo["homepage"] is not None else ""
                } for repo in self.response if repo["name"] in self.repositories_to_show]
            return []
        except Exception as err:
            self.is_processing = False
            raise Exception(err)
        finally:
            self.is_processing = False
            self.is_finished = True
            return user_repos