# Supplier Benchmarking — 3-Agent AI Prototype

This project demonstrates how multi-agent AI systems can solve a real business problem:
**supplier benchmarking and shortlisting**.

## Business Problem
Organizations often deal with multiple suppliers offering similar products. Evaluating
them consistently across factors like **price, quality, lead time, and location**
is tedious and prone to bias.

## Solution
This prototype uses a **3-Agent AI pipeline**:

1. **Collector Agent**  
   Cleans and structures supplier data (CSV input).
2. **Analyst Agent**  
   Scores suppliers across weighted factors.
3. **Recommender Agent**  
   Produces a shortlist of the top-3 suppliers with risks, notes, and a verification checklist.

## Example Output
Top 3 Suppliers:

| Supplier            | Score | Strongest Factors      |
|---------------------|-------|------------------------|
| Orion Components    | 0.768 | Price, Geo Proximity   |
| Alpha Castings      | 0.709 | Quality, Geo Proximity |
| Gamma Foundry       | 0.650 | Quality, Lead Time     |

Risks & Follow-up:
- Beta Metals: Price-aggressive but capacity unknown.
- Delta Tools: ESG policy unclear.
- Nova Alloys: OTD variability in 2023.

