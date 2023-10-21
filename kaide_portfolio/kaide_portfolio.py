import reflex as rx

from kaide_portfolio.pages.index import index
from kaide_portfolio.pages.works import works

from kaide_portfolio.state.state import State


# Add state and page to the app.
app = rx.App(
    state=State,
    )
app.add_page(index)
app.add_page(works)
app.compile()
