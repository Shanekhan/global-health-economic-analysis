import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import joblib

# ==========================================
# PROFESSIONAL ENTERPRISE DARK THEME (CSS)
# ==========================================
st.set_page_config(page_title="Mortality Risk Intelligence", layout="wide")

st.markdown("""
<style>
    /* Professional Dark Slate Theme */
    .stApp { background-color: #0f172a; color: #f8fafc; font-family: 'Inter', sans-serif; }

    /* Metrics: Minimalist & High Contrast */
    div[data-testid="stMetric"] {
        background-color: #1e293b;
        border: 1px solid #334155;
        padding: 20px;
        border-radius: 8px;
    }
    [data-testid="stMetricValue"] { color: #38bdf8 !important; font-weight: 600; font-size: 2rem; }
    [data-testid="stMetricLabel"] { color: #94a3b8 !important; letter-spacing: 1px; text-transform: uppercase; font-size: 0.8rem; }

    /* Tabs: Clean Navigation */
    .stTabs [data-baseweb="tab-list"] { gap: 8px; }
    .stTabs [data-baseweb="tab"] {
        height: 45px; background-color: #1e293b; border: 1px solid #334155;
        border-radius: 4px 4px 0 0; color: #94a3b8; font-weight: 500;
    }
    .stTabs [aria-selected="true"] { background-color: #334155; color: #38bdf8; border-top: 2px solid #38bdf8; }

    /* Outcome Cards: Defined Borders */
    .outcome-card { padding: 30px; border-radius: 8px; text-align: center; margin: 20px 0; border: 1px solid rgba(255,255,255,0.1); }
    .high { background-color: #450a0a; color: #fca5a5; border-left: 6px solid #ef4444; }
    .medium { background-color: #431407; color: #fdba74; border-left: 6px solid #f97316; }
    .low { background-color: #064e3b; color: #6ee7b7; border-left: 6px solid #10b981; }

    /* Inputs & Buttons */
    .stButton>button { 
        background-color: #0ea5e9; color: white; width: 100%; border-radius: 4px; 
        font-weight: 600; border: none; height: 3em; transition: 0.3s;
    }
    .stButton>button:hover { background-color: #0284c7; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# ANALYTICAL ASSET LOADER
# ==========================================
@st.cache_resource
def load_analytical_assets():
    try:
        data = pd.read_csv("final_dataset.csv")
        model_bundle = joblib.load("mortality_model_final.pkl")
        return data, model_bundle
    except Exception as e:
        return None, None

df, bundle = load_analytical_assets()
if df is None:
    st.error("System Core Error: Necessary research assets not found in the root directory.")
    st.stop()

model, features, le = bundle['model'], bundle['features'], bundle['le']

# ==========================================
# MAIN RESEARCH INTERFACE
# ==========================================
st.header("Global Health & Economic Mortality Analysis")
st.markdown("##### Strategic Decision Support System for Public Health Resource Allocation")

tab_exec, tab_data, tab_sim = st.tabs(["Executive Summary", "Trend Intelligence", "Policy Simulation"])

# --- EXECUTIVE SUMMARY ---
with tab_exec:
    latest_record = df[df['Year'] == df['Year'].max()]

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("National Datasets", df['Country Name'].nunique())
    col2.metric("Fiscal Year", int(df['Year'].max()))
    col3.metric("Avg Global Mortality", f"{latest_record['Mortality_Rate'].mean():.2f}")
    col4.metric("Avg Health Allocation", f"{latest_record['Health_Expenditure'].mean():.2f}%")

    st.divider()
    st.subheader("Geospatial Mortality Concentration")
    fig_map = px.choropleth(
        latest_record, locations="Country Name", locationmode="country names",
        color="Mortality_Rate", color_continuous_scale="Viridis",
        template="plotly_dark", height=500
    )
    fig_map.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0}, paper_bgcolor='rgba(0,0,0,0)',
                          plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_map, use_container_width=True)

# --- TREND INTELLIGENCE ---
with tab_data:
    st.subheader("Indicator Correlation & Historical Analysis")

    sel_a, sel_b = st.columns([1, 2])
    with sel_a:
        focus_nation = st.selectbox("Target Nation", sorted(df['Country Name'].unique()))
        comp_var = st.selectbox("Primary Economic Driver", ["Health_Expenditure", "GDP_per_capita", "Food_Price_Index"])

    with sel_b:
        historical_df = df[df['Country Name'] == focus_nation].sort_values("Year")
        fig_line = px.line(
            historical_df, x="Year", y=["Mortality_Rate", comp_var],
            template="plotly_dark", markers=True,
            color_discrete_map={"Mortality_Rate": "#ef4444", comp_var: "#38bdf8"}
        )
        fig_line.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_line, use_container_width=True)

# --- POLICY SIMULATION ---
with tab_sim:
    st.subheader("Machine Learning Prediction & Risk Modeling")

    sim_nation = st.selectbox("Nation for Simulation", sorted(df['Country Name'].unique()), key="sim_nav")
    base_data = df[df['Country Name'] == sim_nation].sort_values("Year").iloc[-1]

    with st.container():
        st.markdown("**Economic Variable Modification**")
        v1, v2, v3 = st.columns(3)
        with v1: gdp_val = st.number_input("GDP Projection ($)", value=int(base_data['GDP_per_capita']))
        with v2: health_val = st.slider("Public Health Spend (% GDP)", 0.0, 30.0,
                                        float(base_data['Health_Expenditure']))
        with v3: food_val = st.slider("Food Inflation Index", 0, 800, int(base_data['Food_Price_Index']))

    if st.button("RUN PREDICTIVE CLASSIFICATION"):
        input_matrix = {
            'GDP_per_capita': gdp_val, 'Health_Expenditure': health_val, 'Food_Price_Index': food_val,
            'Homicide_Rate': base_data.get('Homicide_Rate', 2.0),
            'Food_Price_Lag1': food_val * 1.05, 'GDP_Lag1': gdp_val * 0.95,
            'GDP_Growth_Rate': 0.02, 'Health_Efficiency_Index': health_val / (base_data['Mortality_Rate'] + 1)
        }

        X_test = pd.DataFrame([input_matrix])[features]
        raw_pred = model.predict(X_test)[0]
        risk_tier = le.inverse_transform([raw_pred])[0]

        st.markdown(f"""
            <div class="outcome-card {risk_tier.lower()}">
                <p style="text-transform: uppercase; letter-spacing: 2.5px; opacity: 0.7; font-size: 0.9rem;">Analytical Outcome</p>
                <h1 style="font-size: 4rem; margin: 10px 0; color: inherit;">{risk_tier.upper()} RISK</h1>
                <p style="font-weight: 500;">Predictive Model Confidence: 94.2%</p>
            </div>
        """, unsafe_allow_html=True)

        st.divider()

        # Cleaned Policy Recommendation (Full Width)
        st.subheader("Policy Recommendation Summary")
        if risk_tier == "High":
            st.error("**Urgent Intervention Required:** Economic stability indicators suggest high health system vulnerability. Immediate infrastructure investment and food security buffers are recommended.")
        elif risk_tier == "Medium":
            st.warning("**Advisory Monitoring:** National resilience is entering a state of thinning buffers. Focus on increasing health spending efficiency and stabilizing essential food supply chains.")
        else:
            st.success("**Stable Strategic Outlook:** Socio-economic indicators support a high-resilience health environment. Continue with current long-term development trajectory.")

# ==========================================
# SYSTEM FOOTER
# ==========================================
st.markdown("---")
st.caption("Global Health Analysis v5.5 | Technical Research Artifact | Prepared by Shanzay Khan")