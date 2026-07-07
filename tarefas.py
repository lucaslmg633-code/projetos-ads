import tkinter as tk
from tkinter import messagebox
import sqlite3

# Configuração e inicialização do Banco de Dados SQLite3
def inicializar_banco():
    conexao = sqlite3.connect("tarefas.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            categoria TEXT
        )
    """)
    conexao.commit()
    conexao.close()

# Função para adicionar tarefa
def adicionar_tarefa():
    tarefa = entrada_tarefa.get()
    if tarefa:
        conexao = sqlite3.connect("tarefas.db")
        cursor = conexao.cursor()
        categoria_automatica = "Geral" 
        cursor.execute("INSERT INTO tarefas (descricao, categoria) VALUES (?, ?)", (tarefa, categoria_automatica))
        conexao.commit()
        conexao.close()
        lista_tarefas.insert(tk.END, f"{tarefa} [{categoria_automatica}]")
        entrada_tarefa.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Por favor, digite uma tarefa.")

# Configuração da Interface Gráfica com Tkinter
app = tk.Tk()
app.title("Gerenciador de Tarefas Automatizado")
app.geometry("400x400")

label_titulo = tk.Label(app, text="Minhas Tarefas", font=("Arial", 14, "bold"))
label_titulo.pack(pady=10)

entrada_tarefa = tk.Entry(app, width=30, font=("Arial", 11))
entrada_tarefa.pack(pady=5)

botao_adicionar = tk.Button(app, text="Adicionar Tarefa", command=adicionar_tarefa, bg="#4CAF50", fg="white")
botao_adicionar.pack(pady=5)

lista_tarefas = tk.Listbox(app, width=45, height=12, font=("Arial", 10))
lista_tarefas.pack(pady=10)

inicializar_banco()
app.mainloop()
