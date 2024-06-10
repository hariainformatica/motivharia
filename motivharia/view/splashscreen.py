from textual.screen import Screen
from textual.widgets import Placeholder, Button
from textual.app import ComposeResult
from textual import on
from textual.events import Click
from textual.containers import Horizontal

class SplashScreen(Screen):
    CSS = """
        SplashScreen {
            align: center middle;
            background: green 40%;
        }
        #splash {
            height: 18;
            width: 60;
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
            Placeholder("Texto de bienvenida", classes="texto"),
            Button("Gracias", id="gracias", classes="boton"),
            id="splash"
        )

    @on(Button.Pressed, "#gracias")
    def quitSplash(self) -> None:
        self.screen.dismiss()

    @on(Click)
    def quitSplashs(self) -> None:
        self.screen.dismiss()