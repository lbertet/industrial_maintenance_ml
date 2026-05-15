import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import random

np.random.seed(42)

def generate_machine_data(n_steps=2000):
    data = []

    timestamp = datetime.now()

    # état machine initial
    health = 1.0  # 1 = good, 0 = failure

    for i in range(n_steps):

        # simulation vieillissement machine
        if i % 500 == 0 and i != 0:
            health -= random.uniform(0.1, 0.3)  # dégradation progressive

        health = max(0.1, health)

        # bruit industriel
        noise = lambda scale: np.random.normal(0, scale)

        # FEATURES SIMULÉES

        temperature = 70 + (1 - health) * 60 + noise(2)
        vibration = 0.2 + (1 - health) * 1.5 + noise(0.05)
        pressure = 10 - (1 - health) * 3 + noise(0.3)
        flow = 100 - (1 - health) * 40 + noise(2)
        current = 15 + (1 - health) * 10 + noise(0.5)

        # timestamp
        timestamp += timedelta(minutes=1)

        data.append([
            timestamp,
            temperature,
            vibration,
            pressure,
            flow,
            current,
            health
        ])

    df = pd.DataFrame(data, columns=[
        "timestamp",
        "temperature",
        "vibration",
        "pressure",
        "flow",
        "current",
        "health"
    ])

    return df


if __name__ == "__main__":
    df = generate_machine_data()

    df.to_csv("data/sensor_data.csv", index=False)

    print("Dataset generated:", df.shape)