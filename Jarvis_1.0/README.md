# Documentação do Código do Assistente de Voz J.A.R.V.I.S.
# "Just A Rather Very Intelligent System"
## Descrição Geral
> Este projeto implementa um assistente de voz chamado J.A.R.V.I.S. utilizando a biblioteca tkinter para a interface gráfica, speech_recognition para reconhecimento de fala, pyttsx3 para síntese de voz e a API do Google para realizar pesquisas.

> Dependências
- Para executar este código, você precisará das seguintes bibliotecas:
- tkinter
- threading
- speech_recognition
- os
- pyttsx3
- google.generativeai
- datetime
- webbrowser
- time
- random

> Você pode instalar as bibliotecas necessárias utilizando o pip:
- pip install SpeechRecognition 
- pyttsx3 google-generativeai

### Estrutura do Código
> Importações
- import tkinter as tk
- from threading import Thread
- import speech_recognition as sr
- import os
- import pyttsx3
- import google.generativeai as genai
- from datetime import datetime
- import webbrowser
- import time
- import random

> Classe Principal
- A classe JarvisApp é responsável pela criação da interface gráfica e pela inicialização do assistente de voz.
- O método __init__ inicializa a interface gráfica e configura os elementos da janela principal.

> iniciar_assistente(self)
- Este método inicia o assistente em uma nova thread para permitir a execução assíncrona.

> executar_assistente(self)
- O método principal que mantém o assistente em execução, incluindo a inicialização do motor de síntese de fala e as funções para ouvir comandos.

> Funções Auxiliares
- falar(texto) - Função que utiliza pyttsx3 para converter texto em fala.

> mudar_cor_circulo(cor) - Função que altera a cor do círculo neon na interface gráfica.

> animar_circulo() - Função que anima o círculo neon quando o assistente está falando.

> apresentacao() - Função que faz a apresentação inicial do assistente.

> ouvir_microfone(primeira_vez) - Função que utiliza speech_recognition para capturar e processar comandos de voz.

> reproduzir_musica(microfone) - Função que reproduz música a partir do YouTube com base no comando do usuário.

> pesquisar_no_google(pesquisa) - Função que realiza uma pesquisa no Google utilizando a API do Google Generative AI.

> Loop Principal do Assistente
Para iniciar o assistente, execute o código. A interface gráfica será exibida com um botão para iniciar o assistente. O assistente ficará ouvindo comandos de voz e responderá de acordo com as funções implementadas.

### Comandos Suportados
- Pesquisar: Realiza uma pesquisa no Google.
- Tocar música: Reproduz uma música do YouTube.
- Abrir navegador: Abre o navegador web.
- Abrir calculadora: Abre a calculadora do sistema.
- Abrir Paint: Abre o Paint.
- Abrir bloco de notas: Abre o Bloco de Notas.
- Abrir Excel: Abre o Microsoft Excel.
- Abrir Word: Abre o Microsoft Word.
- Abrir CMD: Abre o prompt de comando.
- Concertar internet: Inicia o solucionador de problemas de rede.
- Abrir vs code: Abre o Visual Studio Code.
- Que horas são: Informa a hora atual.
- Que dia é hoje: Informa a data atual.
- Transcrever: Transcreve uma mensagem e a salva em um arquivo de texto.
- Desligar sistema: Desliga o assistente.

> Conclusão
Este projeto demonstra como criar um assistente de voz com uma interface gráfica em Python. Ele utiliza várias bibliotecas para proporcionar uma experiência de usuário interativa e funcional. 