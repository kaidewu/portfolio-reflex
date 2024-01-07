import reflex as rx

from portfolio.components.layout.main import main
from portfolio.components.projects import title

@rx.page(route="/projects/myhomecloud")
def my_home_cloud() -> rx.Component:
    return main(
        rx.container(
            title(
                "MyHomeCloud"
            ),
            rx.text(
                "MyHomeCloud Page!"
            ),
            rx.link(
                "Learn more",
                href="https://drive.google.com/file/d/1KKawHV5SrMvc3y643f6jUGoK15nwQUQu/view?usp=sharing",
                is_external=True
            )
        )
    )