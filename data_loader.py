"""
data_loader.py
--------------
Handles loading and initial cleaning of the international football results dataset.
"""

import pandas as pd
import os


def load_data(filepath: str = "data/results.csv") -> pd.DataFrame:
    """
    Load the football results CSV file into a pandas DataFrame.

    Parameters
    ----------
    filepath : str
        Path to the results.csv file (relative to project root).

    Returns
    -------
    pd.DataFrame
        Cleaned DataFrame ready for analysis.

    Raises
    ------
    FileNotFoundError
        If the CSV file cannot be found at the given path.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(
            f"Dataset not found at '{filepath}'.\n"
            "Please download 'results.csv' from Kaggle and place it in the 'data/' folder.\n"
            "Dataset: https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017"
        )

    df = pd.read_csv(filepath)

    # ── Basic cleaning ────────────────────────────────────────────────────────
    # Parse date column
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Drop rows where essential columns are null
    essential_cols = ["date", "home_team", "away_team", "home_score", "away_score"]
    before = len(df)
    df.dropna(subset=essential_cols, inplace=True)
    dropped = before - len(df)
    if dropped:
        print(f"  [data_loader] Dropped {dropped} rows with missing essential values.")

    # Ensure score columns are integers
    df["home_score"] = df["home_score"].astype(int)
    df["away_score"] = df["away_score"].astype(int)

    # Extract year for convenience
    df["year"] = df["date"].dt.year

    print(f"  [data_loader] Loaded {len(df):,} rows from '{filepath}'.")
    return df
