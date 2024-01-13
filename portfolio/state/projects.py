import reflex as rx
from typing import List

class Projects(rx.State):
    """Projects State"""
    
    @rx.var
    def repo_name(self) -> str:
        return self.router.page.params.get('repo_name')