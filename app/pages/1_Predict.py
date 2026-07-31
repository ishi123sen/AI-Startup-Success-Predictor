import streamlit as st
import pandas as pd
import joblib
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Startup Success Predictor",
   
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- HIDE STREAMLIT UI ----------------
st.markdown("""
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
[data-testid="stSidebar"] {display:none;}
</style>
""", unsafe_allow_html=True)

# ---------------- PATHS ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, "..", ".."))

css_path = os.path.join(APP_DIR, "styles", "predict.css")
model_path = os.path.join(PROJECT_ROOT, "models", "model.pkl")
scaler_path = os.path.join(PROJECT_ROOT, "models", "scaler.pkl")
encoder_path = os.path.join(PROJECT_ROOT, "models", "category_encoder.pkl")

# ---------------- LOAD CSS ----------------
if os.path.exists(css_path):
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------
try:
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    encoder = joblib.load(encoder_path)
except Exception as e:
    st.error(f"Error loading model files:\n\n{e}")
    st.stop()

# ---------------- NAVBAR ----------------
col1, col2 = st.columns([6, 4])

with col1:
    st.markdown(
        "<h2 style='color:#22c55e;'>VentureIQ AI</h2>",
        unsafe_allow_html=True,
    )

with col2:
    c1, c2, c3 = st.columns(3)

    with c1:
        if st.button(" Home", use_container_width=True):
            st.switch_page("Home.py")

    with c2:
        st.button(" Predict", use_container_width=True)

    with c3:
        if st.button(" Login", use_container_width=True):
            st.switch_page("pages/2_Login.py")

st.markdown("---")

# ---------------- TITLE ----------------
st.markdown(
    "<h1 style='text-align:center;'> Startup Success Predictor</h1>",
    unsafe_allow_html=True,
)

st.write("Enter your startup details below.")

st.write("")

# ---------------- INPUT FORM ----------------
col1, col2 = st.columns(2)

with col1:

    funding_total = st.number_input(
        "Funding Total (USD)",
        min_value=0.0,
        value=1000000.0,
        step=100000.0
    )

    funding_rounds = st.number_input(
        "Funding Rounds",
        min_value=0,
        value=2
    )

    milestones = st.number_input(
        "Milestones",
        min_value=0,
        value=3
    )

    relationships = st.number_input(
        "Relationships",
        min_value=0,
        value=5
    )

with col2:

    age_first_funding_year = st.number_input(
        "Age at First Funding",
        min_value=0.0,
        value=1.5,
        step=0.1
    )

    avg_participants = st.number_input(
        "Average Participants",
        min_value=0.0,
        value=2.0,
        step=0.1
    )

    category = st.selectbox(
        "Category",
        encoder.classes_.tolist()
    )

st.write("")
st.write("")

# ---------------- PREDICTION ----------------
if st.button("Predict Startup Success", use_container_width=True):

    category_encoded = encoder.transform([category])[0]

    input_df = pd.DataFrame([[
        funding_total,
        funding_rounds,
        milestones,
        relationships,
        age_first_funding_year,
        avg_participants,
        category_encoded
    ]], columns=[
        "funding_total_usd",
        "funding_rounds",
        "milestones",
        "relationships",
        "age_first_funding_year",
        "avg_participants",
        "category_code"
    ])

    scaled_input = scaler.transform(input_df)

    prediction = model.predict(scaled_input)[0]

    try:
        probability = model.predict_proba(scaled_input)[0][1]
    except Exception:
        probability = None

    st.write("")
    st.markdown("## Prediction Result")

    if prediction == 1:
        st.success(" This startup has a HIGH chance of success.")
    else:
        st.error(" This startup has a LOW chance of success.")

    if probability is not None:
        st.progress(float(probability))
        st.write(f"**Success Probability:** {probability*100:.2f}%")