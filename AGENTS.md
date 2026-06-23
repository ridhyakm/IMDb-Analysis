# AGENTS.md

Purpose
Provide concise, actionable instructions for AI coding agents working on this repository.

Repository summary
- Small IMDB analysis project using Python (pandas, numpy, matplotlib, seaborn).
- Raw datasets: `imdb_datasets/` (CSV files). Scripts: `scripts/`. Outputs: `visuals/`, `data_clean/`.

Quick run (local)
1. Create and activate a virtual environment.
2. Install dependencies: `pip install pandas numpy matplotlib seaborn`.
3. From the repository root run: `python scripts/imdb_analysis.py`.

Key files and locations
- imdb_datasets/: source CSVs (may be large).
- scripts/imdb_analysis.py: main analysis script to inspect and visualize data.
- scripts/imdb_analysis_clean.py: auxiliary/cleaning script.
- data_clean/imdb_clean.csv: cleaned dataset output (script currently writes `imdb_clean.csv` to repository root).
- visuals/: graphs and saved figures.

Conventions & expectations for agents
- Run scripts from the repository root.
- Prefer non-destructive changes: do not modify source CSVs; write outputs to `data_clean/` or `visuals/`.
- Be mindful of memory: large CSVs may require `dtype` hints or `chunksize` when using `pd.read_csv`.
- Keep edits minimal and consistent with existing style.

First steps for an agent
1. Inspect `scripts/` for entry points and data paths.
2. Run smaller, read-only checks (open files, print head, check dtypes) before running full scripts.
3. If making fixes, run the script and include command output in the change description.

Links
- Project README: [README.md.txt](README.md.txt)

Feedback
Ask the user for preferred Python version, required extra packages, or where to store generated artifacts if different from defaults.
