"""
main.py
-------
Entry point for the International Football Results Analysis project.

Usage
-----
    python main.py
    python main.py --data path/to/results.csv

The script will:
  A. Load and explore the dataset
  B. Analyse goals
  C. Analyse match results
  D. Generate and save visualizations to the outputs/ folder
"""

import argparse
import sys
import os

# Allow running from the project root without installing the package
sys.path.insert(0, os.path.dirname(__file__))

from src.data_loader import load_data
from src.exploration import explore_dataset, print_exploration_results
from src.goals_analysis import add_total_goals, analyse_goals, print_goals_results
from src.match_results import add_result_column, analyse_results, print_results_analysis
from src.visualization import plot_all


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="International Football Results Analysis (1872–2024)"
    )
    parser.add_argument(
        "--data",
        default="data/results.csv",
        help="Path to results.csv (default: data/results.csv)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    print("\n" + "=" * 55)
    print("  INTERNATIONAL FOOTBALL RESULTS ANALYSIS")
    print("  1872 – 2024")
    print("=" * 55)

    # ── A. Load & Explore ─────────────────────────────────────────────────────
    print("\n[Step 1/4] Loading dataset …")
    df = load_data(args.data)

    exploration_stats = explore_dataset(df)
    print_exploration_results(exploration_stats)

    # ── B. Goals Analysis ─────────────────────────────────────────────────────
    print("\n[Step 2/4] Analysing goals …")
    df = add_total_goals(df)
    goals_stats = analyse_goals(df)
    print_goals_results(goals_stats)

    # ── C. Match Results ──────────────────────────────────────────────────────
    print("\n[Step 3/4] Analysing match results …")
    df = add_result_column(df)
    results_stats = analyse_results(df)
    print_results_analysis(results_stats)

    # ── D. Visualizations ─────────────────────────────────────────────────────
    print("\n[Step 4/4] Generating visualizations …")
    plot_all(
        df=df,
        result_counts=results_stats["result_counts"],
        total_wins=results_stats["total_wins"],
    )

    print("\n✅  Analysis complete!")
    print("   Plots saved in the 'outputs/' directory.")
    print("=" * 55 + "\n")


if __name__ == "__main__":
    main()
