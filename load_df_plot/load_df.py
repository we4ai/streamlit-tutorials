import streamlit as st

import pandas as pd

df = pd.read_csv('football_data.csv')

# Way1
st.dataframe(df.head())

#Way2
st.write(df.head())

# Way 3
st.table(df.head())


data = df['Div'].value_counts()
st.bar_chart(data)

st.line_chart(df, x="Date", y=['HS', 'HC', 'HY'])


### Area chart
chart_data = df[['HS', 'HC','HY']][:50]
st.area_chart(chart_data)                 
            
