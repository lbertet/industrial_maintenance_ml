from sqlalchemy import create_engine, text

engine = create_engine(
    "postgresql+psycopg2://admin:admin@localhost:5432/maintenance_db"
)

query = """
CREATE TABLE IF NOT EXISTS oee (
    id SERIAL PRIMARY KEY,

    timestamp TIMESTAMP NOT NULL,

    line1_availability DOUBLE PRECISION,
    line1_load DOUBLE PRECISION,
    line1_quality DOUBLE PRECISION,

    line1_oee DOUBLE PRECISION
);
"""

with engine.connect() as conn:
    conn.execute(text(query))
    conn.commit()

print("OEE table created successfully")