import pandas as pd
import numpy as np
import os

np.random.seed(42)

script_dir = os.path.dirname(os.path.realpath('__file__')) if '__file__' in globals() else os.getcwd()
data_dir = os.path.join(script_dir,"data")
os.makedirs(data_dir, exist_ok=True)

n=10000

data = {
    "event_id": np.arange(1, n+1),
    "match_id": np.random.choice([1001,1002,1003],n),
    "timestamp":pd.date_range("2025-07-01",periods = n, freq = 'S'),
    "event_type": np.random.choice(["pass","shot","goal","tackle"], n, p = [0.5,0.2,0.2,0.1]),
    "player_id": np.random.randint(500,510, size = n),
    "x_coord":np.random.normal(loc = 50, scale = 20, size = n).clip(0,100),
    "y_coord":np.random.normal(loc = 30, scale = 15, size = n).clip(0,100)
}

df = pd.DataFrame(data)

df.to_csv(os.path.join(data_dir, "events_large.csv"), index = False)