import streamlit as st

st.set_page_config(
    page_title="footyLab • Play to Learn | DataRook, Inc.",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://datarook.com/",
        "Report a bug": "https://datarook.com/#copyright",
        "About": "# FootyLab for the 2026 UTK PIPES Investigators Camp. Contact gus@datarook.com to learn more",
    },
)

home = st.Page("home.py", title="Home", icon="🏠")
ani = st.Page("ani.py", title="Ani's App", icon="✈️")
olivia = st.Page("olivia.py", title="Olivia's App", icon="⚾")
lydia = st.Page("lydia.py", title="Lydia's App", icon="🧤")
annakatelynn = st.Page("annakatelynn.py", title="Annakatelynn's App", icon="🏈")

pg = st.navigation([home, olivia, lydia, ani, annakatelynn])
pg.run()
