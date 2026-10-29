from pathlib import Path

from src.extract import extract_projects
from src.transform import transform_projects
from src.load import load_projects
from src.load_postgres import load_projects_postgres
from src.data_quality import (
    validate_required_fields,
    validate_project_ids,
    validate_unique_project_ids,
    validate_financial_values,
)


def run_pipeline():
    """
    Executa o pipeline ETL completo:
    Extract -> Transform -> Load CSV + PostgreSQL.
    """

    project_root = Path(__file__).resolve().parent.parent

    input_path = project_root / "data" / "projects.csv"
    output_path = project_root / "data" / "processed" / "projects_transformed.csv"

    # Extract
    projects = extract_projects(input_path)
    print(f"Extract: {len(projects)} projetos extraídos.")

    # Data Quality
    validate_required_fields(projects)
    validate_project_ids(projects)
    validate_unique_project_ids(projects)
    validate_financial_values(projects)

    print(f"Data Quality: {len(projects)} projetos validados.")

    # Transform
    transformed_projects = transform_projects(projects)
    print(f"Transform: {len(transformed_projects)} projetos transformados.")

    # Load CSV
    saved_path = load_projects(transformed_projects, output_path)
    print(f"Load CSV: dados gravados em {saved_path}")

    # Load PostgreSQL
    loaded_count = load_projects_postgres(transformed_projects)
    print(f"Load PostgreSQL: {loaded_count} projetos carregados.")

    print("Pipeline ETL executado com sucesso!")


if __name__ == "__main__":
    run_pipeline()