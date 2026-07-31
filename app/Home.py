import streamlit as st
import base64
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="VentureIQ AI",
    
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- PATHS ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

css_path = os.path.join(BASE_DIR, "styles", "style.css")
image_path = os.path.join(BASE_DIR, "assets", "hero.png")

# ---------------- LOAD CSS ----------------
with open(css_path, "r", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------------- LOAD IMAGE ----------------
with open(image_path, "rb") as img:
    image = base64.b64encode(img.read()).decode()

# ---------------- NAVBAR ----------------
logo, blank, home, predict, login = st.columns([4, 3, 1, 1, 1])

with logo:
    st.markdown(
        """
        <h2 style="color:#22c55e; margin-top:5px;">
        VentureIQ AI
        </h2>
        """,
        unsafe_allow_html=True,
    )

with home:
    st.button("Home", use_container_width=True)

with predict:
    if st.button("Predict", use_container_width=True):
        st.switch_page("pages/1_Predict.py")

with login:
    if st.button("Login", use_container_width=True):
        st.switch_page("pages/2_Login.py")

st.divider()

# ---------------- HERO SECTION ----------------
left, right = st.columns([1.15, 1])

with left:

    st.markdown("""
    <div class="hero-title">
        AI-Powered <span>Startup Success</span><br>
        Prediction Platform
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero-text">
        VentureIQ AI uses Machine Learning to analyze startup funding,
        milestones, business relationships and company characteristics
        to predict the probability of startup success.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        if st.button("Get Started", use_container_width=True):
            st.switch_page("pages/1_Predict.py")

    with c2:
        st.button("Learn More", use_container_width=True)

with right:
    st.markdown(
        f"""
        <div style="text-align:center;">
            <img src="data:image/png;base64,{image}" width="100%">
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<br><br>", unsafe_allow_html=True)

# ---------------- ABOUT ----------------
st.markdown(
"""
<div class="section-title">
About VentureIQ AI
</div>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div class="about">
VentureIQ AI is an AI-powered startup intelligence platform that predicts
whether a startup is likely to succeed using historical startup data.

The platform analyzes funding amount, business category,
milestones, investor relationships and other key business
features to generate intelligent predictions and insights.

It is designed for entrepreneurs, investors and business analysts
to make smarter, data-driven decisions.
</div>
""",
unsafe_allow_html=True
)

st.markdown("<br><br>", unsafe_allow_html=True)

# ---------------- FEATURES ----------------
st.markdown(
"""
<div class="section-title">
Why Choose VentureIQ AI?
</div>
""",
unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
    <h3> AI Powered</h3>
    Uses a trained Machine Learning model to predict startup success.
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
    <h3>Data Driven</h3>
    Uses funding, milestones and startup relationships to generate insights.
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
    <h3> Fast Prediction</h3>
    Receive startup success predictions instantly with one click.
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- STATS ----------------
st.markdown(
"""
<div class="section-title">
Platform Statistics
</div>
""",
unsafe_allow_html=True
)

s1, s2, s3 = st.columns(3)

with s1:
    st.markdown("""
    <div class="stat-card">
        <h1>900+</h1>
        Startup Records
    </div>
    """, unsafe_allow_html=True)

with s2:
    st.markdown("""
    <div class="stat-card">
        <h1>7</h1>
        Input Features
    </div>
    """, unsafe_allow_html=True)

with s3:
    st.markdown("""
    <div class="stat-card">
        <h1>80%</h1>
        Model Accuracy
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">

<h2>VentureIQ AI</h2>

Helping founders and investors make better startup decisions using Artificial Intelligence.

<br><br>

© 2026 VentureIQ AI. All Rights Reserved.

</div>
""", unsafe_allow_html=True)