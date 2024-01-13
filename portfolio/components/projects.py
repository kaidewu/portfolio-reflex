import reflex as rx

def title(*args) -> rx.Component:
    return rx.box(
        rx.link(
            "Projects",
            href="/projects",
            textColor="#00A9FF"
        ),
        rx.span(
            rx.icon(
                tag="chevron_right"
            )
        ),
        rx.heading(
            *args,
            as_="h3",
            display="inline-block",
            fontSize="20",
            mb="4"
        ),
        pt="5"
    )