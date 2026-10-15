import unittest
from unittest.mock import MagicMock, patch

from src.load_postgres import load_projects_postgres


class TestLoadPostgres(unittest.TestCase):

    def test_empty_projects(self):
        """Deve rejeitar uma lista vazia de projetos."""

        with self.assertRaises(ValueError):
            load_projects_postgres([])

    @patch("src.load_postgres.get_connection")
    def test_load_projects(self, mock_get_connection):
        """Deve enviar os projetos ao PostgreSQL."""

        projects = [
            {
                "project_id": 1,
                "project_name": "Projeto Teste",
                "budget": 100000,
                "actual_cost": 90000,
                "status": "Em execução",
                "budget_variance": -10000,
                "variance_pct": -10.00,
                "over_budget": False,
            }
        ]

        mock_connection = MagicMock()
        mock_cursor = MagicMock()

        mock_get_connection.return_value.__enter__.return_value = mock_connection
        mock_connection.cursor.return_value.__enter__.return_value = mock_cursor

        result = load_projects_postgres(projects)

        self.assertEqual(result, 1)
        mock_get_connection.assert_called_once()
        mock_cursor.executemany.assert_called_once()

        query, parameters = mock_cursor.executemany.call_args.args

        self.assertIn("ON CONFLICT (project_id)", query)
        self.assertEqual(parameters, projects)


if __name__ == "__main__":
    unittest.main()