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


# Week 3 — Deployment of PM2.5 FastAPI App

## Overview
This week focuses on deploying the PM2.5 prediction FastAPI application using **Render** and **Docker**. The app serves a machine learning model to predict air pollution levels based on input environmental features.

## Features
- Serves predictions via FastAPI endpoints
- Handles batch and single data predictions
- Containerized using Docker for easy deployment
- Fully deployable on Render without additional configuration

## Deployment Instructions

1. Clone the repository
git clone https://github.com/devu729/Week2-Environmental-Monitoring-Preprocessing.git
cd Week2-Environmental-Monitoring-Preprocessing

arduino
Copy code

2. Build Docker image locally (optional)
docker build -t pm25-fastapi .

cpp
Copy code

3. Run locally (optional)
docker run -p 8000:8000 pm25-fastapi

markdown
Copy code
Visit `http://localhost:8000/docs` to see the API documentation.

4. Deploy on Render
- Go to [Render Web Services](https://dashboard.render.com/web/services/new)
- Select **Docker** as the environment
- Connect your GitHub repository
- Set the **start command** if needed:
uvicorn app:app --host 0.0.0.0 --port 10000

markdown
Copy code
- Render will automatically build and deploy the Docker container
- Your API is now live at the URL provided by Render

## Environment Variables
- No environment variables required for basic deployment
- Add any future secrets or external connections under **Settings → Environment → Add Environment Variable**

## Notes
- Ensure your `Dockerfile` and `app.py` are in the repository root
- The app includes all dependencies in the `requirements.txt` file
- For any changes in code, push to GitHub; Render auto-deploys updates if auto-deploy  is enabled.
