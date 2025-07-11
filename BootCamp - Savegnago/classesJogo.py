class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo.lower()

    def atacar(self):
        if self.tipo == "mago":
            ataque = "magia"
        elif self.tipo == "guerreiro":
            ataque = "espada"
        elif self.tipo == "monge":
            ataque = "artes marciais"
        elif self.tipo == "ninja":
            ataque = "shuriken"
        else:
            ataque = "um ataque desconhecido"

        print(f"O {self.tipo} atacou usando {ataque}")


heroi1 = Heroi("Ragnar", 35, "guerreiro")
heroi2 = Heroi("Sombra", 28, "ninja")

heroi1.atacar()
heroi2.atacar()
