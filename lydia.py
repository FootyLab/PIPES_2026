import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
# === DATA LOADING SECTION ===
# Load your data here using load_catapult_data()
# Filter and prepare my_data for use in other sections
st.title("lydia's page")
if st.button("balloons"):
    st.balloons()
st.header(" Calculator")
input_one = st.number_input("your first number")
input_two = st.number_input("your second nuumber")
st.write(input_one + input_two)
import streamlit as st 
import numpy.random as rnd
match_minutes = 90
goals_per_match = 2.79
prob_per_minute = goals_per_match/match_minutes 

if st.button("play one match"):
 goals = 0
 for minute in range ( match_minutes):
     r = rnd.rand()
     if r < prob_per_minute:
         st.write(f"minutes{minute}: GOAL!" )
         goals = goals + 1
         st.subheader( f"FINAL WHISTLE - {goals} goals")
         
# === TITLE SECTION ===
import streamlit as st

st.title("The Goalkeepers' Union")
st.subheader("Goalkeepers save games. I can prove it with data.")

color = st.color_picker("Pick A Color", "#00f900")
st.write("The current color is", color)

# === KEY METRICS: GOALKEEPER REPORT CARD ===
# My research question:
# "How do you measure a goalkeeper's quality using xG?"
import streamlit as st
import pandas as pd


@st.cache_data(show_spinner="Loading matches (first time only)...")
def load_matches(comp_id, season_id):
    from mplsoccer import Sbopen
    parser = Sbopen()
    return parser.match(comp_id, season_id)

@st.cache_data(show_spinner="Loading match events (first time only)...")
def load_events(match_id):
    from mplsoccer import Sbopen
    parser = Sbopen()
    return parser.event(match_id)[0]

# Women's World Cup 2023 - Mary Earps (England) won the Golden Glove
matches = load_matches(72, 107)

TEAM = "England Women's"  # try "Australia Women's" or "Spain Women's"!
team_matches = matches[(matches["home_team_name"] == TEAM) | (matches["away_team_name"] == TEAM)]
st.write(f"{TEAM} played {len(team_matches)} World Cup matches")

# Collect every shot AGAINST our goalkeeper
all_shots = []
bar = st.progress(0, text="Collecting shots...")
ids = list(team_matches["match_id"])
for i, mid in enumerate(ids):
    events = load_events(mid)
    shots = events[events["type_name"] == "Shot"]
    all_shots.append(shots[shots["team_name"] != TEAM])
    bar.progress((i + 1) / len(ids), text=f"Match {i + 1} of {len(ids)}")
bar.empty()

shots_faced = pd.concat(all_shots)
on_target = shots_faced[shots_faced["outcome_name"].isin(["Goal", "Saved"])]
goals = (on_target["outcome_name"] == "Goal").sum()
xg_faced = on_target["shot_statsbomb_xg"].sum()

c1, c2, c3 = st.columns(3)
c1.metric("Shots on target faced", len(on_target))
c2.metric("Goals conceded", int(goals))
c3.metric("Goals prevented", f"{xg_faced - goals:+.1f}",
    help="xG faced minus goals conceded. Positive = my keeper beat the math!")
# === VISUALIZATION: EVERY SHOT MY KEEPER FACED ===
from mplsoccer import Pitch

st.header(f"Every shot on target {TEAM} faced")

pitch = Pitch(line_color="black")
fig, ax = pitch.draw()
for _, s in on_target.iterrows():
    color = "red" if s["outcome_name"] == "Goal" else "#4cbce4"
    pitch.scatter(s.x, s.y, s=900 * s["shot_statsbomb_xg"], color=color, alpha=0.7, ax=ax)
st.pyplot(fig)
st.caption("Red = goal. Blue = SAVED. Bigger circle = harder shot (higher xG). Every blue circle is the goalkeeper doing her job.")

# === HIGHLIGHTS: THE BEST SAVES ===
st.header("Top 5 hardest shots she saved")

saves = on_target[on_target["outcome_name"] == "Saved"]
best_saves = saves.sort_values("shot_statsbomb_xg", ascending=False).head(5)
st.dataframe(best_saves[["player_name", "shot_statsbomb_xg"]].rename(
    columns={"player_name": "Shooter", "shot_statsbomb_xg": "Chance quality (xG)"}))

save_pct = 100 * (len(on_target) - goals) / len(on_target)
st.metric("Save percentage", f"{save_pct:.0f}%")

# === INSIGHTS: MY DATA STORY ===
st.header("What I found")
st.write("MY QUESTION: How do you measure a goalkeeper's quality using xG?")
st.write("MY METHOD: I added up the xG of every shot on target my keeper faced. That equals the goals an AVERAGE keeper would concede. Then I compared it to what she actually conceded.")
st.write("GOALS PREVENTED = xG faced minus goals conceded")
st.write("- Positive number = my keeper saved goals an average keeper would have conceded")
st.write("- Negative number = shots went in that should have been stopped")
st.write(f"MY NUMBERS: xG faced {xg_faced:.1f}, goals conceded {int(goals)}, goals prevented {xg_faced - goals:+.1f}")
st.write("WHY I CARE: I'm a goalkeeper. Saves change matches - and now I can prove it with data instead of just feeling it.")

# === SANDBOX SECTION ===
# Your creative space! Add any additional features or experiments here
from streamlit_extras.let_it_rain import rain
def soccer():
    rain(
        emoji= "⚽",
        font_size=80,
        falling_speed=10,
        animation_length=9,
        )
 
if st.button(" a suprise  "):
    soccer()
    
    
    from streamlit_extras.let_it_rain import rain
def ocean():
    rain(
        emoji= "🌊",
        font_size=80,
        falling_speed=10,
        animation_length=9,
        )
 
if st.button(" summer  "):
    ocean()
 
