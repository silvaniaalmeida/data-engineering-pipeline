import unittest
import tempfile
from pathlib import Path

from src.extract import extract_projects


class TestExtractProjects(unittest.TestCase):

    def test_extract_projects_from_csv(self):
        """
        Verifica se os projetos são extraídos corretamente de um CSV.
        """

        with tempfile.TemporaryDirectory() as temp_dir:
            csv_path = Path(temp_dir) / "projects.csv"

            csv_path.write_text(
                "project_id,project_name,budget,actual_cost,status\n"
                "1,Projeto Teste,100000,80000,Concluido\n"
                "2,Projeto Exemplo,200000,150000,Em Execucao\n",
                encoding="utf-8"
            )

            projects = extract_projects(csv_path)

            self.assertEqual(len(projects), 2)
            self.assertEqual(projects[0]["project_name"], "Projeto Teste")
            self.assertEqual(projects[1]["budget"], "200000")


if __name__ == "__main__":
    unittest.main()
