import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
# === DATA LOADING SECTION ===
# Load your data here using load_catapult_data()
# Filter and prepare my_data for use in other sections
#from mplsoccer import Pitch, Sbopen
#import streamlit as st

#parser = Sbopen()
# Women's WC 2023 = (72, 107) | 2019 = (72, 30)
# Men's WC 2022 = (43, 3) | 2018 = (43, 106)

#matches = parser.match(competition_id=72, season_id=107)
#st.dataframe(matches[["match_id", "home_team_name", "away_team_name", "home_score", "away_score"]])

#events = parser.event(3893808)[0]
#shots = events[events["type_name"] == "Shot"]

#team = shots["team_name"].iloc[0]
#pitch = Pitch(line_color="black")
#fig, ax = pitch.draw()

#for _, s in shots[shots["team_name"] == team].iterrows():
#    color = "red" if s["outcome_name"] == "Goal" else "gray"
#    pitch.scatter(s.x, s.y, s=900 * s["shot_statsbomb_xg"], color=color, alpha=0.7, ax=ax)
#st.pyplot(fig)

# === TITLE SECTION ===
# Create your dashboard title and introduction
st.title("The Page!!!")
if st.button("Unicorns are better than Dragons!"):
    st.balloons()
    
    
st.write("6+7")
    
st.write("6+7")
    
#st.header("My calculator")
    
#a = st.number_input("your first number")
#b = st.number_input("your second number")

#st.write(a+b)

# === NFL COMBINE: STRENGTH MEETS DATA ===
# My research question:
# "Does strength (bench press) predict who gets drafted to the NFL?"
import streamlit as st
import pandas as pd


# Web address built from pieces so Notion doesn't make it a link!


@st.cache_data(show_spinner="Loading 20+ years of combine data (first time only)...")
def load_combine():
    COMBINE_URL = "https://" + "github" + ".com" + "/nflverse/nflverse-data" + "/releases/download/combine/combine.csv"
    from pandas import read_csv
    df = read_csv(COMBINE_URL)
    return df.dropna(subset=["bench", "forty"])

combine = load_combine()
st.write(f"{len(combine)} NFL prospects loaded!")

pos_picks = st.multiselect("Pick positions", sorted(combine["pos"].dropna().unique()), default=["QB", "RB", "WR", "DE"])
players = combine[combine["pos"].isin(pos_picks)]
st.dataframe(players[["player_name", "pos", "school", "wt", "forty", "bench", "vertical", "draft_ovr"]])

c1, c2, c3 = st.columns(3)
c1.metric("Most bench reps (225 lbs)", int(players["bench"].max()))
c2.metric("Fastest 40-yard dash", f"{players['forty'].min():.2f}s")
c3.metric("Prospects shown", len(players))

# === VISUALIZATION: STRENGTH vs SPEED ===
import altair as alt

st.header("Bench press reps vs 40-yard dash time")

scatter = alt.Chart(players).mark_circle(size=60).encode(
    x=alt.X("bench:Q", title="Bench press reps at 225 lbs"),
    y=alt.Y("forty:Q", title="40-yard dash (seconds)", scale=alt.Scale(zero=False)),
    color="pos:N",
    tooltip=["player_name", "pos", "school", "bench", "forty", "wt"],
).interactive()
st.altair_chart(scatter, use_container_width=True)

corr = players["bench"].corr(players["forty"])
st.metric("Correlation: bench vs forty", f"{corr:.2f}",
    help="Positive = stronger players tend to run slower. Trade-offs are real!")

drafted = players.dropna(subset=["draft_ovr"])
corr_draft = drafted["bench"].corr(drafted["draft_ovr"])
st.metric("Correlation: bench vs draft pick number", f"{corr_draft:.2f}",
    help="Negative = more reps goes with an EARLIER pick (lower number = drafted sooner)")

url="https://footylab-video-highlights.nyc3.digitaloceanspaces.com/UTKPIPES2026/FLC-107/none.png"

if st.button("rawr"):
    st.markdown(f"""
    <style>
    @keyframes imgFall{{
      0%{{transform:translateY(-20vh);opacity:.99;}}
      100%{{transform:translateY(110vh);opacity:.2;}}
    }}
    @keyframes emoFall{{
      0%{{transform:translateY(-20vh);opacity:1;}}
      100%{{transform:translateY(120vh) translateX(25px);opacity:0;}}
    }}
    .layer{{position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;overflow:hidden;}}
    .img{{position:absolute;width:160px;height:160px;background:url('{url}');background-size:cover;animation:imgFall 3s linear infinite;}}
    .emo{{position:absolute;font-size:65px;animation:emoFall 2.4s linear infinite;}}
    </style>

    <div class="layer">
      {''.join([f"<div class='img' style='left:{i}%;animation-delay:{i/12}s;'></div>" for i in range(0,100,7)])}
    </div>

    <div class="layer">
      {''.join([f"<div class='emo' style='left:{i}%;animation-delay:{(i%9)/4}s;'>{'🦖' if i%2==0 else '❤️'}</div>" for i in range(0,100,5)])}
    </div>
    """,unsafe_allow_html=True)


# === INSIGHTS: MY DATA STORY ===
st.header("What I found")
st.write("MY QUESTION: Does bench press strength predict NFL draft success?")
st.write("MY DATA: 20+ years of NFL Scouting Combine results")
st.write(f"Bench reps vs 40-yard dash correlation: {corr:.2f} (positive = stronger players tend to run slower)")
st.write(f"Bench reps vs draft pick number correlation: {corr_draft:.2f} (negative = more reps goes with an earlier pick)")
st.write("MY TAKE AS A POWERLIFTER: Strength matters, but the combine proves every position needs a DIFFERENT kind of athlete. Data lets teams see past the eye test - the same way xG lets soccer teams judge shots.")
# key= gives this button its own ID so it doesn't clash
# with the SLAYYYYY button on the Highlights tab!
if st.button("SLAYYYYYY", key="data_story_slay"):
    st.balloons()
# === SANDBOX SECTION ===
# Your creative space! Add any additional features or experiments here
from streamlit_extras.let_it_rain import rain

def scubaaaa():
    rain(
        emoji="🥽",
        font_size=89,
        falling_speed = 2,
        animation_length = 7
    )
if st.button("SCUBAAAA"):
    scubaaaa()
    
from streamlit_extras.let_it_rain import rain

def sixseven():
    rain(
        emoji="⁶🤷⁷",
        font_size=89,
        falling_speed = 2,
        animation_length = 7
    )
if st.button("sixseven"):
    sixseven()
