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

#### 🧭 Inicialmente Disponível para Terminal

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

## 🔧 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/theduardomaciel/projeto-bd.git
```

2. Navegue até a pasta do projeto

```bash
cd projeto-bd
```

> 🧰 Recomenda-se a criação de um ambiente virtual Python (venv) para o projeto. Caso não seja de seu interesse, ignore os passos 3 e 4.

3. Crie um ambiente virtual usando o comando:

```bash
python3 -m venv [nome do ambiente de desenvolvimento]
```

4. Ative o ambiente virtual:

- No Linux:
  ```
  source [nome do ambiente de desenvolvimento]/bin/activate
  ```
- No Windows (PowerShell):
  ```
  .\venv\Scripts\Activate.ps1
  ```

5. Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

> [!NOTE]
> Caso uma dependência seja adicionada ao projeto, utilize `pip freeze > requirements.txt` para adicioná-la ao arquivo `requirements.txt`.

## 🚀 Execução

Para executar o projeto, siga os passos abaixo:

1. Certifique-se de estar com o ambiente virtual ativado
2. Caso ainda não esteja, navegue até a pasta do projeto
3. Execute o arquivo principal do projeto:

```
python main.py
```

ou

```
python3 main.py
```

<br />

## 🔗 Links úteis

#### Documentação

- [Documentação oficial do Redis para Python](https://redis.io/docs/connect/clients/python/)
- [Documentação do Redis](https://redis.io/documentation)

#### Instalação do Redis em sistemas Linux

- [Instalação do Redis a partir do código fonte](https://redis.io/docs/install/install-redis/install-redis-from-source/)

<br />

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](./LICENSE) para obter mais detalhes.

---

Feito com ❤️
