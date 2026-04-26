# ⚽ International Football Results Analysis (1872–2024)

A Python data analysis project exploring over 150 years of international football results.  
Built for an Artificial Intelligence / Data Analysis assignment using a public Kaggle dataset.

---

## 📋 Project Description

This project analyses the **International Football Results** dataset to uncover patterns in:

- **Goal-scoring trends** across different eras
- **Home advantage** — does playing at home really matter?
- **Dominant nations** — which countries have won the most international matches?
- **Match outcome distributions** (Home Win / Away Win / Draw)

Four clean, modular Python modules handle each analytical task, and all charts are saved automatically to an `outputs/` folder.

---

## 📁 Project Structure

```
football-analysis/
│── data/
│   └── results.csv          ← Dataset goes here (download from Kaggle)
│── src/
│   ├── __init__.py
│   ├── data_loader.py       ← Loads & cleans the CSV
│   ├── exploration.py       ← Task A: Basic exploration
│   ├── goals_analysis.py    ← Task B: Goals statistics
│   ├── match_results.py     ← Task C: Win/Draw/Loss analysis
│   └── visualization.py     ← Task D: Chart generation
│── outputs/                 ← Auto-created; plots saved here
│── main.py                  ← Entry point — runs all steps
│── requirements.txt
└── README.md
```

---

## 📦 Dataset

| Field | Details |
|---|---|
| **Name** | International Football Results from 1872 to 2024 |
| **Source** | [Kaggle – martj42](https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017) |
| **File** | `results.csv` |
| **Columns** | `date`, `home_team`, `away_team`, `home_score`, `away_score`, `tournament`, `city`, `country`, `neutral` |

> **Note:** Download `results.csv` from Kaggle and place it in the `data/` folder before running.

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/football-analysis.git
cd football-analysis
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv

# Activate (Linux/macOS)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add the dataset

Download `results.csv` from [Kaggle](https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017) and place it at:

```
football-analysis/data/results.csv
```

---

## ▶️ How to Run

```bash
python main.py
```

To use a custom dataset path:

```bash
python main.py --data /path/to/your/results.csv
```

The script will print all analysis results to the console and save three charts to the `outputs/` folder.

---

## 📊 Analysis Tasks

### A – Basic Exploration
- Total number of matches
- Earliest and latest year in the dataset
- Number of unique countries / teams
- Most frequent home team

### B – Goals Analysis
- Derives `total_goals = home_score + away_score`
- Average goals per match
- Highest-scoring match ever
- Home vs Away average goals comparison
- Most common total-goals value

### C – Match Results
- Classifies each match: **Home Win**, **Away Win**, or **Draw**
- Percentage breakdown of outcomes
- Determines whether home advantage exists
- Country with the most all-time wins

### D – Visualizations
| File | Description |
|---|---|
| `outputs/goals_histogram.png` | Histogram of total goals per match |
| `outputs/match_outcomes.png` | Bar chart of Home Win / Away Win / Draw counts |
| `outputs/top10_teams_wins.png` | Horizontal bar chart — top 10 teams by total wins |

---

## 🖼️ Example Console Output

```
=======================================================
  INTERNATIONAL FOOTBALL RESULTS ANALYSIS
  1872 – 2024
=======================================================

[Step 1/4] Loading dataset …
  [data_loader] Loaded 47,898 rows from 'data/results.csv'.

=======================================================
  A. BASIC DATASET EXPLORATION
=======================================================
  Total matches recorded   : 47,898
  Earliest year            : 1872
  Latest year              : 2024
  Unique countries/teams   : 311
  Most frequent home team  : Sweden (703 home matches)
=======================================================

=======================================================
  B. GOALS ANALYSIS
=======================================================
  Average goals per match  : 2.79
  Average home goals       : 1.73
  Average away goals       : 1.06
  Most common total goals  : 2 (20.3% of matches)

  Highest-scoring match:
    Australia 31 – 0 American Samoa  (2001-04-11)
    Total goals: 31
=======================================================

=======================================================
  C. MATCH RESULTS ANALYSIS
=======================================================
  Home Win     :  22,541  (47.1%)
  Away Win     :  12,619  (26.4%)
  Draw         :  12,738  (26.6%)

  Home win percentage      : 47.1%
  Away win percentage      : 26.4%
  Home advantage exists?   : YES ✓

  Country with most wins   : Brazil (1,024 wins)
=======================================================
```

*(Exact numbers will vary depending on the dataset version downloaded from Kaggle.)*

---

## 🛠️ Dependencies

| Library | Purpose |
|---|---|
| `pandas` | Data loading, cleaning, and analysis |
| `matplotlib` | Core charting engine |
| `seaborn` | Enhanced chart styling |

---

## 📄 License

This project is for educational purposes. Dataset credit: [Mart Jürisoo on Kaggle](https://www.kaggle.com/martj42).
