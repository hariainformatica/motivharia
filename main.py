from textual.app import App
from textual.widgets import Static

class MiAplicacion(App):
    def compose(self) -> None:
        yield Static("Hola Mundo")

app = MiAplicacion()
app.run()