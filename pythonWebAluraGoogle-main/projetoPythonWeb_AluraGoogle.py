import tkinter as tk
import requests
import random

# Criar a janela principal
janela = tk.Tk()
janela.title('Jogo da Forca')

# Variáveis globais para armazenar a palavra secreta, a dica e a palavra exibida
palavra_secreta = ''
dica = ''
palavra_exibida = ''
acertou = False

# Função para verificar se a letra está na palavra secreta
def verificar_letra():
    global palavra_secreta, palavra_exibida, acertou
    if acertou:
        return
    letra = entrada_letra.get()
    if letra in palavra_secreta:
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                palavra_exibida = palavra_exibida[:i] + letra + palavra_exibida[i+1:]
                texto_resultado.config(text='Acertou uma letra...')
        texto_palavra.config(text=palavra_exibida)
        if palavra_exibida == palavra_secreta:
            texto_resultado.config(text='Parabéns, você venceu!')
            entrada_letra.config(state=tk.DISABLED)
            acertou = True
    else:
        texto_resultado.config(text='Letra errada, tente novamente.')

# Uma função para obter uma nova palavra secreta da API
def obter_palavra():
    global palavra_secreta, dica, palavra_exibida, acertou
    acertou = False
    entrada_letra.config(state=tk.NORMAL)
    entrada_letra.delete(0, tk.END)
    texto_resultado.config(text='')
    url = 'https://raw.githubusercontent.com/guilhermeonrails/api-imersao-ia/main/words.json'
    resposta = requests.get(url)
    data = resposta.json()
    valor_secreto = random.choice(data)
    palavra_secreta = valor_secreto['palavra']
    dica = valor_secreto['dica']
    # Inicializa a palavra_exibida com '_ ' para cada letra
    palavra_exibida = '_ ' * len(palavra_secreta)
    texto_palavra.config(text=palavra_exibida)
    texto_dica.config(text=f'Dica: {dica}')

# Criar os widgets
texto_palavra = tk.Label(janela, text='')
texto_dica = tk.Label(janela, text='')
entrada_letra = tk.Entry(janela)
texto_resultado = tk.Label(janela, text='')

# Criar os botões
botao_chutar = tk.Button(janela, text='Chutar', command=verificar_letra)
botao_nova_palavra = tk.Button(janela, text='Nova Palavra', command=obter_palavra)

# Organizar os widgets na janela
texto_palavra.grid(row=0, column=1, columnspan=2, padx=10, pady=10)
texto_dica.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
entrada_letra.grid(row=2, column=1, padx=10, pady=10)
botao_chutar.grid(row=2, column=2, padx=10, pady=10)
botao_nova_palavra.grid(row=3, column=1, columnspan=2, padx=10, pady=10)
texto_resultado.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

# Obter a primeira palavra secreta ao iniciar o jogo
obter_palavra()

# Iniciar o loop principal da janela
janela.mainloop()
