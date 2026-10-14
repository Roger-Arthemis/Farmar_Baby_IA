import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageChops
import os

import banco


def preparar_logo(caminho, altura_desejada):
    """Corta as margens em branco da imagem e devolve (imagem, largura, altura) na proporção certa"""
    imagem = Image.open(caminho).convert("RGBA")
    fundo = Image.new("RGBA", imagem.size, (255, 255, 255, 255))
    fundo.alpha_composite(imagem)
    imagem = fundo.convert("RGB")
    diferenca = ImageChops.difference(imagem, Image.new("RGB", imagem.size, (255, 255, 255)))
    caixa = diferenca.convert("L").point(lambda p: 255 if p > 15 else 0).getbbox()
    if caixa:
        imagem = imagem.crop(caixa)
    proporcao = imagem.width / imagem.height
    return imagem, int(altura_desejada * proporcao), altura_desejada


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
            # A altura da logo acompanha a altura da tela (entre 150 e 300 pixels)
            altura_logo = min(max(int(self.master.winfo_screenheight() * 0.25), 150), 300)
            imagem, largura, altura = preparar_logo(caminho_foto, altura_logo)
            self.imagem_logo = ctk.CTkImage(light_image=imagem, dark_image=imagem, size=(largura, altura))
            self.logo_label = ctk.CTkLabel(self.conteudo_centro, image=self.imagem_logo, text="")
            self.logo_label.pack(pady=(0, 10))
        except FileNotFoundError:
            ctk.CTkLabel(self.conteudo_centro, text="[ FARMAR BABY ]", font=("Arial", 22, "bold"), text_color="#ba4b6e").pack(pady=(10, 10))

        # --- SELETOR DE PERFIL (Gestante vs Profissional) ---
        self.perfil_selecionado = ctk.StringVar(value="Gestante")

        self.seletor_perfil = ctk.CTkSegmentedButton(
            self.conteudo_centro,
            values=["Gestante", "Profissional"],
            variable=self.perfil_selecionado,
            selected_color="#ff6b8b",       # Rosa da marca para o botão ativo
            selected_hover_color="#e05372",
            font=("Arial", 13, "bold"),
            width=280,
            height=35
        )
        self.seletor_perfil.pack(pady=(10, 15))

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
        self.usuario.pack(pady=8)

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
        self.senha.pack(pady=8)

        # Apertar Enter em qualquer campo também faz o login
        self.usuario.bind("<Return>", lambda event: self.validar_login())
        self.senha.bind("<Return>", lambda event: self.validar_login())

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
        self.botao_entrar.pack(pady=(20, 15))

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
        email = self.usuario.get().strip()
        senha_digitada = self.senha.get()
        tipo_perfil = self.perfil_selecionado.get().lower()  # "gestante" ou "profissional"

        if not email or not senha_digitada:
            messagebox.showerror("Erro de Acesso", "Preencha o e-mail e a senha.")
            return

        # Acesso de TESTE (para apresentação): admin / 1234 abre o painel do perfil escolhido
        if email == "admin" and senha_digitada == "1234":
            if tipo_perfil == "gestante":
                self.master.abrir_dashboard()
            else:
                self.master.abrir_dashboard_profissional()
            return

        # Confere no banco de dados (e-mail, senha e perfil escolhido)
        usuario = banco.validar_login(email, senha_digitada, tipo_perfil)

        if usuario is None:
            messagebox.showerror("Erro de Acesso", "E-mail, senha ou perfil incorretos!")
            return

        if usuario["tipo"] == "gestante":
            self.master.abrir_dashboard(usuario)
        else:
            self.master.abrir_dashboard_profissional()