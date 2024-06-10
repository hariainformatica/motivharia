from textual.app import App
from textual.widgets import Placeholder

class MiAplicacion(App):
    def compose(self):
        yield Placeholder("Hola Mundo")

app = MiAplicacion()
app.run()