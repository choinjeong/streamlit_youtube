import streamlit as st
import pandas as pd

df = pd.read_csv('Global YouTube Statistics.csv', encoding_errors='ignore', encoding='utf-8')
# df['category'].unique().tolist()

# 사이드바 제목
st.sidebar.title('Global Yotube Statistics')

# 'country' 컬럼으로 select box 만들기 (selectbox/multiselect도 가능)
country = st.sidebar.multiselect(
    '유튜브 채널 국가를 선택하세요.',
    df['Country'].sort_values().unique().tolist()
)

# 'country'를 선택했을 때, 해당하는 데이터 보여주기
# st.table(df[df['Country'] == country].head())

# 'category' 컬럼으로 radio 만들기
category = st.sidebar.radio(
    '유튜브 채널 카테고리를 선택하세요.',
    df['category'].unique().tolist(),
    horizontal=True # False일 경우 아래로 쭉 나열 됨
)

# # 'subscribers' 컬럼으로 slider 만들기
# subscriber = st.sidebar.slider(
#     '유튜브 채널 구독자 범위를 지정하세요.',
#     0.0, # 최솟값
#     float(df['subscribers'].max()), # 최댓값. float 타입만 가능
#     (0.0, float(round(df['subscribers'].mean(),0))) # defalut range, 숫자 하나만 입력할 경우 range를 한쪽만 이동 가능. float 타입으로 입력.
# )


# # 필터 버튼 만들기
# show_button = st.sidebar.button(
#     'show 😎'
# )

# if show_button:
#     tmp = df[df['Country'] == country]
#     tmp = tmp[tmp['category'] == category]
#     tmp = tmp[ (tmp['subscribers'] >= subscriber[0]) & (tmp['subscribers'] <= subscriber[1])]
#     st.table(tmp.head(100)) # 100개 행 출력
#     st.sidebar.success('Show the data!') # 성공 문구
#     st.balloons() # 풍선 날리기 효과
    
# # 로딩상태 만들기
# import time

# with st.spinner('Wait for it...'):
#     time.sleep(5)
#     st.success('Done!')
