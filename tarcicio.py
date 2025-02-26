from tkinter import *
from tkinter import ttk
    
def calculadora():
    def calcularimc(*args):
        try:
           # o calculo do imc
           alturalocal = float(altura.get())
           pesolocal = float(peso.get())
           imc = int((pesolocal/(alturalocal**2)*100000.0))/10.0

           # checa se peso e altura nao sao 0 ou menos porque se fosse a pessoa nao existia ne
           if alturalocal <= 0 or pesolocal <= 0:
               raise ValueError
           
           # logica do texto no resultado
           export.set('')
           if imc < 18.5:
               resultado.set(f'Você está com Peso Baixo ({imc})')
           elif imc < 25:
               resultado.set(f'Você está com Peso Normal ({imc})')
           elif imc < 30:
               resultado.set(f'Você está com Sobrepeso ({imc})')
           elif imc < 35:
               resultado.set(f'Você está com Obesidade ({imc})')
           elif imc < 40:
               resultado.set(f'Você está com Obesidade Severa ({imc})')
           else:
               resultado.set(f'Você está com Obesidade Mórbida ({imc})')

        # se algum dado estiver errado vai dar esses erro aqui
        except ValueError:
           export.set('')
           resultado.set('Verifique os valores e tente novamente.')
        except ZeroDivisionError:
           export.set('')
           resultado.set('Você não tem 0cm de altura, bobinho.')

    def adicionaraobd(*args):
        try:
            # checa se tem todos os itens e se altura e peso sao maiores que 0 (grandissima linha mas funciona)
            if not (nome.get() and data.get() and altura.get() and peso.get()) or int(altura.get()) <= 0 or int(peso.get()) <= 0:
                raise ValueError
            
            # escreve os dados que o cara deu pro bancodedados.txt
            with open(f"bancodedados.txt", 'a') as arquivo:
                arquivo.write(f'{str(nome.get())} | {str(data.get())} | {str(altura.get())} | {str(peso.get())} | {int((int(peso.get())/(int(altura.get())**2)*100000.0))/10.0} \n')
                arquivo.close
                resultado.set('')
                export.set('Dados exportados com sucesso!')

        # se a checagem la de cima funcionar isso aparece
        except ValueError:
            resultado.set('')
            export.set('Não foi possível exportar os dados! \nVerifique os valores e tente novamente.')
    
    # janela do imc
    imc = Toplevel(root)
    imc.title("Calculadora de IMC")
    imcmainframe = ttk.Frame(imc, padding="1c 1c 1c 1c")
    imcmainframe.grid(column=0, row=0, sticky=(N, W, E, S))

    # botao de voltar
    ttk.Button(imcmainframe, text="Voltar", command=imc.destroy).grid(column=1, row=1, sticky=(N, W))
    
    # o input do nome
    nome = StringVar()
    nome_entry = ttk.Entry(imcmainframe, width=10, textvariable=nome)
    nome_entry.grid(column=2, row=2, sticky=(E,S))
    
    # o input da data
    data = StringVar()
    data_entry = ttk.Entry(imcmainframe, width=10, textvariable=data)
    data_entry.grid(column=2, row=3, sticky=(E,S))
    
    # o input da altura
    altura = StringVar()
    altura_entry = ttk.Entry(imcmainframe, width=10, textvariable=altura)
    altura_entry.grid(column=2, row=4, sticky=(E,S))
    
    # o input do peso 
    peso = StringVar()
    peso_entry = ttk.Entry(imcmainframe, width=10, textvariable=peso)
    peso_entry.grid(column=2, row=5, sticky=(E,S))

    # botao de calcular o imc
    ttk.Button(imcmainframe, text="Calcular", command=calcularimc).grid(column=2, row=6, columnspan=2)

    # o label que da o resultado
    resultado = StringVar()
    ttk.Label(imcmainframe, textvariable=resultado).grid(column=2, row=7, columnspan=2)

    # botao de exportar pro banco de dados
    ttk.Button(imcmainframe, text="Exportar dados", command=adicionaraobd).grid(column=4, row=8, sticky=W)

    # label que mostra resultado do exportar dados
    export = StringVar()
    ttk.Label(imcmainframe, textvariable=export).grid(column=2, row=8, columnspan=2, sticky=E)

    # textos do lado dos inputs
    ttk.Label(imcmainframe, text="Seu nome").grid(column=3, row=2, sticky=(S, W))
    ttk.Label(imcmainframe, text="A data atual (dd/mm/aa)").grid(column=3, row=3, sticky=(S, W))
    ttk.Label(imcmainframe, text="Sua altura em cm").grid(column=3, row=4, sticky=(S, W))
    ttk.Label(imcmainframe, text="Seu peso em Kg").grid(column=3, row=5, sticky=(S, W))

    # isso aqui serve pra deixar um espaço entre cada coisa
    for child in imcmainframe.winfo_children(): 
        child.grid_configure(pady=5)

    # se o caba der enter vai calcular o imc tambem
    imc.bind("<Return>", calcularimc)
    
def sobre():
    # janela do sobre
    sobre = Toplevel(root)
    sobre.title("Sobre o aplicativo")
    sobremainframe = ttk.Frame(sobre, padding="1c 1c 3c 1c")
    sobremainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    
    # botao de voltar
    ttk.Button(sobremainframe, text="Voltar", command=sobre.destroy).grid(column=1, row=1, sticky=(N, W))
    
    # texto explicativo woooooooww
    ttk.Label(sobremainframe, text="Calculadora de Índice de Massa Corporal (IMC) em Python \nDisciplina: Programação Orientada a Objetos \n"
                                   "Professor: Michel da Silva \nDesenvolvedores: Eduardo Vicente, Kaio Gabriel e Tarcísio de Freitas").grid(column=2, row=2, rowspan=3, columnspan=2, sticky=E)

# menu
root = Tk()
root.title("Menu")
mainframe = ttk.Frame(root, padding="3c 3c 3c 3c")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# os botao que leva pras outra janela
ttk.Button(mainframe, text="Calculadora de IMC", command=calculadora).grid(column=2, row=4, sticky=W)
ttk.Button(mainframe, text="Sobre", command=sobre).grid(column=2, row=5)

root.mainloop()

# faltou apenas gravar a data atual no arquivo bancodedados.txt, mas o código está bem organizado e funcional. Parabéns!