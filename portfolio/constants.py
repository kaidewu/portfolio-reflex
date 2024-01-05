from dotenv import load_dotenv
from os.path import join, dirname
import os

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

GITHUB_API_TOKEN = os.environ.get("GITHUB_API_TOKEN")
PROFILE_URL = "https://media.licdn.com/dms/image/D4D03AQHJJfsn_R49gQ/profile-displayphoto-shrink_800_800/0/1697579469792?e=1704931200&v=beta&t=zBrddj8GNRF03lb9EjOKg8YMqxayk3_VCU7v0NSHSs8"
GITHUB_URL = "https://github.com/kaidewu"
LINKEDIN_URL = "https://linkedin.com/in/kaidewu"
MAIL = "kaidewu@outlook.es"
GITHUB_PORTFOLIO_REFLEX_URL = "https://github.com/kaidewu/portfolio-reflex"
GITHUB_API_URL = "https://api.github.com/users/kaidewu/" # Change the username to your github username