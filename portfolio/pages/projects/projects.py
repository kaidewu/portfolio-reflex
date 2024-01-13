import reflex as rx

from portfolio.components.layout.main import main
from portfolio.components.project_item import project_item

def projects() -> rx.Component:
    return main(
        rx.container(
            rx.box(
                rx.heading(
                    "Projects",
                    as_="h1",
                    mb="4"
                ),
            ),
            rx.responsive_grid(
                rx.box(
                    project_item(
                        id="sqly",
                        title="SQLY",
                        thumbnail="/example_image.jpg",
                        description="A website that generate SQL Queries"
                    )
                ),
                rx.box(
                    project_item(
                        id="portfolio-reflex-github-api",
                        title="Portfolio Reflex With Github API",
                        thumbnail="/example_image.jpg",
                        description="A portfolio build with Reflex and using Github API"
                    )
                ),
                rx.box(
                    project_item(
                        id="portfolio-reflex",
                        title="Portfolio Reflex",
                        thumbnail="/example_image.jpg",
                        description="A portfolio build with Reflex"
                    )
                ),
                rx.box(
                    project_item(
                        id="cloudy",
                        title="Cloudy",
                        thumbnail="/example_image.jpg",
                        description="A website build with NextJS + FastAPI"
                    )
                ),
                rx.box(
                    project_item(
                        id="myhomecloud",
                        title="MyHomeCloud",
                        thumbnail="/myhomecloud-cover.png",
                        description="Local cloud build with Flask"
                    )
                ),
                columns=[1, 1, 3],
                gap="6"
            ),
            mt="5"
        ),
    )
