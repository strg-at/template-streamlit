import streamlit as st

# update page setup like favicon and title here
st.set_page_config(
    page_title="Streamlit Template",
    page_icon=":material/sentiment_satisfied:",
    layout="centered",
    initial_sidebar_state="auto",
)

home = st.Page("app_pages/home.py", title="Home", default=True)
page_1 = st.Page("app_pages/page1.py", title="Title Of Page 1")

# if submenu needed:
# pg = st.navigation(
#    {
#        "Navigation Submenu": [home, page_1],
#    },
# )

pg = st.navigation([home, page_1])

pg.run()
