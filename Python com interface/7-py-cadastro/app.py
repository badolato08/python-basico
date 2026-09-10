# Cadastro com Login — CustomTkinter + SQLite
# Fluxo: TelaLogin -> (credenciais corretas) -> TelaCadastro -> TelaLista

import customtkinter as ctk
import sqlite3
import hashlib
from tkinter import messagebox, ttk
from PIL import Image
import os
import sys
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
def get_db_path():
    if getattr(sys, "frozen", False):
        application_path = os.path.dirname(sys.executable)
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(application_path, "cadastro.db")

def gerar_hash_senha(senha):
   
    return hashlib.sha256(senha.encode("utf-8")).hexdigest()

class Database:

    def __init__(self, db_name=None):
        self.conn = sqlite3.connect(db_name or get_db_path())
        self.cursor = self.conn.cursor()

        self.create_tables()
        self.create_admin_user()

    def create_tables(self):

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                telefone TEXT NOT NULL
            )
            """
        )

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS credenciais (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_usuario TEXT NOT NULL UNIQUE,
                senha TEXT NOT NULL
            )
            """
        )

        self.conn.commit()

    # --------------------------------------------------------
    # Cria o usuário admin
    # --------------------------------------------------------

    def create_admin_user(self):

        self.cursor.execute(
            "SELECT * FROM credenciais WHERE nome_usuario = ?",
            ("admin",)
        )

        if self.cursor.fetchone() is None:

            self.cursor.execute(
                """
                INSERT INTO credenciais
                (nome_usuario, senha)
                VALUES (?, ?)
                """,
                ("admin", gerar_hash_senha("admin"))
            )

            self.conn.commit()

            print("Usuário admin criado com sucesso.")

    # --------------------------------------------------------
    # Verifica login
    # --------------------------------------------------------

    def verificar_credenciais(self, nome_usuario, senha):

        self.cursor.execute(
            """
            SELECT *
            FROM credenciais
            WHERE nome_usuario = ?
            AND senha = ?
            """,
            (
                nome_usuario,
                gerar_hash_senha(senha)
            )
        )

        return self.cursor.fetchone() is not None


    def insert_user(self, nome, email, telefone):

        self.cursor.execute(
            """
            INSERT INTO usuarios
            (nome, email, telefone)
            VALUES (?, ?, ?)
            """,
            (nome, email, telefone)
        )
        self.conn.commit()


    def get_all_users(self):

        self.cursor.execute(
            "SELECT id, nome, email, telefone FROM usuarios"
        )
        return self.cursor.fetchall()

    def update_user(self, id_usuario, nome, email, telefone):

        self.cursor.execute(
            """
            UPDATE usuarios
            SET nome = ?,
                email = ?,
                telefone = ?
            WHERE id = ?
            """,
            (nome, email, telefone, id_usuario)
        )
        self.conn.commit()
    def delete_user(self, id_usuario):

        self.cursor.execute(
            "DELETE FROM usuarios WHERE id = ?",
            (id_usuario,)
        )
        self.conn.commit()
        if self.conn:
            self.conn.close()
def formatar_telefone(texto):

    numeros = "".join(
        c for c in texto
        if c.isdigit()
    )[:11]

    formatado = ""

    if len(numeros) > 0:

        formatado += f"({numeros[:2]}"

        if len(numeros) >= 2:
            formatado += ")"

        if len(numeros) > 2:
            formatado += f" {numeros[2:7]}"

        if len(numeros) > 7:
            formatado += f"-{numeros[7:]}"

    return formatado
def carregar_icone(nome, tamanho=(20, 20)):

    caminho = resource_path(nome)

    if not os.path.exists(caminho):
        return None

    try:
        imagem = Image.open(caminho)

        return ctk.CTkImage(
            light_image=imagem,
            dark_image=imagem,
            size=tamanho
        )

    except Exception:
        return None


# ============================================================
# TELA DE LOGIN
# ============================================================

class TelaLogin(ctk.CTk):

    def __init__(self, db):

        super().__init__()

        self.db = db

        self.setup_ui()

    # --------------------------------------------------------
    # Interface
    # --------------------------------------------------------

    def setup_ui(self):

        self.title("Login")
        self.geometry("300x250")
        self.resizable(False, False)

        icon_path = resource_path("entrada.ico")

        if os.path.exists(icon_path):

            try:
                self.iconbitmap(icon_path)
            except Exception:
                pass

        self.frame = ctk.CTkFrame(self)

        self.frame.pack(
            pady=20,
            padx=20,
            fill="both",
            expand=True
        )

        self.label = ctk.CTkLabel(
            self.frame,
            text="Login",
            font=("Roboto", 24)
        )

        self.label.pack(pady=10)

        self.nome_usuario_entry = ctk.CTkEntry(
            self.frame,
            placeholder_text="Nome de usuário"
        )

        self.nome_usuario_entry.pack(
            pady=5,
            padx=10,
            fill="x"
        )

        self.senha_entry = ctk.CTkEntry(
            self.frame,
            placeholder_text="Senha",
            show="*"
        )

        self.senha_entry.pack(
            pady=5,
            padx=10,
            fill="x"
        )

        self.login_btn = ctk.CTkButton(
            self.frame,
            text="Entrar",
            command=self.fazer_login
        )

        self.login_btn.pack(pady=10)

        self.senha_entry.bind(
            "<Return>",
            lambda event: self.fazer_login()
        )

    # --------------------------------------------------------
    # Login
    # --------------------------------------------------------

    def fazer_login(self):

        nome_usuario = self.nome_usuario_entry.get().strip()
        senha = self.senha_entry.get()

        if self.db.verificar_credenciais(
            nome_usuario,
            senha
        ):

            self.destroy()

            app = TelaCadastro(self.db)
            app.mainloop()

        else:

            messagebox.showerror(
                "Erro",
                "Nome de usuário ou senha inválidos."
            )


# ============================================================
# TELA DE CADASTRO
# ============================================================

class TelaCadastro(ctk.CTk):

    def __init__(self, db):

        super().__init__()

        self.db = db

        self.setup_ui()

    # --------------------------------------------------------
    # Interface
    # --------------------------------------------------------

    def setup_ui(self):

        self.title("Cadastro de Usuários")
        self.geometry("400x450")
        self.resizable(False, False)

        icon_path = resource_path("entrada.ico")

        if os.path.exists(icon_path):

            try:
                self.iconbitmap(icon_path)
            except Exception:
                pass

        self.frame = ctk.CTkFrame(self)

        self.frame.pack(
            pady=10,
            padx=10,
            fill="both",
            expand=True
        )

        # Ícones
        self.light_icon = carregar_icone(
            "light_icon.png"
        )

        self.dark_icon = carregar_icone(
            "dark_icon.png"
        )

        # Botão de tema
        self.tema_btn = ctk.CTkButton(
            self,
            image=self.dark_icon,
            text="",
            width=30,
            height=30,
            command=self.alternar_tema
        )

        self.tema_btn.place(
            relx=0.95,
            rely=0.05,
            anchor="ne"
        )

        # Título
        self.label = ctk.CTkLabel(
            self.frame,
            text="Cadastro de Usuários",
            font=("Roboto", 24)
        )

        self.label.pack(pady=10)

        # Nome
        self.nome_entry = ctk.CTkEntry(
            self.frame,
            placeholder_text="Nome"
        )

        self.nome_entry.pack(
            pady=5,
            padx=10,
            fill="x"
        )

        # E-mail
        self.email_entry = ctk.CTkEntry(
            self.frame,
            placeholder_text="E-mail"
        )

        self.email_entry.pack(
            pady=5,
            padx=10,
            fill="x"
        )

        # Telefone
        self.telefone_entry = ctk.CTkEntry(
            self.frame,
            placeholder_text="Telefone"
        )

        self.telefone_entry.pack(
            pady=5,
            padx=10,
            fill="x"
        )

        self.telefone_entry.bind(
            "<KeyRelease>",
            self.formatar_telefone
        )

        # Frame dos botões
        self.btn_frame = ctk.CTkFrame(
            self.frame,
            fg_color="transparent"
        )

        self.btn_frame.pack(pady=10)

        # Ícones dos botões
        self.cadastrar_icon = carregar_icone(
            "cadastrar_icon.png"
        )

        self.cancelar_icon = carregar_icone(
            "cancelar_icon.png"
        )

        self.listar_icon = carregar_icone(
            "listar_icon.png"
        )

        # Botão cadastrar
        self.cadastrar_btn = ctk.CTkButton(
            self.btn_frame,
            text="Cadastrar",
            image=self.cadastrar_icon,
            compound="left",
            fg_color="green",
            hover_color="darkgreen",
            command=self.cadastrar
        )
        self.cadastrar_btn.pack(
            side="left",
            padx=5
        )
        self.cancelar_btn = ctk.CTkButton(
            self.btn_frame,
            text="Cancelar",
            image=self.cancelar_icon,
            compound="left",
            fg_color="darkred",
            hover_color="red",
            command=self.fechar
        )
        self.cancelar_btn.pack(
            side="left",
            padx=5
        )
        self.listar_btn = ctk.CTkButton(
            self.frame,
            text="Listar Cadastros",
            image=self.listar_icon,
            compound="left",
            command=self.abrir_lista
        )
        self.listar_btn.pack(
            pady=10,
            padx=10,
            fill="x"
        )
    def formatar_telefone(self, event=None):
        formatado = formatar_telefone(
            self.telefone_entry.get()
        )
        self.telefone_entry.delete(
            0,
            "end"
        )
        self.telefone_entry.insert(
            0,
            formatado
        )
    def cadastrar(self):
        nome = self.nome_entry.get().strip()
        email = self.email_entry.get().strip()
        telefone = self.telefone_entry.get().strip()
        if not nome or not email or not telefone:
            messagebox.showerror(
                "Erro",
                "Por favor, preencha todos os campos."
            )
            return
        self.db.insert_user(
            nome,
            email,
            telefone
        )
        messagebox.showinfo(
            "Sucesso",
            "Usuário cadastrado com sucesso!"
        )
        self.limpar_campos()
    def limpar_campos(self):
        self.nome_entry.delete(0, "end")
        self.email_entry.delete(0, "end")
        self.telefone_entry.delete(0, "end")
    def abrir_lista(self):
        self.withdraw()
        lista_window = TelaLista(
            self,
            self.db
        )
        lista_window.grab_set()
    def alternar_tema(self):
        if ctk.get_appearance_mode() == "Dark":
            ctk.set_appearance_mode("Light")
            if self.light_icon:
                self.tema_btn.configure(
                    image=self.light_icon
                )
        else:
            ctk.set_appearance_mode("Dark")
            if self.dark_icon:
                self.tema_btn.configure(
                    image=self.dark_icon
                )
    def fechar(self):
        self.destroy()
class TelaLista(ctk.CTkToplevel):
    def __init__(self, master, db):
        super().__init__(master)
        self.db = db
        self.setup_ui()
        self.carregar_dados()
        self.protocol(
            "WM_DELETE_WINDOW",
            self.voltar
        )
    def setup_ui(self):
        self.title("Lista de Usuários")
        self.geometry("700x500")
        self.resizable(True, True)
        icon_path = resource_path("entrada.ico")
        if os.path.exists(icon_path):
            try:
                self.iconbitmap(icon_path)
            except Exception:
                pass
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(
            pady=20,
            padx=20,
            fill="both",
            expand=True
        )
        self.label = ctk.CTkLabel(
            self.frame,
            text="Lista de Usuários",
            font=("Roboto", 28)
        )
        self.label.pack(pady=12)
        self.style = ttk.Style(self)
        self.configurar_estilo_treeview()

        self.tree = ttk.Treeview(
            self.frame,
            columns=(
                "ID",
                "Nome",
                "E-mail",
                "Telefone"
            ),
            show="headings"
        )
        self.tree.heading(
            "ID",
            text="ID",
            anchor="center"
        )
        self.tree.heading(
            "Nome",
            text="Nome",
            anchor="center"
        )
        self.tree.heading(
            "E-mail",
            text="E-mail",
            anchor="center"
        )
        self.tree.heading(
            "Telefone",
            text="Telefone",
            anchor="center"
        )
        self.tree.column(
            "ID",
            width=50,
            anchor="center"
        )
        self.tree.column(
            "Nome",
            width=180,
            anchor="center"
        )
        self.tree.column(
            "E-mail",
            width=220,
            anchor="center"
        )
        self.tree.column(
            "Telefone",
            width=150,
            anchor="center"
        )
        self.tree.pack(
            pady=12,
            padx=10,
            fill="both",
            expand=True
        )
        self.btn_frame = ctk.CTkFrame(
            self.frame,
            fg_color="transparent"
        )
        self.btn_frame.pack(
            pady=12,
            padx=10
        )
        self.atualizar_icon = carregar_icone(
            "atualizar_icon.png"
        )
        self.excluir_icon = carregar_icone(
            "excluir_icon.png"
        )
        self.voltar_icon = carregar_icone(
            "voltar_icon.png"
        )
        self.atualizar_btn = ctk.CTkButton(
            self.btn_frame,
            text="Atualizar",
            image=self.atualizar_icon,
            compound="left",
            fg_color="green",
            hover_color="darkgreen",
            command=self.atualizar_usuario
        )
        self.atualizar_btn.pack(
            side="left",
            padx=5
        )
        self.excluir_btn = ctk.CTkButton(
            self.btn_frame,
            text="Excluir",
            image=self.excluir_icon,
            compound="left",
            fg_color="darkred",
            hover_color="red",
            command=self.excluir_usuario
        )
        self.excluir_btn.pack(
            side="left",
            padx=5
        )
        self.voltar_btn = ctk.CTkButton(
            self.btn_frame,
            text="Voltar",
            image=self.voltar_icon,
            compound="left",
            command=self.voltar
        )
        self.voltar_btn.pack(
            side="left",
            padx=5
        )
    def configurar_estilo_treeview(self):
        modo = ctk.get_appearance_mode()
        self.style.theme_use("clam")
        if modo == "Dark":
            self.style.configure(
                "Treeview",
                background="#2a2d2e",
                foreground="white",
                fieldbackground="#2a2d2e",
                font=("Roboto", 12),
                rowheight=30
            )
            self.style.configure(
                "Treeview.Heading",
                background="#565b5e",
                foreground="white",
                font=("Roboto", 14)
            )
        else:
            self.style.configure(
                "Treeview",
                background="white",
                foreground="black",
                fieldbackground="white",
                font=("Roboto", 12),
                rowheight=30
            )
            self.style.configure(
                "Treeview.Heading",
                background="#e1e1e1",
                foreground="black",
                font=("Roboto", 14)
            )
        self.style.map(
            "Treeview",
            background=[
                ("selected", "#22559b")
            ]
        )
        self.style.map(
            "Treeview",
            foreground=[
                ("selected", "white")
            ]
        )
        self.style.configure(
            "Treeview.Heading",
            relief="flat"
        )

        self.style.map(
            "Treeview.Heading",
            background=[
                ("active", "#3484F0")
            ]
        )

    # --------------------------------------------------------
    # Carrega dados
    # --------------------------------------------------------

    def carregar_dados(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

        usuarios = self.db.get_all_users()

        for row in usuarios:

            self.tree.insert(
                "",
                "end",
                values=row
            )

    # --------------------------------------------------------
    # Atualizar usuário
    # --------------------------------------------------------

    def atualizar_usuario(self):

        selected = self.tree.selection()

        if not selected:

            messagebox.showerror(
                "Erro",
                "Por favor, selecione um usuário para atualizar."
            )

            return

        usuario = self.tree.item(
            selected[0]
        )["values"]

        update_window = ctk.CTkToplevel(self)

        update_window.title(
            "Atualizar Usuário"
        )

        update_window.geometry(
            "350x350"
        )

        update_window.resizable(
            False,
            False
        )

        icon_path = resource_path(
            "entrada.ico"
        )

        if os.path.exists(icon_path):

            try:
                update_window.iconbitmap(
                    icon_path
                )
            except Exception:
                pass

        # Nome
        ctk.CTkLabel(
            update_window,
            text="Nome:"
        ).pack(pady=(15, 5))

        nome_entry = ctk.CTkEntry(
            update_window,
            width=250
        )

        nome_entry.pack(pady=5)

        nome_entry.insert(
            0,
            usuario[1]
        )

        # E-mail
        ctk.CTkLabel(
            update_window,
            text="E-mail:"
        ).pack(pady=(10, 5))

        email_entry = ctk.CTkEntry(
            update_window,
            width=250
        )

        email_entry.pack(pady=5)

        email_entry.insert(
            0,
            usuario[2]
        )

        # Telefone
        ctk.CTkLabel(
            update_window,
            text="Telefone:"
        ).pack(pady=(10, 5))

        telefone_entry = ctk.CTkEntry(
            update_window,
            width=250
        )

        telefone_entry.pack(pady=5)

        telefone_entry.insert(
            0,
            usuario[3]
        )

        # Formata telefone
        def formatar_e_atualizar(event=None):

            formatado = formatar_telefone(
                telefone_entry.get()
            )

            telefone_entry.delete(
                0,
                "end"
            )

            telefone_entry.insert(
                0,
                formatado
            )

        telefone_entry.bind(
            "<KeyRelease>",
            formatar_e_atualizar
        )

        # Salvar atualização
        def salvar_atualizacao():

            nome = nome_entry.get().strip()
            email = email_entry.get().strip()
            telefone = telefone_entry.get().strip()

            if not nome or not email or not telefone:

                messagebox.showerror(
                    "Erro",
                    "Preencha todos os campos.",
                    parent=update_window
                )

                return

            self.db.update_user(
                usuario[0],
                nome,
                email,
                telefone
            )

            messagebox.showinfo(
                "Sucesso",
                "Usuário atualizado com sucesso!",
                parent=update_window
            )

            update_window.destroy()

            self.carregar_dados()

        ctk.CTkButton(
            update_window,
            text="Salvar",
            command=salvar_atualizacao
        ).pack(pady=20)

        update_window.grab_set()

    # --------------------------------------------------------
    # Excluir usuário
    # --------------------------------------------------------

    def excluir_usuario(self):

        selected = self.tree.selection()

        if not selected:

            messagebox.showerror(
                "Erro",
                "Por favor, selecione um usuário para excluir."
            )

            return

        confirmar = messagebox.askyesno(
            "Confirmar",
            "Tem certeza que deseja excluir este usuário?"
        )

        if confirmar:

            usuario = self.tree.item(
                selected[0]
            )["values"]

            self.db.delete_user(
                usuario[0]
            )

            messagebox.showinfo(
                "Sucesso",
                "Usuário excluído com sucesso!"
            )

            self.carregar_dados()

    # --------------------------------------------------------
    # Voltar
    # --------------------------------------------------------

    def voltar(self):

        self.master.deiconify()

        self.destroy()


# ============================================================
# APLICAÇÃO
# ============================================================

class App:

    def __init__(self):

        ctk.set_appearance_mode("dark")

        ctk.set_default_color_theme("blue")

        self.db = Database()

        self.login_window = TelaLogin(
            self.db
        )

    def run(self):

        self.login_window.mainloop()

    def __del__(self):

        try:
            self.db.close()
        except Exception:
            pass


# ============================================================
# INÍCIO DO PROGRAMA
# ============================================================

if __name__ == "__main__":

    app = App()

    app.run()

