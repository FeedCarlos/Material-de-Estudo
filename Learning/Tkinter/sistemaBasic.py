# Programado na intenção de ser apenas uma tela

import tkinter as tk
# Importando fonte
from tkinter.font import Font

window = tk.Tk()

# Nome da janela
window.title("Sistema de Estoque")

# Tamanho da janela
window.geometry("900x600")

# Criar elementos 
titulo = tk.Label(text="Estoque Importinvest", font=Font(size=22, weight="bold", family="Arial"))


# Posicionar os elementos
titulo.pack(pady=(10, 10))


# Manter a janela aberta pelo loop
window.mainloop()