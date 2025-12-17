# Survival Prediction (Titanic)

This project demonstrates a reproducible machine learning workflow for predicting survival on the Titanic dataset. The notebook now uses the real Titanic CSV and includes:

- Exploratory data analysis (EDA) and visualizations
- Feature engineering (titles, family features, fares, missing value handling)
- Preprocessing pipelines and cross-validated evaluation
- Hyperparameter tuning with RandomizedSearchCV
- Model interpretability using SHAP and LIME

Files
- `survival_prediction.ipynb` — Updated Jupyter notebook (complete analysis)
- `requirements.txt` — Runtime dependencies (now includes `shap` and `lime`)
- `data/download_titanic.py` — Helper script to fetch the public Titanic CSV

How to run
1. Create and activate a virtual environment and install requirements:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate   # Windows
   pip install -r requirements.txt
   ```
2. Download the dataset:
   ```bash
   python data/download_titanic.py
   ```
3. Start Jupyter and open the notebook:
   ```bash
   jupyter notebook survival_prediction.ipynb
   ```

Notes & next steps
- The notebook uses RandomForest by default. For better performance try Gradient boosting models (XGBoost / LightGBM) and add an `environment.yml` for Binder/Colab compatibility.
- SHAP plots may open interactive figures in some environments; the notebook samples data for speed.

License: permissive (MIT-style) — this is a teaching/demo dataset and code.

