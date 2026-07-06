import customtkinter as ctk
import time

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

        self.subtitle = ctk.CTkLabel(self.barra_lateral, text="", font=ctk.CTkFont(size=12, weight="bold"))
        self.subtitle.pack(pady=(0, 5))
        
        self.button_itens = ctk.CTkButton(self.barra_lateral, text="Itens", command=self.itens)
        self.button_itens.pack(pady=(30, 30), padx=(10,10))

        self.switch_modeDark = ctk.CTkSwitch(self.barra_lateral, text="Modo Escuro", command=self.mode_white)
        self.switch_modeDark.pack(pady=(10, 10), side="bottom" )
        self.switch_modeDark.select()

    def construir_abaPerfil(self):
        # Criando abas
        self.aba_perfil = self.principal_abas.tab("Perfil")
        # Campo de nome
        self.name_field = ctk.CTkEntry(self.aba_perfil, placeholder_text="Digite seu nome", width=300)
        self.name_field.pack(pady=(10, 10))

        # radio button do nivel de usuario
        self.nivel_user = ctk.IntVar(value=0)
        
        self.radio_title = ctk.CTkLabel(self.aba_perfil, text="Nivel de Usuário")
        self.radio_title.pack(pady=(10,10))
        
        self.radio_basic = ctk.CTkRadioButton(self.aba_perfil, text="Básico", variable=self.nivel_user, value=1)
        self.radio_basic.pack(pady=(5,5))
        self.radio_admin = ctk.CTkRadioButton(self.aba_perfil, text='Admin', variable=self.nivel_user, value=2)
        self.radio_admin.pack(pady=(5,5))

        # chackbox de notificacao
        self.checkbox_notify = ctk.CTkCheckBox(self.aba_perfil, text="Receber Notificações por e-mail")
        self.checkbox_notify.pack(pady=(10,10))

        # botao salvar perfil
        self.button_profile = ctk.CTkButton(self.aba_perfil, text="Salvar Perfil", fg_color="purple", hover_color="green", command=self.save_profile)
        self.button_profile.pack(pady=(20,20))

    def construir_abaPreferencias(self):
        self.aba_preferencias = self.principal_abas.tab("Preferências")

        # Lebal
        self.lebal_linguage = ctk.CTkLabel(self.aba_preferencias, text="Selecione o idioma")
        self.lebal_linguage.pack(pady=(10,5))
        
        # Menu de idiomas
        self.menu_linguage = ctk.CTkOptionMenu(self.aba_preferencias, values=["Português", "English", "Espanhol"])
        self.menu_linguage.pack(pady=(5,5))
        
        # Lebal
        self.label_volume = ctk.CTkLabel(self.aba_preferencias, text="Volume do Sistema")
        self.label_volume.pack(pady=(10,10))

        # Slider
        self.slider_volume = ctk.CTkSlider(self.aba_preferencias, from_=0, to=100, command=self.att_volume)
        self.slider_volume.pack()
        # setando valor de 50
        self.slider_volume.set(50)
        self.label_porcen_volume = ctk.CTkLabel(self.aba_preferencias, text="50%")
        self.label_porcen_volume.pack()
        
    def construir_abaSistema(self):
        self.abaSistema = self.principal_abas.tab("Itens")

        # Label
        self.label_itens = ctk.CTkLabel(self.abaSistema, text="Testar Carregamento do Sistema", font=ctk.CTkFont(size=16))
        self.label_itens.pack(pady=(10,10))

        # Slider
        self.progress_bar = ctk.CTkProgressBar(self.abaSistema, width=400)
        self.progress_bar.pack(pady=(20,20))
        self.progress_bar.set(0)

        # Button
        self.button_progress = ctk.CTkButton(self.abaSistema, text="Iniciar Carregamento", command=self.loading)
        self.button_progress.pack(pady=(10,10))

    def itens(self):
        self.principal_abas.set("Itens")

    def mode_white(self):
        if self.switch_modeDark.get() == 1:
            ctk.set_appearance_mode("Dark")
        else:
            ctk.set_appearance_mode("Light")
    
    def save_profile(self):
        name = self.name_field.get()
        nivel = ""
        if self.nivel_user.get() == 2:
            nivel = "Admin"
        else:
            nivel = "Básico"
        receive_notification = self.checkbox_notify.get()
        print("Nome", name)
        print("Nível", nivel)
        print(receive_notification)
        self.nivel_user.get()
        self.title_side.configure(text=f"{name} App")
        self.subtitle.configure(text=nivel)

    def att_volume(self, new_volume):
        self.label_porcen_volume.configure(text=f"{int(new_volume)}%")

    def loading(self):
        for i in range(100):
            # executar uma tarefa que pode demorar
            time.sleep(0.1)
            self.progress_bar.set((i + 1) / 100)
            self.update()

window = Aplicativo()
window.mainloop()

