CREATE TABLE IF NOT EXISTS projects (
    project_id INTEGER PRIMARY KEY,
    project_name TEXT NOT NULL,
    budget NUMERIC(15, 2) NOT NULL,
    actual_cost NUMERIC(15, 2) NOT NULL,
    status TEXT NOT NULL,
    budget_variance NUMERIC(15, 2) NOT NULL,
    variance_pct NUMERIC(10, 2),
    over_budget BOOLEAN NOT NULL
);