from __future__ import annotations

import reflex as rx
from portfolio.components.layout.main import main
from portfolio.state.state import typewrite
from portfolio.state.github import Github

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
                                    "Implementation Consultant",
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
                        as_="h2",
                        fontSize="2em",
                        variant="section-title",
                        textDecoration="underline",
                        textDecorationThickness="2.5px",
                        fontWeight="bold",
                        pb="2"
                    ),
                    rx.text(
                        "In my free time, I like to immerse myself in the world of programming. I enjoy creating personal projects, exploring the latest tech trends, and continuously expanding my skills.",
                        textAlign="justify"
                    ),
                    rx.html("<br>"),
                    rx.text(
                        "I am deeply in love of Python. Also I have some knownledge of Javascript, PHP, Java and C# (Unity)",
                        textAlign="justify"
                    ),
                ),
                delay="0.1",
                pt="10"
            ),
            rx.container(
                rx.foreach(
                    Github.user_repos,
                    lambda repository: rx.link_box(
                        rx.box(
                            rx.box(
                                rx.box(
                                    rx.span(repository[4]),
                                    rx.span(class_name="w-px flex-1 bg-blue-900/10"),
                                    rx.span(repository[5]),
                                    class_name="flex items-center justify-between gap-4 text-xs font-bold uppercase"
                                ),
                                as_="time",
                                date_time=f"{repository[3]}",
                                class_name="rotate-180 p-2 [writing-mode:_vertical-lr]"
                            ),
                            rx.box(
                                rx.image(
                                    alt=f"{repository[0]}",
                                    src="/example_image.jpg",
                                    max_w='{{ base: "100%", sm: "200px" }}',
                                    class_name="aspect-square h-full w-full object-cover"
                                )
                            ),
                            rx.box(
                                rx.box(
                                    rx.link_overlay(
                                        rx.text(
                                            repository[0],
                                            class_name="font-bold uppercase font-size-20"
                                        ),
                                        href=f"{repository[2]}",
                                        is_external=True
                                    ),
                                    rx.text(
                                        repository[1],
                                        class_name="mt-2 line-clamp-3 text-sm/relaxed"
                                    ),
                                    rx.box(
                                        rx.foreach(
                                            [repository[6]],
                                            lambda topic: rx.span(
                                                topic,
                                                class_name="whitespace-nowrap rounded-full bg-purple-100 px-2.5 py-0.5 text-xs text-purple-600"
                                            ),
                                        ),
                                        class_name="mt-4 flex flex-wrap gap-1"
                                    ),
                                ),
                                class_name="flex flex-1 flex-col justify-between p-3"    
                            ),
                            class_name="flex transition hover:shadow-xl pt-5 rounded-lg"
                        ),
                        as_="article"
                    ),
                ),
                rx.box(
                    rx.center(
                        rx.link(
                            rx.button(
                                "More Projects",
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
            )
        )
    )