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
	"name": "João Victor Anastácio",
	"email": "joaoanastacio@gmail.com"
}
```