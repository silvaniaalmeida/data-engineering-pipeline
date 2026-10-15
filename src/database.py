import os

import psycopg


def get_connection():
    """Cria uma conexão com o PostgreSQL."""

    password = os.environ.get("POSTGRES_PASSWORD")

    if not password:
        raise ValueError(
            "A variável de ambiente POSTGRES_PASSWORD não está definida."
        )

    return psycopg.connect(
        host="127.0.0.1",
        port=5433,
        dbname="engineering_db",
        user="etl_user",
        password=password,
    )