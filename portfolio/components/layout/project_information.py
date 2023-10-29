import reflex as rx

def project_information(title: str, *args) -> rx.Component:
    return rx.container(
            rx.link(
                rx.button(
                rx.icon(tag="arrow_back"),
                "Go Back"
                ),
                href="/projects"
            ),
            rx.box(
                rx.heading(
                    title,
                    as_="h3",
                    mb={4}
                ),
            ),
            *args
        )