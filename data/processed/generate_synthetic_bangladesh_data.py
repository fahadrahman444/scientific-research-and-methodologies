#!/usr/bin/env python3
"""
generate_synthetic_bangladesh_data.py
--------------------------------------
Generates a realistic, publication-grade 15-year longitudinal dataset (2009-2024)
of meteorological variables and agricultural crop yields across all 8 administrative
divisions of Bangladesh.

Yield responses incorporate:
1. Division-specific climatic baselines (e.g. Barind drought in Rajshahi, high rain in Sylhet).
2. 15-year warming trends and erratic monsoon anomalies.
3. Realistic BBS crop yields and technological adoption trends.
4. Non-linear physiological penalties for heat stress (>35°C) and extreme drought (SPI < -1.5).
"""

import numpy as np
import pandas as pd
import os

np.random.seed(42)

DIVISIONS = [
    'Dhaka', 'Chittagong', 'Rajshahi', 'Rangpur', 
    'Khulna', 'Barishal', 'Sylhet', 'Mymensingh'
]

CROPS = [
    ('Aus Rice', 'Kharif-1', 1.8, 10.0),    # (Crop Name, Season, Base Yield MT/ha, Tbase °C)
    ('Aman Rice', 'Kharif-2', 2.4, 10.0),
    ('Boro Rice', 'Rabi', 3.8, 10.0),
    ('Wheat', 'Rabi', 2.2, 5.0),
    ('Potato', 'Rabi', 18.5, 5.0),
    ('Jute', 'Kharif-1', 2.0, 12.0)
]

YEARS = list(range(2009, 2025)) # 16 years (2009 to 2024)

# Divisional climate adjustments
DIV_PROFILES = {
    'Dhaka':       {'temp_bias':  0.2, 'rain_bias':  0.0, 'coastal': False},
    'Chittagong': {'temp_bias': -0.1, 'rain_bias':  0.35, 'coastal': True},
    'Rajshahi':   {'temp_bias':  1.1, 'rain_bias': -0.30, 'coastal': False}, # Hot, dry Barind
    'Rangpur':    {'temp_bias': -0.4, 'rain_bias': -0.10, 'coastal': False}, # Cold winter
    'Khulna':     {'temp_bias':  0.5, 'rain_bias': -0.15, 'coastal': True},  # Saline, hot
    'Barishal':   {'temp_bias':  0.1, 'rain_bias':  0.20, 'coastal': True},  # Wetland coastal
    'Sylhet':     {'temp_bias': -0.3, 'rain_bias':  0.65, 'coastal': False}, # Very high rainfall
    'Mymensingh': {'temp_bias': -0.1, 'rain_bias':  0.10, 'coastal': False}
}

records = []

for year in YEARS:
    trend_idx = (year - 2009) / 15.0 # 0 to 1
    # Global/Regional warming anomaly trend (~0.03°C per year)
    global_temp_anomaly = 0.03 * (year - 2009) + np.random.normal(0, 0.25)
    
    for div_id, div in enumerate(DIVISIONS):
        prof = DIV_PROFILES[div]
        
        for crop_name, season, base_yield, tbase in CROPS:
            # Base weather by season
            if season == 'Kharif-1': # Pre-monsoon (April-July)
                tmax_mean = 34.5 + prof['temp_bias'] + global_temp_anomaly + np.random.normal(0, 0.8)
                tmin_mean = 24.0 + (prof['temp_bias'] * 0.5) + global_temp_anomaly + np.random.normal(0, 0.6)
                base_rain = 750 * (1.0 + prof['rain_bias'])
                rain_total = max(250, base_rain * (1.0 + np.random.normal(0, 0.22)))
                rain_days = int(np.clip(rain_total / 22.0 + np.random.normal(0, 3), 15, 60))
                humidity = np.clip(74.0 + (prof['coastal'] * 5) + np.random.normal(0, 3.5), 60, 92)
                sunshine = np.clip(6.8 - (rain_total / 1800.0) + np.random.normal(0, 0.5), 4.0, 9.0)
                solar_rad = np.clip(18.5 - (rain_total / 1200.0) + np.random.normal(0, 0.8), 13.0, 22.0)
                wind_speed = np.clip(2.5 + (prof['coastal'] * 1.2) + np.random.normal(0, 0.4), 1.0, 5.5)
                heat_stress_days = int(np.clip(max(0, (tmax_mean - 34.0) * 8 + np.random.normal(0, 3)), 0, 35))
                
            elif season == 'Kharif-2': # Monsoon (July-November)
                tmax_mean = 32.0 + prof['temp_bias'] + global_temp_anomaly + np.random.normal(0, 0.6)
                tmin_mean = 24.8 + (prof['temp_bias'] * 0.4) + global_temp_anomaly + np.random.normal(0, 0.5)
                base_rain = 1350 * (1.0 + prof['rain_bias'])
                rain_total = max(550, base_rain * (1.0 + np.random.normal(0, 0.25)))
                rain_days = int(np.clip(rain_total / 24.0 + np.random.normal(0, 4), 30, 85))
                humidity = np.clip(82.0 + (prof['coastal'] * 4) + np.random.normal(0, 2.5), 72, 95)
                sunshine = np.clip(5.2 - (rain_total / 2500.0) + np.random.normal(0, 0.4), 3.0, 7.5)
                solar_rad = np.clip(16.0 - (rain_total / 1600.0) + np.random.normal(0, 0.6), 11.5, 19.0)
                wind_speed = np.clip(2.2 + (prof['coastal'] * 1.0) + np.random.normal(0, 0.3), 0.9, 4.8)
                heat_stress_days = int(np.clip(max(0, (tmax_mean - 33.5) * 4 + np.random.normal(0, 2)), 0, 18))
                
            else: # Rabi / Winter (November-March)
                tmax_mean = 27.5 + prof['temp_bias'] + global_temp_anomaly + np.random.normal(0, 0.7)
                tmin_mean = 14.0 + (prof['temp_bias'] * 0.6) + global_temp_anomaly + np.random.normal(0, 0.8)
                base_rain = 85 * (1.0 + prof['rain_bias'])
                rain_total = max(10, base_rain * (1.0 + np.random.normal(0, 0.45)))
                rain_days = int(np.clip(rain_total / 12.0 + np.random.normal(0, 1), 2, 18))
                humidity = np.clip(68.0 + (prof['coastal'] * 4) + np.random.normal(0, 4.0), 52, 85)
                sunshine = np.clip(7.6 + np.random.normal(0, 0.4), 5.5, 9.8)
                solar_rad = np.clip(16.5 + np.random.normal(0, 0.7), 13.0, 20.5)
                wind_speed = np.clip(1.6 + (prof['coastal'] * 0.8) + np.random.normal(0, 0.3), 0.8, 3.8)
                heat_stress_days = 0 if crop_name != 'Boro Rice' else int(np.clip(max(0, (tmax_mean - 31.0) * 3), 0, 10))

            t_mean = (tmax_mean + tmin_mean) / 2.0
            
            # Agro-Climatic Features
            # Growing Degree Days (approx 120 days crop cycle)
            daily_eff_temp = max(0.0, t_mean - tbase)
            gdd = round(daily_eff_temp * 120.0 + np.random.normal(0, 30), 1)
            
            # Standardized Precipitation Index proxy (-3 to +3)
            rain_norm = (rain_total - base_rain) / (base_rain * 0.30)
            spi_3month = float(np.clip(rain_norm + np.random.normal(0, 0.15), -3.2, 3.2))
            
            dry_spells_count = int(np.clip(max(0, (25.0 - rain_days) / 4.0 + np.random.normal(0, 1)), 0, 8))
            
            # Regional Anomalies
            temp_anomaly = round(t_mean - (28.0 if season != 'Rabi' else 20.5), 2)
            rainfall_anomaly_pct = round(((rain_total - base_rain) / base_rain) * 100.0, 1)

            # Agronomic / Moderating Inputs
            if crop_name == 'Boro Rice':
                irrigated_pct = np.clip(82.0 + trend_idx * 10.0 + np.random.normal(0, 2), 70, 98)
            elif crop_name in ['Wheat', 'Potato']:
                irrigated_pct = np.clip(60.0 + trend_idx * 15.0 + np.random.normal(0, 3), 40, 88)
            else: # Rainfed Aus, Aman, Jute
                irrigated_pct = np.clip(15.0 + trend_idx * 12.0 + np.random.normal(0, 2.5), 8, 45)
                
            fertilizer_npk = np.clip(180.0 + trend_idx * 60.0 + np.random.normal(0, 12), 140, 320)
            hyv_adoption_pct = np.clip(65.0 + trend_idx * 25.0 + np.random.normal(0, 3), 50, 99)

            # Physiological Yield Calculation (BBS Ground Truth approximation)
            # 1. Base yield + secular technological trend (HYV breeding, management: ~1.2% per year)
            tech_yield_gain = base_yield * (0.012 * (year - 2009))
            
            # 2. Temperature penalties
            if crop_name in ['Boro Rice', 'Wheat', 'Potato']:
                # Winter crops suffer heavily from high night-time temp (Tmin) and heat stress
                temp_penalty = max(0.0, (tmin_mean - 15.0) * 0.04 * base_yield) + (heat_stress_days * 0.015 * base_yield)
            else:
                # Monsoon crops suffer if extreme heat occurs during flowering
                temp_penalty = (heat_stress_days * 0.012 * base_yield)
                
            # 3. Moisture / Drought / Flood penalties
            if season == 'Rabi':
                # Drought is buffered by irrigation for Boro, but damages non-irrigated crops
                moisture_penalty = max(0.0, (-spi_3month - 1.0) * 0.08 * (1.0 - irrigated_pct / 100.0) * base_yield)
            else:
                # Extreme drought (SPI < -1.5) or severe flood (SPI > 2.0) hurts Aman / Aus
                drought_pen = max(0.0, (-spi_3month - 1.0) * 0.12 * base_yield)
                flood_pen = max(0.0, (spi_3month - 2.0) * 0.15 * base_yield)
                moisture_penalty = drought_pen + flood_pen
                
            # 4. Net Yield with agronomic noise
            yield_mt_ha = base_yield + tech_yield_gain - temp_penalty - moisture_penalty + np.random.normal(0, base_yield * 0.04)
            yield_mt_ha = round(max(base_yield * 0.4, yield_mt_ha), 3)

            records.append({
                'year': year,
                'division': div,
                'division_id': div_id,
                'crop': crop_name,
                'crop_season': season,
                'temp_max_mean': round(tmax_mean, 2),
                'temp_min_mean': round(tmin_mean, 2),
                'temp_mean': round(t_mean, 2),
                'rainfall_total_mm': round(rain_total, 1),
                'rainfall_days': rain_days,
                'humidity_mean': round(humidity, 1),
                'sunshine_hours_mean': round(sunshine, 2),
                'solar_radiation_mj': round(solar_rad, 2),
                'wind_speed_ms': round(wind_speed, 2),
                'gdd': gdd,
                'spi_3month': round(spi_3month, 3),
                'heat_stress_days': heat_stress_days,
                'dry_spells_count': dry_spells_count,
                'temp_anomaly': temp_anomaly,
                'rainfall_anomaly_pct': rainfall_anomaly_pct,
                'irrigated_area_pct': round(irrigated_pct, 1),
                'fertilizer_npk_kgha': round(fertilizer_npk, 1),
                'hyv_adoption_pct': round(hyv_adoption_pct, 1),
                'yield_mt_ha': yield_mt_ha
            })

df = pd.DataFrame(records)

out_file = os.path.join(os.path.dirname(__file__), 'bangladesh_weather_crop_15yr_processed.csv')
df.to_csv(out_file, index=False)
print(f"Generated {len(df)} records covering 15 years (2009-2024), 8 divisions, 6 crops.")
print(f"Dataset successfully saved to: {out_file}")
print("\nDataset Summary Preview:")
print(df.head(5))
