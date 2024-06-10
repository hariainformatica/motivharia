from textual.screen import Screen
from textual.widgets import Placeholder, Button
from textual.app import ComposeResult
from textual import on
from textual.events import Click
from textual.containers import Horizontal

class AcercaScreen(Screen):
    CSS = """
        AcercaScreen {
            align: center middle;
        }
        #Acerca {
            height: 20;
            width: 80;
            align: left bottom;
        }
        .logo {
            width: 2fr;
            height: 40%;
            align: left top;
        }
        .texto {
            width: 6fr;
            height: 100%;
        }
        .boton {
            width: 2fr;
            height: 20%;
        }  
    """

    def compose(self) -> ComposeResult:
        yield Horizontal(
            Placeholder("Logo", classes="logo"),
            Placeholder("Texto sobre la app", classes="texto"),
            Button("Okiiiiii", id="gracias", classes="boton"),
            id="acerca"
        )

    @on(Button.Pressed, "#gracias")
    def quitAcerca(self) -> None:
        self.screen.dismiss()

    @on(Click)
    def quitAcercas(self) -> None:
        self.screen.dismiss()