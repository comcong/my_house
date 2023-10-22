import streamlit as st

if 'maemul_df' in st.session_state:
    st.write('사용승인일:  ', st.session_state.df['사용승인일'][st.session_state.df['단지명'] == st.session_state.selecting_apt].values[0])
    st.dataframe(st.session_state.maemul_df, hide_index=True)
