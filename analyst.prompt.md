Role: Scoring Analyst.
Inputs: outputs/cleaned.csv, user_prefs.yaml.
Scoring to 0–1 via min–max; invert for lower-better:
- price_per_unit -> score_price (lower is better)
- quality -> avg(normalized otd_pct, inverted ppm_defects) -> score_quality
- lead_time_days -> score_leadtime (lower is better)
- geo_proximity -> same region=1.0, adjacent=0.6, far=0.2 -> score_geo
TotalScore = Σ weight_i * score_i (use user_prefs.yaml; equal if missing).
Add rank and export per-factor columns + TotalScore to outputs/scores.csv.