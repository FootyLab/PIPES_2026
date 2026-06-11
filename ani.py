import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
# === DATA LOADING: WORLD CUP RESULTS ===
# My research question:
# "Did teams that traveled farther to Qatar 2022 perform worse?"
st.header ("Ani's World Cup Distance Analysis")
st.subheader ("Does the distance that teams travel for the World Cup affect their performance?")
st.write ("Using the data from the 2022 Men's World Cup that was based in Qatar. Travel distances can effect players through things like jet lag, climate swings, altitude changes, and more. In addition, the closer that a team is to the host country will allow fans to support them easier.")

import streamlit as st
import pandas as pd

@st.cache_data(show_spinner="Loading World Cup 2022 results (first time only)...")
def load_matches(comp_id, season_id):
    from mplsoccer import Sbopen
    parser = Sbopen()

    return parser.match(comp_id, season_id)

matches = load_matches(43, 106)  # Men's World Cup 2022
st.write(f"Loaded all {len(matches)} matches from Qatar 2022!")

st.subheader ("Distance to Qatar Capital (km)")
import pandas as pd

teams = [
    {"Team": "Qatar", "Distance_km": 0},
    {"Team": "Saudi Arabia", "Distance_km": 800},
    {"Team": "Iran", "Distance_km": 1900},
    {"Team": "Serbia", "Distance_km": 3400},
    {"Team": "Croatia", "Distance_km": 3700},
    {"Team": "Poland", "Distance_km": 3900},
    {"Team": "Tunisia", "Distance_km": 3900},
    {"Team": "Germany", "Distance_km": 4200},
    {"Team": "Switzerland", "Distance_km": 4300},
    {"Team": "Cameroon", "Distance_km": 4600},
    {"Team": "Denmark", "Distance_km": 4700},
    {"Team": "Netherlands", "Distance_km": 4900},
    {"Team": "France", "Distance_km": 4900},
    {"Team": "Belgium", "Distance_km": 4900},
    {"Team": "England", "Distance_km": 5200},
    {"Team": "Wales", "Distance_km": 5300},
    {"Team": "Spain", "Distance_km": 5400},
    {"Team": "Ghana", "Distance_km": 5800},
    {"Team": "Portugal", "Distance_km": 6000},
    {"Team": "Morocco", "Distance_km": 6000},
    {"Team": "Senegal", "Distance_km": 7000},
    {"Team": "South Korea", "Distance_km": 7900},
    {"Team": "Japan", "Distance_km": 8300},
    {"Team": "Canada", "Distance_km": 10700},
    {"Team": "USA", "Distance_km": 11300},
    {"Team": "Brazil", "Distance_km": 11800},
    {"Team": "Australia", "Distance_km": 12300},
    {"Team": "Argentina", "Distance_km": 13200},
    {"Team": "Uruguay", "Distance_km": 13300},
    {"Team": "Ecuador", "Distance_km": 13500},
    {"Team": "Mexico", "Distance_km": 13700},
    {"Team": "Costa Rica", "Distance_km": 13900},
]

df = pd.DataFrame(teams)

# Sort by distance
df_sorted = df.sort_values("Distance_km", ascending=True)

st.dataframe(df_sorted)
    
# === KEY METRICS: THE POINTS TABLE ===
# Win = 3 points, draw = 1, loss = 0 (just like the real table)
points = {}
wins = {}
for _, m in matches.iterrows():
    home, away = m["home_team_name"], m["away_team_name"]
    hs, aw = m["home_score"], m["away_score"]
    for t in (home, away):
        points.setdefault(t, 0)
        wins.setdefault(t, 0)
    if hs > aw:
        points[home] += 3
        wins[home] += 1
    elif aw > hs:
        points[away] += 3
        wins[away] += 1
    else:
        points[home] += 1
        points[away] += 1

results = pd.DataFrame({"Team": list(points.keys()),
                        "Points": list(points.values()),
                        "Wins": list(wins.values())})

# StatsBomb calls the USA "United States" - make the names match mine
df_sorted["Team"] = df_sorted["Team"].replace({"USA": "United States"})

missing = set(df_sorted["Team"]) - set(results["Team"])
if missing:
    st.warning(f"These teams didn't match - check spelling: {missing}")

df_merged = df_sorted.merge(results, on="Team")
st.subheader("Travel Distance + World Cup Results")
st.dataframe(df_merged.sort_values("Points", ascending=False))

# === VISUALIZATION: THE ANSWER ===
import altair as alt

st.header("Travel Distance vs World Cup Points")

base = alt.Chart(df_merged)
dots = base.mark_circle(size=120, color="#FFFFFF").encode(
    x=alt.X("Distance_km:Q", title="Distance traveled to Qatar (km)"),
    y=alt.Y("Points:Q", title="Points earned"),
    tooltip=["Team", "Distance_km", "Points", "Wins"],
)
labels = base.mark_text(dy=-12, fontSize=10).encode(
    x="Distance_km:Q", y="Points:Q", text="Team")
trend = dots.transform_regression("Distance_km", "Points").mark_line(color="#cc222a")

st.altair_chart((dots + labels + trend).interactive(), use_container_width=True)

corr = df_merged["Distance_km"].corr(df_merged["Points"])
st.metric("Correlation: distance vs points", f"{corr:.2f}",
    help="From -1 to 1. Near 0 = no connection. Negative = more travel, fewer points.")
# === INSIGHTS: MY DATA STORY ===
st.header("Results")
st.write("My Question: Did teams that traveled farther to Qatar 2022 perform worse?")
st.write("My Method: I built a travel-distance table for all 32 teams, used StatsBomb data to calculate every team's points (3 per win, 1 per draw), merged the two tables, and measured the correlation.")
st.write(f"My Correlation: {corr:.2f}. This is a very weak correlation that is very close to zero.")
st.write("My Answer: Argentina traveled 13,200 km... and won the whole World Cup. The data says jet lag is not destiny.")
st.write("Data Science Cycle: Collect, store, load, analyze, share")
st.write ("Future Research: Use data from other World Cup tournaments to see if the same theme holds true.")

# === SANDBOX SECTION ===
# Your creative space! Add any additional features or experiments here
from streamlit_extras.let_it_rain import rain
def basketball_rain():
    rain(
        emoji="🏀",
        font_size=100,
        falling_speed=2,
        animation_length=2,
        )
if st.button("What is the best sport?"):
    basketball_rain()
    
    
def USA_rain():
    rain(
        emoji="🇺🇸",
        font_size=100,
        falling_speed=2,
        animation_length=2,
        )
if st.button ("Which women's team has won the most world cups?"):
    USA_rain()
    
def brazil_rain():
    rain(
        emoji="🇧🇷",
        font_size=100,
        falling_speed=2,
        animation_length=2,
        )
if st.button ("Which men's team has won the most world cups?"):
    brazil_rain()
