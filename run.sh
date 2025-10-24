#!/usr/bin/env bash
set -euo pipefail

mkdir -p outputs

# 1) Collector
gemini run \
  --approval-mode yolo \
  --include-directories agents,data \
  --prompt-file agents/collector.prompt.md \
  --input-file data/suppliers.csv \
  --input-file data/user_prefs.yaml \
  --output-file outputs/cleaned.csv

# 2) Analyst
gemini run \
  --approval-mode yolo \
  --include-directories agents,data,outputs \
  --prompt-file agents/analyst.prompt.md \
  --input-file outputs/cleaned.csv \
  --input-file data/user_prefs.yaml \
  --output-file outputs/scores.csv

# 3) Recommender
gemini run \
  --approval-mode yolo \
  --include-directories agents,outputs \
  --prompt-file agents/recommender.prompt.md \
  --input-file outputs/scores.csv \
  --output-file outputs/recommendations.md

# Fallback shortlist if the model didn't emit it
{ head -n 1 outputs/scores.csv; tail -n +2 outputs/scores.csv | head -n 3; } > outputs/shortlist.csv || true

echo "Artifacts written to ./outputs"