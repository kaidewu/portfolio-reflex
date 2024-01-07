from __future__ import annotations

import reflex as rx
from portfolio.components.layout.main import main
from portfolio.state.state import typewrite
from portfolio.state.github import Github
from portfolio.components.projects_cards import projects_cards
from portfolio.components.about_me import about_me
from portfolio.components.contact import contact

def index() -> rx.Component:
    """Index page"""
    return main(
        rx.container(
            rx.container(
                rx.box(
                    rx.heading(
                        "Hey, ",
                        rx.span(
                            "👋🏻",
                            id="wave",
                            role="img"
                        ),
                        " !",
                        as_="h1",
                        fontSize="40",
                        variant="section-title"
                    ),
                    rx.heading(
                        "I'm ",
                        rx.span(
                            "Kaide Wu",
                            textColor="#00A9FF"
                        ),
                        as_="h1",
                        fontSize="55",
                        variant="section-title"
                    ),
                    rx.heading(
                        typewrite(
                            options={
                                'strings': [
                                    "Implementation Consultant",
                                    "SysAdmin",
                                    "Software Developer"
                                ],
                                'autoStart': True,
                                'loop': True,
                                'deleteSpeed': 50
                            }
                        ),
                        as_="h1",
                        fontSize="40",
                        variant="section-title"
                    ),
                ),
                delay="0.1",
                pt="10"
            ),
            about_me(),
            contact(),
            rx.container(
                projects_cards(Github)
            )
        )
    )