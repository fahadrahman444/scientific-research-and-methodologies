# Systematic Literature Review: Weather Variability and Crop Yields in Bangladesh

---

## 1. Introduction and Thematic Organization

This systematic literature review synthesizes prior research across four interdependent pillars:
1. **Pillar 1:** Meteorological trends and climate variability in Bangladesh (BMD, IPCC, empirical time series).
2. **Pillar 2:** Econometric and statistical modeling of climate-crop interactions (Just-Pope production functions, OLS, panel regressions).
3. **Pillar 3:** Machine Learning and Deep Learning architectures for agricultural yield estimation.
4. **Pillar 4:** Explainable Artificial Intelligence (XAI) and decision-support systems for climate adaptation.

---

## 2. Comparative Synthesis of Key Benchmark Literature

| Study | Methodology / Architecture | Spatial & Temporal Scope | Target Crops | Key Findings & Limitations |
| :--- | :--- | :--- | :--- | :--- |
| **Sarker et al. (2012, 2014)** | Feasible Generalized Least Squares (FGLS), Cobb-Douglas | Bangladesh National & Sub-national (1972–2009) | Aus, Aman, Boro Rice | Minimum temperature has a positive impact on Aman but maximum temperature negatively affects Boro. *Limitation:* Linear econometric model unable to handle extreme non-linear weather shocks. |
| **Shahid (2010)** | Mann-Kendall Test, Sen's Slope | 34 BMD stations (1958–2007) | Meteorological (Precipitation) | Significant increase in pre-monsoon and monsoon rainfall across western zones; increased frequency of dry spells. *Limitation:* Did not model crop yield response. |
| **Alamgir et al. (2015)** | Standardized Precipitation Index (SPI-3, SPI-6) | 27 weather stations (1961–2010) | Drought hazard | Northwestern divisions (Rajshahi, Rangpur) experience recurrent severe meteorological droughts during Rabi season. |
| **Rahman et al. (2018)** | Ordinary Least Squares (OLS) & Multiple Linear Regression | 7 divisions (1980–2014) | Rice, Wheat, Potato | Rising temperatures and shifting monsoon onset reduce wheat and potato productivity by 8–12%. *Limitation:* High collinearity between temperature and solar radiation not resolved. |
| **Nasir et al. (2020)** | Systematic Review of ML in Agri-Tech | Global Meta-Analysis | Multi-crop | Ensemble tree algorithms (Random Forest, XGBoost) consistently outperform linear regressions in RMSE by 22–38%. |
| **Khaki & Wang (2019)** | Deep Neural Networks (DNN), CNN-LSTM | US Midwest (30 years) | Maize, Soybean | Deep architectures model complex environmental interactions effectively when temporal sequencing is preserved. |
| **Chowdhury et al. (2021)** | Autoregressive Distributed Lag (ARDL) Model | Bangladesh (1988–2018) | Boro Rice | Confirmed long-run cointegration between climatic variables and Boro output; irrigation acted as a major buffer against drought. |
| **Proposed Research (2026)** | **Gradient Boosting (XGBoost, CatBoost, LightGBM) + Sequential LSTM + SHAP Explainability** | **8 Divisions of Bangladesh (2009–2024, 15-Year Longitudinal)** | **Aus, Aman, Boro Rice, Wheat, Potato, Jute** | **Resolves non-linearity, incorporates regional division stratification, evaluates drought/heat indices, and unpacks feature thresholds via XAI in Google Colab.** |

---

## 3. Identification of Critical Research Gaps

1. **Gap 1: Absence of Recent 15-Year High-Resolution Spatiotemporal Analysis.** Most peer-reviewed literature terminates historical analysis around 2012–2016, omitting the unprecedented weather anomalies of the 2018–2024 period (historic heatwaves in 2023–2024 and aberrant cyclones).
2. **Gap 2: Crop Multiplicity Beyond Monoculture Rice.** The vast majority of studies focus exclusively on Boro and Aman rice, largely ignoring other vital nutritional and economic crops like Wheat, Potato, and Jute.
3. **Gap 3: The "Black Box" Barrier in Precision Agriculture.** While contemporary computer science papers apply deep learning, they routinely fail to extract physiological thresholds (e.g., specific temperatures and rainfall bounds) that agronomists require. Incorporating SHAP bridges this crucial research gap.
