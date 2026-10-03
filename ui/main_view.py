import os
import tkinter as tk
from tkinter import ttk, messagebox
from modelos.producto import Producto

class MainView(tk.Frame):
    def __init__(self, master, servicio, usuario_actual):
        self.FONDO_GENERAL = "#F0F4F8"
        super().__init__(master, bg=self.FONDO_GENERAL)
        self.servicio = servicio
        self.usuario_actual = usuario_actual

        janela = self.winfo_toplevel()
        janela.title("Restaurante - Tkinter")
        janela.geometry("1060x650")
        janela.resizable(True, True)

        self.COLOR_ROJO = "#DC2626"
        self.COLOR_ROJO_OSCURO = "#991B1B"
        self.NEGRO_BOTON = "#1E1E1E"
        self.COLOR_CABECERA_VERDE = "#D1FAE5"
        self.COLOR_TEXTO_VERDE = "#064E3B"
        self.COLOR_PIE_ROJO = "#DC2626"

        self.AZUL_MARCO = "#DBEAFE"
        self.AZUL_FILA_1 = "#EFF6FF"
        self.AZUL_FILA_2 = "#DBEAFE"

        self.GRIS_ENTRY = "#E5E7EB"

        self._configurar_estilos_ttk()
        self._iniciar_interfaz()

    def _configurar_estilos_ttk(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Verde.Treeview.Heading",
            background=self.COLOR_CABECERA_VERDE,
            foreground=self.COLOR_TEXTO_VERDE,
            font=("Segoe UI", 9, "bold"),
            borderwidth=1,
            relief="solid"
        )
        style.map("Verde.Treeview.Heading", background=[("active", "#A7F3D0")])

        style.configure(
            "Azul.Treeview",
            background=self.AZUL_FILA_1,
            foreground="#0F172A",
            fieldbackground=self.AZUL_FILA_1,
            rowheight=24,
            font=("Segoe UI", 9)
        )

    def _iniciar_interfaz(self):
        self.pack(fill="both", expand=True)

        self.sidebar = tk.Frame(self, bg="#0D0D0D", width=210)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        frame_user = tk.Frame(self.sidebar, bg="#0D0D0D")
        frame_user.pack(fill="x", padx=15, pady=(20, 15))

        ruta_logo = os.path.join("assets", "logo.png")
        if os.path.exists(ruta_logo):
            try:
                img_orig = tk.PhotoImage(file=ruta_logo)
                factor = max(1, img_orig.width() // 45, img_orig.height() // 45)
                self.img_logo_sidebar = img_orig.subsample(factor, factor)
                lbl_logo = tk.Label(frame_user, image=self.img_logo_sidebar, bg="#0D0D0D")
                lbl_logo.pack(anchor="w", pady=(0, 6))
            except Exception:
                pass

        lbl_marca = tk.Label(
            frame_user,
            text="RESTAURANTE",
            font=("Segoe UI", 13, "bold"),
            bg="#0D0D0D",
            fg="#FFFFFF"
        )
        lbl_marca.pack(anchor="w")

        nome_user = getattr(self.usuario_actual, "nombre", str(self.usuario_actual))
        lbl_user = tk.Label(
            frame_user,
            text=nome_user,
            font=("Segoe UI", 10),
            bg="#0D0D0D",
            fg="#A0A0A0"
        )
        lbl_user.pack(anchor="w", pady=(2, 0))

        self.btn_nav_inicio = tk.Button(
            self.sidebar, text="  🏠  Inicio", font=("Segoe UI", 10, "bold"),
            bg=self.COLOR_ROJO, fg="#FFFFFF", relief="flat", anchor="w", padx=15, pady=9,
            cursor="hand2", command=self._mostrar_painel_inicio
        )
        self.btn_nav_inicio.pack(fill="x", padx=10, pady=3)

        self.btn_nav_usuarios = tk.Button(
            self.sidebar, text="  👤  Usuarios", font=("Segoe UI", 10, "bold"),
            bg=self.NEGRO_BOTON, fg="#CCCCCC", relief="flat", anchor="w", padx=15, pady=9,
            cursor="hand2", command=self._mostrar_painel_usuarios
        )
        self.btn_nav_usuarios.pack(fill="x", padx=10, pady=3)

        self.btn_nav_produtos = tk.Button(
            self.sidebar, text="  📦  Productos", font=("Segoe UI", 10, "bold"),
            bg=self.NEGRO_BOTON, fg="#CCCCCC", relief="flat", anchor="w", padx=15, pady=9,
            cursor="hand2", command=self._mostrar_painel_productos
        )
        self.btn_nav_produtos.pack(fill="x", padx=10, pady=3)

        self.btn_nav_vendas = tk.Button(
            self.sidebar, text="  🛒  Ventas", font=("Segoe UI", 10, "bold"),
            bg=self.NEGRO_BOTON, fg="#CCCCCC", relief="flat", anchor="w", padx=15, pady=9,
            cursor="hand2", command=self._mostrar_painel_ventas
        )
        self.btn_nav_vendas.pack(fill="x", padx=10, pady=3)

        btn_sair = tk.Button(
            self.sidebar, text="  🚪  Cerrar sesión", font=("Segoe UI", 10, "bold"),
            bg=self.COLOR_ROJO, fg="#FFFFFF", relief="flat", anchor="w", padx=15, pady=8,
            cursor="hand2", command=self._encerrar_sessao
        )
        btn_sair.pack(side="bottom", fill="x", padx=10, pady=20)

        self.rodape = tk.Frame(self, bg=self.COLOR_PIE_ROJO, height=30)
        self.rodape.pack(side="bottom", fill="x")

        self.lbl_rodape = tk.Label(
            self.rodape,
            text="",
            font=("Segoe UI", 9, "bold"),
            bg=self.COLOR_PIE_ROJO,
            fg="#FFFFFF"
        )
        self.lbl_rodape.pack(side="left", padx=15, pady=5)

        self.container_conteudo = tk.Frame(self, bg=self.FONDO_GENERAL)
        self.container_conteudo.pack(side="top", fill="both", expand=True, padx=30, pady=20)

        self._mostrar_painel_inicio()

    def _limpar_conteudo(self):
        for widget in self.container_conteudo.winfo_children():
            widget.destroy()

    def _destacar_botao(self, boton_activo):
        botones = [self.btn_nav_inicio, self.btn_nav_usuarios, self.btn_nav_produtos, self.btn_nav_vendas]
        for b in botones:
            if b == boton_activo:
                b.configure(bg=self.COLOR_ROJO, fg="#FFFFFF")
            else:
                b.configure(bg=self.NEGRO_BOTON, fg="#CCCCCC")

    def _atualizar_dados_rodape(self):
        n_prod = len(self.servicio.obtener_productos())
        n_user = len(self.servicio.obtener_usuarios())
        n_vent = len(self.servicio.obtener_ventas())
        self.lbl_rodape.config(
            text=f"Productos: {n_prod} | Usuarios: {n_user} | Ventas: {n_vent} | Datos JSON locales"
        )

    def _mostrar_painel_inicio(self):
        self._destacar_botao(self.btn_nav_inicio)
        self._limpar_conteudo()
        self._atualizar_dados_rodape()

        tk.Label(
            self.container_conteudo,
            text="Panel principal",
            font=("Segoe UI", 24, "bold"),
            bg=self.FONDO_GENERAL,
            fg="#111827"
        ).pack(anchor="w", pady=(0, 4))

        tk.Label(
            self.container_conteudo,
            text="Consulte usuarios, gestione productos y registre ventas desde el menú lateral.",
            font=("Segoe UI", 11),
            bg=self.FONDO_GENERAL,
            fg="#4B5563"
        ).pack(anchor="w", pady=(0, 25))

        cards_frame = tk.Frame(self.container_conteudo, bg=self.FONDO_GENERAL)
        cards_frame.pack(fill="x", pady=10)

        n_user = len(self.servicio.obtener_usuarios())
        n_prod = len(self.servicio.obtener_productos())
        n_vent = len(self.servicio.obtener_ventas())

        self._crear_card(cards_frame, "Usuarios registrados", str(n_user), 0)
        self._crear_card(cards_frame, "Productos registrados", str(n_prod), 1)
        self._crear_card(cards_frame, "Ventas registradas", str(n_vent), 2)

    def _crear_card(self, parent, titulo, valor, col):
        card = tk.Frame(parent, bg=self.AZUL_MARCO, padx=25, pady=20, relief="solid", bd=1)
        card.grid(row=0, column=col, padx=(0, 20), sticky="nsew")
        parent.grid_columnconfigure(col, weight=1)

        tk.Label(card, text=titulo, font=("Segoe UI", 10, "bold"), bg=self.AZUL_MARCO, fg="#1E3A8A").pack(anchor="w")
        tk.Label(card, text=valor, font=("Segoe UI", 28, "bold"), bg=self.AZUL_MARCO, fg=self.COLOR_ROJO).pack(anchor="w", pady=(8, 0))

    def _mostrar_painel_usuarios(self):
        self._destacar_botao(self.btn_nav_usuarios)
        self._limpar_conteudo()
        self._atualizar_dados_rodape()

        es_admin = getattr(self.usuario_actual, "rol", "Cliente") == "Administrador"

        tk.Label(
            self.container_conteudo,
            text="Gestión de usuarios" if es_admin else "Consulta de usuarios",
            font=("Segoe UI", 22, "bold"),
            bg=self.FONDO_GENERAL,
            fg="#111827"
        ).pack(anchor="w", pady=(0, 15))

        contenedor_paneles = tk.Frame(self.container_conteudo, bg=self.FONDO_GENERAL)
        contenedor_paneles.pack(fill="both", expand=True)

        if es_admin:
            frame_form = tk.LabelFrame(
                contenedor_paneles,
                text="Datos del usuario",
                font=("Segoe UI", 10, "bold"),
                bg=self.AZUL_MARCO,
                fg=self.COLOR_ROJO,
                padx=15,
                pady=15,
                width=320
            )
            frame_form.pack(side="left", fill="y", padx=(0, 15))
            frame_form.pack_propagate(False)

            tk.Label(frame_form, text="Usuario:", bg=self.AZUL_MARCO, fg="#1E3A8A", font=("Segoe UI", 9, "bold")).grid(row=0, column=0, sticky="w", pady=4)
            self.ent_u_user = tk.Entry(frame_form, font=("Segoe UI", 9), bg=self.GRIS_ENTRY, relief="solid", bd=1)
            self.ent_u_user.grid(row=0, column=1, sticky="ew", padx=(10, 0), pady=4)

            tk.Label(frame_form, text="Nombre:", bg=self.AZUL_MARCO, fg="#1E3A8A", font=("Segoe UI", 9, "bold")).grid(row=1, column=0, sticky="w", pady=4)
            self.ent_u_nom = tk.Entry(frame_form, font=("Segoe UI", 9), bg=self.GRIS_ENTRY, relief="solid", bd=1)
            self.ent_u_nom.grid(row=1, column=1, sticky="ew", padx=(10, 0), pady=4)

            tk.Label(frame_form, text="Contraseña:", bg=self.AZUL_MARCO, fg="#1E3A8A", font=("Segoe UI", 9, "bold")).grid(row=2, column=0, sticky="w", pady=4)
            self.ent_u_pass = tk.Entry(frame_form, show="*", font=("Segoe UI", 9), bg=self.GRIS_ENTRY, relief="solid", bd=1)
            self.ent_u_pass.grid(row=2, column=1, sticky="ew", padx=(10, 0), pady=4)

            tk.Label(frame_form, text="Rol:", bg=self.AZUL_MARCO, fg="#1E3A8A", font=("Segoe UI", 9, "bold")).grid(row=3, column=0, sticky="w", pady=4)
            self.cmb_u_rol = ttk.Combobox(frame_form, values=["Cliente", "Empleado", "Administrador"], state="readonly")
            self.cmb_u_rol.current(0)
            self.cmb_u_rol.grid(row=3, column=1, sticky="ew", padx=(10, 0), pady=4)

            self.lbl_info_rol = tk.Label(frame_form, text="Rol: Acceso básico de compras", bg=self.AZUL_MARCO, fg="#4B5563", font=("Segoe UI", 8, "italic"))
            self.lbl_info_rol.grid(row=4, column=0, columnspan=2, sticky="w", pady=(2, 6))

            frame_form.grid_columnconfigure(1, weight=1)

            btn_reg_u = tk.Button(frame_form, text="➕ Registrar", font=("Segoe UI", 9, "bold"), bg=self.COLOR_ROJO, fg="#FFFFFF", relief="flat", cursor="hand2", command=self._registrar_usuario)
            btn_reg_u.grid(row=5, column=0, columnspan=2, sticky="ew", pady=(8, 3))

            btn_act_u = tk.Button(frame_form, text="🔄 Actualizar", font=("Segoe UI", 9, "bold"), bg=self.COLOR_ROJO, fg="#FFFFFF", relief="flat", cursor="hand2", command=self._actualizar_usuario)
            btn_act_u.grid(row=6, column=0, columnspan=2, sticky="ew", pady=3)

            btn_eli_u = tk.Button(frame_form, text="🗑 Eliminar", font=("Segoe UI", 9, "bold"), bg=self.COLOR_ROJO_OSCURO, fg="#FFFFFF", relief="flat", cursor="hand2", command=self._eliminar_usuario)
            btn_eli_u.grid(row=7, column=0, columnspan=2, sticky="ew", pady=3)

            btn_lim_u = tk.Button(frame_form, text="🧹 Limpiar (Esc)", font=("Segoe UI", 9, "bold"), bg=self.NEGRO_BOTON, fg="#FFFFFF", relief="flat", cursor="hand2", command=self._limpiar_formulario_usuario)
            btn_lim_u.grid(row=8, column=0, columnspan=2, sticky="ew", pady=3)

            self.cmb_u_rol.bind("<<ComboboxSelected>>", self._on_rol_selected)

            for widget in (self.ent_u_user, self.ent_u_nom, self.ent_u_pass, self.cmb_u_rol):
                widget.bind("<Return>", lambda e: self._actualizar_usuario() if self.tv_user.selection() else self._registrar_usuario())
                widget.bind("<Escape>", lambda e: self._limpiar_formulario_usuario())

        frame_tabla = tk.LabelFrame(
            contenedor_paneles,
            text="Usuarios registrados",
            font=("Segoe UI", 10, "bold"),
            bg=self.AZUL_MARCO,
            fg=self.COLOR_ROJO,
            padx=10,
            pady=10
        )
        frame_tabla.pack(side="right", fill="both", expand=True)

        cols = ("usr", "nom", "rol")
        self.tv_user = ttk.Treeview(frame_tabla, columns=cols, show="headings", style="Azul.Treeview", selectmode="browse")
        self.tv_user.heading("usr", text="Usuario")
        self.tv_user.heading("nom", text="Nombre")
        self.tv_user.heading("rol", text="Rol")

        self.tv_user.column("usr", width=140, anchor="w")
        self.tv_user.column("nom", width=240, anchor="w")
        self.tv_user.column("rol", width=120, anchor="center")

        self.tv_user.tag_configure("par", background=self.AZUL_FILA_1)
        self.tv_user.tag_configure("impar", background=self.AZUL_FILA_2)

        sc_u = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tv_user.yview)
        self.tv_user.configure(yscrollcommand=sc_u.set)

        self.tv_user.pack(side="left", fill="both", expand=True)
        sc_u.pack(side="right", fill="y")

        self.tv_user.bind("<<TreeviewSelect>>", self._on_treeview_user_select)
        self.tv_user.bind("<Escape>", lambda e: self._limpiar_formulario_usuario())

        self._refrescar_tabla_usuarios()

    def _on_rol_selected(self, event):
        rol = self.cmb_u_rol.get()
        descripciones = {
            "Cliente": "Rol: Acceso básico de compras",
            "Empleado": "Rol: Operación de productos y ventas",
            "Administrador": "Rol: Control total y gestión de usuarios"
        }
        texto = descripciones.get(rol, f"Rol seleccionado: {rol}")
        if hasattr(self, 'lbl_info_rol'):
            self.lbl_info_rol.config(text=texto)

    def _refrescar_tabla_usuarios(self):
        for row in self.tv_user.get_children():
            self.tv_user.delete(row)

        for i, u in enumerate(self.servicio.obtener_usuarios()):
            usr = getattr(u, 'username', '')
            nom = getattr(u, 'nombre', '')
            rol = getattr(u, 'rol', 'Cliente')
            tag = "par" if i % 2 == 0 else "impar"
            self.tv_user.insert("", tk.END, values=(usr, nom, rol), tags=(tag,))

    def _on_treeview_user_select(self, event):
        seleccion = self.tv_user.selection()
        if not seleccion:
            return
        item = seleccion[0]
        if not item:
            return
        datos = self.tv_user.item(item, "values")
        if datos and hasattr(self, 'ent_u_user') and self.ent_u_user.winfo_exists():
            username = datos[0]
            user = self.servicio.buscar_usuario_por_username(username)
            if user:
                self.ent_u_user.config(state="normal")
                self.ent_u_user.delete(0, tk.END)
                self.ent_u_user.insert(0, user.username)
                self.ent_u_user.config(state="disabled")

                self.ent_u_nom.delete(0, tk.END)
                self.ent_u_nom.insert(0, user.nombre)

                self.ent_u_pass.delete(0, tk.END)
                self.cmb_u_rol.set(user.rol)
                self._on_rol_selected(None)

    def _limpiar_formulario_usuario(self):
        if hasattr(self, 'ent_u_user') and self.ent_u_user.winfo_exists():
            self.ent_u_user.config(state="normal")
            self.ent_u_user.delete(0, tk.END)
            self.ent_u_nom.delete(0, tk.END)
            self.ent_u_pass.delete(0, tk.END)
            self.cmb_u_rol.current(0)
            self._on_rol_selected(None)
            if self.tv_user.selection():
                self.tv_user.selection_remove(self.tv_user.selection())

    def _actualizar_combos_ventas_si_existen(self):
        if hasattr(self, 'cmb_v_user') and self.cmb_v_user.winfo_exists():
            usuarios = self.servicio.obtener_usuarios()
            self.cmb_v_user["values"] = [
                f"{getattr(u, 'username', '')} - {getattr(u, 'nombre', '')}"
                for u in usuarios
            ]

    def _registrar_usuario(self):
        u = self.ent_u_user.get().strip()
        n = self.ent_u_nom.get().strip()
        p = self.ent_u_pass.get().strip()
        r = self.cmb_u_rol.get().strip()

        exito, msg = self.servicio.crear_usuario(u, p, n, r)
        if exito:
            messagebox.showinfo("Éxito", msg)
            self._refrescar_tabla_usuarios()
            self._limpiar_formulario_usuario()
            self._actualizar_combos_ventas_si_existen()
            self._atualizar_dados_rodape()
        else:
            messagebox.showerror("Error", msg)

    def _actualizar_usuario(self):
        u = self.ent_u_user.get().strip()
        n = self.ent_u_nom.get().strip()
        p = self.ent_u_pass.get().strip()
        r = self.cmb_u_rol.get().strip()

        exito, msg = self.servicio.actualizar_usuario(u, p, n, r)
        if exito:
            messagebox.showinfo("Éxito", msg)
            self._refrescar_tabla_usuarios()
            self._limpiar_formulario_usuario()
            self._actualizar_combos_ventas_si_existen()
            self._atualizar_dados_rodape()
        else:
            messagebox.showerror("Error", msg)

    def _eliminar_usuario(self):
        u = self.ent_u_user.get().strip()
        if not u:
            messagebox.showwarning("Atención", "Seleccione un usuario de la lista.")
            return

        usuario_activo = getattr(self.usuario_actual, "username", "")
        if u == usuario_activo:
            messagebox.showwarning("Atención", "No puede eliminar al usuario activo.")
            return
        if messagebox.askyesno("Confirmar", f"¿Eliminar al usuario '{u}'?"):
            exito, msg = self.servicio.eliminar_usuario(u, usuario_activo)
            if exito:
                messagebox.showinfo("Éxito", msg)
                self._refrescar_tabla_usuarios()
                self._limpiar_formulario_usuario()
                self._actualizar_combos_ventas_si_existen()
                self._atualizar_dados_rodape()
            else:
                messagebox.showerror("Error", msg)

    def _mostrar_painel_productos(self):
        self._destacar_botao(self.btn_nav_produtos)
        self._limpar_conteudo()
        self._atualizar_dados_rodape()

        tk.Label(
            self.container_conteudo,
            text="Gestión de productos",
            font=("Segoe UI", 22, "bold"),
            bg=self.FONDO_GENERAL,
            fg="#111827"
        ).pack(anchor="w", pady=(0, 15))

        contenedor_paneles = tk.Frame(self.container_conteudo, bg=self.FONDO_GENERAL)
        contenedor_paneles.pack(fill="both", expand=True)

        frame_form = tk.LabelFrame(
            contenedor_paneles,
            text="Datos del producto",
            font=("Segoe UI", 10, "bold"),
            bg=self.AZUL_MARCO,
            fg=self.COLOR_ROJO,
            padx=15,
            pady=15,
            width=320
        )
        frame_form.pack(side="left", fill="y", padx=(0, 15))
        frame_form.pack_propagate(False)

        campos = [("Código", "ent_cod"), ("Nombre", "ent_nom"), ("Categoría", "ent_cat"), ("Precio", "ent_prc"), ("Stock", "ent_stk")]
        self.entradas_prod = {}

        for i, (texto, var_name) in enumerate(campos):
            tk.Label(
                frame_form,
                text=texto,
                bg=self.AZUL_MARCO,
                fg="#1E3A8A",
                font=("Segoe UI", 9, "bold"),
                anchor="w"
            ).grid(row=i, column=0, sticky="w", pady=4)

            ent = tk.Entry(
                frame_form,
                font=("Segoe UI", 9),
                bg=self.GRIS_ENTRY,
                fg="#111111",
                relief="solid",
                bd=1,
                highlightthickness=0
            )
            ent.grid(row=i, column=1, sticky="ew", padx=(10, 0), pady=4)
            self.entradas_prod[var_name] = ent

        frame_form.grid_columnconfigure(1, weight=1)

        btn_reg = tk.Button(frame_form, text="➕ Registrar", font=("Segoe UI", 9, "bold"), bg=self.COLOR_ROJO, fg="#FFFFFF", relief="flat", cursor="hand2", command=self._registrar_producto)
        btn_reg.grid(row=6, column=0, columnspan=2, sticky="ew", pady=(15, 3))

        btn_car = tk.Button(frame_form, text="🔍 Cargar por código", font=("Segoe UI", 9, "bold"), bg=self.NEGRO_BOTON, fg="#FFFFFF", relief="flat", cursor="hand2", command=self._cargar_producto)
        btn_car.grid(row=7, column=0, columnspan=2, sticky="ew", pady=3)

        btn_act = tk.Button(frame_form, text="🔄 Actualizar", font=("Segoe UI", 9, "bold"), bg=self.COLOR_ROJO, fg="#FFFFFF", relief="flat", cursor="hand2", command=self._actualizar_producto)
        btn_act.grid(row=8, column=0, columnspan=2, sticky="ew", pady=3)

        btn_eli = tk.Button(frame_form, text="🗑 Eliminar", font=("Segoe UI", 9, "bold"), bg=self.COLOR_ROJO_OSCURO, fg="#FFFFFF", relief="flat", cursor="hand2", command=self._eliminar_producto)
        btn_eli.grid(row=9, column=0, columnspan=2, sticky="ew", pady=3)

        btn_lim = tk.Button(frame_form, text="🧹 Limpiar", font=("Segoe UI", 9, "bold"), bg=self.NEGRO_BOTON, fg="#FFFFFF", relief="flat", cursor="hand2", command=self._limpiar_formulario_prod)
        btn_lim.grid(row=10, column=0, columnspan=2, sticky="ew", pady=3)

        frame_tabla = tk.LabelFrame(
            contenedor_paneles,
            text="Productos registrados",
            font=("Segoe UI", 10, "bold"),
            bg=self.AZUL_MARCO,
            fg=self.COLOR_ROJO,
            padx=10,
            pady=10
        )
        frame_tabla.pack(side="right", fill="both", expand=True)

        cols = ("cod", "nom", "cat")
        self.tv_prod = ttk.Treeview(frame_tabla, columns=cols, show="headings", style="Azul.Treeview")
        self.tv_prod.heading("cod", text="Código")
        self.tv_prod.heading("nom", text="Nombre")
        self.tv_prod.heading("cat", text="Categoría")

        self.tv_prod.column("cod", width=90, anchor="center")
        self.tv_prod.column("nom", width=180, anchor="w")
        self.tv_prod.column("cat", width=140, anchor="w")

        self.tv_prod.tag_configure("par", background=self.AZUL_FILA_1)
        self.tv_prod.tag_configure("impar", background=self.AZUL_FILA_2)

        sc_prod = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tv_prod.yview)
        self.tv_prod.configure(yscrollcommand=sc_prod.set)

        self.tv_prod.pack(side="left", fill="both", expand=True)
        sc_prod.pack(side="right", fill="y")

        self._refrescar_tabla_productos()

    def _refrescar_tabla_productos(self):
        for row in self.tv_prod.get_children():
            self.tv_prod.delete(row)
        for i, p in enumerate(self.servicio.obtener_productos()):
            tag = "par" if i % 2 == 0 else "impar"
            self.tv_prod.insert("", tk.END, values=(p.id_producto, p.nombre, p.categoria), tags=(tag,))

    def _limpiar_formulario_prod(self):
        for ent in self.entradas_prod.values():
            ent.delete(0, tk.END)

    def _registrar_producto(self):
        c = self.entradas_prod["ent_cod"].get().strip()
        n = self.entradas_prod["ent_nom"].get().strip()
        cat = self.entradas_prod["ent_cat"].get().strip()
        p = self.entradas_prod["ent_prc"].get().strip()
        s = self.entradas_prod["ent_stk"].get().strip()

        if not c or not n or not cat or not p or not s:
            messagebox.showwarning("Atención", "Complete todos los campos.")
            return

        try:
            nuevo = Producto(c, n, cat, float(p), int(s))
            exito, msg = self.servicio.crear_producto(nuevo)
            if exito:
                messagebox.showinfo("Éxito", msg)
                self._refrescar_tabla_productos()
                self._limpiar_formulario_prod()
                self._atualizar_dados_rodape()
            else:
                messagebox.showerror("Error", msg)
        except ValueError:
            messagebox.showerror("Error", "Precio y stock deben ser numéricos.")

    def _cargar_producto(self):
        c = self.entradas_prod["ent_cod"].get().strip()
        if not c:
            messagebox.showwarning("Atención", "Ingrese el código a buscar.")
            return
        p = self.servicio.buscar_producto_por_id(c)
        if p:
            self._limpiar_formulario_prod()
            self.entradas_prod["ent_cod"].insert(0, p.id_producto)
            self.entradas_prod["ent_nom"].insert(0, p.nombre)
            self.entradas_prod["ent_cat"].insert(0, p.categoria)
            self.entradas_prod["ent_prc"].insert(0, str(p.precio))
            self.entradas_prod["ent_stk"].insert(0, str(p.stock))
        else:
            messagebox.showerror("Error", "Producto no encontrado.")

    def _actualizar_producto(self):
        c = self.entradas_prod["ent_cod"].get().strip()
        n = self.entradas_prod["ent_nom"].get().strip()
        cat = self.entradas_prod["ent_cat"].get().strip()
        p = self.entradas_prod["ent_prc"].get().strip()
        s = self.entradas_prod["ent_stk"].get().strip()

        try:
            prod_mod = Producto(c, n, cat, float(p), int(s))
            exito, msg = self.servicio.actualizar_producto(prod_mod)
            if exito:
                messagebox.showinfo("Éxito", msg)
                self._refrescar_tabla_productos()
            else:
                messagebox.showerror("Error", msg)
        except Exception:
            messagebox.showerror("Error", "Revise los campos numéricos.")

    def _eliminar_producto(self):
        c = self.entradas_prod["ent_cod"].get().strip()
        if not c:
            messagebox.showwarning("Atención", "Ingrese el código a eliminar.")
            return
        if messagebox.askyesno("Confirmar", f"¿Eliminar producto {c}?"):
            exito, msg = self.servicio.eliminar_producto(c)
            if exito:
                messagebox.showinfo("Éxito", msg)
                self._refrescar_tabla_productos()
                self._limpiar_formulario_prod()
                self._atualizar_dados_rodape()
            else:
                messagebox.showerror("Error", msg)

    def _mostrar_painel_ventas(self):
        self._destacar_botao(self.btn_nav_vendas)
        self._limpar_conteudo()
        self._atualizar_dados_rodape()

        tk.Label(
            self.container_conteudo,
            text="Registro de ventas",
            font=("Segoe UI", 22, "bold"),
            bg=self.FONDO_GENERAL,
            fg="#111827"
        ).pack(anchor="w", pady=(0, 15))

        contenedor_paneles = tk.Frame(self.container_conteudo, bg=self.FONDO_GENERAL)
        contenedor_paneles.pack(fill="both", expand=True)

        frame_nv = tk.LabelFrame(
            contenedor_paneles,
            text="Nueva venta",
            font=("Segoe UI", 10, "bold"),
            bg=self.AZUL_MARCO,
            fg=self.COLOR_ROJO,
            padx=15,
            pady=15,
            width=340
        )
        frame_nv.pack(side="left", fill="y", padx=(0, 15))
        frame_nv.pack_propagate(False)

        tk.Label(frame_nv, text="Usuario", font=("Segoe UI", 9, "bold"), bg=self.AZUL_MARCO, fg="#1E3A8A").grid(row=0, column=0, sticky="w", pady=6)
        self.cmb_v_user = ttk.Combobox(frame_nv, state="readonly", width=22)
        self.cmb_v_user.grid(row=0, column=1, sticky="ew", padx=(10, 0), pady=6)

        tk.Label(frame_nv, text="Producto", font=("Segoe UI", 9, "bold"), bg=self.AZUL_MARCO, fg="#1E3A8A").grid(row=1, column=0, sticky="w", pady=6)
        self.cmb_v_prod = ttk.Combobox(frame_nv, state="readonly", width=22)
        self.cmb_v_prod.grid(row=1, column=1, sticky="ew", padx=(10, 0), pady=6)

        frame_nv.grid_columnconfigure(1, weight=1)

        btn_reg_v = tk.Button(
            frame_nv,
            text="➕ Registrar venta",
            font=("Segoe UI", 9, "bold"),
            bg=self.COLOR_ROJO,
            fg="#FFFFFF",
            relief="flat",
            cursor="hand2",
            command=self.callback_registrar_venta
        )
        btn_reg_v.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(20, 5))

        self._refrescar_combos_ventas()

        frame_tv = tk.LabelFrame(
            contenedor_paneles,
            text="Ventas registradas",
            font=("Segoe UI", 10, "bold"),
            bg=self.AZUL_MARCO,
            fg=self.COLOR_ROJO,
            padx=10,
            pady=10
        )
        frame_tv.pack(side="right", fill="both", expand=True)

        cols = ("num", "usr", "prd")
        self.tv_ventas = ttk.Treeview(frame_tv, columns=cols, show="headings", style="Azul.Treeview")
        self.tv_ventas.heading("num", text="N°")
        self.tv_ventas.heading("usr", text="Usuario")
        self.tv_ventas.heading("prd", text="Producto")

        self.tv_ventas.column("num", width=90, anchor="center")
        self.tv_ventas.column("usr", width=180, anchor="w")
        self.tv_ventas.column("prd", width=220, anchor="w")

        self.tv_ventas.tag_configure("par", background=self.AZUL_FILA_1)
        self.tv_ventas.tag_configure("impar", background=self.AZUL_FILA_2)

        sc_v = ttk.Scrollbar(frame_tv, orient="vertical", command=self.tv_ventas.yview)
        self.tv_ventas.configure(yscrollcommand=sc_v.set)

        self.tv_ventas.pack(side="left", fill="both", expand=True)
        sc_v.pack(side="right", fill="y")

        self._refrescar_tabla_ventas()

    def _refrescar_combos_ventas(self):
        usuarios = self.servicio.obtener_usuarios()
        self.cmb_v_user["values"] = [
            f"{getattr(u, 'id_usuario', getattr(u, 'id', getattr(u, 'username', '')))} - {getattr(u, 'nombre', '')}"
            for u in usuarios
        ]

        productos = self.servicio.obtener_productos()
        self.cmb_v_prod["values"] = [f"{p.id_producto} - {p.nombre}" for p in productos]

    def _refrescar_tabla_ventas(self):
        for row in self.tv_ventas.get_children():
            self.tv_ventas.delete(row)

        for i, v in enumerate(self.servicio.obtener_ventas(), 1):
            try:
                num = v["id_venta"] if isinstance(v, dict) else getattr(v, "id_venta", str(i))
                usr = v["nombre_usuario"] if isinstance(v, dict) else getattr(v, "nombre_usuario", "")
                prod = v["nombre_producto"] if isinstance(v, dict) else getattr(v, "nombre_producto", "")
            except Exception:
                continue
            tag = "par" if i % 2 == 0 else "impar"
            self.tv_ventas.insert("", tk.END, values=(num, usr, prod), tags=(tag,))

    def callback_registrar_venta(self):
        sel_u = self.cmb_v_user.get().strip()
        sel_p = self.cmb_v_prod.get().strip()

        if not sel_u or not sel_p:
            messagebox.showwarning("Atención", "Seleccione usuario y producto.")
            return

        id_u = sel_u.split(" - ")[0]
        id_p = sel_p.split(" - ")[0]

        exito, res = self.servicio.registrar_venta(id_u, id_p)
        if exito:
            id_txt = getattr(res, 'id_venta', str(res))
            messagebox.showinfo("Éxito", f"Venta registrada ({id_txt}).")
            self._refrescar_tabla_ventas()
            self._atualizar_dados_rodape()
        else:
            messagebox.showerror("Error", str(res))

    def _encerrar_sessao(self):
        if messagebox.askyesno("Cerrar sesión", "¿Desea cerrar la sesión actual?"):
            self.master.winfo_toplevel().destroy()
