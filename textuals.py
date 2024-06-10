from textual.app import App, ComposeResult
from textual.widgets import Placeholder, Footer, Header, Button
from textual.screen import Screen
from textual.containers import Horizontal, Vertical
from textual import on
from textual.events import Click
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
class AutoresTablaScreen(Screen):
    BINDINGS = {
        Binding("a", "push_screen('AutoresTablaScreen')","Autores", show=False),
        Binding("f", "push_screen('FrasesTablaScreen')","Frases"),
        Binding("v", "push_screen('PrincipalScreen')","Volver"),
        Binding("?", "push_screen('AcercaScreen')","Y esto?"),
        Binding("q", "quit()","Salir", show=False),
    }     
    def compose(self) -> ComposeResult:
        yield Header("Autores")
        yield Placeholder("Tabla de autores")
        yield Footer()

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

class MiAplicacion(App):
    MODES = {
        "PrincipalScreen": PrincipalScreen,
        "AutoresTablaScreen": AutoresTablaScreen,
        "FrasesTablaScreen": FrasesTablaScreen,
    }
    SCREENS = {
        "SplashScreen": SplashScreen,
        "AcercaScreen": AcercaScreen,
        "PrincipalScreen": PrincipalScreen,
        "AutoresTablaScreen": AutoresTablaScreen,
        "FrasesTablaScreen": FrasesTablaScreen,
    }
    BINDINGS = {
        Binding("a", "push_screen('AutoresTablaScreen')","Autores"),
        Binding("f", "push_screen('FrasesTablaScreen')","Frases"),
        Binding("q", "quit()","Salir", show=True),
        Binding("?", "push_screen('AcercaScreen')","Y esto?"),
        Binding("v", "switch_screen('PrincipalScreen')","Volver",show=False),
    }
    def on_mount(self) -> None:
        self.switch_mode("PrincipalScreen")
        self.push_screen("SplashScreen")
        

app = MiAplicacion()
app.run()