import reflex as rx
from typing import List, Dict

def render_topics(topic: str) -> rx.Component:
    return rx.span(
        topic,
        class_name="whitespace-nowrap rounded-full bg-purple-100 px-2.5 py-0.5 text-xs text-purple-600"
    )

def render_projects_cards(repository: Dict[str, List[str]]) -> rx.Component:
    return rx.link_box(
        rx.box(
            rx.box(
                rx.box(
                    rx.span(repository['year']),
                    rx.span(class_name="w-px flex-1 bg-blue-900/10"),
                    rx.span(repository['month_day']),
                    class_name="flex items-center justify-between gap-4 text-xs font-bold uppercase"
                ),
                as_="time",
                date_time=f"{repository['created_at']}",
                class_name="rotate-180 p-2 [writing-mode:_vertical-lr]"
            ),
            rx.box(
                rx.image(
                    alt=f"{repository['name']}",
                    src=f"/{repository['name']}.png",
                    max_w='{{ base: "100%", sm: "200px" }}',
                    class_name="aspect-square h-full w-full object-cover"
                )
            ),
            rx.box(
                rx.box(
                    rx.link_overlay(
                        rx.text(
                            repository['name'],
                            class_name="font-bold uppercase font-size-20"
                        ),
                        href=f"/projects/{repository['name']}/"
                    ),
                    rx.text(
                        repository['description'],
                        class_name="mt-2 line-clamp-5 text-sm/relaxed"
                    ),
                    rx.box(
                        rx.foreach(
                            repository['topics'],
                            render_topics
                        ),
                        class_name="mt-4 flex flex-wrap gap-1"
                    )
                ),
                class_name="flex flex-1 flex-col justify-between p-3"    
            ),
            class_name="flex transition hover:shadow-xl pt-5 rounded-lg"
        ),
        as_="article"
    )

def projects_cards(Github) -> rx.Component:
    return rx.box(
        rx.heading(
            "<Projects />",
            as_="h2",
            fontSize="2em",
            variant="section-title",
            textDecorationThickness="2.5px",
            fontWeight="bold",
            pt="5",
            pb="2"
        ),
        rx.cond(
            Github.is_processing,
            rx.center(rx.circular_progress(is_indeterminate=True)),
            rx.cond(
                Github.is_finished,
                rx.foreach(
                    Github.get_repositories,
                    render_projects_cards
                ),
            )
        ),
    )