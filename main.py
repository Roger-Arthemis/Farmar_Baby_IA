import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações básicas da janela principal do computador
        self.title("Farmar Baby - Sistema de Gestão de Gestação")
        self.geometry("750x550")
        self.resizable(False, False) # Mantém o tamanho fixo para o layout não quebrar
        ctk.set_appearance_mode("Light") # Força o tema claro para combinar com a logo branca/rosa
        
        # Inicia o programa direto na tela de login (que vamos criar a seguir)
        self.abrir_login()

    def limpar_janela(self):
        """Remove todos os componentes antigos da tela para desenhar os novos"""
        for componente in self.winfo_children():
            componente.destroy()

    def abrir_login(self):
        self.limpar_janela()
        # Aqui vamos chamar a tela de login dividida em 2 colunas
        from login import TelaLogin
        TelaLogin(self)

    def abrir_cadastro(self):
        self.limpar_janela()
        # Aqui vamos chamar a tela de cadastro em duas colunas
        from cadastro import TelaCadastro
        TelaCadastro(self)

    def abrir_dashboard(self):
        self.limpar_janela()
        # Aqui vamos chamar o menu com a barra lateral e os painéis (IA, Caderneta, etc)
        from dashboard import TelaDashboard
        TelaDashboard(self)

if __name__ == "__main__":
    app = App()
    app.mainloop()