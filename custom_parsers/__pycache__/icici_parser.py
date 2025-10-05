import pandas as pd
from pathlib import Path

def parse(csv_path: str) -> pd.DataFrame:
    """
    Reads a CSV bank statement and returns a DataFrame.
    """
    csv_file = Path(csv_path)
    if not csv_file.exists():
        raise FileNotFoundError(f"{csv_path} not found")

    df = pd.read_csv(csv_file)
    return df
