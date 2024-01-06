import reflex as rx

from portfolio.pages.index import index
from portfolio.pages.works import works
from portfolio.pages.contact import contact
from portfolio.pages import page404

# Add state and page to the app.
app = rx.App(
    stylesheets={
        "/styles.css"
    }
    )
app.add_page(index)
app.add_page(works)
app.add_page(contact)
app.add_custom_404_page(page404.index)
app.compile()
