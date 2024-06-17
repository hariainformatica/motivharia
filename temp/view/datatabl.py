from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import DataTable, Button, Placeholder
from textual.containers import Horizontal
from textual import on


class ListaAlumnos:
    datos = [
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

    def leer(self):
        return self.datos

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
        yield Button("hola2", id="bHola2")

    def on_mount(self) -> None:
        self.rows = ListaAlumnos().leer()
        table = self.query_one(DataTable)
        table.add_columns(*self.rows[0])
        table.add_rows(self.rows[1:])

    @on(Button.Pressed, "#bHola2")
    def bHola2Pressed(self):
        self.rows.append((11, "Alvaro"))
        self.app.pop_screen()
        self.app.push_screen(NuestraScreen())


class TableApp(App):
    def on_mount(self) -> None:
        self.push_screen(NuestraScreen())

app = TableApp()
if __name__ == "__main__":
    app.run()