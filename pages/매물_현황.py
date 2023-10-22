import streamlit as st
from datetime import datetime as dt
today = dt.today().strftime("%Y_%m_%d")

print(today)

if 'maemul_df' in st.session_state:
    st.write('사용승인일:  ', st.session_state.df['사용승인일'][st.session_state.df['단지명'] == st.session_state.selecting_apt].values[0])
    st.dataframe(st.session_state.maemul_df, hide_index=True)

    @st.cache_data
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('euc-kr')

    csv = convert_df(st.session_state.maemul_df)

    # 다운로드 버튼
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name=f'{st.session_state.selecting_apt}_{today}.csv',
        mime='text/csv',

    )

