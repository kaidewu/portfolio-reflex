import reflex as rx

from portfolio.components.layout.main import main
from portfolio.components.work_item import work_item

def works() -> rx.Component:
    return main(
        rx.container(
            rx.heading(
                "My Projects!",
                as_="h3",
                fontSize={20},
                mb={4}
            ),
            rx.responsive_grid(
                
                columns=[1, 1, 3],
                gap={6}
            ),
            mt={20}
        )
    )