# Bangladesh Agricultural & Weather Dataset Sources

This directory documents the primary repositories, institutional datasets, and retrieval protocols for conducting 15-year weather-crop analytics in Bangladesh.

---

## 1. Official Meteorological Data Sources

### A. Bangladesh Meteorological Department (BMD)
* **Website:** [http://bmd.gov.bd](http://bmd.gov.bd)
* **Stations:** 35 Synoptic Weather Stations covering all 8 administrative divisions (Dhaka, Chittagong, Cox's Bazar, Rajshahi, Ishwardi, Bogra, Rangpur, Dinajpur, Khulna, Jessore, Barishal, Sylhet, Srimangal, Mymensingh, etc.).
* **Recorded Parameters:**
  * Daily Maximum Temperature ($T_{max}$, °C)
  * Daily Minimum Temperature ($T_{min}$, °C)
  * Daily Total Rainfall ($P$, mm)
  * Relative Humidity ($RH$, % at 00, 03, 12 UTC)
  * Sunshine Duration (Hours/day from Campbell-Stokes recorders)

### B. NASA Prediction of Worldwide Energy Resources (POWER)
* **Website:** [https://power.larc.nasa.gov](https://power.larc.nasa.gov)
* **API / Web Portal:** Global $0.5^\circ \times 0.5^\circ$ daily satellite and assimilation model data.
* **Relevant Features:**
  * All-Sky Surface Incident Shortwave Solar Radiation (`ALLSKY_SFC_SW_DWN`, $\text{MJ/m}^2/\text{day}$)
  * Wind Speed at 2 Meters (`WS2M`, m/s)
  * Dew/Frost Point Temperature (`T2MDEW`, °C)

---

## 2. Official Agricultural Output Data Sources

### A. Bangladesh Bureau of Statistics (BBS) — Agriculture Wing
* **Website:** [http://bbs.gov.bd](http://bbs.gov.bd)
* **Annual Publications:** *Yearbook of Agricultural Statistics of Bangladesh* (Published annually from 2009 to 2024).
* **Metrics:** Harvested Acreage (Acres/Hectares), Total Production (Metric Tons), and Yield Rate per Hectare (MT/ha) across all 64 districts.
* **Target Crops:**
  1. Aus Rice (Harvested July–August)
  2. Aman Rice (Harvested November–January, primarily rainfed)
  3. Boro Rice (Harvested April–June, intensive winter irrigation)
  4. Wheat (Harvested March–April)
  5. Potato (Harvested February–March)
  6. Jute (Harvested July–September)

### B. Department of Agricultural Extension (DAE) & BADC
* **Website:** [http://dae.gov.bd](http://dae.gov.bd)
* **Ancillary Data:** Irrigation coverage, deep/shallow tubewell counts, chemical fertilizer allocation (Urea, TSP, MoP, Gypsum).

---

## 3. Dataset Generation & Reproducibility Script

For local simulation and instant Colab notebook execution, execute:
```bash
python data/processed/generate_synthetic_bangladesh_data.py
```
This generates `data/processed/bangladesh_weather_crop_15yr_processed.csv` adhering to actual historical agro-climatic parameters, division trends, and BBS yield ranges.
