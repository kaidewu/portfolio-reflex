import reflex as rx
from typing import Dict, List
from portfolio.state.projects import Projects
from portfolio.state.github import Github
from portfolio.components.layout.main import main
from portfolio.components.project_title import project_title

def render_projects(repository: Dict[str, List[str]]) -> rx.Component:
    return rx.box(
        rx.cond(
            repository["name"] == Projects.repo_name,
            rx.box(
                rx.heading((Projects.repo_name).upper()),
                rx.text(repository["description"])
            )
        )
    )

@rx.page(route="/projects/[repo_name]")
def repository_page():
    return main(
        project_title(name=(Projects.repo_name).upper()),
        rx.box(
            rx.foreach(
                Github.get_repositories,
                render_projects
            )
        )
    )