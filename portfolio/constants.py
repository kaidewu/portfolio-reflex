from __future__ import annotations

import os
from dotenv import load_dotenv
from typing import List

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))

# Github Username
GITHUB_USERNAME: str = "kaidewu"

# Username
USERNAME: str = "kaidewu"

# Name
NAME: str = "Kaide Wu"

# Profile image (link or path)
PROFILE_URL: str = "/profile_photo.jpg" # https://media.licdn.com/dms/image/D4D03AQHJJfsn_R49gQ/profile-displayphoto-shrink_800_800/0/1697579469792?e=1704931200&v=beta&t=zBrddj8GNRF03lb9EjOKg8YMqxayk3_VCU7v0NSHSs8"

# Github URL
GITHUB_URL: str = f"https://github.com/{USERNAME}"

# Linkedin URL
LINKEDIN_URL: str = f"https://linkedin.com/in/{USERNAME}"

# Mail
MAIL: str = "kaidewu@outlook.es"

# Github USER API URL
GITHUB_API_URL: str = f"https://api.github.com/users/{GITHUB_USERNAME}/repos" # Change the username to your github username

# Github USER API TOKEN
GITHUB_API_TOKEN: str = os.environ.get("GITHUB_API_TOKEN")

# List of your main projects to not show all repositories in index page
REPOSITORIES: List[str] = ["Cloudy", "MyHomeCloud", "portfolio", "portfolio-reflex", "sqly"]