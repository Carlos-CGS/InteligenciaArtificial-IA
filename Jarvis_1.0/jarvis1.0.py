import tkinter as tk
from threading import Thread
import speech_recognition as sr
import os
import pyttsx3
import google.generativeai as genai
from datetime import datetime
import webbrowser
import time
import random

class JarvisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jarvis")
        self.root.geometry("200x190")
        # Definindo as cores
        bg_color = "#006400"
        fg_color = "#000000"
        self.root.configure(bg=bg_color)

        self.label = tk.Label(root, text="Assistente de Voz - J.A.R.V.I.S.", bg=bg_color, fg=fg_color)
        self.label.pack(pady=10)

        # Criar o círculo brilhante neon
        self.canvas = tk.Canvas(root, width=100, height=100, bg=bg_color, highlightthickness=0)
        self.circle = self.canvas.create_oval(30, 30, 70, 70, outline="black", width=5)
        self.canvas.pack()

        self.btn_iniciar = tk.Button(root, text="Iniciar Assistente", command=self.iniciar_assistente, bg=fg_color, fg=bg_color)
        self.btn_iniciar.pack(pady=5)

        self.thread = None
        self.running = False
        self.listening = False
        self.speaking = False

    def iniciar_assistente(self):
        if not self.running:
            self.thread = Thread(target=self.executar_assistente)
            self.thread.start()
            self.running = True
            self.label.config(text="Assistente Executando...")

    def executar_assistente(self):
        # Inicializar o engine de síntese de fala
        engine = pyttsx3.init()

        # Faz o computador falar
        def falar(texto):
            mudar_cor_circulo("#00FF00") 
            self.speaking = True
            engine.say(texto)
            engine.runAndWait()
            self.speaking = False
            mudar_cor_circulo("#00FFFF")  


        # Muda a cor do círculo
        def mudar_cor_circulo(cor):
            self.canvas.itemconfig(self.circle, outline=cor)

        def animar_circulo():
            if self.speaking:
                for i in range(5, 18, 5):
                    if not self.speaking:
                        break
                    self.canvas.coords(self.circle, 20 - i, 20 - i, 80 + i, 80 + i)
                    self.canvas.update()
                    time.sleep(0.05)
                for i in range(17, 4, -5):
                    if not self.speaking:
                        break
                    self.canvas.coords(self.circle, 20 - i, 20 - i, 80 + i, 80 + i)
                    self.canvas.update()
                    time.sleep(0.05)
            self.root.after(47, animar_circulo)

        def apresentacao():
            # Obtendo a hora atual
            hora_atual = datetime.now().hour
            animar_circulo()
            if 0 <= hora_atual < 12:
                saudacao = "Bom dia"
            elif 12 <= hora_atual < 18:
                saudacao = "Boa tarde"
            else:
                saudacao = "Boa noite"
            falar(f"{saudacao} DIGITE_SEU_NOME_AQUI. Hoje é {datetime.now().strftime("%d/%m/%Y")}, são {datetime.now().strftime("%H:%M")}. Me chamo Jarvis.")
            self.label.config(text="Se precisar de algo, fale meu nome....")
            falar("Se precisar de algo, fale meu nome.")
        
        # Função para ouvir e reconhecer fala:
        def ouvir_microfone(primeira_vez):
            # Habilita microfone usuário
            microfone = sr.Recognizer()

            # Apresentação apenas na primeira vez
            if primeira_vez:
                apresentacao()
                primeira_vez = False

            while self.running:
                with sr.Microphone() as source:
                    # Chama um algoritmo de redução de ruídos no som
                    microfone.adjust_for_ambient_noise(source)

                    # Armazena o que foi dito numa variável
                    print("Esperando pelo comando 'Jarvis'...")
                    self.label.config(text="Esperando pelo comando 'Jarvis'...")
                    audio = microfone.listen(source)

                    try:
                        # Passa a variável para o algoritmo reconhecer os padrões
                        frase = microfone.recognize_google(audio, language='pt-BR')
                        print(f"Comando reconhecido: {frase}")

                        # Lista de respostas possíveis
                        respostas = [
                            "Como posso te ajudar?",
                            "Pois não?",
                            "Sim?",
                            "O que você precisa?",
                            "O que você deseja?",
                            "Em que posso ser útil?"
                        ]
                        # Verifica se a palavra "Jarbas" foi dita
                        if "Jarvis" in frase: 
                            # Seleciona uma resposta aleatoriamente da lista
                            resposta = random.choice(respostas)
                            self.label.config(text=resposta)
                            falar(resposta)
    
                            # Escuta o próximo comando
                            with sr.Microphone() as source:
                                audio = microfone.listen(source)

                            try:
                                # Passa a variável para o algoritmo reconhecer os padrões
                                comando = microfone.recognize_google(audio, language='pt-BR')
                                 
                                if "pesquisar" in comando:
                                    pesquisa = comando.split("pesquisar", 1)[1].strip()
                                    if pesquisa:
                                        self.label.config(text="Um momento, estou pesquisando.")
                                        falar("Um momento, estou pesquisando.")
                                        resposta = pesquisar_no_google(f"Resposta em forma discursiva, variando entre 20 e 40 palavras dependendo da complexidade da pergunta, falando da mesma forma que o jarvis a ia do homem de ferro, sobre o seguinte assunto: {pesquisa}")
                                        falar(resposta)
                                    else:
                                        self.label.config(text="Sobre o que deseja saber?")
                                        falar("Sobre o que deseja saber?")
                                        with sr.Microphone() as source:
                                            audio = microfone.listen(source)
                                        try:
                                            pesquisa = microfone.recognize_google(audio, language='pt-BR')
                                            self.label.config(text="Só um momento, estou pesquisando.")
                                            falar("Só um momento, estou pesquisando.")
                                            resposta = pesquisar_no_google(f"Resposta em forma discursiva, variando entre 20 e 40 palavras dependendo da complexidade da pergunta, falando da mesma forma que o jarvis a ia do homem de ferro, sobre o seguinte assunto: {pesquisa}")
                                            falar(resposta)
                                        except sr.UnknownValueError:
                                            self.label.config(text="Não entendi, repita o que deseja.")
                                            falar("Não consegui entender a pesquisa.")
                                elif "tocar música" in comando:
                                    reproduzir_musica(microfone)
                                elif "Abrir navegador" in comando:
                                    os.system("start chrome.exe")
                                    falar("Abrindo o navegador")
                                elif "Abrir calculadora" in comando:
                                    os.system("start calc.exe")
                                    falar("Abrindo a calculadora")
                                elif "Abrir Paint" in comando:
                                    os.system("start mspaint.exe")
                                    falar("Abrindo o Paint")
                                elif "Abrir bloco de notas" in comando:
                                    os.system("start notepad.exe")
                                    falar("Abrindo o bloco de notas")
                                elif "Abrir Excel" in comando:
                                    os.system("start Excel.exe")
                                    falar("Abrindo o Excel")
                                elif "Abrir Word" in comando:
                                    os.system("start winword.exe")
                                    falar("Abrindo o Word")
                                elif "Abrir CMD" in comando:
                                    os.system("start cmd.exe")
                                    falar("Abrindo o prompt de comando")
                                    self.parar_assistente()
                                elif "Concertar internet" in comando:
                                    falar("Iniciando o solucionador de problemas de rede")
                                    os.system("msdt.exe /id NetworkDiagnosticsNetworkAdapter")
                                elif "Abrir vs code" in comando:
                                    os.system("code")
                                    falar("Abrindo o Visual Studio Code")
                                elif "Que horas são" in comando:
                                    hora_atual = datetime.now().strftime("%H:%M")
                                    falar(f"Agora são {hora_atual}.")
                                elif "Que dia é hoje" in comando:
                                    data_atual = datetime.now().strftime("%d/%m/%Y")
                                    falar(f"Hoje é {data_atual}.")
                                elif "transcrever" in comando:
                                    falar("Qual mensagem você gostaria de salvar?")
                                    with sr.Microphone() as source:
                                        audio = microfone.listen(source)
                                    try:
                                        mensagem = microfone.recognize_google(audio, language='pt-BR')
                                        caminho_arquivo = r"C:\Users\CARLOS GARCIA\Desktop\mensagens_salvas.txt"
                                        with open(caminho_arquivo, "a") as arquivo:
                                            arquivo.write(f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - {mensagem}\n")
                                        falar("Mensagem salva com sucesso.")
                                    except sr.UnknownValueError:
                                        falar("Não consegui entender a mensagem. Tente novamente.")
                                elif "desligar sistema" in comando:
                                    falar("Finalizando o sistema. Até logo.")
                                    self.running = False
                                    self.label.config(text="Assistente Desligado.")
                                else:
                                    falar(f"O comando {comando} não foi reconhecido, tente novamente.")
                            except sr.UnknownValueError:
                                self.label.config(text="Não entendi, repita o que deseja.")
                                falar("Não entendi, repita o que deseja.")
                    except sr.UnknownValueError:
                                pass
            return False

        # Função para reproduzir música do YouTube
        def reproduzir_musica(microfone):
            # Solicita ao usuário o nome da música
            falar("Qual música você deseja ouvir?")
            with sr.Microphone() as source:
                audio = microfone.listen(source)
            try:
                musica = microfone.recognize_google(audio, language='pt-BR')
                # Se não foi especificado o nome da música, solicita novamente
                if not musica:
                    falar("Por favor, diga o nome da música.")
                    with sr.Microphone() as source:
                        audio = microfone.listen(source)
                    musica = microfone.recognize_google(audio, language='pt-BR')
                # Formata a música para a busca no YouTube
                musica_formatada = musica.replace(" ", "+")
                # URL de pesquisa do YouTube com a música
                url_youtube = f"https://www.youtube.com/results?search_query={musica_formatada}"
                # Abre o navegador e redireciona para o youtube
                webbrowser.open(url_youtube)
            except sr.UnknownValueError:
                falar("Desculpe, não consegui entender. Por favor, repita.")
            
        # Função para pesquisar no Google usando a API
        def pesquisar_no_google(pesquisa):
            # Configurando a API do Google
            GOOGLE_AI_KEY = "COLE_SUA_CHAVE_API_AQUI"
            genai.configure(api_key=GOOGLE_AI_KEY)
            # Configurando a Temperatura das Respostas
            configurar_geracao = {
                "candidate_count": 1,
                "temperature": 0.9,
            }
            # Configurando os níveis de segurança das respostas (Ofensivas, Raciais, Sexuais, etc.)
            configurar_seguranca = {
                "HARASSMENT": "BLOCK_NONE",
                "HATE": "BLOCK_NONE",
                "SEXUAL": "BLOCK_NONE",
                "DANGEROUS": "BLOCK_NONE",
            }
            # Definindo o Modelo Usado para Pesquisa
            model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                          generation_config=configurar_geracao,
                                          safety_settings=configurar_seguranca)
            # Configurando o Histórico de Pesquisa
            chat = model.start_chat(history=[])
            response = chat.send_message(pesquisa)
            return response.text

        # Loop do Assistente Jarbas
        primeira_vez = True
        while self.running:
            if ouvir_microfone(primeira_vez):
                break
            primeira_vez = False

# Criar a Interface Gráfica
root = tk.Tk()
app = JarvisApp(root)
root.mainloop()