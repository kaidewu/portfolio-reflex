import reflex as rx

def bio_section(*args) -> rx.Component:
    return rx.box(
        *args,
        pl="3.4em",
        textIndent="-3.4em",
        pt="0.5em",
        pb="0.5em"
    )

def bio_year(*args) -> rx.Component:
    return rx.span(
        *args,
        fontWeight="bold",
        mr="1em"
    )