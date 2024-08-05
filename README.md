<div align="center">
  <h2 align="center">Whatask</h2>

  <p align="center">
    Gerenciador de tarefa para a sua rotina!
  </p>
</div>

### Tecnologias

Dentro das tecnologias sugeridas este projeto utiliza Click para CLI e PostegreSQL para banco de dados

### Setando o ambiente

```bash
$ git clone https://github.com/peterhttps/Whatask # Clonando o repositório
$ cd Whatask
```

Crie um arquivo .env na raiz do projeto e copie para ele o conteúdo de .env.example

```bash
$ python -m venv venv
$ source venv/bin/activate  # No Windows use `venv\Scripts\activate`
$ pip install -r requirements.txt
$ docker-compose build
$ docker-compose up
```

### Tests

Para testar a aplicação

```bash
$ pytest
```