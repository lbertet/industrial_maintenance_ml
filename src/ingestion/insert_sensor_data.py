import pandas as pd
from sqlalchemy import create_engine

# connexion DB
engine = create_engine(
    "postgresql+psycopg2://admin:admin@localhost:5432/maintenance_db"
)

# lecture CSV
df = pd.read_csv("data/sensor_data.csv")

# ajout equipment_id
df["equipment_id"] = 1

# garder uniquement colonnes utiles DB
df_db = df[
    [
        "equipment_id",
        "timestamp",
        "temperature",
        "vibration",
        "pressure",
        "flow",
        "current"
    ]
]

# insertion SQL
df_db.to_sql(
    "sensor_data",
    engine,
    if_exists="append",
    index=False,
    method="multi",
    chunksize=1000
)

print("Sensor data inserted successfully")