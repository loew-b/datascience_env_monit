# Data dictionary — practice dataset

**File:** `raw/XX-Demo_daily_2022-2023.csv`
**Site:** `XX-Demo` (fictional site; synthetic data generated for teaching)
**Temporal coverage:** 2022-01-01 to 2023-12-31, daily (730 rows)
**Missing-value code:** `-9999`
**Licence / citation:** course teaching material; not real observations — do not cite or use for scientific conclusions.

The column names follow FLUXNET conventions so that the workflow transfers to the real data in block 4.

| Column | Description | Unit | Notes |
|---|---|---|---|
| `TIMESTAMP` | Date | `YYYYMMDD` | Stored as an integer; convert to a date |
| `TA_F` | Air temperature | °C | `_F` = gap-filled in FLUXNET; contains a few `-9999` here |
| `SW_IN_F` | Incoming shortwave radiation | W m⁻² | Daily mean |
| `VPD_F` | Vapour pressure deficit | hPa | |
| `P_F` | Precipitation | mm d⁻¹ | Daily sum |
| `GPP_NT_VUT_REF` | Gross primary productivity | g C m⁻² d⁻¹ | Derived (night-time partitioning), not measured directly; gap 2023-03-10 to 03-24 |
| `RECO_NT_VUT_REF` | Ecosystem respiration | g C m⁻² d⁻¹ | Derived; same gap |
| `NEE_VUT_REF` | Net ecosystem exchange | g C m⁻² d⁻¹ | Negative = uptake by the ecosystem; same gap |

Questions to keep in mind for the real data: Which variables are **measured** and which are **derived**? What does a gap mean? Who produced the file, which version, and under which licence?
