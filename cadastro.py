import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime

import banco


class TelaCadastro:
    def __init__(self, master):
        self.master = master

        # Container principal ocupando toda a tela branca
        self.painel_principal = ctk.CTkFrame(
            self.master,
            fg_color="white",
            corner_radius=0
        )
        self.painel_principal.pack(fill="both", expand=True)

        # Sub-container centralizado para os elementos
        self.conteudo_centro = ctk.CTkFrame(
            self.painel_principal,
            fg_color="white"
        )
        self.conteudo_centro.pack(expand=True)

        # Título interno do formulário
        ctk.CTkLabel(
            self.conteudo_centro,
            text="Dados Cadastrais",
            font=("Arial", 26, "bold"),
            text_color="#ba4b6e"
        ).pack(pady=(20, 20))

        # --- CONTAINER PARA OS CAMPOS EM DUAS COLUNAS ---
        container_campos = ctk.CTkFrame(self.conteudo_centro, fg_color="transparent")
        container_campos.pack(padx=10, pady=5)

        # Linha 1: Nome e E-mail
        self.nome = ctk.CTkEntry(container_campos, width=220, height=42, placeholder_text="Nome Completo", fg_color="#f8fafc", border_color="#e2e8f0", border_width=1)
        self.nome.grid(row=0, column=0, padx=12, pady=10)

        self.email = ctk.CTkEntry(container_campos, width=220, height=42, placeholder_text="E-mail", fg_color="#f8fafc", border_color="#e2e8f0", border_width=1)
        self.email.grid(row=0, column=1, padx=12, pady=10)

        # Linha 2: Telefone e Data de Nascimento
        self.telefone = ctk.CTkEntry(container_campos, width=220, height=42, placeholder_text="Telefone (DDD)", fg_color="#f8fafc", border_color="#e2e8f0", border_width=1)
        self.telefone.grid(row=1, column=0, padx=12, pady=10)

        self.data_nasc = ctk.CTkEntry(container_campos, width=220, height=42, placeholder_text="Data de Nascimento (DD/MM/AAAA)", fg_color="#f8fafc", border_color="#e2e8f0", border_width=1)
        self.data_nasc.grid(row=1, column=1, padx=12, pady=10)

        # Vincula a função de máscara automática ao campo de data
        self.data_nasc.bind("<KeyRelease>", self.formatar_data)

        # Linha 3: Senha e Confirmar Senha
        self.senha = ctk.CTkEntry(container_campos, width=220, height=42, placeholder_text="Senha (mín. 6 caracteres)", show="*", fg_color="#f8fafc", border_color="#e2e8f0", border_width=1)
        self.senha.grid(row=2, column=0, padx=12, pady=10)

        self.conf_senha = ctk.CTkEntry(container_campos, width=220, height=42, placeholder_text="Confirmar Senha", show="*", fg_color="#f8fafc", border_color="#e2e8f0", border_width=1)
        self.conf_senha.grid(row=2, column=1, padx=12, pady=10)

        # --- TERMOS DE USO (Checkbox) ---
        self.termos = ctk.CTkCheckBox(
            self.conteudo_centro,
            text="Li e aceito os Termos de Uso e Política de Privacidade",
            font=("Arial", 12),
            text_color="gray",
            fg_color="#ff6b8b",
            hover_color="#e05372"
        )
        self.termos.pack(pady=20)

        # --- BOTÃO CADASTRAR ---
        self.botao_cadastrar = ctk.CTkButton(
            self.conteudo_centro,
            width=464, # Ajustado para bater certinho com a largura total das colunas
            height=45,
            text="Cadastrar",
            font=("Arial", 16, "bold"),
            fg_color="#ff6b8b",
            hover_color="#e05372",
            corner_radius=8,
            command=self.executar_cadastro
        )
        self.botao_cadastrar.pack(pady=10)

        # --- LINK PARA VOLTAR AO LOGIN ---
        self.link_login = ctk.CTkButton(
            self.conteudo_centro,
            text="Já tem uma conta? Entrar",
            font=("Arial", 12, "underline"),
            fg_color="transparent",
            text_color="#ba4b6e",
            hover_color="#feebf1",
            command=self.master.abrir_login
        )
        self.link_login.pack(pady=5)

    def formatar_data(self, event):
        """Adiciona automaticamente as barras na data enquanto digita e limita o tamanho"""
        # Ignora teclas de controle como Backspace ou Setas para não atrapalhar o usuário apagando
        if event.keysym in ("Backspace", "Delete", "Left", "Right"):
            return

        texto = self.data_nasc.get()
        # Remove qualquer caractere que não seja número
        texto_limpo = "".join([c for c in texto if c.isdigit()])

        texto_formatado = ""

        # Reconstrói a string inserindo as barras de forma automática
        if len(texto_limpo) > 0:
            texto_formatado += texto_limpo[:2]
        if len(texto_limpo) > 2:
            texto_formatado += "/" + texto_limpo[2:4]
        if len(texto_limpo) > 4:
            texto_formatado += "/" + texto_limpo[4:8] # Limita o ano em até 4 dígitos

        # Atualiza o campo com o texto formatado
        self.data_nasc.delete(0, "end")
        self.data_nasc.insert(0, texto_formatado)

    def validar_campos(self, nome, email, telefone, data_nasc, senha, conf_senha):
        """Retorna uma mensagem de erro, ou None se estiver tudo certo"""
        if not all([nome, email, telefone, data_nasc, senha, conf_senha]):
            return "Preencha todos os campos."

        if len(nome.split()) < 2:
            return "Digite o nome completo (nome e sobrenome)."

        if "@" not in email or "." not in email.split("@")[-1]:
            return "Digite um e-mail válido."

        digitos_telefone = "".join(c for c in telefone if c.isdigit())
        if len(digitos_telefone) not in (10, 11):
            return "Digite o telefone com DDD (10 ou 11 números)."

        try:
            nascimento = datetime.strptime(data_nasc, "%d/%m/%Y")
        except ValueError:
            return "Data de nascimento inválida. Use o formato DD/MM/AAAA."
        if nascimento > datetime.now():
            return "A data de nascimento não pode estar no futuro."

        if len(senha) < 6:
            return "A senha precisa ter pelo menos 6 caracteres."

        if senha != conf_senha:
            return "As senhas não coincidem."

        if not self.termos.get():
            return "Você precisa aceitar os Termos de Uso para continuar."

        return None

    def executar_cadastro(self):
        nome = self.nome.get().strip()
        email = self.email.get().strip()
        telefone = self.telefone.get().strip()
        data_nasc = self.data_nasc.get().strip()
        senha = self.senha.get()
        conf_senha = self.conf_senha.get()

        erro = self.validar_campos(nome, email, telefone, data_nasc, senha, conf_senha)
        if erro:
            messagebox.showerror("Erro no cadastro", erro)
            return

        sucesso, mensagem = banco.cadastrar_usuario(nome, email, telefone, data_nasc, senha)
        if sucesso:
            messagebox.showinfo("Cadastro", mensagem + "\nAgora faça o login.")
            self.master.abrir_login()
        else:
            messagebox.showerror("Erro no cadastro", mensagem)