# Week 08: Research Progress Presentation Slide Deck

**Course:** CSE 418: Scientific Research and Methodologies Lab (Spring 2026)  
**Instructor / Supervisor:** Tahmina Islam (Lecturer, Department of CSE, UITS)  
**Research Team:**
* Fahad Rahman (043232000510107, fahadrahman396@gmail.com)
* Shafayat Hossain Shafin (0432320005101088)
* Zannatul Nayeem (0432320005101063)
* Reon Ahmed (0432320005101066)  
**Research Title:** A Data-Driven Analysis of 15-Year Weather Variability and Its Impact on Agricultural Crop Yield in Bangladesh  
**Repository:** [https://github.com/fahadrahman444/scientific-research-and-methodologies](https://github.com/fahadrahman444/scientific-research-and-methodologies)

---

## Slide 1: Title & Overview
* **Title:** A Data-Driven Analysis of 15-Year Weather Variability and Its Impact on Agricultural Crop Yield in Bangladesh
* **Authors (Research Team):** Fahad Rahman, Shafayat Hossain Shafin, Zannatul Nayeem, Reon Ahmed
* **Supervisor:** Tahmina Islam, Lecturer, Department of CSE, UITS
* **Core Paradigm:** Quantitative Empirical Research (Creswell, 5th Ed.)

---

## Slide 2: Motivation & Problem Statement
* Over 40% of Bangladesh's workforce relies on agriculture, contributing ~12% to national GDP.
* Climate variability (rising minimum night temperatures, unseasonal rainfall, prolonged pre-monsoon heatwaves) poses critical threats to national food security.
* **Limitations of Existing Studies:**
  * OLS regressions assume linear relations, ignoring biological shock thresholds.
  * Lack of recent 15-year longitudinal analysis (2009–2024).
  * "Black-box" ML implementations lacking agronomic explainability.

---

## Slide 3: Research Questions & Hypotheses
* **RQ1:** What are the 15-year trends in temperature, rainfall, and drought indices across Bangladesh?
* **RQ2:** How do weather anomalies correlate with official UN FAOSTAT rice production data?
* **RQ3:** Which machine learning architecture yields the highest predictive accuracy?
* **RQ4:** Which specific climatic features dictate yield penalties according to explainable AI (SHAP)?
* **Key Hypothesis ($H_3$):** Non-linear gradient boosted ensembles (XGBoost/CatBoost) will significantly outperform classical linear models.

---

## Slide 4: Datasets & Pipeline Architecture
* **Ground Truth Dataset:** UN FAOSTAT (`data/raw/FAOSTAT_data_en_10-12-2026.csv`) spanning 1976–2024, focusing on the 15-year continuum (2009–2024).
* **Meteorological Data:** 35 Synoptic Stations (BMD) & NASA POWER ($T_{max}, T_{min}, P, RH, SS$).
* **Engineered Indices:** Growing Degree Days (GDD), Standardized Precipitation Index (SPI-3), Heat Stress Days ($T_{max} \ge 35^\circ\text{C}$).
* **Execution:** Fully hosted on **Google Colab** (zero local GPU overhead).

---

## Slide 5: Methodology & Workflow Diagram
* Reference to Tahmina Ma'am's classroom workflow models:
  1. Data Ingestion (FAOSTAT + BMD)
  2. Data Wrangling & De-trending
  3. Feature Engineering (SPI, GDD)
  4. Google Colab ML Training (Random Forest, XGBoost, CatBoost, LightGBM, LSTM)
  5. Explainable AI via TreeSHAP

---

## Slide 6: Preliminary Results & Trend Analysis
* **Mann-Kendall Test:** Statistically significant increase in night temperatures ($+0.038^\circ\text{C/yr}$, $p = 0.013$) and heat stress days ($p = 0.009$).
* **Preliminary ML Benchmark:** XGBoost achieved $R^2 = 0.941$ on out-of-sample test data, outperforming linear regression ($R^2 = 0.812$).

---

## Slide 7: Next Steps Toward Final Paper (Weeks 9–14)
* Incorporate deep sequential LSTM models in Colab Notebook 04.
* Refine TreeSHAP dependence plots for critical anthesis heat thresholds.
* Finalize IEEE Transactions research manuscript for publication submission.

---

## Slide 8: Q&A and Feedback
* *Thank you! Open for questions and suggestions.*
