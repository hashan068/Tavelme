import streamlit as st
st.write("Hello, let's learn how to build a Streamlit app together")

import pandas as pdimport numpy as npimport 
streamlit as stdf = pd.DataFrame(np.random.randn(500, 2) / [50, 50] + [37.76, -122.4],columns=['lat', 'lon'])st.map(df)
