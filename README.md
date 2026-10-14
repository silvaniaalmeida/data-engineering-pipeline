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
- Validar as funcionalidades com testes automatizados.

## 2. Arquitetura

O pipeline segue a arquitetura ETL:

CSV de entrada
      |
      v
Extract (src/extract.py)
      |
      v
Transform (src/transform.py)
      |
      v
Load (src/load.py)
      |
      v
CSV processado

A execução completa é coordenada pelo módulo
`src/pipeline.py`.

## 3. Tecnologias utilizadas

- Python
- Biblioteca csv
- Biblioteca decimal
- pathlib
- unittest
- Git e GitHub
- GitHub Actions

Tecnologias previstas para futuras evoluções:

- SQL
- PostgreSQL

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
    |-- src/
    |   |-- extract.py
    |   |-- transform.py
    |   |-- load.py
    |   |-- pipeline.py
    |
    |-- tests/
    |   |-- test_extract.py
    |   |-- test_transform.py
    |   |-- test_load.py
    |
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

Na raiz do projeto, execute:

    python -m src.pipeline

O pipeline realiza as etapas Extract, Transform e Load.

O resultado é gravado em:

    data/processed/projects_transformed.csv

## 7. Testes automatizados

O projeto utiliza a biblioteca `unittest` do Python.

Para executar todos os testes:

    python -m unittest discover -s tests -p "test_*.py" -v

Atualmente, existem cinco testes unitários:

- 1 teste de extração.
- 2 testes de transformação.
- 2 testes de carregamento.

Os testes validam cálculos financeiros,
tratamento de orçamento zero, gravação de CSV
e tratamento de listas vazias.

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

## 9. Próximas evoluções

- Implementar carregamento em PostgreSQL.
- Adicionar validações de qualidade dos dados.
- Implementar logging estruturado.
- Criar testes de integração.
- Expandir os indicadores de projetos.

## 10. Status do projeto

- [x] Estruturar o projeto.
- [x] Criar dados de exemplo.
- [x] Implementar extração.
- [x] Implementar transformação.
- [x] Implementar carregamento.
- [x] Criar orquestração ETL.
- [x] Criar testes automatizados.
- [x] Configurar GitHub Actions.
- [x] Publicar o projeto no GitHub.
- [ ] Implementar integração com PostgreSQL.
