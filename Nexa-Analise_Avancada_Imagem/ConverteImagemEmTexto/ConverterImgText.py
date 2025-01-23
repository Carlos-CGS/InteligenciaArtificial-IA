import os
import google.generativeai as genai
from dotenv import load_dotenv
import tkinter as tk
from tkinter import filedialog, Text, Label, Frame
from PIL import Image, ImageTk

# Carregar as variáveis de ambiente
load_dotenv()

# Configurar a API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

filepath = None


# Função para carregar e exibir a imagem
def selecionar_imagem():
    global img_tk, filepath
    filepath = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")]
    )

    if filepath:
        # Exibir o nome do arquivo
        label_nome_arquivo.config(
            text=f"Arquivo selecionado: {os.path.basename(filepath)}"
        )

        # Carregar a imagem com PIL e redimensionar para caber na interface
        img = Image.open(filepath)
        img = img.resize((300, 300), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)

        # Exibir a imagem no Label
        label_imagem.config(image=img_tk)
        label_imagem.image = img_tk


def transcrever_imagem():
    if filepath:
        # Carregar a imagem para o modelo e transcrever
        chat_session = model.start_chat(
            history=[
                {
                    "role": "user",
                    "parts": [genai.upload_file(filepath)],
                }
            ]
        )
        response = chat_session.send_message("Transcreva o que foi escrito acima")

        # Exibir a transcrição no campo de texto
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, response.text)


# Configuração da interface Tkinter
root = tk.Tk()
root.title("Transcrever Imagem para Texto - CGS")

root.configure(bg="#005B3D")

frame_botoes = Frame(root, bg="#005B3D")
frame_botoes.pack(pady=10)

btn_selecionar_imagem = tk.Button(
    frame_botoes,
    text="Selecionar Imagem",
    command=selecionar_imagem,
    bg="#007A52",
    fg="white",
)
btn_selecionar_imagem.pack(side=tk.LEFT, padx=5)

btn_transcrever = tk.Button(
    frame_botoes,
    text="Transcrever Imagem",
    command=transcrever_imagem,
    bg="#007A52",
    fg="white",
)
btn_transcrever.pack(side=tk.LEFT, padx=5)

# Frame para a imagem e o campo de texto
frame_conteudo = Frame(root, bg="#005B3D")
frame_conteudo.pack(pady=10)

# Label para exibir a imagem selecionada
label_imagem = Label(frame_conteudo, bg="#005B3D")
label_imagem.pack(side=tk.LEFT, padx=10)

# Campo de texto para mostrar a transcrição
text_output = Text(
    frame_conteudo, wrap=tk.WORD, height=15, width=50, bg="#8CCB8C", fg="black"
)
text_output.pack(side=tk.LEFT, padx=10)

# Label para mostrar o nome do arquivo
label_nome_arquivo = Label(
    root, text="Nenhum arquivo selecionado", bg="#005B3D", fg="white"
)
label_nome_arquivo.pack(pady=5)

root.mainloop()
