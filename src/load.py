import csv
from pathlib import Path


def load_projects(projects, output_path):
    """
    Grava os projetos transformados em um arquivo CSV.
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if not projects:
        raise ValueError("Nenhum projeto disponível para carregar.")

    fieldnames = list(projects[0].keys())

    with open(output_path, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for project in projects:
            writer.writerow(project)

    return output_path
