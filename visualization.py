"""
visualization.py
----------------
Task D – Visualization.
Generates and saves all required charts to the /outputs folder.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns


# ── Global style settings ─────────────────────────────────────────────────────
sns.set_theme(style="whitegrid", palette="muted")
COLORS = sns.color_palette("muted")
OUTPUT_DIR = "outputs"


def _ensure_output_dir() -> None:
    """Create the outputs directory if it doesn't already exist."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)


def plot_goals_histogram(df: pd.DataFrame) -> str:
    """
    Plot and save a histogram of total goals per match.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame with 'total_goals' column.

    Returns
    -------
    str
        File path of the saved image.
    """
    _ensure_output_dir()
    fig, ax = plt.subplots(figsize=(10, 6))

    max_goals = int(df["total_goals"].max())
    bins = range(0, max_goals + 2)

    sns.histplot(
        df["total_goals"],
        bins=bins,
        kde=True,
        color=COLORS[0],
        edgecolor="white",
        linewidth=0.6,
        ax=ax,
    )

    ax.set_title("Distribution of Total Goals per Match\n(International Football 1872–2024)",
                 fontsize=14, fontweight="bold", pad=12)
    ax.set_xlabel("Total Goals in Match", fontsize=12)
    ax.set_ylabel("Number of Matches", fontsize=12)
    ax.xaxis.set_major_locator(mticker.MultipleLocator(1))

    # Annotate mean line
    mean_val = df["total_goals"].mean()
    ax.axvline(mean_val, color="crimson", linestyle="--", linewidth=1.5,
               label=f"Mean = {mean_val:.2f}")
    ax.legend(fontsize=11)

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "goals_histogram.png")
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"  [visualization] Saved → {path}")
    return path


def plot_match_outcomes(result_counts: pd.Series) -> str:
    """
    Plot and save a bar chart of match outcomes (Home Win / Away Win / Draw).

    Parameters
    ----------
    result_counts : pd.Series
        Value counts of the 'result' column.

    Returns
    -------
    str
        File path of the saved image.
    """
    _ensure_output_dir()
    labels = ["Home Win", "Away Win", "Draw"]
    values = [result_counts.get(l, 0) for l in labels]
    palette = [COLORS[2], COLORS[4], COLORS[7]] if len(COLORS) > 7 else COLORS[:3]

    fig, ax = plt.subplots(figsize=(8, 6))
    bars = ax.bar(labels, values, color=palette, edgecolor="white", linewidth=0.8, width=0.5)

    # Add count + percentage labels on top of each bar
    total = sum(values)
    for bar, val in zip(bars, values):
        pct = val / total * 100
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + total * 0.005,
            f"{val:,}\n({pct:.1f}%)",
            ha="center", va="bottom", fontsize=10, fontweight="bold",
        )

    ax.set_title("International Football Match Outcomes\n(1872–2024)",
                 fontsize=14, fontweight="bold", pad=12)
    ax.set_ylabel("Number of Matches", fontsize=12)
    ax.set_ylim(0, max(values) * 1.15)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "match_outcomes.png")
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"  [visualization] Saved → {path}")
    return path


def plot_top10_teams(total_wins: pd.Series) -> str:
    """
    Plot and save a horizontal bar chart of the top 10 teams by total wins.

    Parameters
    ----------
    total_wins : pd.Series
        Series indexed by team name, values are total wins.

    Returns
    -------
    str
        File path of the saved image.
    """
    _ensure_output_dir()
    top10 = total_wins.nlargest(10).sort_values()  # ascending for horizontal bar

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(
        top10.index, top10.values,
        color=sns.color_palette("Blues_r", len(top10)),
        edgecolor="white", linewidth=0.6,
    )

    # Value labels at end of each bar
    for bar, val in zip(bars, top10.values):
        ax.text(
            bar.get_width() + top10.max() * 0.005,
            bar.get_y() + bar.get_height() / 2,
            f"{val:,}",
            va="center", fontsize=10,
        )

    ax.set_title("Top 10 Teams by Total Wins (Home + Away)\nInternational Football 1872–2024",
                 fontsize=14, fontweight="bold", pad=12)
    ax.set_xlabel("Total Wins", fontsize=12)
    ax.set_xlim(0, top10.max() * 1.12)
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "top10_teams_wins.png")
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"  [visualization] Saved → {path}")
    return path


def plot_all(df: pd.DataFrame, result_counts: pd.Series, total_wins: pd.Series) -> None:
    """
    Generate and save all three required visualizations.

    Parameters
    ----------
    df            : DataFrame with 'total_goals' column.
    result_counts : Value counts of the 'result' column.
    total_wins    : Series of total wins per team.
    """
    print("\n[visualization] Generating plots …")
    plot_goals_histogram(df)
    plot_match_outcomes(result_counts)
    plot_top10_teams(total_wins)
    print("[visualization] All plots saved to the 'outputs/' folder.\n")
