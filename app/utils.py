
import pandas as pd

def load_and_clean_data():
    # Load each dataset
    benin = pd.read_csv("data/benin_clean.csv")
    togo = pd.read_csv("data/togo-dapaong_qc.csv")
    sierra = pd.read_csv("data/sierraleone-bumbuna.csv")

    # Select only the relevant columns
    cols = ["Timestamp", "GHI", "DNI", "DHI"]

    benin = benin[cols].copy()
    benin["Country"] = "Benin"

    togo = togo[cols].copy()
    togo["Country"] = "Togo"

    sierra = sierra[cols].copy()
    sierra["Country"] = "Sierra Leone"

    # Combine and clean
    df = pd.concat([benin, togo, sierra], ignore_index=True)
    df = df[(df["GHI"] >= 0) & (df["DNI"] >= 0) & (df["DHI"] >= 0)]

    return df
