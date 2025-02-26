class Info:
  def __init__(self, idade, altura, peso):
    self.idade = idade
    self.altura = altura
    self.peso = peso
  
  def show_info(self):
    return {
      "idade": self.idade,
      "altura": self.altura,
      "peso" : self.peso
    }

pessoa = Info(15, 1.62, 70)


from tkinter import *
from tkinter import ttk
# from Class import Info  # Certifique-se de que a classe está implementada corretamente
# from Class import pessoa

def abrir_calculadora():
    """Abre a janela da Calculadora de IMC"""
    janela_calculadora = Toplevel(janela_principal) #Cria outra janela, fazendo com que duas existam ao mesmo tempo.\

    janela_calculadora.title("Calculadora de IMC")
    # janela_calculadora.geometry("500x500")
    janela_calculadora.configure(bg="#19181B")

    # Criando a estilização dos widgets
    style = ttk.Style()
    style.theme_use("clam")

    # Estilizando botões
    style.configure("TButton", 
                    font=("Arial", 14, "bold"), 
                    padding=10)

    # Estilizando labels
    style.configure("TLabel", font=("Arial", 12), foreground="#444")

    # Criando os elementos da interface
    titulo = Label(janela_calculadora, text="Calculadora IMC", font=("Arial", 16), bg="#19181B", fg="#DBC170")
    titulo.grid(padx=20, pady=20, column=1, row=1)

    botao = ttk.Button(janela_calculadora, text="Calcular", command=calcular_imc)
    botao.grid(padx=20, pady=20, column=1, row=2)

    global resposta, resposta_class
    resposta = Label(janela_calculadora, text="Seu IMC é:", font=("Arial", 14), bg="#B8952E", fg="#050505")
    resposta.grid(padx=20, pady=10, column=1, row=3)

    resposta_class = Label(janela_calculadora, text="", font=("Arial", 15), bg="#19181B", fg="white")
    resposta_class.grid(row=4, pady=10, column=1)

    botao_salvar = ttk.Button(janela_calculadora, text="Salvar Dados", command=salvar_dados)
    botao_salvar.grid(column=1, row=4, pady=10)
def abrir_sobre():
    """Abre a janela Sobre o Autor"""
    janela_sobre = Toplevel(janela_principal)
    janela_sobre.title("Sobre o Autor")
    janela_sobre.geometry("400x300")
    janela_sobre.configure(bg="#19181B")

    label_autor = Label(janela_sobre, text="Criado por: Pedro Davi Vital da Silva", font=("Arial", 14), bg="#19181B", fg="white") #fg = cor do texto
    label_autor.pack(pady=50)

def calcular_imc():
    """Calcula o IMC e atualiza a interface gráfica"""
    
    pessoa_info_dict = pessoa.show_info()
    
    # Cálculo do IMC
    imc = pessoa_info_dict["peso"] / (pessoa_info_dict["altura"] ** 2)
    imc_formatado = f"{imc:.2f}"
    
    # Atualizando a interface
    resposta["text"] = f"Seu IMC é: {imc_formatado}"
    classificar(float(imc_formatado))  # Enviando o IMC formatado para a função de classificação

def classificar(imc):
    """Classifica o IMC e exibe o resultado"""
    if imc < 18.5:
        texto = "Seu peso é baixo"
    elif 18.5 <= imc < 24.9:
        texto = "Peso normal"
    elif 25 <= imc < 29.9:
        texto = "Sobrepeso"
    elif 30 <= imc < 34.9:
        texto = "Obesidade Grau I"
    elif 35 <= imc < 39:
        texto = "Obesidade Grau II"
    else:
        texto = "Obesidade Grau III"

    # Atualizando o texto na Label de classificação
    resposta_class["text"] = texto

def salvar_dados():
    pessoa_info_dict = pessoa.show_info()
    imc = pessoa_info_dict["peso"] / (pessoa_info_dict["altura"] ** 2)
    imc_formatado = f"{imc:.2f}"

    with open("dados_imc.txt", "a") as arquivo:
      arquivo.write(f"Idade: {pessoa_info_dict['idade']} anos\n")
      arquivo.write(f"Altura: {pessoa_info_dict['altura']} m\n")
      arquivo.write(f"Peso: {pessoa_info_dict['peso']} kg\n")
      arquivo.write(f"IMC: {imc_formatado}\n")
      arquivo.write("-" * 30 + "\n")  # Linha separadora

# Criando a janela principal
janela_principal = Tk()
janela_principal.title("Menu Principal")
janela_principal.geometry("500x400")
janela_principal.configure(bg="#19181B")

titulo_menu = Label(janela_principal, text="Menu Principal", font=("Arial", 18), bg="#19181B", fg="#DBC170")
titulo_menu.pack(pady=20)

botao_imc = ttk.Button(janela_principal, text="Calculadora de IMC", command=abrir_calculadora)
botao_imc.pack(pady=10)

botao_sobre = ttk.Button(janela_principal, text="Sobre o Autor", command=abrir_sobre)
botao_sobre.pack(pady=10)



janela_principal.mainloop()