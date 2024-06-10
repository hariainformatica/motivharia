from textual.screen import Screen
from textual.widgets import Button, Header, Footer, DataTable
from textual.app import ComposeResult
from textual import on
from textual.events import Click
from textual.containers import Horizontal
from textual.binding import Binding

ROWS = [
    ("lane", "swimmer", "country", "time"),
    (4, "Joseph Schooling", "Singapore", 50.39),
    (2, "Michael Phelps", "United States", 51.14),
    (5, "Chad le Clos", "South Africa", 51.14),
    (6, "László Cseh", "Hungary", 51.14),
    (3, "Li Zhuhao", "China", 51.26),
    (8, "Mehdy Metella", "France", 51.58),
    (7, "Tom Shields", "United States", 51.73),
    (1, "Aleksandr Sadovnikov", "Russia", 51.84),
    (10, "Darren Burns", "Scotland", 51.84),
]

class AutoresTablaScreen(Screen):
    CSS = """
        AutoresTablaScreen {
            align: center middle;
        }
        #table{
        }
        #place{
        }
        #volver{
    }"""
    
    BINDINGS = {
        Binding("a", "push_screen('AutoresTablaScreen')","Autores", show=False),
        Binding("f", "push_screen('FrasesTablaScreen')","Frases"),
        Binding("v", "push_screen('PrincipalScreen')","Volver"),
        Binding("?", "push_screen('AcercaScreen')","Y esto?"),
        Binding("q", "quit()","Salir", show=False),
    }

     
    def compose(self) -> ComposeResult:
        yield Header("Autores")
        #yield Placeholder("Tabla de autores", id="place")
        yield DataTable()
        yield Button("Volver", id="volver")
        yield Footer()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns(*ROWS[0])
        table.add_rows(ROWS[1:])

    @on(Button.Pressed, "#volver")
    def volver(self) -> None:
        self.app.switch_screen("PrincipalScreen")