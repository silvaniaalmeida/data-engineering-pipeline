# Data Engineering Pipeline

Pipeline ETL (Extract, Transform, Load) desenvolvido em Python
para processamento de dados de projetos de engenharia,
com foco em indicadores de desempenho financeiro.

O projeto demonstra práticas de Engenharia de Dados,
versionamento com Git, testes automatizados e
Integração Contínua (CI) com GitHub Actions.

## 1. Objetivo

Desenvolver um pipeline capaz de:

- Extrair dados de projetos a partir de arquivos CSV.
- Transformar e padronizar os dados.
- Calcular indicadores de desempenho orçamentário.
- Gravar os resultados em um novo arquivo CSV.
- Persistir os dados transformados em PostgreSQL.
- Evitar duplicações por meio de operações UPSERT.
- Validar as funcionalidades com testes automatizados.


## 2. Arquitetura

O pipeline segue a arquitetura ETL:

CSV de entrada (data/projects.csv)
             |
             v
Extract (src/extract.py)
             |
             v
Transform (src/transform.py)
             |
             v
      Dados transformados
             |
       +-----+------+
       |            |
       v            v
Load CSV       Load PostgreSQL
(src/load.py)  (src/load_postgres.py)
       |            |
       v            v
CSV processado  Tabela projects
                (PostgreSQL)


A execução completa é coordenada pelo módulo
`src/pipeline.py`.

## 3. Tecnologias utilizadas

- Python 3.12
- Biblioteca csv
- Biblioteca decimal
- pathlib
- unittest
- PostgreSQL 17
- SQL
- Psycopg 3 (conexão Python com PostgreSQL)
- Docker e Docker Compose
- Git e GitHub
- GitHub Actions (Integração Contínua)

Tecnologias previstas para futuras evoluções:

- Pandas
- Apache Spark
- Databricks

## 4. Estrutura do projeto

data-engineering-pipeline/
|
|-- .github/
|   |-- workflows/
|       |-- ci.yml
|
|-- data/
|   |-- projects.csv
|   |-- processed/
|
|-- sql/
|   |-- create_projects_table.sql
|
|-- src/
|   |-- database.py
|   |-- extract.py
|   |-- transform.py
|   |-- load.py
|   |-- load_postgres.py
|   |-- pipeline.py
|
|-- tests/
|   |-- test_extract.py
|   |-- test_transform.py
|   |-- test_load.py
|   |-- test_load_postgres.py
|
|-- compose.yaml
|-- requirements.txt
|-- .gitignore
|-- README.md

A pasta `data/processed/` contém arquivos gerados
pelo pipeline e está configurada no `.gitignore`.

## 5. Indicadores calculados

O módulo Transform calcula os seguintes indicadores:

### Desvio orçamentário

budget_variance = actual_cost - budget

### Desvio percentual

variance_pct = (budget_variance / budget) * 100

O resultado é arredondado para duas casas decimais.

Quando o orçamento é zero, o desvio percentual
recebe o valor `None`, evitando divisão por zero.

### Indicador de estouro de orçamento

over_budget = actual_cost > budget

Esse indicador retorna `True` quando o custo
realizado ultrapassa o orçamento.

## 6. Como executar o pipeline

### Pré-requisitos

- Python 3.12
- Docker e Docker Compose
- Dependências Python instaladas

### Configurar o PostgreSQL

O banco PostgreSQL é executado em um contêiner Docker,
conforme a configuração do arquivo `compose.yaml`.

Crie um arquivo `.env` na raiz do projeto contendo:

POSTGRES_PASSWORD=sua_senha_local

O arquivo `.env` está incluído no `.gitignore` e não
deve ser enviado ao GitHub.

Instale as dependências Python:

    python -m pip install -r requirements.txt

Inicie o PostgreSQL:

    docker compose up -d

Crie a tabela `projects` no banco de dados:

    docker compose exec -T postgres psql -U etl_user -d engineering_db < sql/create_projects_table.sql

Antes de executar o pipeline, disponibilize a variável
de ambiente `POSTGRES_PASSWORD` no Terminal:

    set -a; source .env; set +a

### Executar o pipeline ETL

Após configurar o PostgreSQL e criar a tabela `projects`,
execute o pipeline na raiz do projeto:

    python -m src.pipeline

O pipeline realiza as etapas:

1. Extract: extrai os dados do arquivo CSV.
2. Transform: calcula os indicadores financeiros.
3. Load CSV: grava os dados transformados em CSV.
4. Load PostgreSQL: insere ou atualiza os projetos no banco.

Os resultados são armazenados em dois destinos:

**Arquivo CSV:**

    data/processed/projects_transformed.csv

**Banco de dados PostgreSQL:**

    engineering_db
    Tabela: projects

O carregamento no PostgreSQL utiliza UPSERT para atualizar
projetos existentes sem criar registros duplicados.

## 7. Testes automatizados

O projeto utiliza a biblioteca `unittest` do Python.

Para executar todos os testes:

    python -m unittest discover -s tests -p "test_*.py" -v

Atualmente, existem sete testes unitários:

- 1 teste de extração.
- 2 testes de transformação.
- 2 testes de carregamento em CSV.
- 2 testes de carregamento em PostgreSQL.

Os testes validam:

- Extração e processamento dos dados.
- Cálculos dos indicadores financeiros.
- Tratamento de orçamento zero.
- Gravação dos resultados em CSV.
- Tratamento de listas vazias.
- Execução da carga PostgreSQL utilizando mocks.
- Utilização de UPSERT para evitar duplicações.

Os testes PostgreSQL utilizam mocks para simular
a conexão com o banco, permitindo sua execução
sem um PostgreSQL ativo.

## 8. Integração Contínua

O projeto utiliza GitHub Actions para executar
automaticamente os testes unitários.

O workflow está definido em:

    .github/workflows/ci.yml

A automação é acionada em:

- Pull Requests direcionados à branch main.
- Pushes realizados na branch main.

Os testes são executados em ambiente Ubuntu
com Python 3.12.

Antes da execução dos testes, o GitHub Actions
instala automaticamente as dependências definidas
no arquivo `requirements.txt`.

O workflow executa as seguintes etapas:

1. Checkout do código-fonte.
2. Configuração do Python 3.12.
3. Instalação das dependências Python.
4. Execução dos testes automatizados com unittest.

Os testes PostgreSQL utilizam mocks e não exigem
um banco de dados ativo durante a execução do CI.

## 9. Próximas evoluções

- Adicionar validações de qualidade dos dados.
- Implementar logging estruturado.
- Criar testes de integração com PostgreSQL.
- Parametrizar as configurações de conexão com o banco.
- Expandir os indicadores de projetos.
- Implementar transformações com Pandas.
- Explorar processamento distribuído com Apache Spark.
- Avaliar integração com Databricks.

## 10. Status do projeto

- [x] Estruturar o projeto.
- [x] Criar dados de exemplo.
- [x] Implementar extração.
- [x] Implementar transformação.
- [x] Implementar carregamento em CSV.
- [x] Criar orquestração ETL.
- [x] Criar testes automatizados.
- [x] Configurar GitHub Actions.
- [x] Publicar o projeto no GitHub.
- [x] Configurar PostgreSQL com Docker Compose.
- [x] Criar tabela de projetos no PostgreSQL.
- [x] Implementar conexão Python com PostgreSQL.
- [x] Implementar carregamento PostgreSQL com UPSERT.
- [x] Integrar PostgreSQL ao pipeline ETL.
- [x] Validar a integração com testes automatizados.
- [ ] Implementar validações de qualidade dos dados.
- [ ] Implementar logging estruturado.
- [ ] Criar testes de integração com PostgreSQL.
