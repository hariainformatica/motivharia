from textual.app import App
from textual.widgets import Placeholder

class MiAplicacion(App):
    def compose(self) -> None:
        yield Placeholder("Hola Mundo", justify="center")

app = MiAplicacion()
app.run()