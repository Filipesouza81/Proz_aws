import sqlite3

# Função para conectar ao banco de dados e criar a tabela
def conectar_banco():
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Função para adicionar um cliente ao banco de dados
def adicionar_cliente(nome, email, telefone):
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO clientes (nome, email, telefone)
        VALUES (?, ?, ?)
    ''', (nome, email, telefone))
    conn.commit()
    conn.close()

# Função para buscar todos os clientes
def buscar_clientes():
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clientes')
    clientes = cursor.fetchall()
    conn.close()
    return clientes
import tkinter as tk
from tkinter import messagebox

# Função para cadastrar novo cliente
def cadastrar_cliente():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()

    if nome and email and telefone:
        adicionar_cliente(nome, email, telefone)
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
        entry_nome.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
    else:
        messagebox.showwarning("Erro", "Todos os campos são obrigatórios.")

# Função para visualizar os clientes cadastrados
def visualizar_clientes():
    clientes = buscar_clientes()
    janela_clientes = tk.Toplevel()
    janela_clientes.title("Clientes Cadastrados")

    text = tk.Text(janela_clientes)
    text.pack()

    for cliente in clientes:
        text.insert(tk.END, f"ID: {cliente[0]} | Nome: {cliente[1]} | Email: {cliente[2]} | Telefone: {cliente[3]}\n")

# Função principal da interface gráfica
def interface_principal():
    global entry_nome, entry_email, entry_telefone

    janela = tk.Tk()
    janela.title("Cadastro de Clientes")
    janela.geometry("400x300")

    # Labels e Entradas
    label_nome = tk.Label(janela, text="Nome:")
    label_nome.pack()
    entry_nome = tk.Entry(janela)
    entry_nome.pack()

    label_email = tk.Label(janela, text="Email:")
    label_email.pack()
    entry_email = tk.Entry(janela)
    entry_email.pack()

    label_telefone = tk.Label(janela, text="Telefone:")
    label_telefone.pack()
    entry_telefone = tk.Entry(janela)
    entry_telefone.pack()

    # Botões
    botao_cadastrar = tk.Button(janela, text="Cadastrar Cliente", command=cadastrar_cliente)
    botao_cadastrar.pack(pady=10)

    botao_visualizar = tk.Button(janela, text="Visualizar Clientes", command=visualizar_clientes)
    botao_visualizar.pack()

    janela.mainloop()

# Inicializando o banco de dados e a interface
if __name__ == "__main__":
    conectar_banco()
    interface_principal()
    import os
import winshell # type: ignore
from win32com.client import Dispatch # type: ignore

def criar_atalho():
    desktop = winshell.desktop()
    caminho_atalho = os.path.join(desktop, "CadastroClientes.lnk")
    target = os.path.join(os.getcwd(), "cadastro_clientes.py")
    icone = os.path.join(os.getcwd(), "icone.ico")  # Opcional

    shell = Dispatch('WScript.Shell')
    atalho = shell.CreateShortCut(caminho_atalho)
    atalho.Targetpath = target
    atalho.WorkingDirectory = os.getcwd()
    atalho.IconLocation = icone if os.path.exists(icone) else ""
    atalho.save()

if __name__ == "__main__":
    criar_atalho()