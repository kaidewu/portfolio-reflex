import os
import json
import httpx


# GraphQL queries (borrowed from https://github.com/anuraghazra/github-readme-stats/blob/master/src/fetchers/stats-fetcher.js).
GRAPHQL_REPOS_QUERY = """
  query userInfo($login: String!, $after: String) {
    user(login: $login) {
      repositories(first: 100, ownerAffiliations: OWNER, orderBy: {direction: DESC, field: STARGAZERS}, after: $after) {
            nodes {
                name
                url
                description
            }
        }
    }
  }
"""

# Set your GitHub personal access token (Replace with your actual token)
GITHUB_API_TOKEN = "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"#os.environ.get("GITHUB_API_TOKEN")

# Set the GitHub GraphQL API URL
GITHUB_GRAPHQL_URL = "https://api.github.com/graphql"


async def user_repos(username: str):
    if GITHUB_API_TOKEN is None:
        raise RuntimeError("Set GITHUB_API_TOKEN in the environment")

    # Create a dictionary for the request headers with the Authorization header
    headers = {
        "Authorization": f"Bearer {GITHUB_API_TOKEN}",
        "Content-Type": "application/json",
    }

    # Create a dictionary for the request payload
    payload = {
        "query": GRAPHQL_REPOS_QUERY,
        "variables": {
            "login": username,
        },
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(GITHUB_GRAPHQL_URL, headers=headers, json=payload)

        response.raise_for_status()

        if response.status_code == 200:
            data = response.json()
            user_data = data["data"]["user"]
            if user_data is None:
                print(f"User {username} not found")
                return None
            return data["data"]["user"]["repositories"]["nodes"]


# Run the asynchronous function
if __name__ == "__main__":
    import asyncio

    asyncio.run(user_repos("kaidewu"))

    