import reflex as rx
from reflex.vars import Var
from typing import Dict, Any

class State(rx.State):
    """The base state."""

    @rx.var
    def current_page(self) -> str:
        """The current page."""
        return self.router.page.full_path

class TypewriterLib(rx.Component):
    """ Typewriter component """

    library="typewriter-effect"
    
    is_default=True

class Typewriter(TypewriterLib):

    tag="Typewriter"

    options: Var[Dict[Any, Any]]


typewrite = Typewriter.create