# 📱 Aplicativo Mobile de Registro de Faltas e Coberturas

Projeto desenvolvido como **Desafio de Projeto 01** do bootcamp  
**CAIXA – Inteligência Artificial na Prática**, da **DIO (Digital Innovation One)**.

---

## 📌 Descrição do Projeto

Este projeto consiste em um **aplicativo mobile-first** voltado para a **supervisão operacional**, permitindo o registro rápido e centralizado de faltas de colaboradores e suas respectivas coberturas.

O desafio segue a abordagem **Vibe Coding**, onde o foco está no **uso de Inteligência Artificial como acelerador de desenvolvimento**, explorando ferramentas como **GitHub Copilot** e **Lovable**, sem a necessidade de escrever código manualmente.

---

## 🎯 Objetivos do Desafio

- Aplicar o conceito de **Vibe Coding**
- Aprender a utilizar o **GitHub Copilot** para estruturar ideias e requisitos
- Utilizar o **Lovable** para criar uma aplicação completa **sem escrever uma única linha de código**
- Traduzir um problema real em um PRD claro e funcional
- Centralizar informações operacionais de forma simples e eficiente

---

## 👥 Perfis de Usuário

### 🔑 Admin Geral (Acesso Master)

- Cadastra e gerencia supervisores
- Cadastra postos de trabalho
- Visualiza, edita e exclui todos os registros
- Exporta dados por supervisor ou de forma consolidada

### 👷 Supervisor

- Acessa o app pelo celular
- Registra faltas e coberturas
- Visualiza apenas seus próprios registros
- Exporta apenas seus próprios dados

---

## 🔐 Autenticação

- Login com email e senha
- Opção **“Manter conectado”** para persistência de sessão no celular

---

## 📝 Funcionalidades Principais

- Registro de faltas com:
  - Posto de trabalho (busca por nome)
  - Data (automática, editável)
  - Colaborador ausente
  - Colaborador que cobriu
  - Tipo de ocorrência (**ENUM: FALTA | ATESTADO**)
  - Horário fixo ou personalizado
  - Descrição opcional (até 100 caracteres)
- Persistência de dados em banco
- Exportação automática ou manual para Excel
- Organização de relatórios por supervisor

---

## 📊 Exportação de Relatórios (Excel)

- Geração de arquivos `.xlsx`
- Ordenação crescente por data
- Planilhas separadas por supervisor
- Pasta raiz única para organização

### Campos do Relatório

- Data
- Posto
- Colaborador ausente
- Colaborador que cobriu
- Tipo de ocorrência (FALTA | ATESTADO)
- Horário de cobertura
- Descrição
- Supervisor responsável

---

## 🧠 Regras de Negócio

- Banco de dados é a única fonte de verdade
- Excel é apenas relatório/exportação
- Campos obrigatórios devem ser validados
- Supervisor não acessa dados de outros supervisores
- Admin possui acesso total a todas as funcionalidades

---

## 🧠 Metodologia – Vibe Coding

Este desafio adota a metodologia **Vibe Coding**, onde o desenvolvedor:

- Define claramente o problema e as regras de negócio
- Utiliza **IA generativa** para estruturar o produto
- Usa ferramentas como **Copilot** para refinar requisitos
- Usa o **Lovable** para gerar a aplicação completa
- Foca em **decisão, validação e produto**, não em sintaxe

O objetivo é demonstrar que, com um bom entendimento do domínio, é possível criar soluções reais **sem escrever código manualmente**.

---

## 🚀 Tecnologias / Ferramentas

- GitHub Copilot
- Lovable
- PRD (Product Requirements Document)
- Conceitos de:
  - Mobile-first
  - Controle de acesso
  - Modelagem de domínio
  - Automação de relatórios

---

## 🎓 Bootcamp

**CAIXA – Inteligência Artificial na Prática**  
Plataforma: **DIO**

Este projeto faz parte da trilha prática do bootcamp e demonstra o uso de **IA como ferramenta central no processo de desenvolvimento de software**.

---

## 📎 Observações Finais

Este projeto foi pensado para uso real em ambientes operacionais e serve como prova de conceito do uso de **IA para criar aplicações completas sem codificação manual**.

Evoluções futuras podem incluir:

- Dashboards gerenciais
- Indicadores operacionais
- Integrações com sistemas de RH
- Análises inteligentes com IA

<img src=./02.png>
<img src=./01.png>
