

from decimal import Decimal, InvalidOperation

REQUIRED_FIELDS = (
    "project_id",
    "project_name",
    "budget",
    "actual_cost",
    "status",
)


def validate_required_fields(projects):
    """
    Valida se todos os projetos possuem
    os campos obrigatórios preenchidos.
    """
    for row_number, project in enumerate(projects, start=1):
        for field in REQUIRED_FIELDS:
            value = project.get(field)

            if value is None or str(value).strip() == "":
                raise ValueError(
                    f"Registro {row_number}: "
                    f"campo obrigatório '{field}' vazio ou ausente."
                )

    return projects

def validate_unique_project_ids(projects):
    """
    Verifica se existem identificadores de projetos duplicados.
    """
    seen_ids = set()

    for row_number, project in enumerate(projects, start=1):
        project_id = project["project_id"]

        if project_id in seen_ids:
            raise ValueError(
                f"Registro {row_number}: "
                f"project_id duplicado: {project_id}"
            )

        seen_ids.add(project_id)

    return projects

   


def validate_project_ids(projects):
    """
    Verifica se os identificadores dos projetos
    são números inteiros positivos.
    """
    for row_number, project in enumerate(projects, start=1):
        project_id = project["project_id"]

        try:
            numeric_id = int(project_id)
        except (ValueError, TypeError):
            raise ValueError(
                f"Registro {row_number}: "
                f"project_id inválido: {project_id}"
            ) from None

        if numeric_id <= 0:
            raise ValueError(
                f"Registro {row_number}: "
                f"project_id deve ser maior que zero: {project_id}"
            )

    return projects



def validate_financial_values(projects):
    """
    Valida os campos financeiros dos projetos.
    """
    financial_fields = ("budget", "actual_cost")

    for row_number, project in enumerate(projects, start=1):
        for field in financial_fields:
            value = project[field]

            try:
                numeric_value = Decimal(str(value))
            except (InvalidOperation, ValueError, TypeError):
                raise ValueError(
                    f"Registro {row_number}: "
                    f"valor inválido no campo '{field}': {value}"
                ) from None

            if not numeric_value.is_finite():
                raise ValueError(
                    f"Registro {row_number}: "
                    f"valor não finito no campo '{field}': {value}"
                )

            if numeric_value < 0:
                raise ValueError(
                    f"Registro {row_number}: "
                    f"valor negativo no campo '{field}': {value}"
                )

    return projects





