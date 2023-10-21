import streamlit as st
import pandas as pd
st.dataframe(st.session_state.maemul_df, hide_index=True)
# st.session_state.maemul_df = pd.DataFrame()