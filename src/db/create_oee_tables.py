from sqlalchemy import create_engine, text

engine = create_engine(
    "postgresql+psycopg2://admin:admin@localhost:5432/maintenance_db"
)

queries = [
"""
CREATE TABLE IF NOT EXISTS line_1 (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    incineration_on BOOLEAN,
    steam_flow DOUBLE PRECISION,
    steam_temperature DOUBLE PRECISION
);
""",
"""
CREATE TABLE IF NOT EXISTS line_2 (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    incineration_on BOOLEAN,
    steam_flow DOUBLE PRECISION,
    steam_temperature DOUBLE PRECISION
);
""",
"""
CREATE TABLE IF NOT EXISTS turbine (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    incineration_on BOOLEAN,
    steam_flow DOUBLE PRECISION,
    steam_temperature DOUBLE PRECISION
);
"""
]

with engine.connect() as conn:
    for q in queries:
        conn.execute(text(q))

    conn.commit()

print("OEE tables created successfully")