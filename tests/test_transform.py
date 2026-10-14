import unittest
from decimal import Decimal

from src.transform import transform_projects


class TestTransformProjects(unittest.TestCase):

    def test_budget_variance(self):
        """
        Verifica o cálculo do desvio orçamentário.
        """

        projects = [
            {
                "project_id": "1",
                "project_name": "Projeto Teste",
                "budget": "100000",
                "actual_cost": "80000",
                "status": "Concluido"
            }
        ]

        result = transform_projects(projects)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["project_id"], 1)
        self.assertEqual(result[0]["budget"], Decimal("100000"))
        self.assertEqual(result[0]["actual_cost"], Decimal("80000"))
        self.assertEqual(result[0]["budget_variance"], Decimal("-20000"))
        self.assertEqual(result[0]["variance_pct"], Decimal("-20.00"))
        self.assertFalse(result[0]["over_budget"])

    def test_zero_budget(self):
        """
        Verifica o tratamento de projetos com orçamento zero.
        """

        projects = [
            {
                "project_id": "2",
                "project_name": "Projeto Sem Orcamento",
                "budget": "0",
                "actual_cost": "15000",
                "status": "Em Execucao"
            }
        ]

        result = transform_projects(projects)

        self.assertEqual(result[0]["budget"], Decimal("0"))
        self.assertEqual(result[0]["budget_variance"], Decimal("15000"))
        self.assertIsNone(result[0]["variance_pct"])
        self.assertTrue(result[0]["over_budget"])


if __name__ == "__main__":
    unittest.main()
