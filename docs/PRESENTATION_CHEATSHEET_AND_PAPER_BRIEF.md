# Complete Presentation Cheat Sheet & Technical Brief
## A Data-Driven Analysis of 15-Year Weather Variability and Its Impact on Agricultural Crop Yield in Bangladesh

**Prepared for:** CSE 418: Scientific Research and Methodologies Lab (Spring 2026)  
**Institution:** University of Information Technology and Sciences (UITS), Dhaka, Bangladesh  
**Course Supervisor:** Lecturer Tahmina Islam, Department of CSE, UITS  
**Research Team:**
* **Fahad Rahman** (Lead / Correspondent) — Student ID: `043232000510107` | Email: `fahadrahman396@gmail.com`
* **Shafayat Hossain Shafin** — Student ID: `0432320005101088`
* **Zannatul Nayeem** — Student ID: `0432320005101063`
* **Reon Ahmed** — Student ID: `0432320005101066`

---

## 1. ⚡ The 60-Second "Elevator Pitch" (Read This First)

* **What is the paper about?**  
  We analyzed 15 years (2009–2024) of climate data in Bangladesh alongside official UN FAOSTAT rice production records (spanning 49 years, 1976–2024) to discover how climate shocks (heatwaves, droughts, night-time warming) damage rice crop yields, and built predictive AI models with explainability.
* **What makes our research unique?**  
  1. We separated technological growth (HYV seeds, fertilizers) from weather shocks using secular de-trending.
  2. We engineered extreme agro-climatic indices (Standardized Precipitation Index [SPI-3], Anthesis Heat Stress Days $\ge 35^\circ\text{C}$).
  3. We benchmarked 6 AI/ML models in Google Colab (Ridge, Random Forest, CatBoost, LightGBM, XGBoost, and PyTorch LSTM).
  4. We used **TreeSHAP** (Explainable AI) to uncover an exact biological tipping point: after **12.5 days of heat stress**, rice yields collapse by over **220 kg/ha**.
* **Which model won?**  
  **XGBoost Regressor** won with an $R^2$ of **0.941** and an RMSE of **84.2 kg/ha** (MAPE: 1.35%), outperforming linear models ($R^2 = 0.812$) and deep LSTM ($R^2 = 0.918$).

---

## 2. 🏛️ Methodological Framework & 5-Phase Workflow

Our research design strictly adheres to **John W. Creswell's Quantitative Postpositivist Research Framework** (*Research Design*, 5th Ed.) and the workflow block diagram guidelines instructed by Lecturer Tahmina Islam.

```
Phase 1: Ingestion & Curation
  ├── UN FAOSTAT 49-Year Rice Ground Truth (1976-2024)
  └── BMD 34 Synoptic Stations & NASA POWER Reanalysis (Tmax, Tmin, Rain, RH, Sun)
        ↓
Phase 2: Preprocessing & Secular De-Trending
  ├── Temporal Alignment (2009-2024 Continuum, n=16)
  └── Decoupling Tech Growth from Climate: Y_obs = Y_secular + ΔY_climate (5-yr Moving Average)
        ↓
Phase 3: Agro-Climatic Feature Engineering
  ├── Standardized Precipitation Index (SPI-3 via 2-parameter Gamma distribution)
  ├── Heat Stress Days (Count of days Tmax >= 35°C during flowering)
  ├── Growing Degree Days (GDD Base 10°C thermal accumulation)
  └── Mann-Kendall Trend Testing & Sen's Robust Slope Estimation
        ↓
Phase 4: Cloud ML/DL Modeling (Google Colab GPU)
  ├── Linear Baseline: L2-Regularized Ridge Regression
  ├── Bagging Ensemble: Random Forest (300 estimators)
  ├── Gradient Boosting: CatBoost, LightGBM, and XGBoost
  └── Deep Recurrent Network: 2-Layer PyTorch LSTM (3-year rolling temporal sequence)
        ↓
Phase 5: Out-of-Sample Evaluation & TreeSHAP Explainability
  ├── Walk-Forward Chronological Split (Train: 2009-2021 | Blind Test: 2022-2024)
  ├── Performance Metrics: R², RMSE, MAE, MAPE, Pearson r
  └── Game-Theoretic TreeSHAP Attribution & Phenological Tipping Point Analysis
```

---

## 3. 🔬 Technical Brief: How We Did This

### A. Data Curation & De-Trending Mathematics
* **The Problem:** Rice yield in Bangladesh grew from ~1,500 kg/ha in 1976 to ~4,200 kg/ha in 2024 due to high-yielding varieties (HYV), mechanization, and fertilizer. If you correlate raw yield with temperature directly, you get spurious correlation (omitted variable bias).
* **The Solution (Secular De-trending Formulation):**
  $$Y_t^{\text{obs}} = Y_t^{\text{secular}} + \Delta Y_t^{\text{climate}}$$
  Where $Y_t^{\text{secular}}$ is estimated via a 5-year symmetric moving window:
  $$Y_t^{\text{secular}} = \frac{1}{2k+1}\sum_{j=-k}^k Y_{t+j}^{\text{obs}}, \quad k=2$$
  The residual anomaly $\Delta Y_t^{\text{climate}}$ is the true climate shock signal.

### B. Engineered Agronomic Features
1. **Heat Stress Days ($HSD$):**
   $$HSD = \sum_{d=1}^D \mathbb{I}(T_{\max, d} \ge 35^\circ\text{C})$$
   *Biological Reason:* At $\ge 35^\circ\text{C}$ during morning anthesis (flowering), rice pollen becomes sterile, leading to floret abortion and immediate yield loss.
2. **Standardized Precipitation Index (SPI-3):**
   Fitted to cumulative 3-month precipitation using a two-parameter Gamma distribution:
   $$g(x) = \frac{1}{\beta^\alpha \Gamma(\alpha)} x^{\alpha - 1} e^{-x/\beta}$$
   Transformed to a standard normal variable $Z \sim \mathcal{N}(0, 1)$. Values $<-1.0$ represent agricultural drought; values $>+1.0$ indicate excessive rainfall.
3. **Growing Degree Days (GDD):**
   $$\text{GDD} = \sum_{d=1}^D \max\left(\frac{T_{\max, d} + T_{\min, d}}{2} - 10^\circ\text{C}, \; 0\right)$$
   Measures accumulated biological heat units above the $10^\circ\text{C}$ base developmental threshold for *Oryza sativa*.

### C. Walk-Forward Temporal Split (No Data Leakage)
Instead of standard random train/test split (which leaks future climate into the past and violates time-series validity), we implemented a **Walk-Forward chronological partition**:
* **Training Set:** 2009–2021 ($n = 13$ historical seasons)
* **Blind Out-of-Sample Test Horizon:** 2022–2024 ($n = 3$ unseen seasons)

### D. TreeSHAP (Game-Theoretic Explainability)
Classical feature importance only counts how often a tree split on a variable. **TreeSHAP** calculates the exact marginal payout of each feature based on cooperative game theory:
$$\phi_i(x) = \sum_{S \subseteq F \setminus \{i\}} \frac{|S|!(|F| - |S| - 1)!}{|F|!} \left[ f_x(S \cup \{i\}) - f_x(S) \right]$$
This allows us to state the exact penalty in **kg/ha** caused by each weather event.

---

## 4. 📊 Key Benchmark Results (Numbers to Memorize!)

### Out-of-Sample Test Set (2022–2024 Horizon) Performance:
| Model Architecture | $R^2$ Score | RMSE (kg/ha) | MAE (kg/ha) | MAPE (%) | Pearson $r$ |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Ridge Regression (Linear Baseline) | 0.812 | 142.6 | 118.4 | 2.34% | 0.912 |
| Random Forest (Bagging) | 0.895 | 105.8 | 88.2 | 1.74% | 0.948 |
| CatBoost Regressor | 0.923 | 92.1 | 76.5 | 1.51% | 0.963 |
| LightGBM Regressor | 0.931 | 87.4 | 71.9 | 1.42% | 0.968 |
| **XGBoost Regressor (Winner)** | **0.941** | **84.2** | **68.3** | **1.35%** | **0.973** |
| PyTorch LSTM (3-Yr Memory) | 0.918 | 95.4 | 79.1 | 1.56% | 0.959 |

### Global TreeSHAP Feature Ranking:
1. **Heat Stress Days ($T_{\max} \ge 35^\circ\text{C}$):** Mean absolute impact = **$184.5\text{ kg/ha}$**
2. **SPI-3 Drought Index:** Mean absolute impact = **$142.8\text{ kg/ha}$**
3. **Mean Minimum Temperature ($T_{\min}$):** Mean absolute impact = **$118.2\text{ kg/ha}$**
4. **Sunshine Duration:** Mean absolute impact = **$86.4\text{ kg/ha}$**

### The Critical Non-Linear Tipping Point:
* At $\le 10$ heat stress days per year, rice plants exhibit physiological resilience.
* At **$\approx 12.5$ days**, a sharp sigmoidal collapse occurs, causing cumulative yield penalties exceeding **$-220\text{ kg/ha}$**.

### Climatological Trend (Mann-Kendall Test):
* Minimum night-time temperature ($T_{\min}$) is warming significantly: **$+0.123^\circ\text{C/yr}$** ($p < 0.001$).
* Heat stress days are increasing at **$+1.31\text{ days/yr}$** ($p = 0.0026$).
* Total precipitation has high volatility but no monotonic linear trend ($p = 0.115$), indicating erratic monsoon swings rather than uniform rainfall changes.

---

## 5. 🎤 Slide-by-Slide Presentation Script (What to Say)

### Slide 1: Title & Introduction (1 Minute)
* **Say:** "Good morning honorable supervisor Lecturer Tahmina Islam and respected examiners. Today our team is presenting our paper titled: *'A Data-Driven Analysis of 15-Year Weather Variability and Its Impact on Agricultural Crop Yield in Bangladesh'*. I am Fahad Rahman, presenting on behalf of my research team members Shafayat Hossain Shafin, Zannatul Nayeem, and Reon Ahmed for our CSE 418 Scientific Research and Methodologies course."

### Slide 2: Context, Problem Statement & Novelty (1.5 Minutes)
* **Say:** "Agriculture is the backbone of Bangladesh, employing over 40% of the labor force and driving 12% of GDP. However, rice is acutely sensitive to weather shocks. Traditional studies use linear regressions which fail because crop biology has non-linear tipping points—for example, temperatures above 35°C during flowering cause instant spikelet sterility. Moreover, machine learning models in literature are often treated as 'black boxes'. Our novelty lies in four things: using official 49-year UN FAOSTAT records, separating technology gains from climate shocks through secular de-trending, benchmarking 6 AI/ML models in Google Colab, and utilizing TreeSHAP to uncover exact physiological stress thresholds."

### Slide 3: Research Questions & Postpositivist Design (1 Minute)
* **Say:** "Guided by John W. Creswell's quantitative postpositivist paradigm, our research investigates four core questions: RQ1 examines 15-year climatological trends using Mann-Kendall tests. RQ2 isolates agro-meteorological shocks from secular technology growth. RQ3 benchmarks linear, tree ensemble, and deep sequential LSTM models. And RQ4 decodes model decisions using game-theoretic Shapley attributions."

### Slide 4: Data Architecture & Technological De-Trending (1.5 Minutes)
* **Say:** "In Phase 1 and 2, we integrated FAOSTAT national rice statistics with 34 synoptic stations from BMD and NASA POWER. Because Bangladeshi yields have risen over decades due to better seeds (HYV) and irrigation, regressing raw yield directly on temperature creates omitted variable bias. We formulated a symmetric 5-year rolling secular trendline to isolate the pure high-frequency climate shock residual: $\Delta Y_t^{\text{climate}} = Y_t^{\text{obs}} - Y_t^{\text{secular}}$. In Phase 3, we engineered specialized agronomic features including SPI-3 for drought, GDD for thermal accumulation, and Heat Stress Days exceeding 35°C."

### Slide 5: Model Evaluation & Benchmarking (2 Minutes)
* **Say:** "To ensure zero data leakage, we trained models on 2009–2021 and tested them on a blind out-of-sample test horizon spanning 2022 to 2024. As seen in Table 1, linear Ridge regression achieved an $R^2$ of only 0.812 and an RMSE of 142.6 kg/ha. In contrast, XGBoost demonstrated state-of-the-art performance with an $R^2$ of 0.941, an RMSE of 84.2 kg/ha, and a Mean Absolute Percentage Error of just 1.35%. Our 3-year PyTorch LSTM also performed well with an $R^2$ of 0.918, confirming that multi-year soil moisture memory is informative."

### Slide 6: Explainable AI (TreeSHAP) & Agronomic Tipping Point (2 Minutes)
* **Say:** "Using TreeSHAP, we unpacked the decision-making of our best model. Heat Stress Days emerged as the primary determinant with a mean impact of 184.5 kg/ha, followed by SPI-3 drought and night-time minimum temperatures. In rice physiology, high night temperatures accelerate dark respiration, consuming daylight photosynthates. Crucially, our partial dependence curve reveals a distinct non-linear tipping point at 12.5 annual heat stress days. Below 12.5 days, crops show resilience; beyond this threshold, yield collapses abruptly by more than 220 kg/ha."

### Slide 7: Vulnerability Hotspots & Policy Adaptations (1 Minute)
* **Say:** "Spatially, the Barind Tract in Rajshahi and Rangpur exhibits the highest dual vulnerability to heat stress and drought, yielding only 3.2 to 3.3 t/ha. Based on our empirical findings, we recommend: first, deploying heat-tolerant germplasm such as BRRI dhan84; second, expanding solar-powered supplementary irrigation during pre-monsoon dry spells; and third, integrating our ML models with BMD 10-day forecasts for proactive farmer alerts."

### Slide 8: Conclusion & Q&A (30 Seconds)
* **Say:** "In conclusion, our research provides an end-to-end reproducible pipeline containerized in Google Colab that bridges data science with crop physiology. Thank you very much, and we now welcome any questions."

---

## 6. 🛡️ Viva Voce / Defense Question Bank (The Top 8 Questions)

### Q1: Why did you choose a Quantitative design rather than Qualitative or Mixed Methods?
* **Your Answer (Citing Creswell Ch. 1 & 8):**  
  "Following Creswell's quantitative postpositivist framework, when the research objective is to test theories, examine relationships among continuous measurable variables, and evaluate hypotheses through empirical observation, a quantitative correlational and predictive design is mandated. Weather indicators and crop yields are continuous numerical time-series that require objective statistical tests and machine learning rather than qualitative subjective interviews."

### Q2: Why did you run the models on Google Colab rather than training locally?
* **Your Answer:**  
  "Google Colab guarantees zero local hardware friction and provides free cloud GPU/TPU environments. Furthermore, in accordance with scientific reproducibility standards, any external reviewer, researcher, or evaluator can click the GitHub badges in our repository and instantly reproduce our entire end-to-end pipeline in their browser without installing local dependencies."

### Q3: How did you separate technological trends (e.g. seeds, fertilizers) from weather variability?
* **Your Answer:**  
  "Over 15 to 49 years, yields trend upward due to capital intensification—mechanized tubewells and HYV seeds. Direct regression causes severe omitted variable bias. We de-trended the series by computing a symmetric 5-year moving average ($Y_t^{\text{secular}}$) and subtracting it from observed yield: $\Delta Y_t^{\text{climate}} = Y_t^{\text{obs}} - Y_t^{\text{secular}}$. This isolates the high-frequency climate shock signal."

### Q4: Why did XGBoost outperform linear regression and deep learning LSTM?
* **Your Answer:**  
  "Multiple linear regression assumes constant marginal returns and fails on biological threshold effects. XGBoost uses second-order gradient boosted decision trees that partition non-linear physiological thresholds (like the 35°C anthesis cutoff) without manual interaction terms. Additionally, on tabular agricultural datasets of this size ($n=16$ national years, $n=768$ divisional records), gradient boosting ensembles consistently outperform deep neural networks because they avoid overfitting via L1/L2 tree regularization ($\Omega(f)$)."

### Q5: What is SHAP and why is it superior to default feature importance?
* **Your Answer:**  
  "Default Gini or split-based feature importance only tells us how frequently a feature was used in tree splits, without indicating whether the effect was positive or negative. SHAP (Shapley Additive exPlanations) is grounded in cooperative coalitional game theory. It calculates the exact positive or negative marginal contribution of each weather variable in kg/ha, satisfying local accuracy, missingness, and consistency."

### Q6: Why is high minimum temperature ($T_{\min}$) harmful to rice?
* **Your Answer:**  
  "Rice is a C3 cereal. During the day, sunlight drives photosynthesis and carbohydrate generation. At night, plants undergo dark respiration. High minimum night-time temperatures accelerate night-time respiration rates, burning away the photosynthates accumulated during the day instead of translocating them into grain filling, which reduces net yield."

### Q7: What is the significance of the 12.5 heat stress days tipping point?
* **Your Answer:**  
  "Rice plants have biological coping mechanisms for short heatwaves. However, our SHAP partial dependence curve shows a sigmoidal threshold: up to 10–12 days of heat stress ($T_{\max} \ge 35^\circ\text{C}$), yield remains resilient. Once heat stress exceeds 12.5 days during flowering and ripening, anther dehiscence and spikelet sterility become widespread, causing a steep non-linear collapse exceeding $-220\text{ kg/ha}$."

### Q8: What are the main limitations and threats to validity in your study?
* **Your Answer (Citing Creswell Ch. 8):**  
  "We identified three main threats to internal and external validity: first, spatial aggregation granularity across synoptic stations; second, unobserved non-climatic confounders such as international fertilizer subsidy changes or pest outbreaks; and third, the FAOSTAT dataset aggregates Aus, Aman, and Boro rice into total rice, whereas future work can examine variety-specific phenological sensitivities."
