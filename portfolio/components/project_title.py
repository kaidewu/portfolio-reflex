import reflex as rx

def project_title(name: str) -> rx.Component:
    return rx.box(
        rx.link(
            "Home",
            href="/",
            textColor="#00A9FF",
            font_size="14"
        ),
        rx.span(
            rx.icon(
                tag="chevron_right"
            )
        ),
        rx.heading(
            name,
            as_="h3",
            display="inline-block",
            fontSize="24",
            mb="4"
        ),
        pt="5"
    )