# PRD – Aplicativo Mobile de Registro de Faltas e Coberturas

## 1. Contexto do Produto

Aplicativo **mobile-first**, projetado para rodar em **celulares (Android e iOS)**, utilizado por supervisores operacionais para registrar faltas de colaboradores de forma rápida e padronizada.

O objetivo do app é **centralizar informações**, eliminar controles informais (papel, WhatsApp, planilhas manuais) e permitir geração automática de relatórios.

O tempo médio esperado para um registro completo é **inferior a 1 minuto**.

---

## 2. Perfis de Usuário

### Admin Geral (Acesso Master)

- Acesso total a todas as funcionalidades
- Cadastra, edita e desativa supervisores
- Cadastra e edita postos de trabalho
- Visualiza, edita e exclui todos os registros
- Exporta dados:
  - por supervisor
  - ou de forma consolidada (todos)

### Supervisor

- Acessa o app via celular
- Registra faltas e coberturas
- Visualiza apenas seus próprios registros
- Exporta apenas seus próprios dados

---

## 3. Autenticação

- Tela de login com email e senha
- Checkbox “Manter conectado”
  - Quando ativo, o usuário permanece logado ao reabrir o aplicativo

---

## 4. Fluxo Principal (Supervisor)

1. Abre o aplicativo no celular
2. Realiza login (ou entra automaticamente se “manter conectado” estiver ativo)
3. Inicia um novo registro de falta
4. Preenche os campos obrigatórios
5. Confirma o registro
6. Dados são salvos no banco

---

## 5. Registro de Falta

### Campos

1. Posto
   - Campo de busca com autocomplete
2. Data
   - Preenchida automaticamente com a data atual
   - Pode ser alterada para datas passadas ou futuras
3. Colaborador ausente
4. Colaborador que cobriu
5. Tipo de Ocorrência
   - Campo do tipo **ENUM**
   - Valores permitidos:
     - FALTA
     - ATESTADO
   - Seleção obrigatória
6. Horário de Cobertura
   - 07:00 às 19:00
   - 19:00 às 07:00
   - Horário personalizado (formato obrigatório: HH:mm às HH:mm)
7. Descrição da Falta
   - Campo de texto livre
   - Opcional
   - Limite máximo de **100 caracteres**

---

## 6. Persistência de Dados

- Todos os registros devem ser **salvos exclusivamente no banco de dados**
- Planilhas Excel são apenas relatórios/exportações
- O banco é a única fonte de verdade dos dados

---

## 7. Exportação (Excel)

### Regras Gerais

- Exportação gera arquivos `.xlsx`
- Registros sempre ordenados por **data crescente**
- Dados extraídos diretamente do banco

### Supervisor

- Pode exportar apenas seus próprios registros
- Gera uma planilha individual

### Admin Geral

- Pode exportar:
  - dados de um supervisor específico
  - ou dados consolidados de todos os supervisores

### Organização

- Cada supervisor possui sua própria planilha
- Todas as planilhas ficam organizadas em uma mesma pasta raiz

### Tipos de Exportação

- Automática mensal
- Manual, acionada pelo usuário no aplicativo

### Campos no Excel

- Data
- Posto
- Colaborador ausente
- Colaborador que cobriu
- Tipo de ocorrência (FALTA | ATESTADO)
- Horário de cobertura
- Descrição (até 100 caracteres)
- Supervisor responsável

---

## 8. Regras de Negócio

- Não permitir salvar registros com campos obrigatórios vazios
- Tipo de ocorrência é obrigatório e exclusivo (ENUM)
- Supervisor só acessa seus próprios dados
- Admin possui acesso total a todas as funcionalidades
- Descrição é opcional, mas sempre exportada
