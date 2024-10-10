# streamlit: page title: Home
import streamlit as st
from functions import *

menu()

st.title("NBA Data 2023-2024 season")
st.subheader("Demo app by Jose Martin")

url = 'https://www.basketball-reference.com/leagues/NBA_2024_per_game.html'
urlComp = '/compare'
urlPlot = '/plot'
urlGit = 'https://github.com/josmarsan24/streamlit'

st.markdown("This app was made to explore the players data from the 2023-2024 season, this was made with streamlit, the data source is " f"[BasketballReference]({url})")
st.markdown("You can compare two players data in the " f"[compare players]({urlComp})" " tab and plot different statistics in the " f"[plot metrics]({urlPlot})" " tab")
st.markdown("You can check the code in " f"[GitHub]({urlGit})")

st.image("home.webp")
