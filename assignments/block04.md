# Block 04 assignment

------------------------------------------------------------------------

------------------------------------------------------------------------

## Data import

Importing required packages:

```{python}
import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
import seaborn as sns
```

Loading data from `.csv` files:

```{python}
# ---- File locations ----
files = {
    'CA_Ca3': 'data/processed/AMF_CA-Ca3_FLUXNET_2001-2024_v1.3_r1/AMF_CA-Ca3_FLUXNET_FLUXMET_HH_2001-2024_v1.3_r1.csv',
    'US_Whs': 'data/processed/AMF_US-Whs_FLUXNET_2007-2025_v1.3_r1/AMF_US-Whs_FLUXNET_FLUXMET_HH_2007-2025_v1.3_r1.csv',
    'CN_Nmn': 'data/processed/CNF_CN-Nmn_FLUXNET_2015-2019_v1.3_r1/CNF_CN-Nmn_FLUXNET_FLUXMET_HH_2015-2019_v1.3_r1.csv',
    'FR_Pue': 'data/processed/ICOS_FR-Pue_FLUXNET_2000-2026_v1.3_r1/ICOS_FR-Pue_FLUXNET_FLUXMET_HH_2000-2026_v1.3_r1.csv',
    'AU_Rig': 'data/processed/TERN_AU-Rig_FLUXNET_2011-2017_v1.3_r1/TERN_AU-Rig_FLUXNET_FLUXMET_HH_2011-2017_v1.3_r1.csv'
}

# ---- Reading data from file locations ----
data = {
    'CA_Ca3': pd.read_csv(
        files['CA_Ca3'],
        na_values=[-9999],
        dtype={"TIMESTAMP_START": str, "TIMESTAMP_END": str}
    ),
    'US_Whs': pd.read_csv(
        files['US_Whs'],
        na_values=[-9999],
        dtype={"TIMESTAMP_START": str, "TIMESTAMP_END": str}
    ),
    'CN_Nmn': pd.read_csv(
        files['CN_Nmn'],
        na_values=[-9999],
        dtype={"TIMESTAMP_START": str, "TIMESTAMP_END": str}
    ),
    'FR_Pue': pd.read_csv(
        files['FR_Pue'],
        na_values=[-9999],
        dtype={"TIMESTAMP_START": str, "TIMESTAMP_END": str}
    ),
    'AU_Rig': pd.read_csv(
        files['AU_Rig'],
        na_values=[-9999],
        dtype={"TIMESTAMP_START": str, "TIMESTAMP_END": str}
    )
}
```

------------------------------------------------------------------------

## Site overview

[Table:]{.underline}

| ID | Name | IGBP | Lat | Lon | Years | Hub | Citation |
|---------|---------|---------|---------|---------|---------|---------|---------|
| CA-Ca3 | British Columbia - Pole sapling Douglas-fir stand | ENF | 49.5346 | -124.9004 | 2001-2024 | AmeriFlux | T. Andrew Black (2026), AmeriFlux FLUXNET-1F CA-Ca3 British Columbia - Pole sapling Douglas-fir stand, Ver. v1.3_r1 (2001-2024), AmeriFlux AMP, (Dataset). <https://doi.org/10.17190/AMF/3027312> |
| US-Whs | Walnut Gulch Lucky Hills Shrub | OSH | 31.7438 | -110.0522 | 2007-2025 | AmeriFlux | Russ Scott (2026), AmeriFlux FLUXNET-1F US-Whs Walnut Gulch Lucky Hills Shrub, Ver. v1.3_r1 (2007-2025), AmeriFlux AMP, (Dataset). <https://doi.org/10.17190/AMF/1984574> |
| CN-Nmn | Naiman | CRO | 42.94611 | 120.72694 | 2015-2019 | ChinaFlux | Li, Y. (2026). Fluxnet Archive Product from Naiman, 2015–2019, FLUXNET, <https://hdl.handle.net/11676/0v70myjZ6UGZr9O6hJG55c-t> |
| FR-Pue | Puechabon | EBF | 43.7413 | 3.5957 | 2000-2026 | European Fluxes Database | Limousin, J.-M., Joffre, R., Kempf, J., Ourcival, J.-M., Piquemal, K., Veuillen, L. (2026). Fluxnet Archive Product from Puechabon, 2000-01-01–2026-09-06, FLUXNET, <https://hdl.handle.net/11676/zX4eolqNe8xbcMScyT2IQ9XV> |
| AU-Rig | Riggs Creek | GRA | -36.6499 | 145.5759 | 2011-2017 | OzFlux | Beringer, J., McHugh, I. (2026): Riggs Creek FLUXNET Release 2026_r1 . Version 2026_r1. Terrestrial Ecosystem Research Network (TERN). (Dataset). |

[Map:]{.underline}

```{python}
# ---- World map as background ----
world = gpd.read_file('data/processed/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp')

fig, ax = plt.subplots(figsize=(10, 6))
world.plot(ax=ax, color='lightblue', edgecolor='black')

# ---- Coordinates of selected stations ----
coords = [
    {'lon':-124.9004, 'lat':49.5346, 'stn':'CA-Ca3'},
    {'lon':-110.0522, 'lat':31.7438, 'stn':'US-Whs'},
    {'lon':120.72694, 'lat':42.94611, 'stn':'CN-Nmn'},
    {'lon':3.5957, 'lat':43.7413, 'stn':'FR-Pue'},
    {'lon':145.5759, 'lat':-36.6499, 'stn':'AU-Righ'}
]

# ---- Plot stations into world map ----
for stn in coords:
    gpd.GeoDataFrame(
        geometry=[Point(stn['lon'], stn['lat'])],
        crs='EPSG:4326'
    ).plot(ax=ax, color='red', markersize=50, marker='o', label=stn['stn'])

# ---- Show plot ----
plt.legend()
plt.show()
```

------------------------------------------------------------------------

### Data coverage

Share of measured NEE (QC 0) per site and year, as a heat map:

```{python}
range = ('200001010000', '202601010000') # 2000-2025

NEE = pd.DataFrame({
    'CA_Ca3': data['CA_Ca3']['NEE_CUT_MEAN_QC'][(data['CA_Ca3']['TIMESTAMP_START']>=range[0]) & (data['CA_Ca3']['TIMESTAMP_END']<range[1])],
    'US_Whs': data['US_Whs']['NEE_CUT_MEAN_QC'][(data['US_Whs']['TIMESTAMP_START']>=range[0]) & (data['US_Whs']['TIMESTAMP_END']<range[1])],
    'CN_Nmn': data['CN_Nmn']['NEE_CUT_MEAN_QC'][(data['CN_Nmn']['TIMESTAMP_START']>=range[0]) & (data['CN_Nmn']['TIMESTAMP_END']<range[1])],
    'FR_Pue': data['FR_Pue']['NEE_CUT_MEAN_QC'][(data['FR_Pue']['TIMESTAMP_START']>=range[0]) & (data['FR_Pue']['TIMESTAMP_END']<range[1])],
    'AU_Rig': data['AU_Rig']['NEE_CUT_MEAN_QC'][(data['AU_Rig']['TIMESTAMP_START']>=range[0]) & (data['AU_Rig']['TIMESTAMP_END']<range[1])]
})

# for stn in data:
#     data[stn]['NEE_CUT_MEAN_QC'][(data[stn]['TIMESTAMP_START']>=range[0]) & (data[stn]['TIMESTAMP_END'] <range[1])]

# sns.kdeplot(, , cmap="Reds", fill=True, thresh=0.05)

stmps_true = []
for stmp in data['CA_Ca3']['TIMESTAMP_START']: stmps_true.append(stmp[0:4]=='2010')
```

------------------------------------------------------------------------

### Summary statistics

Mean, min, max and % missing of TA, SW_IN, VPD, P, NEE, GPP, RECO, H, LE:

```{python}
var_list = [
    'TA_F_QC', 'SW_IN_F_QC', 'VPD_F_QC', 'P_F_QC', 'NEE_CUT_MEAN_QC', 'GPP_DT_CUT_MEAN', 'RECO_DT_CUT_MEAN', 'H_F_MDS_QC', 'LE_F_MDS_QC'
]

def isna_mean(x):
    return x.isna().mean()

summaries = []
for stn in data:
    summaries.append(round(data[stn][var_list].agg(['mean', 'min', 'max', isna_mean]), 2))

print('CA_Ca3:')
summaries[0]
print('----------')
```

------------------------------------------------------------------------

### Time series

Daily NEE, GPP and RECO aggregated from the half-hourly data:

```{python}

```

------------------------------------------------------------------------

### Diurnal cycles

Mean daily course of NEE and LE per season, all five sites:

```{python}

```

------------------------------------------------------------------------

### My reading

Energy balance plot for one site and 5–8 sentences comparing the towers:

```{python}

```

...