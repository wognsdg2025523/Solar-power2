import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import plotly.express as px

st.title("🔮 미래 TOP 5 국가 예측")

df = pd.read_csv("solar-energy-consumption.csv")

# 국가만 선택
df = df[df["Code"].notna()]
df = df[~df["Code"].str.contains("OWID", na=False)]

predict_year = st.slider(
    "예측 연도 선택",
    2026,
    2050,
    2035
)

predictions = []

for country in df["Entity"].unique():

    country_df = df[df["Entity"] == country]

    if len(country_df) < 5:
        continue

    X = country_df["Year"].values.reshape(-1, 1)
    y = country_df["Solar"].values

    model = LinearRegression()
    model.fit(X, y)

    pred = model.predict([[predict_year]])[0]

    predictions.append([country, max(pred, 0)])

pred_df = pd.DataFrame(
    predictions,
    columns=["Country", "Predicted Solar"]
)

top5 = pred_df.sort_values(
    "Predicted Solar",
    ascending=False
).head(5)

st.subheader(f"{predict_year}년 예상 TOP 5 국가")

st.dataframe(top5)

fig = px.bar(
    top5,
    x="Country",
    y="Predicted Solar",
    title=f"{predict_year}년 예상 태양광 발전 사용량 TOP 5"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("""
### 예측 방법
- 각 국가별 연도 데이터를 사용
- 선형회귀(Linear Regression) 적용
- 선택한 미래 연도의 사용량 예측
- 예측값 기준 TOP 5 국가 선정
""")
