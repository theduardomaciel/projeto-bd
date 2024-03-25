<h1 align="center">
    Projeto CRUD com Redis
</h1>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./.github/cover.png">
  <source media="(prefers-color-scheme: light)" srcset="./.github/cover_light.png">
  <img alt="Capa do Projeto CRUD com Redis" src="/.github/cover_light.png">
</picture>

## 💻 Projeto

Um aplicativo CRUD para gerenciamento de dados no Banco de Dados Redis, desenvolvido como projeto para a disciplina de Banco de Dados por estudantes do curso de Ciência da Computação.

<br />

## ✨ Tecnologias

| Backend |
| ------- |
| Redis   |

<br />

## 🧠 Princípios

1.  Implementar operações de **criação, leitura, atualização e exclusão** (**CRUD**) para gerenciamento de dados no Redis
2.  Documentar todas as operações e funções do banco de dados
3.  Garantir tratamento de erros e validação de dados para robustez
4.  Utilizar **Python** como linguagem principal

<br />

## 🔧 Configuração do Redis

Para a instalação do Redis compatível com o projeto, é possível tomar dois caminhos:

1. Instalação do Redis Stack (já vem com os pacotes utilizados pré-instalados)
2. É necessário instalar e conectar os pacotes necessários

### Redis Stack

1. Utilize o Redis Stack em seu sistema operacional seguindo a documentação oficial: https://redis.io/docs/install/install-stack/

   > Para dispositivos equipados com o sistema Linux, basta [baixar executar o AppImage disponível aqui](https://redis.io/download/#redis-stack-downloads)

2. Clone o repositório:

```bash
git clone https://github.com/theduardomaciel/projeto-bd.git
```

3. Navegue até a pasta do projeto

```bash
cd projeto-bd
```

#### Execução do servidor

- Agora, para executar o projeto, utilize o seguinte comando:
  ```bash
  redis-server
  ```

### Redis Padrão

1. Instale o Redis em seu sistema operacional seguindo a documentação oficial: https://redis.io/docs/install/install-redis/

2. Clone o repositório:

```bash
git clone https://github.com/theduardomaciel/projeto-bd.git
```

3. Navegue até a pasta do projeto

```bash
cd projeto-bd
```

4. Instale os pacotes necessários. Para esse projeto, utilizamos os pacotes RedisJSON e RediSearch, que podem ser instalados de diversas maneiras.  
   Em razão de problemas de compatibilidade com o sistema operacional utilizado pela equipe (Debian 12 Bookworm), foi necessário compilar o pacote da origem (source).  
   Para reproduzir o que fizemos, caso se encontre na mesma versão do sistema, você pode seguir os seguintes passos:

   > Caso seu sistema operacional não seja Linux, [siga a documentação oficial](https://redis.io/docs/data-types/json/#run-with-docker) para os passos de instalação.

   - [Instale a linguagem Rust](https://www.rust-lang.org/tools/install) em sua máquina
   - [Instale a linguagem Lua](https://www.lua.org/download.html) em sua máquina
   - Crie uma pasta `\packages` dentro do repositório local do projeto

   #### RedisJSON

   - Clone o [repositório do RedisJSON](https://github.com/RedisJSON/RedisJSON) nela (certifique-se de incluir a opção `--recursive` para clonar os submódulos corretamente):

     ```bash
     mkdir packages
     cd packages
     ```

     ```bash
     git clone --recursive https://github.com/RedisJSON/RedisJSON.git
     cd RedisJSON
     ```

   - Instale as dependências do RedisJSON:

     ```sh
     ./sbin/setup
     ```

   - Construa o pacote:

     ```sh
     make build
     ```

   #### RediSearch

   - Para o Debian, instale o RediSearch por meio de `sudo apt install redis-redisearch`

   #### Execução do servidor

   - Agora, para executar o projeto, utilize o seguinte comando:

     ```bash
     redis-server --loadmodule packages/RedisJSON/bin/linux-x64-release/target/release/librejson.so --loadmodule /usr/lib/redis/modules/redisearch.so
     ```

<br />

## 🧰 Configuração do Python

> [!IMPORTANT]
> Caso o Python não esteja instalado em sua máquina, você pode baixá-lo [neste link](https://www.python.org/downloads/).

Para a configuração do projeto em Python, recomenda-se a criação de um ambiente virtual Python (venv) para o projeto (obrigatório em dispositivos Linux)

> Caso não seja de seu interesse, ignore os passos 1 e 2.

1. Crie um ambiente virtual usando o comando:

```bash
python3 -m venv [nome do ambiente de desenvolvimento]
```

2. Ative o ambiente virtual:

- No Linux:
  ```
  source [nome do ambiente de desenvolvimento]/bin/activate
  ```
- No Windows (PowerShell):
  ```
  .\venv\Scripts\Activate.ps1
  ```

3. Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

> [!NOTE]
> Caso uma nova dependência passe a ser utilizada ao projeto, utilize `pip freeze > requirements.txt` para adicioná-la ao arquivo `requirements.txt`.

<br />

## 🚀 Execução

Para executar o projeto, siga os passos abaixo:

1. Certifique-se de estar com o ambiente virtual ativado

2. Caso ainda não esteja, navegue até a pasta do projeto

3. Inicie o servidor Redis:

#### Redis Stack

1. Caso o arquivo `AppImage` do RedisStack esteja presente em `\packages`, por exemplo, acesse a pasta e o execute

   ```bash
   cd packages/
   ```

   ```bash
   ./redis-stack-server-7.2.0-v9-x86_64.appimage
   ```

2. Execute o arquivo principal do projeto:

   ```bash
   python3 main.py # ou python main.py, dependendo de sua versão do Python
   ```

#### Somente Redis

1. Caso não esteja fazendo uso do RedisStack, inicie o servidor com os módulos necessários

   ```bash
   redis-server --loadmodule packages/RedisJSON/bin/linux-x64-release/target/release/librejson.so --loadmodule /usr/lib/redis/modules/redisearch.so
   ```

2. Execute o arquivo principal do projeto:

   ```bash
   python3 main.py # ou python main.py, dependendo de sua versão do Python
   ```

<br />

## 🔗 Links úteis

#### Datasets

- [Dataset utilizado - Mudanças de temperatura globais entre 1961-2022](https://www.kaggle.com/datasets/princeiornongu/merged-cc)

  > [!NOTE]
  > Para acessar o Dataset sem ter passado por um processo de normalização, acesse: https://www.fao.org/faostat/en/#data/ET

- [Recomendação de jogos no Steam](https://www.kaggle.com/datasets/antonkozyriev/game-recommendations-on-steam)
- [Engajamento global em notícias ao redor do mundo](https://www.kaggle.com/datasets/kanchana1990/global-news-engagement-on-social-media)

> Como os _scripts_ de conversão do projeto foram escritos de forma dinâmica, basta alterar os valores no arquivo `config.ini` e realizar as adaptações necessárias em `main.py`.

#### Documentação

- [Documentação oficial do Redis para Python](https://redis.io/docs/connect/clients/python/)
- [Documentação do Redis](https://redis.io/documentation)

#### Instalação do Redis em sistemas Linux

- [Instalação do Redis a partir do código fonte](https://redis.io/docs/install/install-redis/install-redis-from-source/)

<br />

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](./LICENSE) para obter mais detalhes.
