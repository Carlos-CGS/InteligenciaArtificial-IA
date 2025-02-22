# Desafio de Projeto - DIO

# 📦 Modelo Conceitual de Banco de Dados para E-commerce

## 📌 Visão Geral

Este modelo conceitual representa a estrutura de um banco de dados para um sistema de e-commerce. Ele abrange informações essenciais, como cadastro de clientes (Pessoa Física e Jurídica), produtos, pedidos, pagamentos e entregas.

---

## 🏗 Estrutura do Modelo

### Usuário (usuario)

Representa os clientes da plataforma. Um usuário pode ser uma **Pessoa Física (PF)** ou **Pessoa Jurídica (PJ)**, mas nunca ambos.

| Campo      | Tipo         | Descrição                      |
| ---------- | ------------ | ------------------------------ |
| id_usuario | INT (PK)     | Identificador único do usuário |
| nome       | VARCHAR(255) | Nome do cliente                |
| email      | VARCHAR(255) | Email único para login         |
| senha      | VARCHAR(255) | Senha criptografada            |
| tipo       | ENUM(PF, PJ) | Define se o usuário é PF ou PJ |

---

### 🏢 Pessoa Jurídica (pessoa_juridica)

Caso o usuário seja um CNPJ, seus dados são armazenados nesta tabela.

| Campo        | Tipo         | Descrição                            |
| ------------ | ------------ | ------------------------------------ |
| id_usuario   | INT (FK)     | Chave estrangeira para `usuario`     |
| cnpj         | VARCHAR(14)  | Cadastro Nacional da Pessoa Jurídica |
| razao_social | VARCHAR(255) | Nome registrado da empresa           |

---

### 🧑 Pessoa Física (pessoa_fisica)

Caso o usuário seja um CPF, seus dados são armazenados aqui.

| Campo      | Tipo        | Descrição                        |
| ---------- | ----------- | -------------------------------- |
| id_usuario | INT (FK)    | Chave estrangeira para `usuario` |
| cpf        | VARCHAR(11) | Cadastro de Pessoa Física        |

---

### 🛒 Produto (produto)

Lista os produtos disponíveis na plataforma.

| Campo      | Tipo          | Descrição                      |
| ---------- | ------------- | ------------------------------ |
| id_produto | INT (PK)      | Identificador único do produto |
| nome       | VARCHAR(255)  | Nome do produto                |
| descricao  | TEXT          | Descrição detalhada            |
| preco      | DECIMAL(10,2) | Preço do produto               |
| estoque    | INT           | Quantidade disponível          |
| categoria  | VARCHAR(100)  | Categoria do produto           |

---

### 📦 Pedido (pedido)

Registra os pedidos realizados pelos usuários.

| Campo       | Tipo                                                     | Descrição                     |
| ----------- | -------------------------------------------------------- | ----------------------------- |
| id_pedido   | INT (PK)                                                 | Identificador único do pedido |
| id_usuario  | INT (FK)                                                 | Cliente que realizou o pedido |
| data_pedido | DATETIME                                                 | Data e hora do pedido         |
| status      | ENUM('Em andamento', 'Enviado', 'Entregue', 'Cancelado') | Status do pedido              |

---

### 📜 Itens do Pedido (item_pedido)

Relaciona produtos a pedidos, permitindo múltiplos itens em um único pedido.

| Campo          | Tipo          | Descrição                             |
| -------------- | ------------- | ------------------------------------- |
| id_item        | INT (PK)      | Identificador único do item           |
| id_pedido      | INT (FK)      | Chave estrangeira para `pedido`       |
| id_produto     | INT (FK)      | Chave estrangeira para `produto`      |
| quantidade     | INT           | Quantidade do produto no pedido       |
| preco_unitario | DECIMAL(10,2) | Preço do produto no momento da compra |

---

### 💳 Pagamento (pagamento)

Registra as formas de pagamento associadas ao usuário.

| Campo        | Tipo                                       | Descrição                            |
| ------------ | ------------------------------------------ | ------------------------------------ |
| id_pagamento | INT (PK)                                   | Identificador único do pagamento     |
| id_usuario   | INT (FK)                                   | Chave estrangeira para `usuario`     |
| tipo         | ENUM('Cartão de Crédito', 'Boleto', 'Pix') | Tipo de pagamento                    |
| dados        | TEXT                                       | Informações encriptadas do pagamento |

---

### 🚚 Entrega (entrega)

Gerencia o status da entrega dos pedidos.

| Campo           | Tipo                                                          | Descrição                                |
| --------------- | ------------------------------------------------------------- | ---------------------------------------- |
| id_entrega      | INT (PK)                                                      | Identificador único da entrega           |
| id_pedido       | INT (FK)                                                      | Pedido associado à entrega               |
| status          | ENUM('Em separação', 'Despachado', 'Em trânsito', 'Entregue') | Status da entrega                        |
| codigo_rastreio | VARCHAR(50)                                                   | Código de rastreamento da transportadora |

---

## 🔗 Relacionamentos

1. **Usuário** pode ser **Pessoa Física (PF)** ou **Pessoa Jurídica (PJ)**, mas não ambos.
2. **Usuário** pode realizar **múltiplos pedidos**.
3. **Pedido** pode conter **vários produtos** através da tabela **item_pedido**.
4. **Usuário** pode ter **múltiplos métodos de pagamento**.
5. **Cada pedido** está associado a uma **entrega** com status e código de rastreio.

---

Este modelo fornece uma base sólida para um e-commerce funcional, garantindo separação clara de responsabilidades e escalabilidade.
