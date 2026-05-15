import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

N_POINTS = 2000

start_time = datetime.now()


def generate_line_data(
    base_flow,
    base_temp,
    noise_flow=0.5,
    noise_temp=3
):

    rows = []
    current_time = start_time

    for i in range(N_POINTS):

        current_time += timedelta(minutes=1)

        steam_flow = np.random.uniform(
            base_flow - noise_flow,
            base_flow + noise_flow
        )

        steam_temp = np.random.uniform(
            base_temp - noise_temp,
            base_temp + noise_temp
        )

        rows.append({
            "timestamp": current_time,
            "incineration_on": True,
            "steam_flow": steam_flow,
            "steam_temperature": steam_temp
        })

    return pd.DataFrame(rows)


# ==============================
# Ligne 1
# ==============================

line1_df = generate_line_data(
    base_flow=40,
    base_temp=395
)


# ==============================
# Ligne 2 (20% plus petite)
# ==============================

line2_df = generate_line_data(
    base_flow=32,
    base_temp=316
)


# ==============================
# Turbine
# ==============================

# La turbine consomme la vapeur globale
# donc débit = ligne1 + ligne2 + bruit

rows_turbine = []

for i in range(N_POINTS):

    flow = (
        line1_df.loc[i, "steam_flow"]
        + line2_df.loc[i, "steam_flow"]
        + np.random.normal(0, 0.8)
    )

    temp = (
        (
            line1_df.loc[i, "steam_temperature"]
            + line2_df.loc[i, "steam_temperature"]
        ) / 2
        + np.random.normal(0, 2)
    )

    rows_turbine.append({
        "timestamp": line1_df.loc[i, "timestamp"],
        "incineration_on": True,
        "steam_flow": flow,
        "steam_temperature": temp
    })


turbine_df = pd.DataFrame(rows_turbine)


# ==============================
# Export CSV
# ==============================

line1_df.to_csv("data/line1.csv", index=False)
line2_df.to_csv("data/line2.csv", index=False)
turbine_df.to_csv("data/turbine.csv", index=False)

print("Datasets generated successfully")