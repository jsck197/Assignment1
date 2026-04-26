"""
goals_analysis.py
-----------------
Task B – Goals analysis.
Adds a total_goals column and computes goal-related statistics.
"""

import pandas as pd


def add_total_goals(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add a 'total_goals' column (home_score + away_score) to the DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        Football results DataFrame.

    Returns
    -------
    pd.DataFrame
        DataFrame with the new 'total_goals' column added.
    """
    df = df.copy()
    df["total_goals"] = df["home_score"] + df["away_score"]
    return df


def analyse_goals(df: pd.DataFrame) -> dict:
    """
    Compute goal-related statistics.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame that already contains a 'total_goals' column.

    Returns
    -------
    dict
        Dictionary containing:
        - avg_goals_per_match   : float
        - highest_scoring_match : pd.Series  (single row)
        - avg_home_goals        : float
        - avg_away_goals        : float
        - most_common_total     : int
        - most_common_total_pct : float
    """
    avg_goals_per_match = round(df["total_goals"].mean(), 2)

    # Row with the highest total goals (first occurrence if tied)
    highest_scoring_match = df.loc[df["total_goals"].idxmax()]

    avg_home_goals = round(df["home_score"].mean(), 2)
    avg_away_goals = round(df["away_score"].mean(), 2)

    # Most common total goals value
    most_common_total = int(df["total_goals"].mode()[0])
    most_common_total_pct = round(
        (df["total_goals"] == most_common_total).sum() / len(df) * 100, 1
    )

    return {
        "avg_goals_per_match": avg_goals_per_match,
        "highest_scoring_match": highest_scoring_match,
        "avg_home_goals": avg_home_goals,
        "avg_away_goals": avg_away_goals,
        "most_common_total": most_common_total,
        "most_common_total_pct": most_common_total_pct,
    }


def print_goals_results(stats: dict) -> None:
    """Pretty-print goals analysis results."""
    hm = stats["highest_scoring_match"]
    print("\n" + "=" * 55)
    print("  B. GOALS ANALYSIS")
    print("=" * 55)
    print(f"  Average goals per match  : {stats['avg_goals_per_match']}")
    print(f"  Average home goals       : {stats['avg_home_goals']}")
    print(f"  Average away goals       : {stats['avg_away_goals']}")
    print(f"  Most common total goals  : {stats['most_common_total']}"
          f" ({stats['most_common_total_pct']}% of matches)")
    print(f"\n  Highest-scoring match:")
    print(f"    {hm['home_team']} {int(hm['home_score'])} – "
          f"{int(hm['away_score'])} {hm['away_team']}"
          f"  ({str(hm['date'])[:10]})")
    print(f"    Total goals: {int(hm['total_goals'])}")
    print("=" * 55)
