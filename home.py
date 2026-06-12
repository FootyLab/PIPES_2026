import streamlit as st
import pandas as pd

st.title("Welcome to our 2026 UTK PIPES Soccer Data Science App!")

st.image("./pics/2026_pipes_campers.png",width=600)

st.header("Soccer... and Data... *and* Science?")
st.write(
    "One of the biggest soccer clubs in the world, Liverpool FC, hired "
    "particle physicists to improve their team. This week, four investigators "
    "learned to do what they do: turn a question into data, data into a "
    "picture, and a picture into an answer."
)

st.header("Who we are")
info = {
    "Name": ["Olivia", "Lydia", "Ani", "Annakatelynn"],
    "Grade": ["Senior", "Senior", "Rising Senior", "Junior"],
    "High School": ["Sweetwater", "Sweetwater", "L&N STEM", "Sweetwater"],
    "Research Question": [
        "What really wins baseball games: home runs or just scoring runs?",
        "How do you measure a goalkeeper's quality using xG?",
        "Did teams that traveled farther to Qatar 2022 perform worse?",
        "Does bench press strength predict NFL draft success?",
    ],
}
st.dataframe(pd.DataFrame(info), use_container_width=True)

st.header("Data is a *Collection* of *Structured* *Information*")
st.write(
    "Every project here followed the data science cycle: "
    "**collect → store → load → analyze → share**. "
    "This app is the *share* step!"
)

st.divider()
st.subheader("Explore our projects!")
st.page_link("ani.py", label="Ani: World Cup Travel Distance", icon="✈️")
st.page_link("olivia.py", label="Olivia: The Moneyball Project", icon="⚾")
st.page_link("lydia.py", label="Lydia: The Goalkeepers' Union", icon="🧤")
st.page_link("annakatelynn.py", label="Annakatelynn: NFL Combine Secrets", icon="🏈")

st.divider()
st.header("The 5-sentence data story")
st.write("1. I wondered ... ?")
st.write("2. So I found data about ...")
st.write("3. I measured ... and made a chart")
st.write("4. The data showed ...")
st.write("5. That matters because ...")
