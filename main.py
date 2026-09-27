import tkinter as tk
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Restaurante - Tkinter")
        self.geometry("980x620")
        self.minsize(850, 580)

        self.servicio = RestauranteServicio()

        self.contenedor = tk.Frame(self)
        self.contenedor.pack(fill=tk.BOTH, expand=True)

        self.vista_actual = None
        self.mostrar_login()

    def cambiar_vista(self, nueva_vista):
        if self.vista_actual is not None:
            self.vista_actual.destroy()
        self.vista_actual = nueva_vista
        self.vista_actual.pack(fill=tk.BOTH, expand=True)

    def mostrar_login(self):
        self.cambiar_vista(LoginView(self.contenedor, self, self.servicio))

    def mostrar_main_view(self, usuario):
        self.cambiar_vista(MainView(self.contenedor, self.servicio, usuario))

if __name__ == "__main__":
    app = App()
    app.mainloop()