import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
import os

class TelaLogin:
    def __init__(self, master):
        self.master = master
        
        # Cria o container principal ocupando toda a tela branca
        self.painel_principal = ctk.CTkFrame(
            self.master,
            fg_color="white",
            corner_radius=0
        )
        self.painel_principal.pack(fill="both", expand=True)
        
        # Cria um sub-container invisível no centro para segurar os componentes alinhados
        self.conteudo_centro = ctk.CTkFrame(
            self.painel_principal,
            fg_color="white"
        )
        self.conteudo_centro.pack(expand=True)
        
        # --- CARREGAR A LOGO ---
        caminho_atual = os.path.dirname(__file__)
        caminho_foto = os.path.join(caminho_atual, "foto_login.png")
        
        try:
            self.imagem_logo = ctk.CTkImage(
                light_image=Image.open(caminho_foto),
                dark_image=Image.open(caminho_foto),
                size=(180, 210)
            )
            self.logo_label = ctk.CTkLabel(self.conteudo_centro, image=self.imagem_logo, text="")
            self.logo_label.pack(pady=(0, 20))
        except FileNotFoundError:
            ctk.CTkLabel(self.conteudo_centro, text="[ FARMAR BABY ]", font=("Arial", 22, "bold"), text_color="#ba4b6e").pack(pady=(20, 20))

        # --- CAMPOS DE ENTRADA ---
        self.usuario = ctk.CTkEntry(
            self.conteudo_centro,
            width=280,
            height=42,
            placeholder_text="Digite seu e-mail",
            fg_color="#f8fafc",
            border_color="#e2e8f0",
            border_width=1
        )
        self.usuario.pack(pady=12)
        
        self.senha = ctk.CTkEntry(
            self.conteudo_centro,
            width=280,
            height=42,
            placeholder_text="Digite sua senha",
            show="*",
            fg_color="#f8fafc",
            border_color="#e2e8f0",
            border_width=1
        )
        self.senha.pack(pady=12)
        
        # --- BOTÃO ENTRAR ---
        self.botao_entrar = ctk.CTkButton(
            self.conteudo_centro,
            width=280,
            height=45,
            text="Entrar",
            font=("Arial", 16, "bold"),
            fg_color="#ff6b8b",
            hover_color="#e05372",
            corner_radius=8,
            command=self.validar_login
        )
        self.botao_entrar.pack(pady=(25, 15))
        
        # --- LINK PARA O CADASTRO ---
        self.link_cadastro = ctk.CTkButton(
            self.conteudo_centro,
            text="Ainda não tem uma conta? Cadastre-se",
            font=("Arial", 12, "underline"),
            fg_color="transparent",
            text_color="#ba4b6e",
            hover_color="#feebf1",
            command=self.master.abrir_cadastro
        )
        self.link_cadastro.pack(pady=5)

    def validar_login(self):
        nome_usuario = self.usuario.get()
        senha_digitada = self.senha.get()
        
        if nome_usuario == "admin" and senha_digitada == "1234":
            self.master.abrir_dashboard()
        else:
            messagebox.showerror("Erro de Acesso", "E-mail ou senha incorretos!")