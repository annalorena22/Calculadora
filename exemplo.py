import customtkinter as ctk
import tkinter as tk

# Variáveis globais para o estado da calculadora
is_on = True
is_scientific = False

def button_click(display, text):
    """
    Função chamada quando um botão é clicado.
    Atualiza o display com base no texto do botão pressionado.
    """
    if not is_on:
        return  # Se a calculadora está desligada, não faz nada.

    current_text = display.get()  # Obtém o texto atual do display
    
    if text == 'C':
        # Limpa o display
        display.delete(0, tk.END)
    elif text == '=':
        # Avalia a expressão matemática no display
        expression = current_text.replace('^', '**')  # Substitui '^' por '**' para potência
        if all(c in '0123456789+-*/(). ' for c in expression):  # Verifica se a expressão é válida
            try:
                result = eval(expression)  # Avalia a expressão matemática
                display.delete(0, tk.END)  # Limpa o display
                display.insert(0, str(result))  # Insere o resultado
            except:
                display.delete(0, tk.END)  # Limpa o display
                display.insert(0, "Erro")  # Insere "Erro" se a avaliação falhar
        else:
            display.delete(0, tk.END)  # Limpa o display
            display.insert(0, "Erro")  # Insere "Erro" se a expressão for inválida
    elif text == '√':
        # Calcula a raiz quadrada
        if current_text and current_text.replace('.', '', 1).isdigit():  # Verifica se o texto é um número
            result = float(current_text) ** 0.5  # Calcula a raiz quadrada
            display.delete(0, tk.END)  # Limpa o display
            display.insert(0, str(result))  # Insere o resultado
        else:
            display.delete(0, tk.END)  # Limpa o display
            display.insert(0, "Erro")  # Insere "Erro" se a entrada não for um número
    elif text == '^':
        # Calcula a potência base^expoente
        parts = current_text.split()  # Divide o texto em partes
        if len(parts) == 2 and all(p.replace('.', '', 1).isdigit() for p in parts):
            base = float(parts[0])  # Obtém a base
            exponent = float(parts[1])  # Obtém o expoente
            result = base ** exponent  # Calcula a potência
            display.delete(0, tk.END)  # Limpa o display
            display.insert(0, str(result))  # Insere o resultado
        else:
            display.delete(0, tk.END)  # Limpa o display
            display.insert(0, "Erro")  # Insere "Erro" se a entrada estiver incorreta
    else:
        # Adiciona o texto do botão ao display
        display.insert(tk.END, text)

def handle_keypress(event, display):
    """
    Função chamada quando uma tecla é pressionada.
    Permite a entrada via teclado.
    """
    if not is_on:
        return  # Se a calculadora está desligada, não faz nada.

    key = event.char  # Obtém o caractere da tecla pressionada
    
    if key.isdigit() or key in '+-*/().':
        button_click(display, key)  # Processa números e operadores
    elif key == '\r':  # Tecla Enter
        button_click(display, '=')  # Processa a tecla Enter como "="
    elif key == '\x7f':  # Tecla Backspace
        button_click(display, 'C')  # Processa a tecla Backspace como "C"

def toggle_power(display, power_button, scientific_frame):
    """
    Alterna o estado de liga/desliga da calculadora.
    """
    global is_on
    if is_on:
        # Desliga a calculadora
        display.delete(0, tk.END)  # Limpa o display
        display.insert(0, "Calculadora Desligada")  # Exibe mensagem de desligado
        is_on = False  # Atualiza o estado para desligado
        scientific_frame.pack_forget()  # Remove a seção científica
    else:
        # Liga a calculadora
        display.delete(0, tk.END)  # Limpa o display
        is_on = True  # Atualiza o estado para ligado
        scientific_frame.pack(pady=10)  # Reexibe a seção científica

def toggle_scientific(scientific_frame):
    """
    Alterna a visibilidade dos botões científicos.
    """
    global is_scientific
    if is_scientific:
        scientific_frame.pack_forget()  # Remove a seção científica
        is_scientific = False  # Atualiza o estado para não científico
    else:
        scientific_frame.pack(pady=10)  # Exibe a seção científica
        is_scientific = True  # Atualiza o estado para científico

def create_calculator():
    """
    Cria e exibe a interface da calculadora.
    """
    # Cria a janela principal
    root = ctk.CTk()
    root.title("Calculadora")  # Define o título da janela
    root.geometry("400x600")  # Define o tamanho da janela

    # Cria o display da calculadora
    display = ctk.CTkEntry(root, state="normal", font=("Arial", 24))
    display.pack(pady=20, fill="both", padx=20)  # Adiciona o display à janela

    # Cria o frame para os botões da calculadora
    button_frame = ctk.CTkFrame(root)
    button_frame.pack(pady=10, padx=10, fill="both", expand=True)

    # Cria o frame para os botões científicos
    scientific_frame = ctk.CTkFrame(root)

    # Lista de botões padrão da calculadora
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
        ('=', 5, 0, 4)  # Botão "=" ocupa 4 colunas
    ]

    # Cria os botões padrão
    for button in buttons:
        if len(button) == 4:
            text, row, col, colspan = button  # Desempacota botão com colspan
        else:
            text, row, col = button  # Desempacota botão sem colspan
            colspan = 1  # Define colspan como 1 por padrão
        # Cria o botão e o adiciona ao frame
        ctk.CTkButton(button_frame, text=text, command=lambda t=text: button_click(display, t)).grid(row=row, column=col, columnspan=colspan, sticky="nsew")

    # Lista de botões científicos
    scientific_buttons = [
        ('√', 0, 0), ('^', 0, 1)
    ]

    # Cria os botões científicos
    for button in scientific_buttons:
        text, row, col = button
        ctk.CTkButton(scientific_frame, text=text, command=lambda t=text: button_click(display, t)).grid(row=row, column=col, sticky="nsew")

    # Cria o botão de ligar/desligar
    power_button = ctk.CTkButton(root, text="ON/OFF", command=lambda: toggle_power(display, power_button, scientific_frame))
    power_button.pack(pady=10)

    # Cria o botão de alternância da calculadora científica
    scientific_button = ctk.CTkButton(root, text="Toggle Scientific", command=lambda: toggle_scientific(scientific_frame))
    scientific_button.pack(pady=10)

    # Configura o tratamento de eventos do teclado
    root.bind("<Key>", lambda event: handle_keypress(event, display))

    # Inicia o loop principal da interface gráfica
    root.mainloop()

if __name__ == "__main__":
    create_calculator()

# Importações e Variáveis Globais:

# import customtkinter as ctk: Importa a biblioteca customTkinter para criar a interface gráfica.
# import tkinter as tk: Importa a biblioteca tkinter para uso básico de widgets.
# is_on e is_scientific: Variáveis que controlam o estado da calculadora e a visibilidade dos botões científicos.
# Função button_click:

# Lida com a lógica de exibição e cálculos quando um botão é pressionado.
# Limpa o display, avalia expressões, calcula raízes quadradas e potências, e lida com entradas gerais.
# Função handle_keypress:

# Permite a entrada de teclado na calculadora, tratando caracteres digitados e teclas especiais.
# Função toggle_power:

# Alterna entre os estados ligado e desligado da calculadora, e controla a visibilidade dos botões científicos.
# Função toggle_scientific:

# Alterna a visibilidade dos botões científicos.
# Função create_calculator:

# Configura e cria a interface gráfica da calculadora, incluindo o display, os botões, e a estrutura dos frames.
# Bloco if __name__ == "__main__":

# Garante que a função create_calculator seja executada apenas quando o script é executado diretamente, e não quando importado como um módulo.