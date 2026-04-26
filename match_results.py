"""
match_results.py
----------------
Task C – Match results analysis.
Classifies each match as Home Win / Away Win / Draw and computes win statistics.
"""

import pandas as pd


def add_result_column(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add a 'result' column that labels each match as:
      - 'Home Win'  : home_score > away_score
      - 'Away Win'  : away_score > home_score
      - 'Draw'      : scores are equal

    Parameters
    ----------
    df : pd.DataFrame
        Football results DataFrame.

    Returns
    -------
    pd.DataFrame
        DataFrame with the new 'result' column added.
    """
    df = df.copy()

    def classify(row: pd.Series) -> str:
        if row["home_score"] > row["away_score"]:
            return "Home Win"
        elif row["away_score"] > row["home_score"]:
            return "Away Win"
        return "Draw"

    df["result"] = df.apply(classify, axis=1)
    return df


def analyse_results(df: pd.DataFrame) -> dict:
    """
    Compute match-result statistics.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame with 'result' column already added.

    Returns
    -------
    dict
        Dictionary containing:
        - result_counts        : pd.Series  (Home Win / Away Win / Draw)
        - home_win_pct         : float
        - home_advantage       : bool
        - country_most_wins    : str
        - country_wins_count   : int
    """
    result_counts = df["result"].value_counts()

    total = len(df)
    home_win_pct = round(result_counts.get("Home Win", 0) / total * 100, 1)
    away_win_pct = round(result_counts.get("Away Win", 0) / total * 100, 1)

    # Home advantage exists if home wins % > away wins %
    home_advantage = home_win_pct > away_win_pct

    # Country with most wins overall (home or away)
    home_wins = df[df["result"] == "Home Win"]["home_team"].value_counts()
    away_wins = df[df["result"] == "Away Win"]["away_team"].value_counts()

    total_wins = home_wins.add(away_wins, fill_value=0).astype(int)
    country_most_wins = total_wins.idxmax()
    country_wins_count = int(total_wins.max())

    return {
        "result_counts": result_counts,
        "home_win_pct": home_win_pct,
        "away_win_pct": away_win_pct,
        "home_advantage": home_advantage,
        "country_most_wins": country_most_wins,
        "country_wins_count": country_wins_count,
        "total_wins": total_wins,
    }


def print_results_analysis(stats: dict) -> None:
    """Pretty-print match result statistics."""
    rc = stats["result_counts"]
    print("\n" + "=" * 55)
    print("  C. MATCH RESULTS ANALYSIS")
    print("=" * 55)
    for label in ["Home Win", "Away Win", "Draw"]:
        count = rc.get(label, 0)
        pct = round(count / rc.sum() * 100, 1)
        print(f"  {label:<12} : {count:>7,}  ({pct}%)")
    print()
    print(f"  Home win percentage      : {stats['home_win_pct']}%")
    print(f"  Away win percentage      : {stats['away_win_pct']}%")
    advantage = "YES ✓" if stats["home_advantage"] else "NO ✗"
    print(f"  Home advantage exists?   : {advantage}")
    print(f"\n  Country with most wins   : {stats['country_most_wins']}"
          f" ({stats['country_wins_count']:,} wins)")
    print("=" * 55)
