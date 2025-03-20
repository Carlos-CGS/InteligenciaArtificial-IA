# Exemplo de código de Média de Notas:
# Todo o código fpi criado usando o GitHub Copilot e revisado por mim,
# conforme proposta do desafio de projeto.

# Solicita o nome do aluno
nome_aluno = input("Digite o nome do aluno: ")

# Solicita as quatro notas do aluno
notas = []
for i in range(1, 5):
    nota = float(input(f"Digite a nota do {i}º semestre: "))
    notas.append(nota)

# Calcula a média
media = sum(notas) / len(notas)

# Determina a situação do aluno
if media < 5:
    situacao = "Reprovado"
elif 5 <= media <= 7:
    situacao = "Recuperação"
else:
    situacao = "Aprovado"

# Exibe o resultado
print(f"\n O Aluno: {nome_aluno}, com média {media:.2f}, está {situacao}")
