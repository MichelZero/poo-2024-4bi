import tkinter as tk
from tkinter import messagebox
from datetime import datetime


# Função para calcular o IMC
def calcular_imc():
    try:
        nome = entry_nome.get()
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())


        if peso <= 0 or altura <= 0:
            raise ValueError("Peso e altura devem ser positivos.")


        imc = peso / (altura ** 2)


        # Classificação do IMC
        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            classificacao = "Peso normal"
        elif 25 <= imc < 29.9:
            classificacao = "Sobrepeso"
        elif 30 <= imc < 39.9:
            classificacao = "Obesidade"
        else:
            classificacao = "Obesidade grave"


        # Exibe o resultado
        label_resultado.config(text=f"IMC: {imc:.2f}\nClassificação: {classificacao}")
    except ValueError as e:
        messagebox.showerror("Erro", str(e))


# Função para salvar os dados em um arquivo
def salvar_dados():
    nome = entry_nome.get()
    peso = entry_peso.get()
    altura = entry_altura.get()
    data = entry_data.get()


    try:
        peso = float(peso)
        altura = float(altura)
    except ValueError:
        messagebox.showerror("Erro", "Peso e altura devem ser números válidos.")
        return


    # Validação de data
    try:
        data_formatada = datetime.strptime(data, "%d/%m/%Y")
    except ValueError:
        messagebox.showerror("Erro", "Data inválida. Use o formato dd/mm/aaaa.")
        return


    imc = peso / (altura ** 2)


    with open("dados_imc.txt", "a") as file:
        file.write(f"Nome: {nome}, Peso: {peso}, Altura: {altura}, Data: {data}, IMC: {imc:.2f}\n")


    messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")


# Função para exibir a janela "Sobre"
def sobre():
    sobre_janela = tk.Toplevel()
    sobre_janela.title("Sobre o Aplicativo")
    sobre_janela.geometry("300x150")
    label_sobre = tk.Label(sobre_janela, text="Desenvolvedores: João, Maria\nDisciplina: Programação\nProfessor: Dr. Silva")
    label_sobre.pack(pady=20)


# Função para abrir a janela de calculadora IMC
def janela_imc():
    imc_janela = tk.Toplevel()
    imc_janela.title("Calculadora IMC")
    imc_janela.geometry("400x300")


    global entry_nome, entry_peso, entry_altura, entry_data, label_resultado


    # Labels e Entradas
    tk.Label(imc_janela, text="Nome:").pack(pady=5)
    entry_nome = tk.Entry(imc_janela)
    entry_nome.pack(pady=5)


    tk.Label(imc_janela, text="Peso (kg):").pack(pady=5)
    entry_peso = tk.Entry(imc_janela)
    entry_peso.pack(pady=5)


    tk.Label(imc_janela, text="Altura (m):").pack(pady=5)
    entry_altura = tk.Entry(imc_janela)
    entry_altura.pack(pady=5)


    tk.Label(imc_janela, text="Data (dd/mm/aaaa):").pack(pady=5)
    entry_data = tk.Entry(imc_janela)
    entry_data.pack(pady=5)


    # Botões
    botao_calcular = tk.Button(imc_janela, text="Calcular IMC", command=calcular_imc)
    botao_calcular.pack(pady=10)


    label_resultado = tk.Label(imc_janela, text="IMC: --\nClassificação: --")
    label_resultado.pack(pady=10)


    botao_salvar = tk.Button(imc_janela, text="Salvar Dados", command=salvar_dados)
    botao_salvar.pack(pady=10)


# Janela Principal
root = tk.Tk()
root.title("Aplicativo IMC")
root.geometry("300x200")


# Botões da janela principal
botao_imc = tk.Button(root, text="Calculadora IMC", command=janela_imc)
botao_imc.pack(pady=20)


botao_sobre = tk.Button(root, text="Sobre", command=sobre)
botao_sobre.pack(pady=20)


# Executa a janela principal
root.mainloop()


