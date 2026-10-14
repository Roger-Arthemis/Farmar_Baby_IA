import tkinter as tk
import customtkinter as ctk


class TelaDashboard:
    # Respostas prontas do Assistente IA (palavra-chave -> resposta)
    RESPOSTAS = {
        "cólica": "Cólicas leves e esporádicas costumam ser normais, pelo crescimento do útero. Se forem fortes, frequentes ou vierem com sangramento, procure atendimento médico.",
        "alimento": "Evite carnes, ovos e peixes crus, leite e queijos não pasteurizados, excesso de cafeína e álcool. Lave bem frutas e verduras. Seu pré-natalista pode ajustar essa lista para você.",
        "exerc": "Caminhada leve, hidroginástica, yoga e alongamentos costumam ser bem indicados na gestação. Confirme com seu médico antes de começar qualquer atividade.",
    }
    RESPOSTA_PADRAO = "Entendi sua dúvida. Lembre-se de manter repouso adequado e consultar o seu pré-natalista para orientações clínicas personalizadas!"

    PERGUNTAS_RAPIDAS = [
        "É normal sentir cólicas?",
        "Quais alimentos devo evitar?",
        "Exercícios recomendados?",
    ]

    # Conteúdo da Caderneta (dados de exemplo; informações gerais, não substituem o pré-natalista)
    CADERNETA = [
        {
            "icone": "📅", "titulo": "Meu Pré-natal", "resumo": "Consultas, exames e vacinas",
            "secoes": [
                ("Próxima consulta", ["Dr. Roberto Silva - 22/10 às 14:00", "Clínica Central"]),
                ("Vacinas", [
                    "dTpa (difteria, tétano e coqueluche): a partir da 20ª semana",
                    "Gripe (influenza): conforme a campanha do ano",
                    "Hepatite B: se o esquema não estiver completo",
                ]),
            ],
        },
        {
            "icone": "👶", "titulo": "Desenvolvimento do Bebê", "resumo": "Acompanhe cada fase",
            "secoes": [
                ("Semana 24 (valores aproximados)", [
                    "Mede cerca de 30 cm e pesa perto de 600 g",
                    "Os pulmões continuam amadurecendo",
                    "Já percebe sons do ambiente, como a sua voz",
                    "Os movimentos ficam mais fortes e frequentes",
                ]),
            ],
        },
        {
            "icone": "🥗", "titulo": "Alimentação e Saúde", "resumo": "Dicas para uma gestação saudável",
            "secoes": [
                ("O que priorizar", [
                    "Alimentos ricos em ferro e cálcio",
                    "Hidratação constante ao longo do dia",
                    "Frutas, verduras e legumes da estação",
                ]),
                ("O que evitar", [
                    "Carnes, ovos e peixes crus ou mal passados",
                    "Leite e queijos não pasteurizados",
                    "Excesso de cafeína e qualquer bebida alcoólica",
                ]),
            ],
        },
        {
            "icone": "🩺", "titulo": "Sintomas e Cuidados", "resumo": "Saiba o que é normal",
            "secoes": [
                ("Costumam ser normais", [
                    "Azia e sensação de estômago cheio",
                    "Inchaço leve nos pés ao fim do dia",
                    "Dor nas costas e cansaço",
                ]),
                ("Procure atendimento se houver", [
                    "Sangramento ou perda de líquido",
                    "Dor de cabeça forte que não passa, ou visão turva",
                    "Inchaço repentino no rosto ou nas mãos",
                    "Febre ou dor ao urinar",
                    "Diminuição dos movimentos do bebê",
                    "Contrações regulares antes de 37 semanas",
                ]),
            ],
        },
        {
            "icone": "🧪", "titulo": "Exames e Resultados", "resumo": "Acompanhe seus exames",
            "secoes": [
                ("Resultados (exemplo)", [
                    "Hemograma: normal",
                    "Glicemia de jejum: normal",
                    "Ultrassom morfológico: normal",
                ]),
                ("Pendentes", [
                    "Teste de tolerância à glicose (entre 24 e 28 semanas)",
                ]),
            ],
        },
        {
            "icone": "🏥", "titulo": "Plano de Parto", "resumo": "Suas preferências e desejos",
            "secoes": [
                ("Preferências (a definir com a equipe)", [
                    "Local do parto: a definir",
                    "Acompanhante: a definir",
                    "Alívio da dor: a definir",
                    "Contato pele a pele logo após o nascimento",
                ]),
            ],
        },
        {
            "icone": "ℹ️", "titulo": "Informações Importantes", "resumo": "Orientações e materiais úteis",
            "secoes": [
                ("Telefones úteis", [
                    "SAMU: 192",
                    "Disque Saúde: 136",
                    "Central de Atendimento à Mulher: 180",
                ]),
                ("Seus direitos", [
                    "Direito a acompanhante durante o trabalho de parto e o parto",
                    "Licença-maternidade de 120 dias",
                ]),
            ],
        },
    ]

    # Histórico de batimentos (dados de exemplo)
    HISTORICO_DIAS = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]
    HISTORICO_BPM = [76, 79, 74, 82, 78, 80, 78]

    def __init__(self, master, usuario=None):
        self.master = master
        self.usuario = usuario # dados de quem fez login (None no acesso de teste)

        # Container principal em toda a tela branca
        self.container_geral = ctk.CTkFrame(self.master, fg_color="white", corner_radius=0)
        self.container_geral.pack(fill="both", expand=True)

        # 1. MENU LATERAL FIXO (Largura: 200px)
        self.menu_lateral = ctk.CTkFrame(
            self.container_geral,
            width=200,
            fg_color="#feebf1", # Rosa claro da identidade visual
            corner_radius=0
        )
        self.menu_lateral.pack(side="left", fill="y")
        self.menu_lateral.pack_propagate(False)

        # Título da Marca no Menu
        ctk.CTkLabel(
            self.menu_lateral,
            text="Farmar Baby",
            font=("Arial", 22, "bold"),
            text_color="#ba4b6e"
        ).pack(pady=(30, 35))

        # Botões de Navegação do Menu Lateral
        self.btn_inicio = self.criar_botao_menu("🏠 Início", "inicio")
        self.btn_caderneta = self.criar_botao_menu("📔 Caderneta Digital", "caderneta")
        self.btn_ia = self.criar_botao_menu("🤖 Assistente IA", "ia")
        self.btn_monitoramento = self.criar_botao_menu("🩺 Monitoramento", "monitoramento")

        # Botão de Sair (Retorna para a tela de Login)
        self.btn_sair = ctk.CTkButton(
            self.menu_lateral,
            text="🚪 Sair",
            font=("Arial", 13, "bold"),
            fg_color="transparent",
            text_color="#a0405e",
            hover_color="#fca1bc",
            command=self.master.abrir_login
        )
        self.btn_sair.pack(side="bottom", pady=25, padx=15, fill="x")

        # 2. PAINEL DE CONTEÚDO (Onde as telas vão mudar)
        self.painel_conteudo = ctk.CTkFrame(self.container_geral, fg_color="white", corner_radius=0)
        self.painel_conteudo.pack(side="right", fill="both", expand=True)

        # Carrega a aba padrão inicial
        self.mudar_aba("inicio")

    def criar_botao_menu(self, texto, nome_aba):
        """Cria um botão do menu lateral (todos começam não selecionados)"""
        botao = ctk.CTkButton(
            self.menu_lateral,
            text=texto,
            font=("Arial", 14, "bold"),
            fg_color="transparent",
            text_color="#ba4b6e",
            hover_color="#fcd0df",
            height=40,
            command=lambda: self.mudar_aba(nome_aba)
        )
        botao.pack(pady=8, padx=15, fill="x")
        return botao

    def limpar_painel(self):
        """Limpa o lado direito antes de desenhar a nova aba"""
        for componente in self.painel_conteudo.winfo_children():
            componente.destroy()

    def mudar_aba(self, nome_aba):
        self.limpar_painel()

        # Reseta as cores dos botões e destaca só o ativo
        botoes = {
            "inicio": self.btn_inicio,
            "caderneta": self.btn_caderneta,
            "ia": self.btn_ia,
            "monitoramento": self.btn_monitoramento,
        }
        for nome, botao in botoes.items():
            if nome == nome_aba:
                botao.configure(fg_color="#ff6b8b", text_color="white")
            else:
                botao.configure(fg_color="transparent", text_color="#ba4b6e")

        if nome_aba == "inicio":
            self.carregar_inicio()
        elif nome_aba == "caderneta":
            self.carregar_caderneta()
        elif nome_aba == "ia":
            self.carregar_assistente_ia()
        elif nome_aba == "monitoramento":
            self.carregar_monitoramento()

    def saudacao(self):
        """Mostra o primeiro nome da gestante logada (ou "Mamãe" no acesso de teste)"""
        if self.usuario:
            return f"Olá, {self.usuario['nome'].split()[0].title()}! 👋"
        return "Olá, Mamãe! 👋"

    # --- ABA 0: INÍCIO ---
    def carregar_inicio(self):
        # Saudação
        ctk.CTkLabel(
            self.painel_conteudo,
            text=self.saudacao(),
            font=("Arial", 24, "bold"),
            text_color="#ba4b6e",
            anchor="w"
        ).pack(fill="x", padx=25, pady=(25, 0))
        ctk.CTkLabel(
            self.painel_conteudo,
            text="Como você está se sentindo hoje?",
            font=("Arial", 13),
            text_color="gray",
            anchor="w"
        ).pack(fill="x", padx=25, pady=(0, 15))

        # Card de progresso da gestação
        card_progresso = ctk.CTkFrame(self.painel_conteudo, fg_color="#feebf1", corner_radius=12)
        card_progresso.pack(fill="x", padx=25, pady=(0, 15))

        ctk.CTkLabel(card_progresso, text="24 semanas e 3 dias", font=("Arial", 20, "bold"), text_color="#ba4b6e", anchor="w").pack(fill="x", padx=20, pady=(15, 0))
        ctk.CTkLabel(card_progresso, text="2º Trimestre", font=("Arial", 12), text_color="#d67493", anchor="w").pack(fill="x", padx=20)

        barra = ctk.CTkProgressBar(card_progresso, progress_color="#ff6b8b", fg_color="white", height=10)
        barra.pack(fill="x", padx=20, pady=(10, 5))
        barra.set(0.6)

        ctk.CTkLabel(card_progresso, text="Você já percorreu 60% da jornada!", font=("Arial", 11), text_color="#d67493", anchor="w").pack(fill="x", padx=20, pady=(0, 15))

        # 3 cards de resumo (próxima consulta, batimento do bebê, peso)
        linha_cards = ctk.CTkFrame(self.painel_conteudo, fg_color="transparent")
        linha_cards.pack(fill="x", padx=25, pady=(0, 15))
        for coluna in range(3):
            linha_cards.columnconfigure(coluna, weight=1)

        resumos = [
            ("📅 Próxima consulta", "22/Out", "14:00"),
            ("❤️ Batimento do bebê", "145", "bpm"),
            ("⚖️ Peso", "68,2", "kg"),
        ]
        for coluna, (titulo, valor, detalhe) in enumerate(resumos):
            card = ctk.CTkFrame(linha_cards, fg_color="#fff5f7", border_color="#fcd0df", border_width=1, corner_radius=12)
            card.grid(row=0, column=coluna, padx=5, sticky="nsew")
            ctk.CTkLabel(card, text=titulo, font=("Arial", 11, "bold"), text_color="#ba4b6e").pack(pady=(12, 2))
            ctk.CTkLabel(card, text=valor, font=("Arial", 20, "bold"), text_color="#ff6b8b").pack()
            ctk.CTkLabel(card, text=detalhe, font=("Arial", 11), text_color="gray").pack(pady=(0, 12))

        # Perguntas rápidas para o Assistente IA
        ctk.CTkLabel(
            self.painel_conteudo,
            text="Pergunte à Assistente IA",
            font=("Arial", 14, "bold"),
            text_color="#ba4b6e",
            anchor="w"
        ).pack(fill="x", padx=25, pady=(5, 5))

        area_perguntas = ctk.CTkFrame(self.painel_conteudo, fg_color="transparent")
        area_perguntas.pack(fill="x", padx=25)
        for pergunta in self.PERGUNTAS_RAPIDAS:
            ctk.CTkButton(
                area_perguntas,
                text=pergunta,
                fg_color="#feebf1",
                text_color="#ba4b6e",
                hover_color="#fcd0df",
                corner_radius=15,
                height=30,
                command=lambda p=pergunta: self.perguntar_pela_inicio(p)
            ).pack(side="left", padx=(0, 8))

    def perguntar_pela_inicio(self, pergunta):
        """Abre a aba da IA e já envia a pergunta escolhida"""
        self.mudar_aba("ia")
        self.enviar_mensagem(pergunta)

    # --- ABA 1: CADERNETA DIGITAL ---
    def carregar_caderneta(self):
        # Cabeçalho com o progresso gestacional
        topo = ctk.CTkFrame(self.painel_conteudo, fg_color="#feebf1", height=80, corner_radius=12)
        topo.pack(fill="x", padx=25, pady=(25, 15))
        topo.pack_propagate(False)

        bloco_esq = ctk.CTkFrame(topo, fg_color="transparent")
        bloco_esq.pack(side="left", padx=20)
        ctk.CTkLabel(bloco_esq, text="Minha Gestação", font=("Arial", 16, "bold"), text_color="#ba4b6e").pack(anchor="w", pady=(16, 0))
        ctk.CTkLabel(bloco_esq, text="Parto previsto: 31/01/2027", font=("Arial", 11), text_color="#d67493").pack(anchor="w")
        ctk.CTkLabel(topo, text="24 semanas e 3 dias", font=("Arial", 18, "bold"), text_color="#ff6b8b").pack(side="right", padx=20)

        # Lista dos itens da caderneta
        lista = ctk.CTkScrollableFrame(self.painel_conteudo, fg_color="transparent")
        lista.pack(fill="both", expand=True, padx=20, pady=(0, 15))

        for item in self.CADERNETA:
            linha = ctk.CTkFrame(lista, fg_color="#fff5f7", border_color="#fcd0df", border_width=1, corner_radius=10)
            linha.pack(fill="x", pady=4, padx=5)
            linha.columnconfigure(1, weight=1)

            ctk.CTkLabel(linha, text=item["icone"], font=("Arial", 22)).grid(row=0, column=0, rowspan=2, padx=(15, 10), pady=10)
            ctk.CTkLabel(linha, text=item["titulo"], font=("Arial", 14, "bold"), text_color="#ba4b6e", anchor="w").grid(row=0, column=1, sticky="w", pady=(10, 0))
            ctk.CTkLabel(linha, text=item["resumo"], font=("Arial", 11), text_color="gray", anchor="w").grid(row=1, column=1, sticky="w", pady=(0, 10))
            ctk.CTkButton(
                linha, text="Abrir ›", width=70, height=30,
                fg_color="#ff6b8b", hover_color="#e05372",
                command=lambda i=item: self.abrir_item_caderneta(i)
            ).grid(row=0, column=2, rowspan=2, padx=15)

    def abrir_item_caderneta(self, item):
        """Mostra o conteúdo de um item da caderneta, com botão para voltar à lista"""
        self.limpar_painel()

        cabecalho = ctk.CTkFrame(self.painel_conteudo, fg_color="transparent")
        cabecalho.pack(fill="x", padx=25, pady=(25, 10))
        ctk.CTkButton(
            cabecalho, text="← Voltar", width=80, height=30,
            fg_color="#feebf1", text_color="#ba4b6e", hover_color="#fcd0df",
            command=self.voltar_caderneta
        ).pack(side="left")
        ctk.CTkLabel(cabecalho, text=f'{item["icone"]} {item["titulo"]}', font=("Arial", 18, "bold"), text_color="#ba4b6e").pack(side="left", padx=15)

        conteudo = ctk.CTkScrollableFrame(self.painel_conteudo, fg_color="#f8fafc", border_color="#e2e8f0", border_width=1, corner_radius=12)
        conteudo.pack(fill="both", expand=True, padx=25, pady=(0, 10))

        for titulo_secao, linhas in item["secoes"]:
            ctk.CTkLabel(conteudo, text=titulo_secao, font=("Arial", 14, "bold"), text_color="#ba4b6e", anchor="w").pack(fill="x", padx=15, pady=(12, 4))
            for linha in linhas:
                ctk.CTkLabel(conteudo, text=f"• {linha}", font=("Arial", 12), text_color="#4a5568", anchor="w", justify="left", wraplength=380).pack(fill="x", padx=25, pady=2)

        ctk.CTkLabel(
            self.painel_conteudo,
            text="Informações gerais e de exemplo. Siga sempre a orientação do seu pré-natalista.",
            font=("Arial", 10), text_color="gray"
        ).pack(pady=(0, 12))

    def voltar_caderneta(self):
        self.limpar_painel()
        self.carregar_caderneta()

    # --- ABA 2: CHAT ASSISTENTE IA ---
    def carregar_assistente_ia(self):
        ctk.CTkLabel(self.painel_conteudo, text="Conversar com a Assistente IA", font=("Arial", 20, "bold"), text_color="#ba4b6e").pack(pady=(20, 10))

        self.caixa_chat = ctk.CTkTextbox(self.painel_conteudo, fg_color="#f8fafc", border_color="#e2e8f0", border_width=1, corner_radius=12)
        self.caixa_chat.pack(fill="both", expand=True, padx=25, pady=10)
        self.caixa_chat.insert("end", "IA Farmar Baby: Olá! Sou sua assistente de saúde virtual da Farmar Baby. Como posso te ajudar com sua gestação hoje?\n\n")
        self.caixa_chat.configure(state="disabled")

        # Botões de sugestão de perguntas
        area_sugestoes = ctk.CTkFrame(self.painel_conteudo, fg_color="transparent")
        area_sugestoes.pack(fill="x", padx=25)
        for pergunta in self.PERGUNTAS_RAPIDAS:
            ctk.CTkButton(
                area_sugestoes,
                text=pergunta,
                fg_color="#feebf1",
                text_color="#ba4b6e",
                hover_color="#fcd0df",
                corner_radius=15,
                height=28,
                command=lambda p=pergunta: self.enviar_mensagem(p)
            ).pack(side="left", padx=(0, 8))

        barra_envio = ctk.CTkFrame(self.painel_conteudo, fg_color="transparent")
        barra_envio.pack(fill="x", padx=25, pady=(10, 25))

        self.campo_texto = ctk.CTkEntry(barra_envio, placeholder_text="Digite sua dúvida sobre a gestação...", fg_color="#f8fafc", border_color="#e2e8f0")
        self.campo_texto.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.campo_texto.bind("<Return>", lambda event: self.enviar_mensagem())

        btn_enviar = ctk.CTkButton(barra_envio, text="Enviar", width=80, fg_color="#ff6b8b", hover_color="#e05372", command=self.enviar_mensagem)
        btn_enviar.pack(side="right")

    def gerar_resposta(self, mensagem):
        """Procura uma palavra-chave na mensagem e devolve a resposta pronta"""
        texto = mensagem.lower()
        for palavra_chave, resposta in self.RESPOSTAS.items():
            if palavra_chave in texto:
                return resposta
        return self.RESPOSTA_PADRAO

    def enviar_mensagem(self, texto=None):
        # Se veio de um botão de sugestão usa o texto dele, senão lê o campo
        if texto is None:
            mensagem_usuario = self.campo_texto.get().strip()
        else:
            mensagem_usuario = texto
        if not mensagem_usuario:
            return

        self.caixa_chat.configure(state="normal")
        self.caixa_chat.insert("end", f"Você: {mensagem_usuario}\n\n")
        self.caixa_chat.insert("end", f"IA Farmar Baby: {self.gerar_resposta(mensagem_usuario)}\n\n")
        self.campo_texto.delete(0, "end")
        self.caixa_chat.configure(state="disabled")
        self.caixa_chat.see("end")

    # --- ABA 3: MONITORAMENTO DE SINAIS VITAIS ---
    def criar_bloco_vital(self, pai, linha, coluna, titulo, valor, estado):
        """Cria um bloco de sinal vital (evita repetir o mesmo código 4 vezes)"""
        bloco = ctk.CTkFrame(pai, fg_color="#fff5f7", border_color="#fcd0df", border_width=1, corner_radius=12)
        bloco.grid(row=linha, column=coluna, padx=8, pady=5, sticky="nsew")
        ctk.CTkLabel(bloco, text=titulo, font=("Arial", 13, "bold"), text_color="#ba4b6e").pack(pady=(10, 2))
        ctk.CTkLabel(bloco, text=valor, font=("Arial", 22, "bold"), text_color="#ff6b8b").pack(pady=2)
        ctk.CTkLabel(bloco, text=estado, font=("Arial", 11), text_color="green").pack(pady=(0, 10))

    def carregar_monitoramento(self):
        ctk.CTkLabel(self.painel_conteudo, text="Sinais Vitais (Sincronizado com Smartwatch)", font=("Arial", 20, "bold"), text_color="#ba4b6e").pack(pady=(20, 10))
 
        # Container grid para organizar os 4 blocos (2x2)
        painel_grid = ctk.CTkFrame(self.painel_conteudo, fg_color="transparent")
        painel_grid.pack(fill="x", padx=17)
 
        self.criar_bloco_vital(painel_grid, 0, 0, "❤️ Batimentos", "78 BPM", "Estado: Normal")
        self.criar_bloco_vital(painel_grid, 0, 1, "🩺 Pressão Arterial", "110/70 mmHg", "Estado: Normal")
        self.criar_bloco_vital(painel_grid, 1, 0, "💧 Oxigênio (SpO₂)", "98%", "Estado: Normal")
        self.criar_bloco_vital(painel_grid, 1, 1, "🌡️ Temperatura", "36,6 °C", "Estado: Normal")
 
        painel_grid.columnconfigure(0, weight=1)
        painel_grid.columnconfigure(1, weight=1)
 
        # --- HISTÓRICO (gráfico de linha dos batimentos) ---
        card_grafico = ctk.CTkFrame(self.painel_conteudo, fg_color="#fff5f7", border_color="#fcd0df", border_width=1, corner_radius=12)
        card_grafico.pack(fill="both", expand=True, padx=25, pady=(8, 20))
 
        ctk.CTkLabel(
            card_grafico,
            text="📈 Histórico de batimentos (últimos 7 dias)",
            font=("Arial", 13, "bold"),
            text_color="#ba4b6e",
            anchor="w"
        ).pack(fill="x", padx=15, pady=(10, 0))
 
        canvas = tk.Canvas(card_grafico, bg="#fff5f7", highlightthickness=0, height=120)
        canvas.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        # Redesenha sempre que o tamanho do canvas mudar (inclui o primeiro desenho)
        canvas.bind("<Configure>", lambda event: self.desenhar_grafico(canvas, self.HISTORICO_DIAS, self.HISTORICO_BPM))
 
    def desenhar_grafico(self, canvas, dias, valores):
        """Desenha um gráfico de linha simples direto no Canvas (sem bibliotecas extras)"""
        canvas.delete("all")
        largura = canvas.winfo_width()
        altura = canvas.winfo_height()
        if largura < 100 or altura < 60:
            return
 
        margem_esq, margem_dir, margem_topo, margem_base = 38, 22, 18, 24
        area_larg = largura - margem_esq - margem_dir
        area_alt = altura - margem_topo - margem_base
 
        minimo = min(valores) - 5
        maximo = max(valores) + 5
 
        # Linhas de grade horizontais com os valores à esquerda
        for i in range(4):
            y = margem_topo + area_alt * i / 3
            valor = maximo - (maximo - minimo) * i / 3
            canvas.create_line(margem_esq, y, largura - margem_dir, y, fill="#fcd0df")
            canvas.create_text(margem_esq - 6, y, text=f"{valor:.0f}", anchor="e", fill="gray", font=("Arial", 9))
 
        # Calcula a posição de cada ponto e escreve o dia embaixo
        pontos = []
        total = len(valores)
        for i, (dia, valor) in enumerate(zip(dias, valores)):
            x = margem_esq + area_larg * i / (total - 1)
            y = margem_topo + area_alt * (maximo - valor) / (maximo - minimo)
            pontos.append((x, y))
            canvas.create_text(x, altura - margem_base / 2, text=dia, fill="gray", font=("Arial", 9))
 
        # Linha e bolinhas
        coordenadas = [c for ponto in pontos for c in ponto]
        canvas.create_line(*coordenadas, fill="#ff6b8b", width=3, smooth=True)
        for x, y in pontos:
            canvas.create_oval(x - 4, y - 4, x + 4, y + 4, fill="#ff6b8b", outline="white", width=2)
 
        # Destaca o último valor
        ultimo_x, ultimo_y = pontos[-1]
        canvas.create_text(ultimo_x, ultimo_y - 12, text=str(valores[-1]), fill="#ba4b6e", font=("Arial", 10, "bold"))
 