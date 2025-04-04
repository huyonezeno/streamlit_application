import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.header('st.write')
#1 nhiều dạng khác nahu trong 1 argument
st.write("Hello, *World* :100:")
#2 dạng số
st.write(1234)
#3 dạng bảng
df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40] 
})
st.write(df)
#4 nhiều argument
st.write('A',df,'B')
#5
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
