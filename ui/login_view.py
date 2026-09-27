import os
import tkinter as tk
from tkinter import ttk, messagebox

class LoginView(tk.Frame):
    def __init__(self, master, controlador, servicio):
        super().__init__(master, bg="#F9F6F7")
        self.controlador = controlador
        self.servicio = servicio

        ventana_raiz = self.winfo_toplevel()
        ventana_raiz.title("Restaurante - Tkinter")
        ventana_raiz.geometry("680x520")
        ventana_raiz.resizable(False, False)

        self._iniciar_interfaz()

    def _iniciar_interfaz(self):
        self.pack(fill="both", expand=True)

        tarjeta = tk.Frame(self, bg="#FFFFFF", padx=35, pady=30, relief="flat")
        tarjeta.place(relx=0.5, rely=0.5, anchor="center", width=340, height=460)

        ruta_logo = os.path.join("assets", "logo.png")
        if os.path.exists(ruta_logo):
            try:
                self.img_logo = tk.PhotoImage(file=ruta_logo)
                ancho = self.img_logo.width()
                alto = self.img_logo.height()
                factor = max(1, ancho // 110, alto // 110)
                if factor > 1:
                    self.img_logo = self.img_logo.subsample(factor, factor)

                lbl_logo = tk.Label(tarjeta, image=self.img_logo, bg="#FFFFFF")
                lbl_logo.pack(pady=(0, 10))
            except Exception:
                pass

        lbl_titulo = tk.Label(
            tarjeta,
            text="Restaurante",
            font=("Segoe UI", 18, "bold"),
            bg="#FFFFFF",
            fg="#111111"
        )
        lbl_titulo.pack(pady=(0, 2))

        lbl_subtitulo = tk.Label(
            tarjeta,
            text="Inicio de sesión",
            font=("Segoe UI", 10),
            bg="#FFFFFF",
            fg="#777777"
        )
        lbl_subtitulo.pack(pady=(0, 20))

        lbl_usuario = tk.Label(
            tarjeta,
            text="Usuario",
            font=("Segoe UI", 9, "bold"),
            bg="#FFFFFF",
            fg="#222222",
            anchor="w"
        )
        lbl_usuario.pack(fill="x")

        self.txt_usuario = tk.Entry(
            tarjeta,
            font=("Segoe UI", 10),
            bg="#FFFFFF",
            relief="solid",
            bd=1,
            highlightthickness=0
        )
        self.txt_usuario.pack(fill="x", ipady=4, pady=(4, 15))
        self.txt_usuario.focus_set()

        lbl_clave = tk.Label(
            tarjeta,
            text="Contraseña",
            font=("Segoe UI", 9, "bold"),
            bg="#FFFFFF",
            fg="#222222",
            anchor="w"
        )
        lbl_clave.pack(fill="x")

        self.txt_clave = tk.Entry(
            tarjeta,
            font=("Segoe UI", 10),
            show="*",
            bg="#FFFFFF",
            relief="solid",
            bd=1,
            highlightthickness=0
        )
        self.txt_clave.pack(fill="x", ipady=4, pady=(4, 25))
        self.txt_clave.bind("<Return>", lambda e: self.procesar_login())

        btn_login = tk.Button(
            tarjeta,
            text="Iniciar sesión",
            font=("Segoe UI", 10, "bold"),
            bg="#DC2626",
            fg="#FFFFFF",
            activebackground="#B91C1C",
            activeforeground="#FFFFFF",
            relief="flat",
            cursor="hand2",
            command=self.procesar_login
        )
        btn_login.pack(fill="x", ipady=6)

    def procesar_login(self):
        usuario = self.txt_usuario.get().strip()
        clave = self.txt_clave.get().strip()

        if not usuario or not clave:
            messagebox.showwarning("Atención", "Por favor ingrese usuario y contraseña.")
            return

        usuario_valido = self.servicio.autenticar(usuario, clave)

        if usuario_valido:
            self.controlador.mostrar_main_view(usuario_valido)
        else:
            messagebox.showerror("Error", "Credenciales incorrectas.")