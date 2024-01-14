import reflex as rx
from reflex.vars import Var
from typing import Dict, Any

class State(rx.State):
    """The base state."""

    @rx.var
    def current_page(self) -> str:
        """The current page."""
        return self.router.page.full_path
    
class State404(State):
    @rx.var
    def origin_url(self) -> str:
        return self.router_data.get("asPath", "")

class TypewriterLib(rx.Component):
    """ Typewriter component """

    library="typewriter-effect"
    
    is_default=True

class Typewriter(TypewriterLib):

    tag="Typewriter"

    options: Var[Dict[Any, Any]]

typewrite = Typewriter.create