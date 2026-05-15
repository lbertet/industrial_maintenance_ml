from sqlalchemy import create_engine, text

engine = create_engine(
    "postgresql+psycopg2://admin:admin@localhost:5432/maintenance_db"
)

queries = [
"""
CREATE TABLE IF NOT EXISTS equipment (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    type VARCHAR(50),
    location VARCHAR(100),
    install_date TIMESTAMP DEFAULT NOW()
);
""",
"""
CREATE TABLE IF NOT EXISTS sensor_data (
    id SERIAL PRIMARY KEY,
    equipment_id INTEGER,
    timestamp TIMESTAMP NOT NULL,
    temperature DOUBLE PRECISION,
    vibration DOUBLE PRECISION,
    pressure DOUBLE PRECISION,
    flow DOUBLE PRECISION,
    current DOUBLE PRECISION
);
""",
"""
CREATE TABLE IF NOT EXISTS anomalies (
    id SERIAL PRIMARY KEY,
    equipment_id INTEGER,
    timestamp TIMESTAMP NOT NULL,
    anomaly_score DOUBLE PRECISION,
    is_anomaly BOOLEAN,
    model_version VARCHAR(50)
);
"""
]

with engine.connect() as conn:
    for q in queries:
        conn.execute(text(q))
    conn.commit()

print("Tables created successfully")