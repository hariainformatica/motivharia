from textual.screen import Screen
from textual.widgets import Header, Footer, Placeholder
from textual.app import ComposeResult
from textual.binding import Binding


class PrincipalScreen(Screen):
    BINDINGS = {
        Binding("a", "push_screen('AutoresTablaScreen')","Autores"),
        Binding("f", "push_screen('FrasesTablaScreen')","Frases"),
        Binding("?", "push_screen('AcercaScreen')","Y esto?"),
        Binding("q", "quit()","Salir", show=True),
    }

    def compose(self) -> ComposeResult:
        yield Header("Principal")
        yield Placeholder("MotivHaría")
        yield Footer()