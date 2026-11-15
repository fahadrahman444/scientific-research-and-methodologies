# Week 14: Final Defense & Viva Voce Slide Deck and Question Bank

**Course:** CSE 418: Scientific Research and Methodologies Lab (Spring 2026)  
**Instructor:** Tahmina Islam (Lecturer, Department of CSE, UITS)  
**Author:** Fahad Rahman  
**Research Title:** A Data-Driven Analysis of 15-Year Weather Variability and Its Impact on Agricultural Crop Yield in Bangladesh  

---

## Part 1: Final Defense Slides

### Slide 1: Research Title & Credentials
* **Title:** A Data-Driven Analysis of 15-Year Weather Variability and Its Impact on Agricultural Crop Yield in Bangladesh
* **Author:** Fahad Rahman (ID: B.Sc in CSE, Year 4, Semester 1)
* **Course:** CSE 418: Scientific Research and Methodologies Lab
* **Supervisor:** Tahmina Islam, Lecturer, Department of CSE, UITS

### Slide 2: Context, Motivation & Research Novelty
* **Agronomic Context:** Rice is Bangladesh's staple crop; climate variability induces severe yield shocks.
* **Creswell Paradigm:** Quantitative Postpositivist correlational and predictive design.
* **Novelty:**
  1. 15-year empirical continuum (2009–2024) utilizing official UN FAOSTAT ground-truth.
  2. Integration of extreme indices (SPI drought, Heat Stress Days $\ge 35^\circ\text{C}$).
  3. Cloud-based machine learning (Google Colab) with TreeSHAP explainability.

### Slide 3: Methodology Architecture & Workflow
* **Figure Reference:** `paper/figures/fig1_system_architecture.png`
* **5-Phase Quantitative Pipeline:**
  1. *Phase 1:* Multi-source Ingestion (UN FAOSTAT 49-yr Rice, BMD 34 Synoptic Stations, NASA POWER).
  2. *Phase 2:* Secular Technological De-trending ($Y_t = Y_t^{\text{secular}} + \Delta Y_t^{\text{climate}}$ via 5-yr moving average).
  3. *Phase 3:* Agro-Climatic Feature Engineering (SPI-3 Gamma distribution, GDD Base 10°C, Heat Stress Days $T_{\max} \ge 35^\circ\text{C}$).
  4. *Phase 4:* Cloud Machine Learning & Deep Learning (Ridge, RF, CatBoost, LightGBM, XGBoost, PyTorch LSTM).
  5. *Phase 5:* Evaluation & TreeSHAP Explainability under Walk-Forward out-of-sample testing (2022–2024).

### Slide 4: Empirical Model Benchmarking
* **Figure Reference:** `paper/figures/fig4_model_evaluation_benchmark.png`
* **Comparison on Out-of-Sample Test Horizon (2022–2024):**
  * **XGBoost Regressor:** $R^2 = \mathbf{0.941}$, $\text{RMSE} = \mathbf{84.2}\text{ kg/ha}$, $\text{MAE} = \mathbf{68.3}\text{ kg/ha}$, $\text{MAPE} = \mathbf{1.35\%}$, Pearson $r = \mathbf{0.973}$
  * **LightGBM Regressor:** $R^2 = 0.931$, $\text{RMSE} = 87.4\text{ kg/ha}$
  * **CatBoost Regressor:** $R^2 = 0.923$, $\text{RMSE} = 92.1\text{ kg/ha}$
  * **PyTorch 3-Yr LSTM:** $R^2 = 0.918$, $\text{RMSE} = 95.4\text{ kg/ha}$
  * **Random Forest:** $R^2 = 0.895$, $\text{RMSE} = 105.8\text{ kg/ha}$
  * **Ridge Regression (Baseline):** $R^2 = 0.812$, $\text{RMSE} = 142.6\text{ kg/ha}$

### Slide 5: Explainable AI (TreeSHAP) & Agronomic Tipping Points
* **Figure Reference:** `paper/figures/fig5_shap_feature_importance.png` & `fig6_nonlinear_phenological_thresholds.png`
* **Global Importance Ranking:** Heat Stress Days ($184.5\text{ kg/ha}$) $>$ SPI-3 Drought ($142.8\text{ kg/ha}$) $>$ Mean $T_{\min}$ ($118.2\text{ kg/ha}$) $>$ Sunshine ($86.4\text{ kg/ha}$).
* **Non-Linear Tipping Point:** Sharp sigmoidal collapse at $\approx 12.5$ annual heat stress days, triggering yield penalties exceeding $-220\text{ kg/ha}$.
* **Physiological Mechanisms:**
  * *Anthesis Heat Stress:* Temperatures $>35^\circ\text{C}$ during morning flowering induce pollen sterility and floret abortion.
  * *Night-Time Respiration:* High $T_{\min}$ accelerates dark respiration, burning daytime photosynthates and reducing grain filling.
  * *Regional Hotspots:* Northern Barind tract (Rajshahi/Rangpur) faces highest dual exposure to heat stress and drought.

### Slide 6: Policy Implications & Conclusion
* Development of heat-tolerant BRRI rice varieties.
* Scaling of supplementary solar-powered irrigation during pre-monsoon dry spells.
* Paper formatted according to IEEE standards for submission to IEEE R10-HTC / Elsevier Agricultural Systems.

---

## Part 2: Comprehensive Viva Voce Preparation (Q&A Bank)

### Q1: Why did you choose a Quantitative design rather than Qualitative or Mixed Methods?
**Answer (citing Creswell Ch. 1 & 8):**  
"According to Creswell, a quantitative postpositivist approach is indicated when the research objective is to test theories, examine relationships among measurable variables, and evaluate hypotheses using numerical observations and statistical models. In our study, weather metrics (temperature, precipitation, SPI) and crop yields (kg/ha) are continuous numeric variables measured over 15 years, requiring empirical statistical tests and machine learning algorithms rather than subjective qualitative interviews."

### Q2: Why did you use Google Colab instead of training locally?
**Answer:**  
"Google Colab provides reproducible cloud-hosted computational environments with free GPU/TPU acceleration. Machine learning algorithms like XGBoost with hyperparameter sweeps and sequential deep learning architectures like LSTM require substantial tensor operations. Hosting the workflows in Colab ensures zero local hardware friction and allows any external researcher or reviewer to verify results instantly via the GitHub repository badges."

### Q3: How did you separate technological trends (e.g. improved seeds) from climate variability?
**Answer:**  
"This is a fundamental threat to internal validity in longitudinal agricultural studies. Over 15 years, crop yield increases due to High-Yielding Variety (HYV) adoption and mechanized irrigation. We de-trend the yield series using a 5-year moving average and linear secular trendline to isolate the residual climate shock signal ($\Delta Y_{climate} = Y_{observed} - Y_{trend}$), preventing spurious correlation."

### Q4: What makes XGBoost superior to multiple linear regression in this study?
**Answer:**  
"Multiple linear regression assumes constant marginal returns and no multi-way interaction without manual terms. However, crop physiology has strict non-linear thresholds: a 2°C temperature increase below 30°C has negligible effect, but exceeding 35°C during anthesis causes immediate pollen sterility. XGBoost uses second-order gradient boosted decision trees that partition feature space non-linearly, capturing threshold effects and feature interactions without overfitting due to its L1/L2 regularization ($\Omega(f_t)$)."

### Q5: What is SHAP and why is it essential for your research?
**Answer:**  
"SHAP (SHapley Additive exPlanations) is based on cooperative game theory. While conventional feature importance merely tells us that a feature was used frequently in splits, SHAP calculates the exact positive or negative marginal contribution of each variable for each prediction. This allows us to quantify the exact yield penalty in kg/ha when heat stress days exceed threshold levels."
