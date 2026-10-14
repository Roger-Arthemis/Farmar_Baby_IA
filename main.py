import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Farmar Baby - Sistema de Gestão de Gestação")
        ctk.set_appearance_mode("Light")  # Força o tema claro para combinar com a logo branca/rosa

        # Janela redimensionável, com tamanho mínimo para o layout não quebrar
        self.geometry("750x550")
        self.minsize(750, 550)
        self.resizable(True, True)

        # Abre ocupando a tela inteira, seja qual for o monitor
        self.after(0, self.maximizar)

        # Inicia o programa direto na tela de login
        self.abrir_login()

    def maximizar(self):
        try:
            self.state("zoomed")              # Windows
        except Exception:
            self.attributes("-zoomed", True)  # Linux

    def limpar_janela(self):
        """Remove todos os componentes antigos da tela para desenhar os novos"""
        for componente in self.winfo_children():
            componente.destroy()

    def abrir_login(self):
        self.limpar_janela()
        from login import TelaLogin
        TelaLogin(self)

    def abrir_cadastro(self):
        self.limpar_janela()
        from cadastro import TelaCadastro
        TelaCadastro(self)

    def abrir_dashboard(self, usuario=None):
        self.limpar_janela()
        from dashboard import TelaDashboard
        TelaDashboard(self, usuario)

    def abrir_dashboard_profissional(self):
        self.limpar_janela()
        # Painel exclusivo do médico/profissional de saúde
        from dashboard_profissional import TelaDashboardProfissional
        TelaDashboardProfissional(self)


if __name__ == "__main__":
    app = App()
    app.mainloop()