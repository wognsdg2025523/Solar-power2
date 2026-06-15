import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 국가별 태양광 발전 사용량 TOP 5")

df = pd.read_csv("solar-energy-consumption.csv")

# 국가만 남기기
df = df[df["Code"].notna()]
df = df[~df["Code"].str.contains("OWID", na=False)]

years = sorted(df["Year"].unique())

before_year = st.selectbox(
    "2000년 이전 연도 선택",
    [y for y in years if y < 2000]
)

after_year = st.selectbox(
    "2000년 이후 연도 선택",
    [y for y in years if y >= 2000],
    index=len([y for y in years if y >= 2000]) - 1
)

col1, col2 = st.columns(2)

with col1:
    st.subheader(f"{before_year}년 TOP 5")

    top_before = (
        df[df["Year"] == before_year]
        .sort_values("Solar", ascending=False)
        .head(5)
    )

    st.dataframe(top_before[["Entity", "Solar"]])

    fig1 = px.bar(
        top_before,
        x="Entity",
        y="Solar",
        title=f"{before_year}년 태양광 발전 TOP 5"
    )

    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader(f"{after_year}년 TOP 5")

    top_after = (
        df[df["Year"] == after_year]
        .sort_values("Solar", ascending=False)
        .head(5)
    )

    st.dataframe(top_after[["Entity", "Solar"]])

    fig2 = px.bar(
        top_after,
        x="Entity",
        y="Solar",
        title=f"{after_year}년 태양광 발전 TOP 5"
    )

    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

common = set(top_before["Entity"]) & set(top_after["Entity"])

st.subheader("🔍 비교 결과")

if common:
    st.success(f"두 시기 모두 TOP 5에 포함된 국가: {', '.join(common)}")
else:
    st.warning("공통 국가가 없습니다.")
