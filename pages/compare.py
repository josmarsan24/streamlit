import streamlit as st
from functions import *
import matplotlib.pyplot as plt
import numpy as np

menu()

st.title("Compare players")

df = read_df()

player1 = st.selectbox("First player: ", df['Player'].sort_values().unique(), index=None)
player2 = st.selectbox("Second player: ", df['Player'].sort_values().unique(), index=None)

fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(polar=True))
ax.set_xticklabels([])
ax.set_yticklabels([])

try:
    fig, ax = radar_plot(player1, player2, df, fig, ax)
    df_compare = df_compare(df, player1, player2)
    st.markdown(df_compare.style.hide(axis="index").to_html(), unsafe_allow_html=True)
except:
    pass

st.pyplot(fig)