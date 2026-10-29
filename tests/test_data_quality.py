import unittest


from src.data_quality import (
    validate_required_fields,
    validate_unique_project_ids,
    validate_project_ids,
    validate_financial_values,
)


class TestDataQuality(unittest.TestCase):

    def test_validate_required_fields_valid_project(self):
        """Verifica se um projeto válido passa na validação."""

        projects = [
            {
                "project_id": "1",
                "project_name": "Projeto CAPEX A",
                "budget": "100000",
                "actual_cost": "95000",
                "status": "Em execução",
            }
        ]

        result = validate_required_fields(projects)

        self.assertEqual(result, projects)


    def test_validate_required_fields_empty_field(self):
        """Verifica se um campo obrigatório vazio gera erro."""

        projects = [
            {
                "project_id": "1",
                "project_name": "",
                "budget": "100000",
                "actual_cost": "95000",
                "status": "Em execução",
            }
        ]

        with self.assertRaisesRegex(
            ValueError,
            "campo obrigatório 'project_name' vazio ou ausente",
        ):
            validate_required_fields(projects)



    def test_validate_required_fields_missing_field(self):
        """Verifica se um campo obrigatório ausente gera erro."""

        projects = [
            {
                "project_id": "1",
                "project_name": "Projeto CAPEX A",
                "budget": "100000",
                "actual_cost": "95000",
                # Campo status ausente
            }
        ]

        with self.assertRaisesRegex(
            ValueError,
            "campo obrigatório 'status' vazio ou ausente",
        ):
            validate_required_fields(projects)




    def test_validate_unique_project_ids_duplicate(self):
        """Verifica se identificadores duplicados geram erro."""

        projects = [
            {
                "project_id": "1",
                "project_name": "Projeto CAPEX A",
            },
            {
                "project_id": "1",
                "project_name": "Projeto CAPEX B",
            },
        ]

        with self.assertRaisesRegex(
            ValueError,
            "project_id duplicado: 1",
        ):
            validate_unique_project_ids(projects)    


    def test_validate_project_ids_invalid(self):
        """Verifica se um identificador não numérico gera erro."""

        projects = [
            {
                "project_id": "ABC",
                "project_name": "Projeto CAPEX A",
            }
        ]

        with self.assertRaisesRegex(
            ValueError,
            "project_id inválido: ABC",
        ):
            validate_project_ids(projects)


    def test_validate_project_ids_non_positive(self):
        """Verifica se identificadores zero ou negativos geram erro."""

        for project_id in ("0", "-5"):
            with self.subTest(project_id=project_id):
                projects = [
                    {
                        "project_id": project_id,
                        "project_name": "Projeto CAPEX A",
                    }
                ]

                with self.assertRaisesRegex(
                    ValueError,
                    "project_id deve ser maior que zero",
                ):
                    validate_project_ids(projects) 

    def test_validate_financial_values_invalid(self):
        """Verifica se valores financeiros não numéricos geram erro."""

        projects = [
            {
                "project_id": "1",
                "project_name": "Projeto CAPEX A",
                "budget": "ABC",
                "actual_cost": "95000",
                "status": "Em execução",
            }
        ]

        with self.assertRaisesRegex(
            ValueError,
            "valor inválido no campo 'budget': ABC",
        ):
            validate_financial_values(projects)

    def test_validate_financial_values_negative(self):
        """Verifica se valores financeiros negativos geram erro."""

        for field in ("budget", "actual_cost"):
            with self.subTest(field=field):
                projects = [
                    {
                        "project_id": "1",
                        "project_name": "Projeto CAPEX A",
                        "budget": "100000",
                        "actual_cost": "95000",
                        "status": "Em execução",
                    }
                ]

                projects[0][field] = "-1500"

                with self.assertRaisesRegex(
                    ValueError,
                    f"valor negativo no campo '{field}'",
                ):
                    validate_financial_values(projects)

    def test_validate_financial_values_non_finite(self):
        """Verifica se valores NaN e Infinity geram erro."""

        for field in ("budget", "actual_cost"):
            for value in ("NaN", "Infinity", "-Infinity"):
                with self.subTest(field=field, value=value):
                    projects = [
                        {
                            "project_id": "1",
                            "project_name": "Projeto CAPEX A",
                            "budget": "100000",
                            "actual_cost": "95000",
                            "status": "Em execução",
                        }
                    ]

                    projects[0][field] = value

                    with self.assertRaisesRegex(
                        ValueError,
                        f"valor não finito no campo '{field}'",
                    ):
                        validate_financial_values(projects)

                          


if __name__ == "__main__":
    unittest.main()