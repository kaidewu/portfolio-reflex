import reflex as rx

def project_information(title: str, *args) -> rx.Component:
    return rx.container(
            rx.link(
                rx.icon_button(
                icon="ArrowBackIcon",
                aria_label="Go Back"
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