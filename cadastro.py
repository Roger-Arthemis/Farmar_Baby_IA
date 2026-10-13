import customtkinter as ctk

class TelaCadastro:
    def __init__(self, master):
        self.master = master
        
        # 1. PAINEL DA ESQUERDA (Identidade Visual)
        self.painel_esquerdo = ctk.CTkFrame(
            self.master,
            width=250, # Um pouco mais estreito que o login para dar mais espaço ao formulário
            height=550,
            fg_color="#feebf1",
            corner_radius=0
        )
        self.painel_esquerdo.place(x=0, y=0)
        
        ctk.CTkLabel(
            self.painel_esquerdo,
            text="Criar Conta",
            font=("Arial", 26, "bold"),
            text_color="#ba4b6e"
        ).pack(pady=(220, 10))
        
        ctk.CTkLabel(
            self.painel_esquerdo,
            text="Preencha seus dados para\ncomeçar o acompanhamento.",
            font=("Arial", 13),
            text_color="#d67493"
        ).pack()

        # 2. PAINEL DA DIREITA (Formulário Lado a Lado)
        self.painel_direito = ctk.CTkFrame(
            self.master,
            width=500,
            height=550,
            fg_color="white",
            corner_radius=0
        )
        self.painel_direito.place(x=250, y=0)
        
        # Título interno do formulário
        ctk.CTkLabel(
            self.painel_direito,
            text="Dados Cadastrais",
            font=("Arial", 22, "bold"),
            text_color="#ba4b6e"
        ).pack(pady=(40, 30))
        
        # --- CONTAINER PARA OS CAMPOS EM DUAS COLUNAS ---
        # Usamos um frame invisível com grid para organizar lado a lado
        container_campos = ctk.CTkFrame(self.painel_direito, fg_color="transparent")
        container_campos.pack(padx=30, pady=10)
        
        # Linha 1: Nome e E-mail
        self.nome = ctk.CTkEntry(container_campos, width=210, height=40, placeholder_text="Nome Completo", fg_color="#f7fafc", border_color="#e2e8f0")
        self.nome.grid(row=0, column=0, padx=10, pady=12)
        
        self.email = ctk.CTkEntry(container_campos, width=210, height=40, placeholder_text="E-mail", fg_color="#f7fafc", border_color="#e2e8f0")
        self.email.grid(row=0, column=1, padx=10, pady=12)
        
        # Linha 2: Telefone e Data de Nascimento
        self.telefone = ctk.CTkEntry(container_campos, width=210, height=40, placeholder_text="Telefone (DDD)", fg_color="#f7fafc", border_color="#e2e8f0")
        self.telefone.grid(row=1, column=0, padx=10, pady=12)
        
        self.data_nasc = ctk.CTkEntry(container_campos, width=210, height=40, placeholder_text="Data de Nascimento", fg_color="#f7fafc", border_color="#e2e8f0")
        self.data_nasc.grid(row=1, column=1, padx=10, pady=12)
        
        # Linha 3: Senha e Confirmar Senha
        self.senha = ctk.CTkEntry(container_campos, width=210, height=40, placeholder_text="Senha", show="*", fg_color="#f7fafc", border_color="#e2e8f0")
        self.senha.grid(row=2, column=0, padx=10, pady=12)
        
        self.conf_senha = ctk.CTkEntry(container_campos, width=210, height=40, placeholder_text="Confirmar Senha", show="*", fg_color="#f7fafc", border_color="#e2e8f0")
        self.conf_senha.grid(row=2, column=1, padx=10, pady=12)
        
        # --- TERMOS DE USO (Checkbox) ---
        self.termos = ctk.CTkCheckBox(
            self.painel_direito,
            text="Li e aceito os Termos de Uso e Política de Privacidade",
            font=("Arial", 11),
            text_color="gray",
            fg_color="#ff6b8b",
            hover_color="#e05372"
        )
        self.termos.pack(pady=20)
        
        # --- BOTÃO CADASTRAR ---
        self.botao_cadastrar = ctk.CTkButton(
            self.painel_direito,
            width=440, # Ocupa a largura esticada das duas colunas
            height=45,
            text="Cadastrar",
            font=("Arial", 16, "bold"),
            fg_color="#ff6b8b",
            hover_color="#e05372",
            command=self.executar_cadastro
        )
        self.botao_cadastrar.pack(pady=10)
        
        # --- LINK PARA VOLTAR AO LOGIN ---
        self.link_login = ctk.CTkButton(
            self.painel_direito,
            text="Já tem uma conta? Entrar",
            font=("Arial", 12),
            fg_color="transparent",
            text_color="#ba4b6e",
            hover_color="#feebf1",
            command=self.master.abrir_login
        )
        self.link_login.pack(pady=5)

    def ejecutar_cadastro(self):
        # Por enquanto, apenas simula o cadastro e joga para o Dashboard
        self.master.abrir_dashboard()