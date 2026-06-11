# === DATA LOADING: BASEBALL! ===
# My research question:
# "What REALLY wins baseball games: home runs or just scoring runs?"
# (This is the Moneyball question!)
import streamlit as st
import pandas as pd
from pandas import read_csv
from streamlit import link_button
import numpy as np
import altair as alt

# The address is built from pieces so Notion
# doesn't turn it into a clickable link!
st.header("The baseball data")
teams = pd.read_csv("./data/mlb_teams.csv")
teams["win_pct"] = teams["wins"] / (teams["wins"] + teams["losses"])
st.success(f"Loaded {len(teams)} MLB team seasons!")

# Keep the modern era so the story is clean
modern = teams[teams["year"] >= 2009].copy()
st.dataframe(modern[["year", "team_name", "wins", "losses", "win_pct", "runs_scored", "homeruns"]])
# === TITLE SECTION ===
# Create your dashboard title and introduction
st.title("Olivia's Page")
if st.button("Baseball is the Best Sport"):
    st.balloons()
from streamlit_extras.let_it_rain import rain
def dolla_bills():
    rain(
        emoji= "🪑",
        font_size=110,
        falling_speed=5,
        animation_length=2,
        )
if st.button("just press it....."):
    dolla_bills()
    st.text("this is the chair Morgan Wallen threw to get arrested. click the button below for context....")
if st.button("We <3 Morgan Wallen"):
    st.image("https://media-cldnry.s-nbcnews.com/image/upload/t_fit-760w,f_auto,q_auto:best/rockcms/2025-10/251001-Morgan-Wallen-ch-1338-58f709.jpg")
    st.text("Don't follow in his footsteps and get arrested, it would not be smart.")
st.header("My Calculator")
a  = st.number_input("the first number")
b  = st.number_input("the second number")
st.write(a + b)
#import time
#with st.empty():
#    for seconds in range(10):
#        st.write(f" {seconds} seconds have passed")
#        time.sleep(1)
#    st.write(":material/check: 10 seconds over!")
#st.button("RERUN!!!")
import numpy.random as rnd
match_minutes = 90
goals_per_match = 2.79
prob_per_minute = goals_per_match/match_minutes
if st.button("Play one match"):
    goals = 0
    for minute in range(match_minutes):
        r = rnd.rand()
        if r < prob_per_minute:
            st.write(f"minute {minute}: GOAL!")
            goals = goals + 1
    st.subheader(f"FINAL WHISTLE - {goals} goals")

# === VISUALIZATION: THE MONEYBALL CHARTS ===
import altair as alt
st.title("The Moneyball Project")
st.header("What wins games: home runs or runs?")

col1, col2 = st.columns(2)
with col1:
    hr = alt.Chart(modern).mark_circle(size=60, color="#cc222a").encode(
        x=alt.X("homeruns:Q", title="Home runs in a season"),
        y=alt.Y("wins:Q", title="Wins"),
        tooltip=["team_name", "year", "homeruns", "wins"],
    ).interactive()
    st.altair_chart(hr, use_container_width=True)
with col2:
    runs = alt.Chart(modern).mark_circle(size=60, color="#359465").encode(
        x=alt.X("runs_scored:Q", title="Runs scored in a season"),
        y=alt.Y("wins:Q", title="Wins"),
        tooltip=["team_name", "year", "runs_scored", "wins"],
    ).interactive()
    st.altair_chart(runs, use_container_width=True)

# Correlation = how connected two things are (-1 to 1)
hr_corr = modern["homeruns"].corr(modern["wins"])
runs_corr = modern["runs_scored"].corr(modern["wins"])
m1, m2 = st.columns(2)
m1.metric("Home runs vs wins", f"{hr_corr:.2f}")
m2.metric("Runs scored vs wins", f"{runs_corr:.2f}")
st.caption("Closer to 1.00 = stronger connection. Which tells the better story?")

# === HIGHLIGHTS: MY TEAM'S STORY ===
st.header("Pick a team, tell its story")

team_pick = st.selectbox("Choose a team", sorted(modern["team_name"].unique()),1)
my_team = teams[teams["team_name"] == team_pick]

line = alt.Chart(my_team).mark_line(color="#0c172c", point=True).encode(
    x=alt.X("year:Q", title="Season"),
    y=alt.Y("wins:Q", title="Wins"),
    tooltip=["year", "wins", "homeruns", "runs_scored"],
).interactive()
st.altair_chart(line, use_container_width=True)

best = my_team.loc[my_team["wins"].idxmax()]
st.success(f"Best season: {int(best['year'])} - {int(best['wins'])} wins, {int(best['homeruns'])} home runs!")

# === INSIGHTS: MY DATA STORY ===
st.header("What I found")
st.write("MY QUESTION: What really wins baseball games - home runs or just scoring runs?")
st.write(f"MY DATA: {len(teams)} real MLB team seasons from the OpenIntro stats website")
st.write(f"Home runs vs wins correlation: {hr_corr:.2f}")
st.write(f"Runs scored vs wins correlation: {runs_corr:.2f}")
winner = "SCORING RUNS" if runs_corr > hr_corr else "HOME RUNS"
st.success(f"The stronger connection is... {winner}!")
st.write("WHY IT MATTERS: This is the discovery behind Moneyball - the Oakland A's won by buying runs (walks, on-base) instead of expensive home-run stars. Data changed baseball forever. Home runs look pretty in the stats, however that is not the only important thing is baseball.")
if st.button("Story complete!"):
    st.balloons()
# === SANDBOX SECTION ===
# Your creative space! Add any additional features or experiments here
import time
with st.spinner("Wait for it...don't go", show_time=True):
    time.sleep(5)
st.success("Done!")
st.button("Rerun so you see a spinner again!")
