# streamlit run my_house.py
# http://localhost:8501/

import pandas as pd
import streamlit as st
from backend import apts
from backend import apt_info

sidebar = st.sidebar.container()

if 'user_input' not in st.session_state:
    city = sidebar.text_input('지역을 입력하세요', '서구 원당동', key='search_local')
else:
    city = sidebar.text_input('지역을 입력하세요', st.session_state.user_input, key='search_local')
st.session_state.user_input = st.session_state.search_local

if 'call_apts' not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=['검색지역', '단지명', '세대수', '사용승인일', '매매', '전세', '월세', '단기'])  # 데이터프레임
    st.session_state.select_box_apt_list = ''   # 드롭 박스
    st.session_state.call_apts = True

if sidebar.button('검색', key='search_apts'):
    # city = st.session_state.search_local
    called_apts = apts.apts(city)  # 지역 안의 아파트들의 정보를 담는다.
    st.session_state.df = called_apts[0]                          # 아파트들 데이터프레임
    st.session_state.select_box_apt_list = called_apts[1]         # 아파트들 튜플 (a,b,c,d, ....)

sidebar.selectbox(       # 드롭 박스
    "아파트를 선택하세요.",
    st.session_state.select_box_apt_list,
    index=None,
    placeholder="아파트를 선택하세요.",
    key='selected_apt'
)

st.dataframe(st.session_state.df, hide_index=True,
             column_order=['검색지역', '단지명', '세대수', '사용승인일', '매매', '전세', '월세', '단기', '총잔량', ],
             )

if 'selected_apt' in st.session_state and sidebar.button('아파트 정보', key='search_apt_info'):
    hscpNo = st.session_state.df['단지ID'][st.session_state.df['단지명'] == st.session_state.selected_apt].values[0]
    maemul_cnt = st.session_state.df['총잔량'][st.session_state.df['단지명'] == st.session_state.selected_apt].values[0]
    if maemul_cnt > 0:  # 매물 총잔량이 1 건 이상인 경우에만 매물 불러오기 함수 실행
        maemul_df = apt_info.apt_info(hscpNo, maemul_cnt)
        st.session_state.maemul_df = maemul_df
    else:
        st.write('매물이 없습니다.')
        st.session_state.maemul_df = pd.DataFrame()

