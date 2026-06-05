import streamlit as st
import pandas as pd
import plotly.express as px

# إعدادات الصفحة
st.set_page_config(page_title="Wheat Genomics Dashboard", layout="wide")

st.title("🌾 Wheat Genomics Dashboard (Salinity Tolerance)")
st.markdown("An interactive web app to analyze wheat genes responsible for salt stress tolerance.")

# بيانات جينات القمح جاهزة ومدمجة داخل الكود لتسهيل التشغيل
data = {
    "Gene_Name": ["TaHKT1;5-D", "TaNHX1", "TaSOS1", "TaDREB2", "TaWRKY10", "TaHKT2;1", "TaNHX2"],
    "Chromosome": ["4D", "2X", "3B", "5A", "7A", "4B", "2B"],
    "Function": ["Sodium Exclusion", "Vacuolar Sequestration", "Plasma Membrane Antiporter", "Transcription Factor", "Stress Regulation", "Ion Transport", "Vacuolar Sequestration"],
    "Length_bp": [1650, 1820, 3450, 1100, 1250, 1700, 1800],
    "Salinity_Tolerance_Score": [95, 85, 90, 75, 70, 60, 80]
}

df = pd.DataFrame(data)

# إحصائيات سريعة
col1, col2, col3 = st.columns(3)
with col1: st.metric(label="Total Genes Analysed", value=len(df))
with col2: st.metric(label="Avg Gene Length (bp)", value=int(df["Length_bp"].mean()))
with col3: st.metric(label="Max Salinity Score", value=f"{df['Salinity_Tolerance_Score'].max()}%")

st.markdown("---")

# جدول البيانات
st.subheader("🧬 Gene Data Table")
st.dataframe(df, use_container_width=True)

# الرسم البياني
st.subheader("📊 Visual Analytics")
fig1 = px.bar(df, x="Gene_Name", y="Salinity_Tolerance_Score", color="Chromosome", text_auto=True, template="plotly_dark")
st.plotly_chart(fig1, use_container_width=True)