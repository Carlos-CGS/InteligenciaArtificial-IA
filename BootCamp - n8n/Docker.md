# Consulte também:

- [Instalação via Terminal (Node.js)](./Terminal.md)

# Passo a Passo para Instalar e Usar o n8n com Docker

## 1. Pré-requisitos

- Ter o Docker instalado em sua máquina.
- Recomenda-se criar uma conta gratuita no Docker Hub: https://hub.docker.com/

## 2. Baixar a Imagem do n8n

Abra o terminal e execute:

```sh
docker pull n8nio/n8n
```

## 3. Rodar o n8n com Docker

Execute o comando abaixo para iniciar o n8n rapidamente:

```sh
docker run -it --rm \
  -p 5678:5678 \
  n8nio/n8n
```

- O parâmetro `-p 5678:5678` expõe a porta padrão do n8n.
- Acesse a interface web em: http://localhost:5678

## 4. Executar em Segundo Plano (Modo Detach)

Se quiser rodar o n8n em segundo plano:

```sh
docker run -d --name n8n \
  -p 5678:5678 \
  n8nio/n8n
```

- Para parar o container:
  ```sh
  docker stop n8n
  ```
- Para remover o container:
  ```sh
  docker rm n8n
  ```

## 5. Persistindo Dados

Para não perder seus fluxos ao reiniciar o container, crie um volume:

```sh
docker run -d --name n8n \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n
```

- Isso garante que os dados do n8n fiquem salvos na sua máquina.

## 6. Dicas

- Consulte a documentação oficial para configurações avançadas: https://docs.n8n.io/hosting/docker/
- Você pode definir variáveis de ambiente para customizar o comportamento do n8n.
