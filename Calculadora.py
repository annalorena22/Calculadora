import tkinter as tk
import math

janelao = tk.Tk()
janelao.title("Calculadora")
janelao.geometry("400x600")

#Função clicar
def clicar(botao, tela):
    global ligada
    if not ligada:
        tela.delete(0, tk.END)
        tela.insert(0, "Calculadora Desligada")
        return

    texto_atual = tela.get()
    
    if botao in '0123456789+-*/':
        tela.insert(tk.END, botao)
    elif botao == 'C':
        tela.delete(0, tk.END)
    elif botao == '=':
        if texto_atual:
            resultado = calcular_expressao(texto_atual)
            tela.delete(0, tk.END)
            tela.insert(0, str(resultado))
    elif botao in ['sqrt', 'pow', 'log', 'exp']:
        if texto_atual:
            resultado = calcular_funcao_cientifica(botao, texto_atual)
            tela.delete(0, tk.END)
            tela.insert(0, str(resultado))

#Função calcular
def calcular_expressao(expressao):
    return eval(expressao)

#Função calcuar modo cientifica
def calcular_funcao_cientifica(funcao, valor):
    valor = float(valor)
    if funcao == 'sqrt':
        return math.sqrt(valor)
    elif funcao == 'pow':
        return math.pow(valor, 2)
    elif funcao == 'log':
        return math.log(valor)
    elif funcao == 'exp':
        return math.exp(valor)

#Função ligar/desligar
def ligar_desligar(botoes_frame, botao_ligar, tela, botoes_cientificos_frame, botao_cientifica):
    global ligada
    if ligada:
        ligada = False
        tela.delete(0, tk.END)
        tela.insert(0, "Calculadora Desligada")
        botoes_frame.pack_forget()
        botoes_cientificos_frame.pack_forget()
        botao_ligar.config(text="Ligar")
        botao_cientifica.pack_forget()  # Remove o botão "Modo Científico"
    else:
        ligada = True
        botoes_frame.pack()
        if cientifica:
            botoes_cientificos_frame.pack()
        tela.delete(0, tk.END)
        botao_ligar.config(text="Desligar")
        botao_cientifica.pack(fill="x")  # Adiciona o botão "Modo Científico" de volta

# Função mudar normal/científico
def alternar_cientifica(botoes_cientificos_frame):
    global cientifica
    cientifica = not cientifica
    if cientifica:
        botoes_cientificos_frame.pack()
    else:
        botoes_cientificos_frame.pack_forget()

#Frame telinha de entry
tela = tk.Entry(janelao, font=("Arial", 24), borderwidth=2, relief="ridge", justify="right")
tela.pack(expand=True, fill="both")

#Botões
botoes_frame = tk.Frame(janelao)
botoes_frame.pack()

botao7 = tk.Button(botoes_frame, text='7', font=("Arial", 18), command=lambda: clicar('7', tela))
botao7.grid(row=0, column=0)

botao8 = tk.Button(botoes_frame, text='8', font=("Arial", 18), command=lambda: clicar('8', tela))
botao8.grid(row=0, column=1)

botao9 = tk.Button(botoes_frame, text='9', font=("Arial", 18), command=lambda: clicar('9', tela))
botao9.grid(row=0, column=2)

botao_dividir = tk.Button(botoes_frame, text='/', font=("Arial", 18), command=lambda: clicar('/', tela))
botao_dividir.grid(row=0, column=3)

botao4 = tk.Button(botoes_frame, text='4', font=("Arial", 18), command=lambda: clicar('4', tela))
botao4.grid(row=1, column=0)

botao5 = tk.Button(botoes_frame, text='5', font=("Arial", 18), command=lambda: clicar('5', tela))
botao5.grid(row=1, column=1)

botao6 = tk.Button(botoes_frame, text='6', font=("Arial", 18), command=lambda: clicar('6', tela))
botao6.grid(row=1, column=2)

botao_multiplicar = tk.Button(botoes_frame, text='*', font=("Arial", 18), command=lambda: clicar('*', tela))
botao_multiplicar.grid(row=1, column=3)

botao1 = tk.Button(botoes_frame, text='1', font=("Arial", 18), command=lambda: clicar('1', tela))
botao1.grid(row=2, column=0)

botao2 = tk.Button(botoes_frame, text='2', font=("Arial", 18), command=lambda: clicar('2', tela))
botao2.grid(row=2, column=1)

botao3 = tk.Button(botoes_frame, text='3', font=("Arial", 18), command=lambda: clicar('3', tela))
botao3.grid(row=2, column=2)

botao_subtrair = tk.Button(botoes_frame, text='-', font=("Arial", 18), command=lambda: clicar('-', tela))
botao_subtrair.grid(row=2, column=3)

botao_C = tk.Button(botoes_frame, text='C', font=("Arial", 18), command=lambda: clicar('C', tela))
botao_C.grid(row=3, column=0)

botao0 = tk.Button(botoes_frame, text='0', font=("Arial", 18), command=lambda: clicar('0', tela))
botao0.grid(row=3, column=1)

botao_igual = tk.Button(botoes_frame, text='=', font=("Arial", 18), command=lambda: clicar('=', tela))
botao_igual.grid(row=3, column=2)

botao_somar = tk.Button(botoes_frame, text='+', font=("Arial", 18), command=lambda: clicar('+', tela))
botao_somar.grid(row=3, column=3)

botoes_cientificos_frame = tk.Frame(janelao)

botao_sqrt = tk.Button(botoes_cientificos_frame, text='sqrt', font=("Arial", 18), command=lambda: clicar('sqrt', tela))
botao_sqrt.pack(side="left")

botao_pow = tk.Button(botoes_cientificos_frame, text='pow', font=("Arial", 18), command=lambda: clicar('pow', tela))
botao_pow.pack(side="left")

botao_log = tk.Button(botoes_cientificos_frame, text='log', font=("Arial", 18), command=lambda: clicar('log', tela))
botao_log.pack(side="left")

botao_exp = tk.Button(botoes_cientificos_frame, text='exp', font=("Arial", 18), command=lambda: clicar('exp', tela))
botao_exp.pack(side="left")

#Botão modo cientifica
botao_cientifica = tk.Button(janelao, text="Modo Científico", command=lambda: alternar_cientifica(botoes_cientificos_frame))
botao_cientifica.pack(fill="x")

#Botão ligar/desligar
botao_ligar = tk.Button(janelao, text="Desligar", command=lambda: ligar_desligar(botoes_frame, botao_ligar, tela, botoes_cientificos_frame, botao_cientifica))
botao_ligar.pack(fill="x")


ligada = True
cientifica = False

janelao.mainloop()
