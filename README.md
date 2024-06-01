
# CRUD Flask

Aplicação com funcionalidade básica das operações:

 - Create
 Operação para criar objetos no banco da dados

  - Read
Operação de visualização dos dados cadastrados no banco de dados

 - Update
Operação de atualização ou edição de objetos no banco de dados

 - Delete
Operação de exclusão do objeto no banco de dados

#### Paginação
 - Recurso adicionado para aplicar paginação na home


## Executando localmente

Clone o projeto

```bash
  https://github.com/IgorStrauss/crud_flask.git
```
---
Entre no diretório do projeto

```bash
  cd crud_flask
```
---
Criar ambiente virtual
 - Poetry
 ```bash
  poetry shell
```

ou


 ```bash
  python3 -m venv venv
```
---

Instale as dependências
 - Poetry
```bash
  poetry install
```
ou

 - pip
```bash
  pip install -r requirements.txt
```

---
Inicie o servidor

 - Makefile
```bash
  make start
```

Com este comando Makefile, será instânciado ambiente de desenvolvimento,
inicializado instância para o banco de dados SQLite, migração das tabelas, e
inicializado servidor.

### Url Home

```bash
 127.0.0.1:5000
```
