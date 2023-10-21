# streamlit run my_house.py
# http://localhost:8501/

import pandas as pd
import streamlit as st
from backend import apts
from backend import apt_info

# st.set_page_config(
#     page_title="Ex-stream-ly Cool App",
#     page_icon="🧊",
#     layout="wide",
#     initial_sidebar_state="expanded",
#     menu_items={
#         'Get Help': 'https://www.extremelycoolapp.com/help',
#         'Report a bug': "https://www.extremelycoolapp.com/bug",
#         'About': "# This is a header. This is an *extremely* cool app!"
#     }
# )



sidebar = st.sidebar.container()
city = sidebar.text_input('지역을 입력하세요', '서구 원당동')

if 'call_apts' not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=['검색지역', '단지명', '세대수', '사용승인일', '매매', '전세', '월세', '단기'])
    st.session_state.select_box_apt_list = ''
    st.session_state.call_apts = True

if sidebar.button('검색', key='search_apts'):
    called_apts = apts.apts(city)  # 지역 안의 아파트들의 정보를 담는다.
    st.session_state.df = called_apts[0]                          # 아파트들 데이터프레임
    st.session_state.select_box_apt_list = called_apts[1]         # 아파트들 리스트

sidebar.selectbox(
    "아파트를 선택하세요.",
    st.session_state.select_box_apt_list,
    index=None,
    placeholder="아파트를 선택하세요.",
    key='selected_apt'
)
st.dataframe(st.session_state.df, hide_index=True)                                        # 아파트들 데이터프레임 출력

if 'selected_apt' in st.session_state and sidebar.button('아파트 정보', key='search_apt_info'):
    hscpNo = st.session_state.df['단지ID'][st.session_state.df['단지명'] == st.session_state.selected_apt].values[0]
    maemul_cnt = st.session_state.df['총잔량'][st.session_state.df['단지명'] == st.session_state.selected_apt].values[0]
    st.dataframe(apt_info.apt_info(hscpNo, maemul_cnt), hide_index=True)   # 아파트 정보 출력



