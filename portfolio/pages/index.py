import reflex as rx

from portfolio.components.layout.main import main
from portfolio.state.state import typewrite

def index() -> rx.Component:
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
                    ),
                    rx.heading(
                        "I'm ",
                        rx.span(
                            "Kaide Wu",
                            textColor="#00A9FF"
                        ),
                        as_="h1",
                        fontSize="50",
                        variant="section-title"
                    ),
                    rx.heading(
                        typewrite(
                            options={
                                'strings': [
                                    "HIS Consultor",
                                    "HIS Implanter",
                                    "SysAdmin",
                                    "Software Developer"
                                ],
                                'autoStart': True,
                                'loop': True,
                                'deleteSpeed': 50
                            }
                        ),
                    ),
                ),
                delay="0.1",
                pt="10"
            ),
            rx.container(
                rx.box(
                    rx.heading(
                        "About me",
                        as_="h1"
                    ),
                    rx.text(
                        "I'm actually working in ",
                        rx.link(
                            "Laberit",
                            href="https://www.laberit.com/",
                            passHref=True,
                            scroll="false",
                            fontWeight="bold"
                        ),
                        " as a Consultant and Implanter of an Hospital Information System (HIS).",
                        textAlign="justify"
                    ),
                    rx.spacer(),
                    rx.text(
                        "As a hobby, I love immersing myself in the world of programming. I enjoy creating personal projects, exploring the latest tech trends, and continuously expanding my skills.",
                        textAlign="justify"
                    ),
                    rx.box(
                        rx.center(
                            rx.link(
                                rx.button(
                                    "My Projects",
                                    rx.icon(
                                        tag="chevron_right",
                                    ),
                                    scroll=False,
                                    border_radius="1em",
                                    box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
                                    background_image="linear-gradient(144deg,#AF40FF,#5B42F3 50%,#00DDEB)",
                                    box_sizing="border-box",
                                    color="white",
                                    opacity="0.6",
                                    _hover={
                                        "opacity": 1,
                                    },
                                ),
                                href="/projects"
                            ),
                        ),
                        my="4"
                    ),
                ),
                delay="0.1",
                pt="10"
            )
        )
    )