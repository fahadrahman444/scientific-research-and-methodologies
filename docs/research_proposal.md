# Research Proposal: A Data-Driven Analysis of 15-Year Weather Variability and Its Impact on Agricultural Crop Yield in Bangladesh

**Course:** CSE 418: Scientific Research and Methodologies Lab  
**Research Team:**
* Fahad Rahman (ID: 043232000510107, Email: fahadrahman396@gmail.com)
* Shafayat Hossain Shafin (ID: 0432320005101088)
* Zannatul Nayeem (ID: 0432320005101063)
* Reon Ahmed (ID: 0432320005101066)  
**Supervisor / Instructor:** Tahmina Islam, Lecturer, Department of CSE, UITS  
**Repository:** [https://github.com/fahadrahman444/scientific-research-and-methodologies](https://github.com/fahadrahman444/scientific-research-and-methodologies)

---

## 1. Executive Summary / Abstract

Bangladesh's agricultural sector is exceptionally vulnerable to anthropogenic climate change and extreme meteorological anomalies. Over 40% of the national labor force depends on agrarian production, which contributes roughly 12% to the national gross domestic product (GDP). Despite substantial advancements in high-yielding rice varieties, unpredictable monsoon onsets, prolonged dry spells, flash floods, and increasing temperature anomalies pose existential threats to staple food security. This research proposes a comprehensive data-driven investigation examining a 15-year historical window (2009–2024) of weather variability across all eight administrative divisions of Bangladesh and its empirical impact on six foundational crops (Aus Rice, Aman Rice, Boro Rice, Wheat, Potato, and Jute). By synthesizing meteorological time series (from the Bangladesh Meteorological Department and NASA POWER) with longitudinal district-level agricultural output records (from the Bangladesh Bureau of Statistics), we build a robust analytical and predictive pipeline. We benchmark conventional statistical regressions against non-linear ensemble algorithms (Random Forest, XGBoost, CatBoost, LightGBM) and deep sequential models (LSTM). To eliminate the "black box" nature of machine learning in environmental decision-making, we apply SHapley Additive exPlanations (SHAP) to isolate critical climatic thresholds during vegetative and reproductive crop stages. All computational experiments and model training workflows are structured for seamless execution on Google Colab.

---

## 2. Research Problem Statement

While macro-level climate trends in South Asia are documented, the localized, non-linear interaction between multi-variable weather anomalies and crop-specific phenological vulnerability remains under-explored across Bangladesh's heterogeneous agro-ecological zones. Existing agricultural econometric literature typically suffers from three fundamental shortcomings:
1. **Linearity Assumption:** Reliance on ordinary least squares (OLS) regressions fails to capture threshold-dependent crop stress (e.g., heat shock exceeding 35°C during anthesis or sudden rainfall deficit during grain filling).
2. **Spatial Aggregation:** Studies often aggregate national figures, ignoring vast regional disparities between the drought-prone northwestern Barind tract, the flood-susceptible northeastern Haor basins, and the saline southern coastal belt.
3. **Lack of Explainable Machine Learning:** Contemporary AI studies frequently report accuracy metrics without providing actionable agronomic explanations or seasonal sensitivity matrices that extension officers and policy planners can act upon.

---

## 3. Research Objectives

* **Objective 1:** Formulate and curate a standardized 15-year (2009–2024) longitudinal spatiotemporal dataset linking multi-station meteorological records (temperature, rainfall, humidity, sunshine duration) with regional yields of six staple crops across all eight divisions.
* **Objective 2:** Conduct rigorous exploratory and inferential statistical analysis (Mann-Kendall trend tests, Sen's slope estimation, and Standardized Precipitation Index) to quantify 15-year climate shifts and seasonal weather anomalies.
* **Objective 3:** Implement, tune, and evaluate machine learning regression algorithms (Random Forest, XGBoost, CatBoost, LightGBM) and deep learning sequential models (LSTM) within Google Colab to forecast crop yield deviations with high predictive accuracy ($R^2$, RMSE, MAE).
* **Objective 4:** Deploy explainable AI techniques (SHAP values and feature importance ranking) to identify specific weather drivers governing yield volatility per crop and formulate data-driven adaptation recommendations.

---

## 4. Research Questions (RQs)

* **RQ1:** How have key meteorological parameters (mean maximum/minimum temperature, erratic monsoon precipitation, sunshine duration, and drought indices) varied across the eight administrative divisions of Bangladesh over the past 15 years?
* **RQ2:** What are the statistically significant correlations and non-linear dependencies between localized seasonal weather anomalies and the productivity of major rice (Aus, Aman, Boro) and non-rice crops?
* **RQ3:** Which machine learning or deep learning architecture yields the lowest prediction error and highest generalization ability when modeling crop yields across diverse agro-ecological conditions?
* **RQ4:** Which climatic features exert the highest marginal contribution on crop yield reductions according to SHAP explainability analysis, and during which phenological stages are crops most sensitive?

---

## 5. Research Hypotheses

* **$H_1$ (Climate Trend Hypothesis):** There is a statistically significant increasing trend in minimum night-time temperatures ($T_{min}$) and an increased variability in monsoon precipitation patterns across Bangladesh over the 15-year period ($p < 0.05$).
* **$H_2$ (Climatic Vulnerability Hypothesis):** Temperature anomalies exceeding $+1.5^\circ\text{C}$ above the 15-year baseline during the flowering stage and precipitation deficits during the tillering stage correlate with statistically significant decreases in Aman and Boro rice yields ($p < 0.01$).
* **$H_3$ (Model Superiority Hypothesis):** Non-linear gradient boosted ensembles (XGBoost / CatBoost) and sequential architectures (LSTM) will outperform traditional multiple linear regression by achieving a higher coefficient of determination ($R^2 > 0.85$) and significantly lower Root Mean Square Error (RMSE).
* **$H_4$ (Explainability Hypothesis):** SHAP value interpretations will reveal that heat stress ($T_{max}$) during the reproductive window is the single most dominant negative factor for Rabi season crops (Boro, Wheat, Potato), whereas precipitation distribution is the dominant driver for Kharif crops (Aus, Aman).

---

## 6. Significance & Expected Deliverables

1. **Academic Contribution:** An end-to-end, reproducible, open-source pipeline demonstrating how machine learning and explainable AI can model complex climate-crop dynamics in developing nations.
2. **Policy Relevance:** Quantified vulnerability indices to guide the Bangladesh Department of Agricultural Extension (DAE) and Bangladesh Rice Research Institute (BRRI) in regional crop planning.
3. **Course Deliverables:**
   * Fully functional GitHub repository with 4 modular Google Colab notebooks.
   * Comprehensive IEEE Transactions-style research paper ready for submission.
   * Complete presentation slide decks for Week 8 progress evaluation and Week 14 final viva voce.
