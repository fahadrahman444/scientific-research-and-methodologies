# Data Dictionary: 15-Year Weather & Crop Yield Dataset (Bangladesh)

This data dictionary outlines the metadata, variable definitions, units of measurement, primary source institutions, and acceptable ranges for all features utilized in this research study.

---

## 1. Spatial & Temporal Identifiers

| Feature Name | Data Type | Units / Encoding | Description | Source |
| :--- | :--- | :--- | :--- | :--- |
| `year` | Integer | Calendar Year [2009–2024] | Annual harvest/observation cycle over the 15-year study window | BBS / BMD |
| `division` | Categorical | 8 Administrative Divisions | Dhaka, Chittagong, Rajshahi, Rangpur, Khulna, Barishal, Sylhet, Mymensingh | Govt of Bangladesh |
| `division_id` | Integer | [0 to 7] | Numeric index assigned for categorical machine learning embedding | Internal Schema |
| `crop` | Categorical | 6 Agricultural Commodities | Aus Rice, Aman Rice, Boro Rice, Wheat, Potato, Jute | BBS |
| `crop_season` | Categorical | Rabi, Kharif-1, Kharif-2 | Agro-climatic growing season | DAE / BBS |

---

## 2. Meteorological Variables (Independent Variables)

| Feature Name | Data Type | Unit | Range | Description | Primary Source |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `temp_max_mean` | Float | °C | 25.0 – 42.0 | Seasonal mean of daily maximum temperatures | BMD (35 Synoptic Stations) |
| `temp_min_mean` | Float | °C | 9.0 – 28.0 | Seasonal mean of daily minimum temperatures | BMD |
| `temp_mean` | Float | °C | 18.0 – 34.0 | Arithmetic mean of daily temperatures: $(T_{max} + T_{min})/2$ | BMD |
| `rainfall_total_mm`| Float | mm | 50.0 – 3500.0 | Cumulative precipitation accumulated over the crop growth cycle | BMD Rain Gauges |
| `rainfall_days` | Integer | Days | 5 – 120 | Count of rainy days ($> 2.5\text{ mm}$ precipitation) during season | BMD |
| `humidity_mean` | Float | % | 50.0 – 95.0 | Mean relative atmospheric humidity | BMD |
| `sunshine_hours_mean`| Float | Hours/Day | 2.5 – 10.5 | Daily average bright sunshine hours (Campbell-Stokes recorder) | BMD |
| `solar_radiation_mj`| Float | $\text{MJ/m}^2/\text{day}$| 12.0 – 24.0 | Daily incident shortwave solar radiation | NASA POWER |
| `wind_speed_ms` | Float | m/s | 0.8 – 6.5 | Mean horizontal wind speed at 2m height | BMD / ERA5 |

---

## 3. Agro-Climatic & Engineered Features

| Feature Name | Data Type | Unit | Range | Description | Formula / Derivation |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `gdd` | Float | °C-days | 800 – 3200 | Growing Degree Days accumulated over crop growing cycle | $\sum \max(\frac{T_{max}+T_{min}}{2} - T_{base}, 0)$ |
| `spi_3month` | Float | Z-score | -3.5 – +3.5 | 3-Month Standardized Precipitation Index (Drought / Excess Water) | Fitted 2-parameter Gamma distribution |
| `heat_stress_days`| Integer | Days | 0 – 45 | Number of days where $T_{max} \ge 35^\circ\text{C}$ during critical anthesis | Threshold count |
| `dry_spells_count`| Integer | Count | 0 – 8 | Number of consecutive dry sequences ($\ge 7$ consecutive days without rain) | Run-length analysis |
| `temp_anomaly` | Float | °C | -2.5 – +3.0 | Deviation of seasonal temperature from 15-year historical division baseline | $T_{season} - \overline{T}_{division, 15yr}$ |
| `rainfall_anomaly_pct`| Float | % | -70.0 – +150.0 | Percentage deviation of seasonal rainfall from 15-year divisional norm | $\frac{P_{season} - \overline{P}_{15yr}}{\overline{P}_{15yr}} \times 100$ |

---

## 4. Agronomic & Moderating Variables

| Feature Name | Data Type | Unit | Range | Description | Source |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `irrigated_area_pct`| Float | % | 5.0 – 95.0 | Percentage of net cultivable area equipped with mechanical irrigation | BBS / BADC |
| `fertilizer_npk_kgha`| Float | kg/ha | 120.0 – 350.0 | Total chemical fertilizer applied (Nitrogen, Phosphorus, Potassium) | DAE |
| `hyv_adoption_pct` | Float | % | 40.0 – 99.0 | Adoption proportion of High-Yielding and Hybrid varieties | BRRI / BARI / BBS |

---

## 5. Target Variable (Dependent Variable)

| Feature Name | Data Type | Unit | Range | Description | Source |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `yield_mt_ha` | Float | Metric Tons/Hectare (MT/ha) | 0.8 – 35.0 | Standardized agricultural crop yield output per unit harvested area | Bangladesh Bureau of Statistics (BBS) Yearbooks of Agricultural Statistics |

*Note on crop-specific expected yield ranges:*
* *Aus Rice:* 1.5 – 3.2 MT/ha
* *Aman Rice:* 2.0 – 3.8 MT/ha
* *Boro Rice:* 3.5 – 5.2 MT/ha
* *Wheat:* 1.8 – 3.6 MT/ha
* *Potato:* 15.0 – 32.0 MT/ha
* *Jute:* 1.6 – 2.8 MT/ha
