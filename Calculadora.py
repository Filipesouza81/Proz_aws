import tkinter as tk
from tkinter import font

# Função para adicionar números e operadores à entrada
def click(event):
    current_text = display.get()
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            # Avalia a expressão e realiza o cálculo
            result = str(eval(current_text))
            display.set(result)
        except:
            display.set("Error")
    elif button_text == "C":
        display.set("")  # Limpa o display
    else:
        display.set(current_text + button_text)  # Adiciona o valor pressionado

# Função para realizar a operação de porcentagem
def percentage():
    current_text = display.get()
    try:
        result = str(eval(current_text) / 100)  # Calcula a porcentagem
        display.set(result)
    except:
        display.set("Error")

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora")
root.geometry("540x600")
root.resizable(False, False)  # Impede redimensionamento
root.config(bg="black")  # Fundo da interface preta

# Fonte personalizada para os botões e display
button_font = font.Font(family="Arial", size=16, weight="bold")
display_font = font.Font(family="Arial", size=24, weight="bold")

# Variável para armazenar o valor digitado
display = tk.StringVar()

# Display (tela de entrada)
entry = tk.Entry(root, textvar=display, font=display_font, bg="black", fg="white", bd=10, insertwidth=2, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipadx=8, ipady=20)

# Lista de botões (incluindo números, operações e limpar)
buttons = [
    'C', '%', '/', '*',
    '7', '8', '9', '-',
    '4', '5', '6', '+',
    '1', '2', '3', '=',
    '0', '.', '(', ')'
]

# Adicionar botões à interface
row_val = 1
col_val = 0

for button in buttons:
    if button == "%":
        btn = tk.Button(root, text=button, padx=20, pady=20, font=button_font, bg="orange", fg="black", command=percentage)
    else:
        btn = tk.Button(root, text=button, padx=20, pady=20, font=button_font, bg="orange", fg="black")
        btn.bind("<Button-1>", click)
    
    btn.grid(row=row_val, column=col_val, padx=5, pady=5)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Inicia o loop da interface
root.mainloop()
