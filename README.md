# Supplier Benchmarking — 3-Agent Prototype (Gemini CLI)
Run:
  bash pipelines/run.sh

Artifacts:
  outputs/cleaned.csv
  outputs/scores.csv
  outputs/recommendations.md
  outputs/shortlist.csv

## Local UI (Streamlit)
Install deps and launch:

  pip install -r requirements.txt
  streamlit run app.py

Upload a CSV, adjust weights, click **Run analysis**. Outputs appear in ./outputs and on the page.