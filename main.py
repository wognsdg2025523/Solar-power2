import streamlit as st

st.set_page_config(
    page_title="태양광 발전 데이터 분석",
    page_icon="☀️",
    layout="wide"
)

st.title("☀️ 국가별 태양광 발전 에너지 사용량 분석")

st.markdown("""
이 웹앱은 국가별 태양광 발전 에너지 사용량 데이터를 분석합니다.

### 기능
1. 📊 과거와 현재의 태양광 발전 사용량 TOP 5 국가 비교
2. 🔮 미래 TOP 5 국가 예측

왼쪽 사이드바에서 페이지를 선택하세요.
""")
