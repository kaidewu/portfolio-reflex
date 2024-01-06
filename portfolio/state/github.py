from __future__ import annotations

import reflex as rx
import httpx
from datetime import datetime
from typing import NamedTuple
from ..constants import GITHUB_API_URL

def github_connection():
    try:
        response =  httpx.get(
            GITHUB_API_URL
        )
        if response.status_code == 200:
            user_repositories = response.json()
            return user_repositories
        return False
    except Exception as err:
        raise Exception(err)

class RepoData(NamedTuple):
    name: str
    description: str
    repo_url: str
    created_at: str
    year: str
    month_day: str
    topics: list

class Github(rx.State):
    """Github Repositories"""
    
    languages: list[str] = ["Python", "HTML", "JavaScript", "TypeScript", "CSS"]
    user_repositories = github_connection()
    
    @rx.var
    def user_repos(self) -> list[RepoData]:
        """Get information of user public repositories

        Args:
            None

        Returns:
            if it is no error returns List[RepoData]:
                name: str
                description: str
                repo_url: str
                created_at: str
                year: str
                month_day: str
            else:
                error message
        """
        repos_data: list[RepoData] = []
        try:
            for repo in self.user_repositories:
                if (repo["language"] in self.languages) and (repo["visibility"] == "public"):
                    repos_data.append(
                        RepoData(
                            name=repo["name"] if repo else "", # 0
                            description=repo["description"] if repo else "", # 1
                            repo_url=repo["html_url"] if repo else "", # 2
                            created_at=repo["created_at"] if repo else "", # 3
                            year=str(datetime.strptime(repo["created_at"], "%Y-%m-%dT%H:%M:%SZ").year) if repo else "", # 4
                            month_day=str(datetime.strptime(repo["created_at"], "%Y-%m-%dT%H:%M:%SZ").strftime("%b %d")) if repo else "", # 5
                            topics=[f"{topic} | " for topic in repo["topics"]] # 6
                        )
                    )
            return repos_data
        except Exception as err:
            raise Exception(err)