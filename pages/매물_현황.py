import streamlit as st

if 'maemul_df' in st.session_state:
    st.write('사용승인일:  ', st.session_state.df['사용승인일'][st.session_state.df['단지명'] == st.session_state.selecting_apt].values[0])
    st.dataframe(st.session_state.maemul_df, hide_index=True)


    # @st.cache
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')

    csv = convert_df(st.session_state.maemul_df)

    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='large_df.csv',
        # mime='text/csv',
    )

    st.write('신명진')