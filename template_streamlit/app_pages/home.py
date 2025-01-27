import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.figure_factory as ff
import plotly.express as px
import seaborn as sns

st.markdown("# HOME 🎉")

# Add `key` argument to automatically access value from session state
st.text_input("Quey Parameter Example", key="example_input", placeholder="test here with some example query parameter")

# add to query parameters
if "example_input" in st.session_state:
    st.query_params.param = st.session_state.example_input
    if st.session_state.example_input == "":
        st.query_params.clear()

# read query parameter
if "param" in st.query_params:
    st.write(f"query param: {st.query_params.param}")


# cache expensive functions like data fetching
@st.cache_data
def create_data():
    return pd.DataFrame(np.random.uniform(0, 5, (20, 3)), columns=["x-axis", "y-axis", "color"])


if "data" not in st.session_state:
    st.session_state.data = create_data()
df = st.session_state.data

with st.expander("Default Chart"):
    st.markdown("### Charting with streamlit default chart")
    st.scatter_chart(
        df,
        x="x-axis",
        y="y-axis",
        size="color",
        color="color",
    )

with st.expander("Altair Chart"):
    st.markdown("### Charting with Altair")

    point_selector = alt.selection_point("point_selection")
    interval_selector = alt.selection_interval("interval_selection")
    chart = (
        alt.Chart(df, width=600)
        .mark_circle()
        .encode(
            x="x-axis",
            y="y-axis",
            size="color",
            color="color",
            tooltip=["x-axis", "y-axis", "color"],
            fillOpacity=alt.condition(point_selector, alt.value(1), alt.value(0.3)),
        )
        .add_params(point_selector, interval_selector)
    )

    altair_event = st.altair_chart(chart, key="alt_chart", on_select="rerun")

    st.write(altair_event)

with st.expander("Plotly Chart"):
    st.markdown("### Charting with Plotly")
    fig = px.scatter(
        df,
        x="x-axis",
        y="y-axis",
        color="color",
        size="color",
    )

    plotly_event = st.plotly_chart(fig, key="x-axis", on_select="rerun")

    st.write(plotly_event)

with st.expander("Seaborn Chart"):
    st.markdown("### Charting with Seaborn (based on plotly)")

    plot = sns.scatterplot(
        df,
        x="x-axis",
        y="y-axis",
        hue='color',
        size='color'
    )

    # Display the plot in Streamlit
    st.pyplot(plot.figure)
