import csv
import tempfile
import unittest
from decimal import Decimal
from pathlib import Path

from src.load import load_projects


class TestLoadProjects(unittest.TestCase):

    def test_load_projects_to_csv(self):
        """
        Verifica se os projetos são gravados corretamente em CSV.
        """

        projects = [
            {
                "project_id": 1,
                "project_name": "Projeto Teste",
                "budget": Decimal("100000"),
                "actual_cost": Decimal("80000"),
                "status": "Concluido",
                "budget_variance": Decimal("-20000"),
                "variance_pct": Decimal("-20.00"),
                "over_budget": False
            }
        ]

        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = Path(temp_dir) / "processed" / "projects.csv"

            saved_path = load_projects(projects, output_path)

            self.assertEqual(saved_path, output_path)
            self.assertTrue(output_path.exists())

            with open(output_path, mode="r", encoding="utf-8", newline="") as file:
                reader = csv.DictReader(file)
                rows = list(reader)

            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["project_name"], "Projeto Teste")
            self.assertEqual(rows[0]["budget_variance"], "-20000")
            self.assertEqual(rows[0]["over_budget"], "False")


    def test_load_empty_projects(self):
        """
        Verifica se uma lista vazia gera um ValueError.
        """

        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = Path(temp_dir) / "projects.csv"

            with self.assertRaises(ValueError):
                load_projects([], output_path)

            self.assertFalse(output_path.exists())

if __name__ == "__main__":
    unittest.main()
