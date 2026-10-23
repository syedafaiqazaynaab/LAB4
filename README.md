# Lab 4: Git and NumPy Performance

## Overview
This project explores Python environment setup, Git version control, and NumPy operations. It includes notebook exercises and a comparison of Python loops with NumPy for numerical computations.

## Project Structure
- `notebooks/` — Lab exercises and NumPy experiments.
- `src/` — Python utility functions.
- `tests/` — Project tests.
- `data/raw/` — Input data.
- `data/processed/` — Processed data and timing results.
- `docs/` — Lab notes and documentation.
- `requirements.txt` — Python package dependencies.
- `.gitignore` — Files and folders excluded from Git.

## Setup
Activate the project's virtual environment and install dependencies:

```powershell
.\venv313\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run the Notebook
Open `notebooks/lab4.ipynb` in VS Code and select the `venv313` Python kernel. Run the notebook cells from top to bottom.

## Results
The project compares loop-based calculations with NumPy-based operations. Timing results are saved in `data/processed/timing_results.csv`, and standardised data is saved in `data/processed/standardised.npy`.

## Version Control
Git is used to track project changes, and the repository is hosted on GitHub.