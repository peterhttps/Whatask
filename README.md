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

### Comandos

```bash
- add TITLE --description DESCRIPTION   Add a new task with a title and optional description.
- delete TASK_ID                        Delete a task by its ID.
- list                                  List all incomplete tasks.
- list --completed                      List all tasks or only completed tasks.
- complete TASK_ID                      Mark a task as completed.
- update TASK_ID --title TITLE --description DESCRIPTION  Update an existing task's title and description.
```

Para mais informações

```bash
$ python -m app.cli help
```

### Testes

Para executar os testes unitários

```bash
$ pytest
```