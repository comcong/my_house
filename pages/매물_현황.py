import streamlit as st


if 'maemul_df' in st.session_state:
    st.dataframe(st.session_state.maemul_df, hide_index=True)
