import customtkinter as ctk

# Tema Escuro como padrão 
ctk.set_appearance_mode("Dark") #Dark, System ou Light
# Tema
ctk.set_default_color_theme("blue") #blue, green, dark-blue

# Criando uma classe para ser janela
class Aplicativo(ctk.CTk):
    # Funão initi para rodar a super classe
    def __init__(self):
    # Super para garantir que tudo vai ser executado na classe original
        super().__init__()
    # Após executar tudo para criar o aplicativo, vai rodar o resto
        # self é um jeito de chamar o aplicativo
        self.title("Sistema de Estoque")

        # Tamanho da tela
        self.geometry("900x600")
        
        # Criar divisão de tela
        # Coluna (weight 1 expande com tela - 0 zero para não expandir)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Parte lateral
        self.barra_lateral = ctk.CTkFrame(self, width=200)
        self.barra_lateral.grid(row=0, column=0, sticky="nsw")

        # Parte principal
        self.principal_abas = ctk.CTkTabview(self, width=400)
        self.principal_abas.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.principal_abas.add("Perfil")
        self.principal_abas.add("Preferências")
        self.principal_abas.add("Itens")

        # Preencher as partes/abas
        # Preencher aba lateral
        self.construir_abaLateral()

        # Preencher aba do perfil
        self.construir_abaPerfil()

        # Preencher aba preferências
        self.construir_abaPreferencias()

        # Preencher aba sistema 
        self.construir_abaSistema()

        self.construir_tela()

    # Para construir tela
    def construir_tela(self):
        pass

    # Construindo barra lateral
    def construir_abaLateral(self):
        self.title_side = ctk.CTkLabel(self.barra_lateral, text="Meu App", font=ctk.CTkFont(size=24, weight="bold"))
        self.title_side.pack(pady=(10, 30), padx=(20, 20))
        
        self.button_itens = ctk.CTkButton(self.barra_lateral, text="Itens")
        self.button_itens.pack(pady=(30, 30), padx=(10,10))

        self.switch_modeDark = ctk.CTkSwitch(self.barra_lateral, text="Modo Escuro")
        self.switch_modeDark.pack(pady=(10, 10), side="bottom" )

    def construir_abaPerfil(self):
        self.aba_perfil = self.principal_abas.tab("Perfil")
        # Campo de nome
        self.name_field = ctk.CTkEntry(self.aba_perfil, placeholder_text="Digite seu nome", width=300)
        self.name_field.pack(pady=(20, 20))

        # radio button do nivel de usuario
        self.nivel_user = ctk.IntVar(value=0)
        
        self.radio_title = ctk.CTkLabel("Nivel de Usuário")
        self.radio_title.pack(pady=(20,20))
        #self.radio_basic = ctk.CTkRadioButton()
        #self.radio_admin = ctk.CTkRadioButton()
        # chackbox de notificacao
        # botao salvar perfil
        pass

    def construir_abaPreferencias(self):
        pass

    def construir_abaSistema(self):
        pass

window = Aplicativo()
window.mainloop()

