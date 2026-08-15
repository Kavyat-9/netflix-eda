import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Netflix Exploratory Data Analysis")

df = pd.read_csv("netflix_titles.csv")

st.subheader("Dataset")
st.write(df)

st.subheader("Movies vs TV Shows")

fig, ax = plt.subplots()
sns.countplot(data=df, x="type", ax=ax)
ax.set_title("Movies vs TV Shows on Netflix")
st.pyplot(fig)