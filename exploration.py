"""
exploration.py
--------------
Task A – Basic dataset exploration.
Provides summary statistics about the international football results dataset.
"""

import pandas as pd


def explore_dataset(df: pd.DataFrame) -> dict:
    """
    Perform basic exploratory analysis on the football dataset.

    Parameters
    ----------
    df : pd.DataFrame
        Cleaned football results DataFrame (output of data_loader.load_data).

    Returns
    -------
    dict
        Dictionary containing key statistics:
        - total_matches       : int
        - earliest_year       : int
        - latest_year         : int
        - unique_countries    : int
        - most_frequent_home  : str
        - all_teams           : list[str]
    """
    # ── Total matches ─────────────────────────────────────────────────────────
    total_matches = len(df)

    # ── Year range ────────────────────────────────────────────────────────────
    earliest_year = int(df["year"].min())
    latest_year = int(df["year"].max())

    # ── Unique countries (home + away combined) ───────────────────────────────
    all_teams = sorted(
        set(df["home_team"].unique()) | set(df["away_team"].unique())
    )
    unique_countries = len(all_teams)

    # ── Most frequent home team ───────────────────────────────────────────────
    most_frequent_home = df["home_team"].value_counts().idxmax()
    home_appearances = int(df["home_team"].value_counts().max())

    stats = {
        "total_matches": total_matches,
        "earliest_year": earliest_year,
        "latest_year": latest_year,
        "unique_countries": unique_countries,
        "most_frequent_home": most_frequent_home,
        "home_appearances": home_appearances,
        "all_teams": all_teams,
    }
    return stats


def print_exploration_results(stats: dict) -> None:
    """Pretty-print the exploration statistics to the console."""
    print("\n" + "=" * 55)
    print("  A. BASIC DATASET EXPLORATION")
    print("=" * 55)
    print(f"  Total matches recorded   : {stats['total_matches']:,}")
    print(f"  Earliest year            : {stats['earliest_year']}")
    print(f"  Latest year              : {stats['latest_year']}")
    print(f"  Unique countries/teams   : {stats['unique_countries']}")
    print(f"  Most frequent home team  : {stats['most_frequent_home']}"
          f" ({stats['home_appearances']:,} home matches)")
    print("=" * 55)
