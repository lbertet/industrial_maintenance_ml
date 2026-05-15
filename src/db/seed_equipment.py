from sqlalchemy import create_engine, text

engine = create_engine(
    "postgresql+psycopg2://admin:admin@localhost:5432/maintenance_db"
)

query = """
INSERT INTO equipment (name, type, location)
VALUES (
    'Pump_001',
    'Industrial Pump',
    'Plant A'
);
"""

with engine.connect() as conn:
    conn.execute(text(query))
    conn.commit()

print("Equipment inserted")