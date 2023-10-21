import streamlit as st
if st.session_state.maemul_df != None:
    st.dataframe(st.session_state.maemul_df, hide_index=True)
    st.session_state.maemul_df = None