import reflex as rx

from portfolio.components.layout.main import main
from portfolio.state.state import State404

def index():
    # Wrap the component in the template.
    return main(
        rx.box(
            rx.center(
                rx.vstack(
                    rx.heading(rx.constants.Page404.TITLE),
                    rx.text(
                        "Oups, the page at ",
                        rx.code(State404.origin_url),
                        " doesn't exist.",
                    ),
                    rx.spacer(),
                ),
                height="60vh"
            )
        )
    )