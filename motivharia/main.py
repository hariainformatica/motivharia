from textual.app import App
from textual.binding import Binding

from motivharia.view.splashscreen import SplashScreen
from motivharia.view.principalscreen import PrincipalScreen
from motivharia.view.autorestablascreen import AutoresTablaScreen
from motivharia.view.frasestablasscreen import FrasesTablaScreen
from motivharia.view.acercascreen import AcercaScreen


class Aplicacion(App):
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
        

app = Aplicacion()
app.run()