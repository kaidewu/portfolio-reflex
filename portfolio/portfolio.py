import reflex as rx

from portfolio.pages.index import index
from portfolio.pages.works import works

from portfolio.state.state import State


# Add state and page to the app.
app = rx.App(
    state=State,
    )
app.add_page(index)
app.add_page(works)
app.compile()
