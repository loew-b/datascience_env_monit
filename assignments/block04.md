# Block 04 assignment

------------------------------------------------------------------------

------------------------------------------------------------------------

## Data import

Importing required packages:

```{python}
import pandas as pd
import zipfile
```

Loading data from `.csv` files:

```{python}
# ---- File locations ----
CA_Ca3_file = 'data/raw/AMF_CA-Ca3_FLUXNET_2001-2024_v1.3_r1.zip/AMF_CA-Ca3_FLUXNET_FLUXMET_HH_2001-2024_v1.3_r1.csv'
US_Whs_file = 'data/raw/'
CN_Nmn_file = 'data/raw/'
FR_Pue_file = 'data/raw/'
AU_Rig_file = 'data/raw/'

# ---- Reading data ----
CA_Ca3_hh = pd.read_csv(
    CA_Ca3_file,
    na_values=[-9999],
    dtype={"TIMESTAMP_START": str, "TIMESTAMP_END": str}
)
US_Whs_hh = pd.read_csv(
    UW_Whs_file,
    na_values=[-9999],
    dtype={"TIMESTAMP_START": str, "TIMESTAMP_END": str}
)
CN_Nmn_hh = pd.read_csv(
    ,
    na_values=[-9999],
    dtype={"TIMESTAMP_START": str, "TIMESTAMP_END": str}
)
FR_Pue_hh = pd.read_csv(
    ,
    na_values=[-9999],
    dtype={"TIMESTAMP_START": str, "TIMESTAMP_END": str}
)
AU_Rig_hh = pd.read_csv(
    ,
    na_values=[-9999],
    dtype={"TIMESTAMP_START": str, "TIMESTAMP_END": str}
)
```

------------------------------------------------------------------------

## Site overview

[Table:]{.underline}

| ID | Name | IGBP | Lat | Lon | Years | Hub | Citation |
|----|----|----|----|----|----|----|----|
| CA-Ca3 | British Columbia - Pole sapling Douglas-fir stand | ENF | 49.5346 | -124.9004 | 2001-2024 | AmeriFlux | T. Andrew Black (2026), AmeriFlux FLUXNET-1F CA-Ca3 British Columbia - Pole sapling Douglas-fir stand, Ver. v1.3_r1 (2001-2024), AmeriFlux AMP, (Dataset). <https://doi.org/10.17190/AMF/3027312> |
| US-Whs | Walnut Gulch Lucky Hills Shrub | OSH | 31.7438 | -110.0522 | 2007-2025 | AmeriFlux | Russ Scott (2026), AmeriFlux FLUXNET-1F US-Whs Walnut Gulch Lucky Hills Shrub, Ver. v1.3_r1 (2007-2025), AmeriFlux AMP, (Dataset). <https://doi.org/10.17190/AMF/1984574> |
| CN-Nmn | Naiman | CRO | 42.94611 | 120.72694 | 2015-2019 | ChinaFlux | Li, Y. (2026). Fluxnet Archive Product from Naiman, 2015–2019, FLUXNET, <https://hdl.handle.net/11676/0v70myjZ6UGZr9O6hJG55c-t> |
| FR-Pue | Puechabon | EBF | 43.7413 | 3.5957 | 2000-2026 | European Fluxes Database | Limousin, J.-M., Joffre, R., Kempf, J., Ourcival, J.-M., Piquemal, K., Veuillen, L. (2026). Fluxnet Archive Product from Puechabon, 2000-01-01–2026-09-06, FLUXNET, <https://hdl.handle.net/11676/zX4eolqNe8xbcMScyT2IQ9XV> |
| AU-Rig | Riggs Creek | GRA | -36.6499 | 145.5759 | 2011-2017 | OzFlux | Beringer, J., McHugh, I. (2026): Riggs Creek FLUXNET Release 2026_r1 . Version 2026_r1. Terrestrial Ecosystem Research Network (TERN). (Dataset). |

[Map:]{.underline}

------------------------------------------------------------------------

### Data coverage

Share of measured NEE (QC 0) per site and year, as a heat map:

```{python}

```

------------------------------------------------------------------------

### Summary statistics

Mean, min, max and % missing of TA, SW_IN, VPD, P, NEE, GPP, RECO, H, LE:

```{python}

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