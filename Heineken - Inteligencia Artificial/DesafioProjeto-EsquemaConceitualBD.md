# Desafio Projeto

# Construindo um Esquema Conceitual para Banco De dados - DIO

### Descrição do Projeto

Este projeto tem como objetivo criar um esquema conceitual para um sistema de controle e gerenciamento de execução de ordens de serviço em uma oficina mecânica. O sistema permitirá o registro de clientes, veículos, mecânicos e serviços prestados, garantindo um fluxo organizado para o atendimento e execução das ordens de serviço (OS).

### Entidades e Relacionamentos

#### 1. Cliente

**Atributos:**

- ID_Cliente (PK)
- Nome
- Endereço
- Telefone
- Email

#### 2. Veículo

**Atributos:**

- ID_Veiculo (PK)
- Placa
- Modelo
- Ano
- Marca
- ID_Cliente (FK)

**Relacionamento:**

Um cliente pode possuir vários veículos, mas um veículo pertence a um único cliente.

#### 3. Mecânico

**Atributos:**

- ID_Mecanico (PK)
- Nome
- Endereço
- Especialidade

**Relacionamento:**

Um mecânico pode fazer parte de várias equipes e atender diferentes OS.

#### 4. Equipe

**Atributos:**

- ID_Equipe (PK)
- Nome da Equipe

**Relacionamento:**

Uma equipe é composta por vários mecânicos, e um mecânico pode pertencer a mais de uma equipe.

Uma equipe pode estar envolvida em várias ordens de serviço.

#### 5. Ordem de Serviço (OS)

**Atributos:**

- ID_OS (PK)
- Numero_OS
- Data_Emissao
- Valor_Total
- Status
- Data_Conclusao
- ID_Equipe (FK)
- ID_Veiculo (FK)

**Relacionamento:**

Cada ordem de serviço está relacionada a um único veículo e a uma equipe responsável.

Um veículo pode ter várias OS ao longo do tempo.

Uma equipe pode ser responsável por várias OS.

#### 6. Serviço

**Atributos:**

- ID_Servico (PK)
- Descrição
- Valor_Mao_Obra (baseado em tabela de referência)

**Relacionamento:**

Uma OS pode conter vários serviços.

Um serviço pode estar presente em diferentes OS.

#### 7. Peça

**Atributos:**

- ID_Peca (PK)
- Nome
- Valor

**Relacionamento:**

Uma OS pode conter várias peças.

Uma peça pode ser utilizada em diferentes OS.

#### 8. OS_Serviço

**Atributos:**

- ID_OS (PK, FK)
- ID_Servico (PK, FK)
- Quantidade
- Valor_Total

**Relacionamento:**

Relação entre Ordem de Serviço e Serviço, contendo detalhes sobre a quantidade e o valor total do serviço prestado.

#### 9. OS_Peça

**Atributos:**

- ID_OS (PK, FK)
- ID_Peca (PK, FK)
- Quantidade
- Valor_Total

**Relacionamento:**

Relação entre Ordem de Serviço e Peça, registrando a quantidade de peças utilizadas e o custo total.

```mermaid
Diagrama Entidade Relacionamento

    CLIENTE {
        int ID_Cliente PK
        string Nome
        string Endereço
        string Telefone
        string Email
    }
    VEICULO {
        int ID_Veiculo PK
        string Placa
        string Modelo
        int Ano
        string Marca
        int ID_Cliente FK
    }
    MECANICO {
        int ID_Mecanico PK
        string Nome
        string Endereço
        string Especialidade
    }
    EQUIPE {
        int ID_Equipe PK
        string Nome_da_Equipe
    }
    ORDEM_DE_SERVICO {
        int ID_OS PK
        string Numero_OS
        date Data_Emissao
        float Valor_Total
        string Status
        date Data_Conclusao
        int ID_Equipe FK
        int ID_Veiculo FK
    }
    SERVICO {
        int ID_Servico PK
        string Descrição
        float Valor_Mao_Obra
    }
    PECA {
        int ID_Peca PK
        string Nome
        float Valor
    }
    OS_SERVICO {
        int ID_OS PK, FK
        int ID_Servico PK, FK
        int Quantidade
        float Valor_Total
    }
    OS_PECA {
        int ID_OS PK, FK
        int ID_Peca PK, FK
        int Quantidade
        float Valor_Total
    }
```
