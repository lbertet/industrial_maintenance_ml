import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://admin:admin@localhost:5432/maintenance_db"
)


def insert_csv(csv_path, table_name):

    df = pd.read_csv(csv_path)

    df.to_sql(
        table_name,
        engine,
        if_exists="append",
        index=False,
        method="multi",
        chunksize=1000
    )

    print(f"Inserted into {table_name}")


insert_csv("data/line1.csv", "line_1")
insert_csv("data/line2.csv", "line_2")
insert_csv("data/turbine.csv", "turbine")