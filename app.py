import streamlit as st

from data.sample_data import load_data
from services.feature_engineering import add_features
from services.model import train_model
from services.risk_engine import apply_risk
from services.recommendation import apply_teacher_need
from services.facility_engine import apply_facility
from visuals.plots import create_geo_plot

# ---------------- UI ----------------

st.title("🛰️ ShikshaGeoAI - Advanced AI Governance System")

st.write("AI-powered education governance simulation system")

# ---------------- DATA ----------------

df = load_data()
st.subheader("📊 Dataset")
st.dataframe(df)

# ---------------- FEATURES ----------------

df = add_features(df)
st.subheader("⚙️ Feature Engineering")
st.dataframe(df)

# ---------------- MODEL ----------------

model, df = train_model(df)
st.subheader("🤖 AI Predictions")
st.dataframe(df)

# ---------------- RISK ----------------

df = apply_risk(df)
st.subheader("🚨 Risk Classification")
st.dataframe(df[["School", "AI_Prediction", "Risk"]])

# ---------------- TEACHER NEED ----------------

df = apply_teacher_need(df)
st.subheader("👨‍🏫 Teacher Requirement")
st.dataframe(df[["School", "Teachers_Required"]])

# ---------------- FACILITY ----------------

df = apply_facility(df)
st.subheader("🏫 Facility Requirement")
st.dataframe(df[["School", "Facility_Need"]])

# ---------------- VISUALIZATION ----------------

st.subheader("🌍 GeoAI Map")
fig = create_geo_plot(df)
st.plotly_chart(fig)

# ---------------- FINAL ----------------

st.success("System fully modularized and production-ready 🚀")