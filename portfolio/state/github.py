from __future__ import annotations

import reflex as rx
import json
import httpx
from datetime import datetime
from typing import List
from ..constants import GITHUB_API_TOKEN, GITHUB_API_URL

class RepoData(rx.Base):
    name: str
    description: str
    repo_url: str
    created_at: str
    year: str
    month_day: str

class Github(rx.State):
    """Github Repositories"""
    response = json.loads(httpx.get(
                GITHUB_API_URL,
                headers={
                    "Accept": "application/vnd.github+json",
                    "Authorization": f"Bearer {GITHUB_API_TOKEN}",
                    "X-GitHub-Api-Version": "2022-11-28", # The date when the API version was released. https://docs.github.com/en/rest/about-the-rest-api/api-versions?apiVersion=2022-11-28
                }
            ).text)

    languages: List[str] = ["python", "html", "javascript", "typescript", "css"]
    
    @rx.var
    def user_repos(self) -> List[RepoData]:
        """
        :params = None
        :description = Returns in JSON format, the all repositories of the user
        :own annotation = Return general information of the user repositories
        """
        repos_data: List[RepoData] = []
        
        for i in range(len(self.response)):
            if (self.response[i]["language"] in self.languages):
                repo_tuple = RepoData(
                name=self.response[i]["name"],
                description=self.response[i]["description"],
                repo_url=self.response[i]["html_url"],
                created_at=self.response[i]["created_at"],
                year=str(datetime.strptime(self.response[i]["created_at"], "%Y-%m-%dT%H:%M:%SZ").year),
                month_day=str(datetime.strptime(self.response[i]["created_at"], "%Y-%m-%dT%H:%M:%SZ").strftime("%b %d"))
                )
            repos_data.append(repo_tuple)
        return repos_data