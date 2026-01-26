# Consulte também:

- [Instalação via Docker](./Docker.md)

# Passo a Passo para Instalar o n8n via Terminal

## 1. Instalar o Node.js

O n8n requer o Node.js (recomenda-se a versão LTS). Siga os passos abaixo:

### Windows

1. Acesse o site oficial: https://nodejs.org/
2. Baixe o instalador da versão LTS.
3. Execute o instalador e siga as instruções.
4. Após a instalação, abra o terminal (PowerShell ou Prompt de Comando) e verifique:
   ```sh
   node -v
   npm -v
   ```
   Ambos devem exibir as versões instaladas.

## 2. Instalar o n8n Globalmente

No terminal, execute:

```sh
npm install n8n -g
```

## 3. Executar o n8n

Após a instalação, basta rodar:

```sh
n8n
```

O n8n será iniciado e exibirá um endereço local (geralmente http://localhost:5678) para acessar a interface web.

## 4. Dicas

- Para interromper o n8n, pressione `Ctrl + C` no terminal.
- Para rodar o n8n em segundo plano, utilize ferramentas como PM2 ou Docker (opcional).

---
