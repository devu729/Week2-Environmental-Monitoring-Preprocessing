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
This week focuses on running the PM2.5 prediction FastAPI application. The app serves a machine learning model to predict air pollution levels based on input environmental features.

## Features
- Serves predictions via FastAPI endpoints
- Handles batch and single data predictions
- Fully containerized using Docker (optional)
- Can run locally without external deployment

## Running the App Locally

### 1. Clone the repository:
```bash
git clone https://github.com/devu729/Week3-Environmental-Monitoring-Preprocessing.git
cd Week3-Environmental-Monitoring-Preprocessing
```

### 2. Set up a Python environment:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI app:
```bash
uvicorn app:app --reload --host 127.0.0.1 --port 8000
```

### 5. Open in browser:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

This shows the interactive API documentation where you can test predictions.

## Example Input
Send a JSON payload to the `/predict` endpoint. Example:

```json
{
  "temp": 5,
  "dewpoint": -3,
  "pressure": 1020,
  "wind_speed": 2,
  "hour_sin": 0.5,
  "hour_cos": -0.8,
  "is_weekend": 0,
  "pm25_lag_12": 45.0,
  "pm25_roll_mean_6h": 42.0,
  "pm25_slope_3h": 1.2,
  "pm25_lag_24": 38.0,
  "month": 9,
  "wind_v": 1.1,
  "dow_cos": 0.87,
  "pm25_lag_3": 43.0,
  "wind_u": -0.5,
  "cbwd": "NW",
  "pm25_lag_1": 44.0,
  "dow_sin": 0.5,
  "pm25_roll_std_6h": 3.2,
  "pm25_lag_6": 42.5
}
```

## Optional: Docker (Local)

### Build Docker image:
```bash
docker build -t pm25-fastapi .
```

### Run Docker container locally:
```bash
docker run -p 8000:8000 pm25-fastapi
```

### Access API:
[http://localhost:8000/docs](http://localhost:8000/docs)

## Note on Render Deployment
The app was intended for deployment on Render using Docker. However, the trained model file (`pm25_model.pkl`) is large and is included in `.gitignore`, which prevents Render from building successfully.  

**Recommendation:** Running locally as described above is fully functional and allows you to test the API endpoints. The Docker setup ensures portability for future deployments if the model file is made available.

