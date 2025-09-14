# Week 1 — Environmental Monitoring (Preprocessing & EDA)

This repository contains **Week 1** work for the Environmental Monitoring & Pollution Control project.  
The focus is on **data preprocessing and exploratory data analysis (EDA)** using the Beijing PM2.5 air quality dataset.

## Key Steps
- Data cleaning & handling missing values  
- Temporal, rolling, and meteorological feature engineering  
- Exploratory visualizations of pollutant trends  
- Reusable `scikit-learn` preprocessing pipeline  

**Note:** No ML models are trained in Week 1. The emphasis is on preparing **high-quality, analysis-ready data** for future weeks.

---

# Week 2 — Advanced Modeling & Diagnostics

In Week 2, we moved beyond the baseline pipeline and built an **advanced modeling workflow** with emphasis on interpretability and diagnostics:  

- Preprocessing pipeline that **imputes missing values, scales numeric features, and one-hot encodes categorical variables** in a version-safe way (no PCA, for interpretability).  
- **Feature selection** using a Random Forest regressor to filter out less informative predictors.  
- **Stacking ensemble** combining HistGradientBoosting, Random Forest, and Extra Trees, with a Ridge regression meta-learner.  
- **Temporal validation:** last 10% of data held out as a “future” test set, with 5-fold `TimeSeriesSplit` CV on the training partition.  
- **Evaluation metrics:** MAE, RMSE, R² reported on the holdout set.  
- **Diagnostics & plots:**  
  - Time-series predictions vs. true PM2.5  
  - Scatter plots of predicted vs. true values  
  - Residual distribution & residual vs. predicted plots  
  - Plots saved under `plots/` directory.  
- **Permutation feature importance** computed on the holdout set; top contributors exported to CSV.  
- **Pipeline serialization** using `joblib` for reuse.  
- **Next steps logged** in a notes file (hyperparameter tuning, quantile HGB for prediction intervals, group-aware CV for multi-station data).

This phase establishes a robust baseline for modeling, interpretation, and future enhancements.


Week 3 — Deployment of PM2.5 FastAPI App
Overview

This week focuses on running the PM2.5 prediction FastAPI application. The app serves a machine learning model to predict air pollution levels based on input environmental features.

Features

Serves predictions via FastAPI endpoints

Handles batch and single data predictions

Fully containerized using Docker (optional)

Can run locally without external deployment

Running the App Locally

Clone the repository:

git clone https://github.com/devu729/Week2-Environmental-Monitoring-Preprocessing.git
cd Week2-Environmental-Monitoring-Preprocessing


Set up a Python environment:

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Run the FastAPI app:

uvicorn app:app --reload --host 127.0.0.1 --port 8000


Open in browser:

http://127.0.0.1:8000/docs


This shows the interactive API documentation where you can test predictions.

Optional: Docker (Local)

Build Docker image:

docker build -t pm25-fastapi .


Run Docker container locally:

docker run -p 8000:8000 pm25-fastapi


Access API:

http://localhost:8000/docs
