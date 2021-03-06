import pandas as pd  #pip install pandas openpyxl
import plotly.express as px
import streamlit as st

st.set_page_config(page_title = "Metric Dataset",
					page_icon = ":bar_chart:",
					layour = "wide")

df = pd.read_excel(
	io='Data.xlsx',
	engine='openpyxl',
	sheet_name='Sheet1',
	skiprows=1,
	usecols='D:CE',
	nrows=128,
)

st.dataframe(df)
