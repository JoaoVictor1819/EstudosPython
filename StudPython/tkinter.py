# interface com botões e caixas de texto (tkinter)

import tkinter as tk
from tkinter import messagebox

pessoas = {}

def adicionar_pessoas():
    nome = nome_entry.get()
    idade = idade_entry.get()
    altura = altura_entry.get()

    if nome and idade and altura:
        pessoas[nome] = {"idade": int(idade), "altura": float(altura)}
        menssagembox.showinfo("Sucesso", f"{nome} foi adicionado com sucesso!")
        nome_entry.delete(0, tk.END)
        idade_entry.delete(0, tk.END)
        altura_entry.delete(0, tk.END)