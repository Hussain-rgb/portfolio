# Survival Prediction (Titanic / 9-11-style demonstration)

This project demonstrates a survival prediction pipeline (data cleaning, feature engineering, model training and evaluation) intended as a reproducible example. It includes a Jupyter notebook with a small example and instructions to run locally.

Files
- `survival_prediction.ipynb` — Example Jupyter notebook (overview + reproducible steps)
- `requirements.txt` — Packages used

How to run
1. Create a Python virtualenv and install requirements: `pip install -r requirements.txt`.
2. Download the sample dataset (TITANIC) used in the notebook:
   - `python data/download_titanic.py` (saves `survival_prediction/data/titanic.csv`)
3. Start Jupyter: `jupyter notebook` and open `survival_prediction.ipynb`.

Notes
- The `download_titanic.py` script fetches a public Titanic CSV from a maintained dataset repository; replace it with your own dataset if needed.

Notes
- This is a demo / teaching example. Replace the dataset with the real dataset for full analysis.
