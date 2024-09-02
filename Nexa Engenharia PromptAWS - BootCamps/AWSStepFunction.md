# Criando um Assistente de Delivery com AWS Step Functions e Bedrock - DIO

AWS Step Functions é um serviço da Amazon Web Services (AWS) que permite a criação de fluxos de trabalho automatizados e orquestrados para aplicações distribuídas e serverless. Ele ajuda a coordenar múltiplos serviços AWS em uma sequência definida, formando um fluxo de trabalho conhecido como **state machine** (máquina de estados).
(Como um carteiro / executando um serviço de mensageria).

## Principais Conceitos

- **State Machine**: Representa o fluxo de trabalho, onde cada passo é um estado. A máquina de estados define como os estados individuais se conectam e as transições entre eles.
- **State**: Cada estado é um passo no fluxo de trabalho, podendo realizar uma tarefa, tomar decisões, esperar, capturar erros, entre outras ações.
- **Task**: Uma tarefa que realiza algum trabalho, como executar uma função Lambda, chamar um serviço AWS, ou até mesmo esperar um determinado período.

## Benefícios

- **Orquestração**: Coordena automaticamente os componentes de uma aplicação, garantindo que tudo aconteça na ordem correta.
- **Escalabilidade**: Suporta desde pequenos fluxos de trabalho até sistemas complexos e distribuídos.
- **Monitoramento e Debug**: Oferece visualização em tempo real do fluxo de trabalho, facilitando o monitoramento e a resolução de problemas.

## Exemplo de Uso

Como exemplo de uso do AWS Step Functions, suponhamos que voce precisa orquestrar um processo de aprovação de pedido, onde cada estado representa uma etapa do processo, como validação de inventário, cobrança, e notificação ao cliente.

```json
{
  "Comment": "Exemplo de fluxo de trabalho Hello World no AWS Step Functions",
  "StartAt": "HelloWorld",
  "States": {
    "HelloWorld": {
      "Type": "Pass",
      "Result": "Hello, World!",
      "End": true
    }
  }
}
