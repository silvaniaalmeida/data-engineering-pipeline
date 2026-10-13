import csv
from pathlib import Path


def extract_projects(file_path):
    """
    Extrai registros de projetos de um arquivo CSV.
    """
    projects = []

    with open(file_path, mode="r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            projects.append(row)

    return projects


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parent.parent
    csv_path = project_root / "data" / "projects.csv"

    projects = extract_projects(csv_path)

    for project in projects:
        print(project)
