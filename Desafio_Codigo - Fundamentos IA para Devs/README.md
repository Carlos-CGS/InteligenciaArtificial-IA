# <img src="https://hermes.dio.me/tracks/84b2d685-23f9-4729-9e3c-28cb84a39b38.png" height="50"> Desafios de Código - Santander 2024 - Fundamentos de IA para Devs

- Desafio de Código proposto em um BootCamp da plataforma do site DIO, o qual nos faz rever os códigos e complementa-los para que ele alcance os objetivos solicitados.

## Desafio 1 - Desafios de Código - Simulando Desafios com IAs Generativas - Analisando Sentimentos
> Descrição: Imagine que você foi designado a criar um algoritmo para analisar o sentimento de um comentário fornecido pelo usuário, simulando analises de sentimentos, um assunto muito comentado dentro do Machine Learning. O programa solicitará ao usuário que insira um comentário, e em seguida, dividirá esse comentário em palavras individuais.

> Após isso, ele contará o número de palavras positivas, negativas e neutras dentro do comentário, baseando-se em uma lista pré-definida de palavras-chave. As palavras consideradas positivas incluem "bom", "ótimo", "excelente", "maravilhoso", "gostei" e "incrível" enquanto as palavras negativas incluem "ruim", "péssimo", "horrível", "terrível" e "odeio". Já as palavras neutras incluem "mas", "deixou", "apesar" e "embora"

> Depois de calcular as contagens de palavras positivas e negativas, o programa determinará o sentimento predominante do comentário. Se houver mais palavras positivas do que negativas, o sentimento será considerado positivo. Se houver mais palavras negativas do que positivas, o sentimento será considerado negativo. Caso contrário, se houver um número igual de palavras positivas e negativas, o sentimento será neutro.

 - Entrada: O usuário será solicitado a fornecer um comentário como entrada para o programa.
 - Saída: O programa exibirá o sentimento do comentário inserido pelo usuário, que pode ser "Positivo", "Negativo" ou "Neutro", dependendo da análise das palavras-chave no comentário.

- Entrada: A mentoria foi incrível, aprendi muito!	Sentimento: 
- Saída: Positivo

## Desafios 2 - Simulando Desafios com IAs Generativas - Avaliando Prompts
> Descrição: Neste desafio, você será solicitado a criar um algoritmo que avalia se um prompt fornecido pelo usuário está adequado. O programa solicitará ao usuário que insira um prompt e, em seguida, verificará se o prompt contém palavras-chave relevantes. As palavras-chave consideradas relevantes serão "inteligência artificial", "sistemas de recomendação online", "exemplo de conversação", "explique conceitos" e "dicas de tecnologia". Se o prompt incluir pelo menos uma dessas palavras-chave, o programa informará que o prompt está adequado; caso contrário, ele indicará que o prompt não está adequado e sugerirá ao usuário que inclua palavras-chave relevantes.

- Entrada: O usuário será solicitado a inserir um prompt como entrada para o programa.
- Saída: O programa exibirá feedback para o usuário com base na avaliação do prompt inserido. Se o prompt contiver palavras-chave relevantes, o programa informará que o prompt está adequado. Caso contrário, ele indicará que o prompt não está adequado e sugerirá ao usuário que inclua palavras-chave relevantes.

- Entrada: Por favor, explique conceitos de inteligência artificial.	
- Saída: O prompt está adequado.

## Desafio 3 - Simulando Desafios com IAs Generativas - Refatorando com Eficiência
> Desafio: Neste desafio, você será solicitado a fornecer uma breve descrição de boas práticas de refatoração de código em três áreas específicas: identificação clara de funções, separação da entrada de dados e uso de nomes descritivos para variáveis e funções.Cada descrição deve indicar como o código pode ser melhorado nesses aspectos. O objetivo é simularmos a ação de pesquisas em IAs Generativas de busca e pesquisa, dessa forma, cada entrada simula um bom prompt de pesquisa.

- Entrada: A entrada será uma string de texto que representa um bom promtp de pesquisa para IAs Generativas.Após inserir sua descrição, o programa irá processá-la e fornecer um retorno sobre a prática de refatoração sugerida. Se a entrada corresponder a uma das três áreas especificadas, o programa irá sugerir a respectiva melhoria. Caso contrário, informará que a opção é inválida.

- Saída: Após inserir sua descrição, o programa irá processá-la e fornecer um retorno sobre a prática de refatoração sugerida. Se a entrada corresponder a uma das três áreas especificadas, o programa irá sugerir a respectiva melhoria. Caso contrário, informe: Opção inválida.

- Entrada: Dica de boas práticas de refatoração de código, nas funções.	
- Saída: Separe funções em unidades coesas e com responsabilidades únicas.

## Desafio 04 - Simulando Desafios com IAs Generativas - Sugestão de Compras Inteligente
> Desafio: Neste desafio, você deve criar um programa que simule o auxílio de vendas de um site de catálogos de cogumelos utilizando inteligência artificial. O intuito é oferecer aos clientes sugestões de cogumelos que estão em promoção. Dessa forma, o programa deve permitir que o usuário informe o nome de um cogumelo desejado e, com base nessa informação, deve sugerir até dois cogumelos adicionais da lista, cujos valores sejam iguais ou menores que o do cogumelo selecionado pelo cliente. No caso de não houver sugestões disponíveis, ou seja, se o cogumelo escolhido for o mais caro, o programa deve exibir uma mensagem indicando que não há sugestões.

> A baixo apresentamos a lista de cogumelos oferecidos pela loja com todos os seus valores. Considere que essa lista já está ordenada por prioridade, ou seja, você deve oferecer como alternativas nessa ordem:

Shitake	10\
Portobello	8\
Shimeji	6\
Champignon	12\
Funghi	16\
Porcini	16

- Entrada: A entrada será uma string representando o nome do cogumelo desejado pelo usuário.
- Saída: Uma lista com no máximo 2 sugestões de cogumelos mais baratos do que o enviado como entrada. Lembrando que a sugestão das alternativas deve considerar a lista de cogumelos na ordem descrita na tabela supracitada neste desafio.

 - Entrada:	Shitake
 - Saída: Portobello - Valor: 8  /   Shimeji - Valor: 6

## Desafio 5 - Simulando Desafios com IAs Generativas - Calculando Métricas de Avaliação
> Desafio: Você faz parte de uma equipe que está desenvolvendo modelos de Machine Learning para identificar a probabilidade de inadimplência em empréstimos concedidos por uma instituição financeira. Após treinar os modelos, sua tarefa é avaliar seu desempenho usando algumas métricas de avaliação. Nesse contexto, o desafio é criar um algoritmo que receba n matrizes de confusão e retorne o índice, precisão e acurácia da matriz que apresenta o melhor desempenho com base no cálculo dessas métricas. Lembrando que:

• Acurácia é calculada pela fórmula: (VP + VN) / (VP + FP + FN + VN)
• Precisão é calculada pela fórmula: VP / (VP + FP)

Onde:

• VP (Verdadeiro Positivo): Casos em que o modelo previu corretamente a classe positiva.
• FP (Falso Positivo ou Erro Tipo I): Casos em que o modelo previu incorretamente a classe positiva.
• FN (Falso Negativo ou Erro Tipo II): Casos em que o modelo previu incorretamente a classe negativa.
• VN (Verdadeiro Negativo): Casos em que o modelo previu corretamente a classe negativa.

- Entrada: A entrada consiste em uma string composta por: n, representando o número de matrizes de confusão, seguido dos valores que compõem as n matrizes.

> Cada matriz consiste em quatro valores, onde os dois primeiros representam a primeira linha da matriz, composta por verdadeiros positivos (VP) e falsos positivos (FP); os dois últimos valores representam a segunda linha, que é composta por falsos negativos (FN) e verdadeiros negativos (VN). As duas linhas e os valores que as compõem estão separados por vírgulas.

- Saída: O resultado esperado inclui o valor do índice, acurácia e precisão (arredondada para duas casas decimais) da matriz com melhor desempenho com base no cálculo dessas métricas.

- Entrada:	
3\
50,10,5,85\
20,5,8,67\
30,12,4,88	
- Saída:Índice: 1\
Acurácia: 0.9\
Precisão: 0.83