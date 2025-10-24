# 🏭 Supplier Analysis Agent with Gemini CLI (Multi-Agent Workflow)

### 1. Project Overview  
Built an **AI-driven supplier benchmarking prototype** using a **multi-agent architecture** (Collector, Analyst, Recommender) orchestrated via **Gemini CLI**. The system automated supplier data collection, benchmarking analysis, and generated structured recommendations for executive decision-making.

### 2. Business Problem  
- **Pain Point:** Supplier evaluation in large enterprises is often **manual, fragmented, and time-intensive**, requiring procurement teams to clean data, score suppliers, and prepare reports.  
- **Existing Methods:** Excel-based scoring models, ad-hoc data collection, and manual slide preparation.  
- **Opportunity:** A multi-agent AI workflow can automate **data cleaning, scoring, and reporting**, drastically cutting turnaround time while improving consistency and transparency.

### 3. Solution  
- **Tools Used:** Gemini CLI, Multi-Agent Workflows, Vertex AI APIs, LangChain-style orchestration.  
- **Workflow:**  
  1) **Collector Agent** → Gathers supplier data (performance metrics, compliance, cost factors).  
  2) **Analyst Agent** → Cleans and benchmarks data against defined KPIs.  
  3) **Recommender Agent** → Summarizes insights and generates **executive-ready recommendations**.  
  4) **Output** → Delivered structured results (tables + narratives) in a concise, strategy-oriented format.  
- **Automation Highlights:** Agents collaborated autonomously to handle tasks end-to-end, reducing manual analyst intervention.

### 4. Input and Output Example  

**Input (supplier dataset extract):**
```csv
Supplier, Cost_Index, Quality_Score, Delivery_Reliability, Compliance_Flag
A, 0.82, 91, 0.95, Yes
B, 0.74, 88, 0.89, Yes
C, 0.91, 79, 0.82, No
```

### 6. Real-World Example (Work at BMW)  
- **Leveraged a GenAI-powered procurement evaluation tool (Claude, LangChain)** to analyze supplier bids for **EV charging rollouts across 14 Asian markets**.  
- Automated benchmarking and scoring of suppliers, cutting manual evaluation time by ~60%.  
- Delivered **executive-ready recommendations**, accelerating procurement decisions and strengthening market entry strategy.  
- Built strong knowledge of **AI architecture**, including **RAG pipelines, vector databases, and tool-calling APIs**.  
