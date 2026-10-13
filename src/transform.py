from decimal import Decimal


def transform_projects(projects):
    """
    Transforma os dados dos projetos e calcula
    indicadores de desvio orçamentário.
    """
    transformed_projects = []

    for project in projects:
        project_id = int(project["project_id"])
        budget = Decimal(project["budget"])
        actual_cost = Decimal(project["actual_cost"])

        budget_variance = actual_cost - budget

        if budget > 0:
            variance_pct = (
                budget_variance / budget
            ) * Decimal("100")
        else:
            variance_pct = None

        transformed_project = {
            "project_id": project_id,
            "project_name": project["project_name"],
            "budget": budget,
            "actual_cost": actual_cost,
            "status": project["status"],
            "budget_variance": budget_variance,
            "variance_pct": variance_pct,
            "over_budget": budget_variance > 0,
        }

        transformed_projects.append(transformed_project)

    return transformed_projects
