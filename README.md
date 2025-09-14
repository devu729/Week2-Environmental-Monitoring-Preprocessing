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
