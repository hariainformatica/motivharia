from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import DataTable, Button, Placeholder
from textual.containers import Horizontal


class ListaAlumnos:
    def leer(self):
        return [
                ("id", "alumno"),
                (4, "Joseph Schooling"),
                (2, "Michael Phelps"),
                (5, "Chad le Clos"),
                (6, "László Cseh"),
                (3, "Li Zhuhao"),
                (8, "Mehdy Metella"),
                (7, "Tom Shields"),
                (1, "Aleksandr Sadovnikov"),
                (10, "Darren Burns"),
            ]

class Ventana(Screen):
    CSS = """
        .box {
            width: 1fr;
        }
        .box2 {
            width: 2fr;
        }
    """
    def compose(self) -> ComposeResult:
        yield Horizontal(
            Placeholder("uno", classes="box"),
            Placeholder("dos", classes="box2")
        )

class NuestraScreen(Screen):
    def compose(self) -> ComposeResult:
        yield DataTable()
        yield Button("hola")
        yield Button("hola2")

    def on_mount(self) -> None:
        rows = ListaAlumnos().leer()
        table = self.query_one(DataTable)
        table.add_columns(*rows[0])
        table.add_rows(rows[1:])

class TableApp(App):
    def on_mount(self) -> None:
        self.push_screen(Ventana())

app = TableApp()
if __name__ == "__main__":
    app.run()