import customtkinter as ctk


class TelaDashboardProfissional:
    # Paleta profissional (azul/cinza). O rosa fica só para a gestante.
    COR_MENU = "#1a365d"
    COR_MENU_HOVER = "#2c5282"
    COR_ATIVO = "#2b6cb0"
    COR_TEXTO_MENU = "#cbd5e0"
    COR_FUNDO = "#f7fafc"
    COR_CARD = "white"
    COR_BORDA = "#e2e8f0"
    COR_TITULO = "#1a365d"
    COR_TEXTO = "#4a5568"
    COR_ALERTA = "#c53030"
    COR_ALERTA_FUNDO = "#fff5f5"
    COR_OK = "#2f855a"
    COR_OK_FUNDO = "#f0fff4"

    # Limites de exemplo para gerar os alertas (podem ser ajustados)
    LIMITE_PA_SISTOLICA = 140
    LIMITE_PA_DIASTOLICA = 90
    LIMITE_BPM = 100
    LIMITE_SPO2 = 95
    LIMITE_FEBRE = 37.8

    # Dados de exemplo (depois podem vir de um banco de dados)
    # pa_sis/pa_dia = pressão arterial, bpm = batimentos, spo2 = oxigênio (%), temp = temperatura (°C)
    PACIENTES = [
        {"nome": "Ana Souza", "semanas": 24, "consulta": "22/10 14:00", "bpm": 78, "pa_sis": 110, "pa_dia": 70, "spo2": 98, "temp": 36.6},
        {"nome": "Beatriz Lima", "semanas": 32, "consulta": "Hoje 09:30", "bpm": 84, "pa_sis": 145, "pa_dia": 95, "spo2": 97, "temp": 36.8},
        {"nome": "Carla Mendes", "semanas": 12, "consulta": "24/10 11:00", "bpm": 72, "pa_sis": 105, "pa_dia": 65, "spo2": 99, "temp": 36.5},
        {"nome": "Daniela Rocha", "semanas": 36, "consulta": "Hoje 14:00", "bpm": 118, "pa_sis": 120, "pa_dia": 80, "spo2": 96, "temp": 36.9},
        {"nome": "Elisa Ferreira", "semanas": 28, "consulta": "Hoje 16:30", "bpm": 80, "pa_sis": 115, "pa_dia": 75, "spo2": 98, "temp": 36.7},
        {"nome": "Fernanda Alves", "semanas": 20, "consulta": "27/10 08:00", "bpm": 76, "pa_sis": 108, "pa_dia": 68, "spo2": 98, "temp": 36.6},
    ]

    def avaliar_paciente(self, paciente):
        """Compara os sinais vitais com os limites e devolve a lista de motivos de alerta"""
        motivos = []
        if paciente["pa_sis"] >= self.LIMITE_PA_SISTOLICA or paciente["pa_dia"] >= self.LIMITE_PA_DIASTOLICA:
            motivos.append(f'Pressão arterial elevada: {paciente["pa_sis"]}/{paciente["pa_dia"]} mmHg')
        if paciente["bpm"] > self.LIMITE_BPM:
            motivos.append(f'Frequência cardíaca alta: {paciente["bpm"]} bpm')
        if paciente["spo2"] < self.LIMITE_SPO2:
            motivos.append(f'Oxigenação baixa: {paciente["spo2"]}%')
        if paciente["temp"] >= self.LIMITE_FEBRE:
            motivos.append(f'Febre: {str(paciente["temp"]).replace(".", ",")} °C')
        return motivos

    def preparar_pacientes(self):
        """Define o status (Normal/Alerta) e o motivo de cada paciente automaticamente"""
        for paciente in self.PACIENTES:
            motivos = self.avaliar_paciente(paciente)
            paciente["status"] = "Alerta" if motivos else "Normal"
            paciente["motivo"] = "; ".join(motivos)

    def __init__(self, master):
        self.master = master
        self.preparar_pacientes()

        # Container principal
        self.container_geral = ctk.CTkFrame(self.master, fg_color=self.COR_FUNDO, corner_radius=0)
        self.container_geral.pack(fill="both", expand=True)

        # 1. MENU LATERAL
        self.menu_lateral = ctk.CTkFrame(self.container_geral, width=200, fg_color=self.COR_MENU, corner_radius=0)
        self.menu_lateral.pack(side="left", fill="y")
        self.menu_lateral.pack_propagate(False)

        ctk.CTkLabel(
            self.menu_lateral,
            text="Farmar Baby",
            font=("Arial", 22, "bold"),
            text_color="white"
        ).pack(pady=(30, 0))
        ctk.CTkLabel(
            self.menu_lateral,
            text="Painel Profissional",
            font=("Arial", 12),
            text_color=self.COR_TEXTO_MENU
        ).pack(pady=(0, 30))

        self.btn_pacientes = self.criar_botao_menu("👥 Pacientes", "pacientes")
        self.btn_alertas = self.criar_botao_menu("⚠️ Alertas", "alertas")
        self.btn_agenda = self.criar_botao_menu("📅 Agenda do Dia", "agenda")

        self.btn_sair = ctk.CTkButton(
            self.menu_lateral,
            text="🚪 Sair",
            font=("Arial", 13, "bold"),
            fg_color="transparent",
            text_color=self.COR_TEXTO_MENU,
            hover_color=self.COR_MENU_HOVER,
            command=self.master.abrir_login
        )
        self.btn_sair.pack(side="bottom", pady=25, padx=15, fill="x")

        # 2. PAINEL DE CONTEÚDO
        self.painel_conteudo = ctk.CTkFrame(self.container_geral, fg_color=self.COR_FUNDO, corner_radius=0)
        self.painel_conteudo.pack(side="right", fill="both", expand=True)

        self.mudar_aba("pacientes")

    # --- NAVEGAÇÃO ---
    def criar_botao_menu(self, texto, nome_aba):
        botao = ctk.CTkButton(
            self.menu_lateral,
            text=texto,
            font=("Arial", 14, "bold"),
            anchor="w",
            fg_color="transparent",
            text_color=self.COR_TEXTO_MENU,
            hover_color=self.COR_MENU_HOVER,
            height=40,
            command=lambda: self.mudar_aba(nome_aba)
        )
        botao.pack(pady=6, padx=15, fill="x")
        return botao

    def limpar_painel(self):
        for componente in self.painel_conteudo.winfo_children():
            componente.destroy()

    def mudar_aba(self, nome_aba):
        self.limpar_painel()

        botoes = {
            "pacientes": self.btn_pacientes,
            "alertas": self.btn_alertas,
            "agenda": self.btn_agenda,
        }
        for nome, botao in botoes.items():
            if nome == nome_aba:
                botao.configure(fg_color=self.COR_ATIVO, text_color="white")
            else:
                botao.configure(fg_color="transparent", text_color=self.COR_TEXTO_MENU)

        if nome_aba == "pacientes":
            self.carregar_pacientes()
        elif nome_aba == "alertas":
            self.carregar_alertas()
        elif nome_aba == "agenda":
            self.carregar_agenda()

    # --- COMPONENTES REUTILIZÁVEIS ---
    def titulo_aba(self, titulo, subtitulo):
        ctk.CTkLabel(
            self.painel_conteudo, text=titulo,
            font=("Arial", 22, "bold"), text_color=self.COR_TITULO, anchor="w"
        ).pack(fill="x", padx=25, pady=(25, 0))
        ctk.CTkLabel(
            self.painel_conteudo, text=subtitulo,
            font=("Arial", 12), text_color=self.COR_TEXTO, anchor="w"
        ).pack(fill="x", padx=25, pady=(0, 15))

    def criar_card(self, pai):
        return ctk.CTkFrame(pai, fg_color=self.COR_CARD, border_color=self.COR_BORDA, border_width=1, corner_radius=10)

    def criar_selo_status(self, pai, status):
        """Selo colorido: vermelho para Alerta, verde para Normal"""
        if status == "Alerta":
            fundo, texto = self.COR_ALERTA_FUNDO, self.COR_ALERTA
        else:
            fundo, texto = self.COR_OK_FUNDO, self.COR_OK
        return ctk.CTkLabel(
            pai, text=status, width=70, height=24, corner_radius=12,
            fg_color=fundo, text_color=texto, font=("Arial", 11, "bold")
        )

    # --- ABA 1: PACIENTES ---
    def carregar_pacientes(self):
        self.titulo_aba("Pacientes", "Acompanhamento das gestantes sob seu cuidado")

        # Resumo em 3 contadores
        total = len(self.PACIENTES)
        em_alerta = len([p for p in self.PACIENTES if p["status"] == "Alerta"])
        hoje = len([p for p in self.PACIENTES if p["consulta"].startswith("Hoje")])

        linha_resumo = ctk.CTkFrame(self.painel_conteudo, fg_color="transparent")
        linha_resumo.pack(fill="x", padx=20, pady=(0, 10))
        for coluna in range(3):
            linha_resumo.columnconfigure(coluna, weight=1)

        resumos = [
            ("Total de pacientes", total, self.COR_TITULO),
            ("Em alerta", em_alerta, self.COR_ALERTA),
            ("Consultas hoje", hoje, self.COR_ATIVO),
        ]
        for coluna, (rotulo, valor, cor) in enumerate(resumos):
            card = self.criar_card(linha_resumo)
            card.grid(row=0, column=coluna, padx=5, sticky="nsew")
            ctk.CTkLabel(card, text=str(valor), font=("Arial", 26, "bold"), text_color=cor).pack(pady=(10, 0))
            ctk.CTkLabel(card, text=rotulo, font=("Arial", 11), text_color=self.COR_TEXTO).pack(pady=(0, 10))

        # Busca por nome
        self.entrada_busca = ctk.CTkEntry(
            self.painel_conteudo,
            placeholder_text="🔍 Buscar paciente pelo nome...",
            fg_color="white", border_color=self.COR_BORDA, height=36
        )
        self.entrada_busca.pack(fill="x", padx=25, pady=(5, 10))
        self.entrada_busca.bind("<KeyRelease>", lambda event: self.desenhar_lista_pacientes())

        # Lista com rolagem
        self.lista_pacientes = ctk.CTkScrollableFrame(self.painel_conteudo, fg_color="transparent")
        self.lista_pacientes.pack(fill="both", expand=True, padx=20, pady=(0, 15))

        self.desenhar_lista_pacientes()

    def desenhar_lista_pacientes(self):
        for componente in self.lista_pacientes.winfo_children():
            componente.destroy()

        filtro = self.entrada_busca.get().strip().lower()
        encontrados = [p for p in self.PACIENTES if filtro in p["nome"].lower()]

        if not encontrados:
            ctk.CTkLabel(self.lista_pacientes, text="Nenhuma paciente encontrada.", text_color=self.COR_TEXTO).pack(pady=20)
            return

        for paciente in encontrados:
            linha = self.criar_card(self.lista_pacientes)
            linha.pack(fill="x", pady=4)
            linha.columnconfigure(0, weight=1)

            ctk.CTkLabel(linha, text=paciente["nome"], font=("Arial", 13, "bold"), text_color=self.COR_TITULO, anchor="w").grid(row=0, column=0, sticky="w", padx=15, pady=(10, 0))
            ctk.CTkLabel(linha, text=f'{paciente["semanas"]} semanas • Consulta: {paciente["consulta"]}', font=("Arial", 11), text_color=self.COR_TEXTO, anchor="w").grid(row=1, column=0, sticky="w", padx=15, pady=(0, 10))
            self.criar_selo_status(linha, paciente["status"]).grid(row=0, column=1, rowspan=2, padx=15)

    # --- ABA 2: ALERTAS ---
    def carregar_alertas(self):
        self.titulo_aba("Alertas", "Pacientes com sinais vitais fora do normal")

        alertas = [p for p in self.PACIENTES if p["status"] == "Alerta"]

        lista = ctk.CTkScrollableFrame(self.painel_conteudo, fg_color="transparent")
        lista.pack(fill="both", expand=True, padx=20, pady=(0, 15))

        if not alertas:
            ctk.CTkLabel(lista, text="Nenhum alerta no momento. ✅", text_color=self.COR_OK, font=("Arial", 14)).pack(pady=30)
            return

        for paciente in alertas:
            card = ctk.CTkFrame(lista, fg_color=self.COR_ALERTA_FUNDO, border_color=self.COR_ALERTA, border_width=1, corner_radius=10)
            card.pack(fill="x", pady=5)
            ctk.CTkLabel(card, text=f'⚠️ {paciente["nome"]} ({paciente["semanas"]} semanas)', font=("Arial", 14, "bold"), text_color=self.COR_ALERTA, anchor="w").pack(fill="x", padx=15, pady=(12, 2))
            ctk.CTkLabel(card, text=paciente["motivo"], font=("Arial", 12), text_color=self.COR_TEXTO, anchor="w").pack(fill="x", padx=15)
            ctk.CTkLabel(card, text=f'Próxima consulta: {paciente["consulta"]}', font=("Arial", 11), text_color=self.COR_TEXTO, anchor="w").pack(fill="x", padx=15, pady=(2, 12))

    # --- ABA 3: AGENDA DO DIA ---
    def carregar_agenda(self):
        self.titulo_aba("Agenda do Dia", "Consultas marcadas para hoje")

        consultas = [p for p in self.PACIENTES if p["consulta"].startswith("Hoje")]
        consultas.sort(key=lambda p: p["consulta"])

        lista = ctk.CTkScrollableFrame(self.painel_conteudo, fg_color="transparent")
        lista.pack(fill="both", expand=True, padx=20, pady=(0, 15))

        if not consultas:
            ctk.CTkLabel(lista, text="Nenhuma consulta para hoje.", text_color=self.COR_TEXTO).pack(pady=30)
            return

        for paciente in consultas:
            hora = paciente["consulta"].replace("Hoje ", "")
            card = self.criar_card(lista)
            card.pack(fill="x", pady=5)
            card.columnconfigure(1, weight=1)

            ctk.CTkLabel(card, text=hora, font=("Arial", 20, "bold"), text_color=self.COR_ATIVO, width=80).grid(row=0, column=0, rowspan=2, padx=(15, 10), pady=12)
            ctk.CTkLabel(card, text=paciente["nome"], font=("Arial", 14, "bold"), text_color=self.COR_TITULO, anchor="w").grid(row=0, column=1, sticky="w", pady=(12, 0))
            ctk.CTkLabel(card, text=f'{paciente["semanas"]} semanas • Pré-natal', font=("Arial", 11), text_color=self.COR_TEXTO, anchor="w").grid(row=1, column=1, sticky="w", pady=(0, 12))
            self.criar_selo_status(card, paciente["status"]).grid(row=0, column=2, rowspan=2, padx=15)