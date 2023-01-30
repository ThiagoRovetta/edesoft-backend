# Edesoft Backend

===============

## Instruções para configurar

Atenção: crie todos os serviços na mesma região da AWS.

### S3

- No console https://s3.console.aws.amazon.com/ do S3, crie um bucket:
  - Insira o nome do bucket e anote-o.
  - Clique em Criar bucket.
  - Dento do bucket que você criou, clique em carregar.
  - Adicione um arquivo .csv contendo os cabeçalhos cpf, cnpj e data, seguindo o arquivo dados.csv deste repositório.
  - Clique em carregar.
  
### Banco de dados

- No console https://console.aws.amazon.com/rds do RDS, crie um banco de dados:
  - selecione Criação padrão;
  - selecione PostgreSQL;
  - selecione o modelo do Nível gratuito;
  - selecione instância de banco de dados única;
  - escolhe o nome do usuário principal (postgres como padrão), e anote-o;
  - adicione uma senha principal, e anote-a;
  - selecione a opção Classes com capacidade de intermitência e selecione a opção db.t3.micro;
  - permita o acesso público;
  - em Configuração adicional, insira o nome do banco de dados inicial, e anote-o;
  - e clique em Criar banco de dados;

- Após finalizado a criação do banco, entre, pelo console, na instância que você acabou de criar.
- Na seção de Segurança e conexão, anote o Endpoint da instância e a Porta (por padrão, 5432).

### Lambda

- No console https://console.aws.amazon.com/lambda do lambda, crie uma função com Python 3.9 no tempo de execução.

- Após criada, entre na função e crie um gatilho para invocá-la:
  - selecione API Gateway como origem;
  - cria uma nova API;
  - escolha uma API do tipo REST API;
  - em segurança, selecione API key;
  - e clique em adicionar.

- Clique no gatilho criado e anote o *API endpoint* e a *API key*.
- Clique na função e vá para a seção de Configuração e vá em Variáveis de ambiente.
- Adicione as seguintes variáveis de ambiente:
    - AWS_DB_HOST	-> é o endpoint da instância do banco de dados
    - AWS_DB_NAME	-> é o nome do banco de dados inicial
    - AWS_DB_PASSWORD	-> é a senha principal do usuário principal do banco de dados
    - AWS_DB_PORT	-> é a porta da instância do banco de dados
    - AWS_DB_USER	-> é o usuário principal do banco de dados
    - USER_ACCESS_KEY	-> é a AWS access key id de um usuário criado na sua conta da AWS
    - USER_SECRET_ACCESS_KEY -> é a AWS secret access key de um usuário criado na sua conta da AWS

- Clone o projeto no github, e em seguida crie um arquivo .zip contendo a pasta app, a pasta psycopg2 e o arquivo lambda_function.py.
- Em seguida, no console da sua função lambda, na seção Código, clique em Fazer upload de arquivo .zip, e insira o arquivo que você acabou de criar.
- Por fim, clique em salvar.

### Testando

Para testar a função, realize uma requisição get para o API Endpoint do gatilho da lambda, passando um header com a API key do gatilho:

```bash
x-api-key: {API key}
```

E passando como queryStrings, o nome do bucket criado e nome do arquivo .csv (inclua a extensão no nome):

```url
?bucket_name={nome do bucket criado}&object_key={nome do arquivo csv}
```
