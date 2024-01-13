import reflex as rx

def paragraph(*args) -> rx.Component:
    return rx.text(
        *args,
        text_align="justify",
        text_indent="1em",
        hyphens="auto"
    )
    