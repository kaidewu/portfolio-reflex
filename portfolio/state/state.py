import reflex as rx

import asyncio
import sys
from portfolio.state.fetcher import user_repos

from typing import List, Dict

async def get_repos(username: str) -> List[List]:
    repos_datas: List[List] = []
    try:
        data = await user_repos(username)
        if data is None:
            raise Exception("Error in fetcher.py file")
        for repos in data:
            repos_datas.append([repos["name"], repos["url"], repos["description"]])
            print(repos)
        return repos_datas
    except Exception as exc:
        print(exc, file=sys.stderr)

class State(rx.State):
    """The app state."""
    
    user_repos: List[List] = asyncio.run(get_repos("kaidewu"))