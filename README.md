# grutec-api-auth
Repositório para a API de autenticação de usuários na plataforma Grutec - MPSP.

## Informações base:
Todos os endpoints, assim que finalizados serão adicionados aqui nesse README.md

## Progresso:
* Início do desenvolvimento da autenticação dos usuários:
  * Configuração do projeto - Sep 4, 2019.
    * **Dockerfile** (Arquivo reponsável pela criação da imagem docker) - OK
    * **Docker-compose** (Arquivo responsável por gerenciar a criação de containers docker) - OK
    * **Requirements.txt** (Arquivo responsável por armazenar todas as dependências utilizadas) - OK
    * **Endpoint de hello world** (Endpoint de teste da API) - OK

## Lista de Endpoints

### GET /v1
Retorna um objeto contendo uma mensagem de hello world. Este é apenas um endpoint de teste da aplicação.

```json
{
    "mensagem": "hello world"
}
```

### POST /v1/users
Endpoint responsável por registrar um usuário na plataforma. Objeto base para criação de usuário:

```json
{
    "username": "joaoanastacio",
	"password": "grutec",
	"name": "João Victor",
	"email": "joao@gmail.com"
}
```

### PUT /v1/users/id_do_usuario
Endpoint responsável por modificar as informações de um usuário na plataforma. Objeto base para modificação de usuário:

Baseado no usuário que foi criado acima:

```json
{
    "username": "joaoanastacio1",
	"password": "grutec1",
	"name": "João Victor",
	"email": "joao@gmail.com"
}
```

Ao executar, a senha e o username serão alterados. Lembrando que o ID do usuário se mantem o mesmo.

### GET /v1/users

Endpoint responsável por retornar todos os usuários cadastrados na plataforma.

Neste caso não é necessário passar nenhum objeto como parâmetro na requisição. Todas as informações cadastradas para todos os usuários serão retornadas.

### GET /v1/users/id_do_usuario

Endpoint responsável por retornar um usuário da plataforma a partir do ID do mesmo.

Neste caso não é necessário passar nenhum objeto como parâmetro na requisição. Todas as informações cadastradas para aquele usuário serão retornadas.

### DELETE /v1/users/id_do_usuario

Endpoint responsável por deletar um usuário da plataforma a partir do seu ID.

Neste caso não é necessário passar nenhum objeto como parâmetro na requisição. Todas as informações cadastradas para aquele usuário serão retornadas para que seja possível apresentar na tela as informações que foram deletadas.