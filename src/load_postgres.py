from src.database import get_connection


def load_projects_postgres(projects):
    """Insere ou atualiza projetos no PostgreSQL."""

    if not projects:
        raise ValueError("Nenhum projeto para carregar.")

    query = """
        INSERT INTO projects (
            project_id,
            project_name,
            budget,
            actual_cost,
            status,
            budget_variance,
            variance_pct,
            over_budget
        )
        VALUES (
            %(project_id)s,
            %(project_name)s,
            %(budget)s,
            %(actual_cost)s,
            %(status)s,
            %(budget_variance)s,
            %(variance_pct)s,
            %(over_budget)s
        )
        ON CONFLICT (project_id)
        DO UPDATE SET
            project_name = EXCLUDED.project_name,
            budget = EXCLUDED.budget,
            actual_cost = EXCLUDED.actual_cost,
            status = EXCLUDED.status,
            budget_variance = EXCLUDED.budget_variance,
            variance_pct = EXCLUDED.variance_pct,
            over_budget = EXCLUDED.over_budget;
    """

    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.executemany(query, projects)

    return len(projects)