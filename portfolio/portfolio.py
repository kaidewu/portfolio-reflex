import reflex as rx

from portfolio.pages.index import index
from portfolio.pages.works import works
from portfolio.pages.projects import repository_page
from portfolio.pages import page404

# Add state and page to the app.
app = rx.App(
    style={
        "background_color": "#D2D6EF"
    },
    stylesheets={
        "/styles.css"
    },
    )
app.add_page(index, title="Portfolio")
app.add_page(works, title="Portfolio")
app.add_page(repository_page, title="Portfolio")
app.add_custom_404_page(page404.index, title="Portfolio")
