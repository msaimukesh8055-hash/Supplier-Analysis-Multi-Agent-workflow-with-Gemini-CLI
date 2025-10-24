import os
import subprocess
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Supplier Benchmarking (3-Agent)", page_icon="🧠", layout="wide")
st.title("Supplier Benchmarking — 3-Agent Prototype")

st.markdown(
    "Upload a suppliers CSV and set preferences in the sidebar. "
    "Click **Run analysis** to execute the Collector → Analyst → Recommender pipeline."
)

# -------- Sidebar: user prefs --------
with st.sidebar:
    st.header("Preferences")
    target_region = st.text_input("Target region", value="South India")
    st.markdown("**Weights (0–1; any scale, normalized by you):**")
    w_price   = st.number_input("Price weight",       min_value=0.0, max_value=1.0, value=0.35, step=0.05)
    w_quality = st.number_input("Quality weight",     min_value=0.0, max_value=1.0, value=0.30, step=0.05)
    w_lead    = st.number_input("Lead time weight",   min_value=0.0, max_value=1.0, value=0.25, step=0.05)
    w_geo     = st.number_input("Geo proximity weight", min_value=0.0, max_value=1.0, value=0.10, step=0.05)

uploaded = st.file_uploader("Upload suppliers.csv", type=["csv"], accept_multiple_files=False)

def write_prefs_yaml(region, w_p, w_q, w_l, w_g):
    txt = f'''target_region: "{region}"
weights:
  price_per_unit: {w_p}
  quality: {w_q}
  lead_time_days: {w_l}
  geo_proximity: {w_g}
tie_breaker: "lower lead_time_days"
'''
    os.makedirs("data", exist_ok=True)
    with open("data/user_prefs.yaml", "w") as f:
        f.write(txt)

def save_uploaded_csv(file):
    os.makedirs("data", exist_ok=True)
    if file is not None:
        df = pd.read_csv(file)
        df.to_csv("data/suppliers.csv", index=False)
        return df
    if os.path.exists("data/suppliers.csv"):
        return pd.read_csv("data/suppliers.csv")
    return None

col1, col2 = st.columns([2, 1], gap="large")

with col1:
    st.subheader("1) Data")
    df_preview = save_uploaded_csv(uploaded)
    if df_preview is None:
        st.info("Upload a CSV or use the demo `data/suppliers.csv` already in the repo.")
    else:
        st.dataframe(df_preview.head(10), use_container_width=True)

with col2:
    st.subheader("2) Run")
    run_clicked = st.button("Run analysis", type="primary", use_container_width=True)

if run_clicked:
    write_prefs_yaml(target_region, w_price, w_quality, w_lead, w_geo)
    os.makedirs("outputs", exist_ok=True)
    with st.status("Running pipeline…", expanded=True) as status:
        try:
            # ensure script is executable
            subprocess.run(["chmod", "+x", "pipelines/run.sh"], check=False)

            # call the pipeline
            p = subprocess.run(
                ["bash", "pipelines/run.sh"],
                capture_output=True,
                text=True,
                check=True,
            )
            st.write(p.stdout)
            if p.stderr:
                st.caption("stderr:")
                st.code(p.stderr)
            status.update(label="Pipeline complete", state="complete", expanded=False)
        except subprocess.CalledProcessError as e:
            st.error("Pipeline failed. See logs below.")
            st.code((e.stdout or "") + "\n" + (e.stderr or ""))
            status.update(label="Pipeline failed", state="error", expanded=True)

st.subheader("3) Results")

def dl_btn(path, label):
    if os.path.exists(path):
        with open(path, "rb") as f:
            st.download_button(label=label, data=f, file_name=os.path.basename(path))
    else:
        st.caption(f"Missing: {path}")

scores_path    = "outputs/scores.csv"
cleaned_path   = "outputs/cleaned.csv"
shortlist_path = "outputs/shortlist.csv"
rec_path       = "outputs/recommendations.md"

colA, colB = st.columns(2, gap="large")
with colA:
    if os.path.exists(scores_path):
        st.markdown("**Scores**")
        st.dataframe(pd.read_csv(scores_path), use_container_width=True)
with colB:
    if os.path.exists(shortlist_path):
        st.markdown("**Top-3 Shortlist**")
        st.dataframe(pd.read_csv(shortlist_path), use_container_width=True)

st.markdown("**Downloads**")
dl_btn(cleaned_path,   "Download cleaned.csv")
dl_btn(scores_path,    "Download scores.csv")
dl_btn(shortlist_path, "Download shortlist.csv")

if os.path.exists(rec_path):
    with open(rec_path, "r", encoding="utf-8") as f:
        st.markdown("**Recommendations (Markdown)**")
        st.code(f.read(), language="markdown")
    dl_btn(rec_path, "Download recommendations.md")

st.caption("Prototype: local Streamlit UI calling a 3-agent pipeline via Gemini CLI.")

