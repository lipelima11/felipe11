import tkinter as tk

# Função para atualizar o texto na tela
def clicar_botao(valor):
    texto_atual = tela.get()
    tela.delete(0, tk.END)
    tela.insert(0, texto_atual + str(valor))

# Função para limpar a tela
def limpar():
    tela.delete(0, tk.END)

# Função para calcular o resultado
def calcular():
    try:
        resultado = eval(tela.get())
        tela.delete(0, tk.END)
        tela.insert(0, str(resultado))
    except ZeroDivisionError:
        tela.delete(0, tk.END)
        tela.insert(0, "Erro: Div/0")
    except Exception:
        tela.delete(0, tk.END)
        tela.insert(0, "Erro")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x400")
janela.configure(bg="#202020")

# Tela de exibição (Input)
tela = tk.Entry(janela, font=("Arial", 24), bg="#303030", fg="white", borderwidth=0, justify="right")
tela.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20, padx=10, pady=10, sticky="nsew")

# Configuração dos botões
botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Estilo dos botões
estilo_num = {"font": ("Arial", 14), "bg": "#3b3b3b", "fg": "white", "activebackground": "#505050", "activeforeground": "white", "borderwidth": 0}
estilo_op = {"font": ("Arial", 14), "bg": "#f38211", "fg": "white", "activebackground": "#d4700f", "activeforeground": "white", "borderwidth": 0}
estilo_c = {"font": ("Arial", 14), "bg": "#a5a5a5", "fg": "black", "activebackground": "#8e8e8e", "borderwidth": 0}

# Criar e posicionar os botões na tela
for (texto, linha, coluna) in botoes:
    if texto == '=':
        acao = calcular
        estilo = estilo_op
    elif texto == 'C':
        acao = limpar
        estilo = estilo_c
    elif texto in ['/', '*', '-', '+']:
        acao = lambda x=texto: clicar_botao(x)
        estilo = estilo_op
    else:
        acao = lambda x=texto: clicar_botao(x)
        estilo = estilo_num
        
    btn = tk.Button(janela, text=texto, command=acao, **estilo)
    btn.grid(row=linha, column=coluna, padx=2, pady=2, sticky="nsew")

# Ajustar o peso das linhas e colunas para expandirem com a janela
for i in range(5):
    janela.rowconfigure(i, weight=1)
for i in range(4):
    janela.columnconfigure(i, weight=1)

# Iniciar o aplicativo
janela.mainloop()
