# Laboratório de Engenharia de Software I - Projeto

## Rodar backend - docker

Certifique-se que você está na branch `develop` para rodar a versão mais atualizada do projeto.

```console
lab_engsoft:~$ cd backend
lab_engsoft/backend:~$ sh scripts/build.sh
```

Os comandos acima rodam o backend em um container de docker chamado `lab_engsoft_backend`, que expoe a API Rest em FastAPI na porta 8080.

O container terá um volume compartilhado com a pasta `lab_engsoft/backend/` do projeto, então não deveria ser necessário recriar a imagem toda vez que fizer alguma alteração, basta salvar o arquivo no seu computador, e as mudanças deveriam ocorrer no container também.

## Acessar Documentação

Após rodar o container, é possível acessar a documentação automática da API no link http://localhost:8080/docs

## Debugging

Para ver mensagens de erro produzidas pela API ao realizar um request, você pode rodar o comando

```console
lab_engsoft:~$ docker logs lab_engsoft_backend
```

## Estrutura do projeto

O projeto está estruturado com Routers, Controllers e Services.

Os Routers servem apenas para definir os endpoints e validar os dados, e deixam a lógica para ser realizada pelos Controllers. Uma rota deve portanto apenas validar os dados e chamar seu método controlador correspondente.

Os Controllers funcionam como um padrão de faixada (facade), e interligam as funcionalidades dos diversos serviços para realizar a lógica necessária para o endpoint.

Os Serviços realizam realmente as funcionalidades, como chamadas para o banco de dados. Os serviços idealmente não devem chamar uns aos outros, para evitar impors circulares.

Um diagrama representando as chamadas de métodos pode ser observado abaixo:

![diagrama de vizualização dos routers, controllers e services](https://github.com/brunomariz/lab_engsoft/blob/develop/img/diagrama.png?raw=true)

## Rodar frontend

Certifique-se que você está na branch `develop` para rodar a versão mais atualizada do projeto.
Certifique-se que você tem Node instalado no seu computador.

```console
lab_engsoft:~$ cd frontend
lab_engsoft/backend:~$ npm install
lab_engsoft/backend:~$ npm run dev
```

Os comandos acima irão iniciar o projeto do front em um servidor, provavelmente no endereço http://localhost:3000, se não houver algo já rodando nessa porta. De qualquer forma, o terminal informará o endereço do servidor, que pode então ser acessado entrando na URL em seu browser.
