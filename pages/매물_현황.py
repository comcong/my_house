import streamlit as st
if st.session_state.maemul_df.any():
    st.dataframe(st.session_state.maemul_df, hide_index=True)
