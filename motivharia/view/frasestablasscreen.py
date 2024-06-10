from textual.screen import Screen
from textual.widgets import Header, Footer, Placeholder
from textual.app import ComposeResult
from textual.binding import Binding

class FrasesTablaScreen(Screen):
    BINDINGS = {
        Binding("a", "push_screen('AutoresTablaScreen')","Autores"),
        Binding("f", "push_screen('FrasesTablaScreen')","Frases", show=False),
        Binding("v", "push_screen('PrincipalScreen')","Volver"),
        Binding("?", "push_screen('AcercaScreen')","Y esto?"),
        Binding("q", "quit()","Salir", show=False),
    }    
    def compose(self) -> ComposeResult:
        yield Header("Frases")
        yield Placeholder("Tabla de frases")
        yield Footer()