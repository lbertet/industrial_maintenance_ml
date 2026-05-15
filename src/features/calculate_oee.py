import pandas as pd
from sqlalchemy import create_engine

# ==============================
# CONFIG
# ==============================

LINE1_DESIGN_FLOW = 42
LINE1_DESIGN_TEMP = 405

# ==============================
# DB CONNECTION
# ==============================

engine = create_engine(
    "postgresql+psycopg2://admin:admin@localhost:5432/maintenance_db"
)

# ==============================
# LOAD DATA
# ==============================

query = """
SELECT *
FROM line_1
ORDER BY timestamp
"""

df = pd.read_sql(query, engine)

# ==============================
# KPI CALCULATIONS
# ==============================

# Availability
df["line1_availability"] = (
    df["incineration_on"]
    .astype(int)
    .expanding()
    .mean()
)

# Load
df["line1_load"] = (
    df["steam_flow"] / LINE1_DESIGN_FLOW
)

# Quality
df["line1_quality"] = (
    df["steam_temperature"] / LINE1_DESIGN_TEMP
)

# OEE global
df["line1_oee"] = (
    df["line1_availability"]
    * df["line1_load"]
    * df["line1_quality"]
)

# ==============================
# FINAL TABLE
# ==============================

oee_df = df[
    [
        "timestamp",
        "line1_availability",
        "line1_load",
        "line1_quality",
        "line1_oee"
    ]
]

# ==============================
# INSERT INTO DB
# ==============================

oee_df.to_sql(
    "oee",
    engine,
    if_exists="append",
    index=False,
    method="multi",
    chunksize=1000
)

print("OEE KPIs calculated and inserted")