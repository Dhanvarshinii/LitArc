import streamlit as st
import pandas as pd
import requests
import io
import plotly.express as px
from corpus_data import corpus_data, image_urls

st.markdown("""
<style>
.litarc-title {
    font-family: Georgia, serif;
    font-size: 4em;
    font-weight: bold;
    text-align: center;
    margin-top: 20px;
    margin-bottom: 30px;
    background: linear-gradient(90deg, #8B0000, #111);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    color: transparent;
}
</style>
<div class="litarc-title">LitArc</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<style>
h1 {{
    font-family: Georgia, serif;
    font-weight: 700;
    font-size: 3.5em;
    text-align: center;
    background: linear-gradient(90deg, #8B0000 50%, #111 50%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    color: transparent;
    margin-bottom: 30px;
}}
.corpus-table {{
    font-family: Georgia, serif;
    border-collapse: collapse;
    width: 80%;
    margin-left: auto;
    margin-right: auto;
    margin-top: 30px;
    box-shadow: 0 0 12px rgba(0,0,0,0.15);
    border-radius: 12px;
    overflow: hidden;
}}
.corpus-table th, .corpus-table td {{
    border: 1px solid #ddd;
    padding: 12px 18px;
    text-align: center;
    font-size: 1.1em;
}}
.corpus-table th {{
    background-color: #8B0000;
    color: white;
    font-weight: 700;
}}
.corpus-table tr:nth-child(even) {{
    background-color: #f9f9f9;
}}
</style>
""", unsafe_allow_html=True)

# Identify this corpus
short = "tat"
data = next((c for c in corpus_data if c[1] == short), None)

# Sample detailed corpus data for table (you can extend this with real data)
# Using dummy numbers matching your original message:
corpus_stats = {
    'Plays': 30,
    'Characters': 375,
    'Male Characters': 232,
    'Female Characters': 110,
    'Spoken Segments': 15092,
    'Stage Directions': 7958,
    'Total Word Count': 329985,
    'Word Count (Spoken Segments)': 312184,
    'Word Count (Stage Directions)': 44647
}

if data:
    name, _, desc = data
    st.set_page_config(page_title=name, layout="centered")

    # Title
    st.markdown(f"<h1>{name}</h1>", unsafe_allow_html=True)

    # Center the image using HTML
    image_url = image_urls.get(short)
    if image_url:
        st.markdown(f"""
            <div style="display: flex; justify-content: center; margin: 20px 0;">
                <img src="{image_url}" style="max-width: 100%; height: auto; border-radius: 10px;">
            </div>
        """, unsafe_allow_html=True)


    # Description
    st.markdown(f"""
    <div style="font-family: Georgia, serif; font-size: 1.2em; text-align: justify; margin-top: 20px;">
        {desc}
    </div>
    """, unsafe_allow_html=True)

    # Key insights table
    st.markdown("""
    <h2 style='text-align: center; font-family: Georgia, serif;'>🎭 Corpus Statistics</h2>
    """, unsafe_allow_html=True)

    # Build the HTML table
    table_html = "<table class='corpus-table'>"
    table_html += "<tr><th>Metric</th><th>Value</th></tr>"
    for key, val in corpus_stats.items():
        table_html += f"<tr><td>{key}</td><td>{val}</td></tr>"
    table_html += "</table>"

    st.markdown(table_html, unsafe_allow_html=True)

else:
    st.error("Corpus not found.")


# Author-Play Catalogue
st.markdown("""
<h2 style='text-align: center; font-family: Georgia, serif;'>🎭 Author-Play Catalogue</h2>
""", unsafe_allow_html=True)

# Sample data
API_BASE = "https://dracor.org/api/v1/"

@st.cache_data
def fetch_metadata(corpus_name: str) -> pd.DataFrame:
    url = f"{API_BASE}corpora/{corpus_name}/metadata/csv"
    resp = requests.get(url)
    resp.raise_for_status()
    return pd.read_csv(io.StringIO(resp.text))

# Select corpus
corpus_code = "tat"
df_meta = fetch_metadata(corpus_code)

# Validate required columns
required_columns = ["firstAuthor", "title", "subtitle", "yearPrinted"]
missing = [col for col in required_columns if col not in df_meta.columns]

if missing:
    st.error(f"Required columns not found in metadata: {missing}")
    st.stop()

# Prepare and rename for display
df_show = df_meta[required_columns].rename(columns={
    "firstAuthor": "Author",
    "title": "Title",
    "subtitle": "Subtitle",
    "yearPrinted": "Year Printed"
})

# Inject custom scrollable style and display the table
st.markdown("""
<style>
.center-table-container {
    display: flex;
    justify-content: center;
    margin-top: 20px;
    margin-bottom: 40px;
}

.scroll-table-wrapper {
    max-height: 400px;
    overflow-y: auto;
    border-radius: 12px;
    box-shadow: 0 0 12px rgba(0,0,0,0.1);
    width: 90%;
}

/* Style the actual table */
.scroll-table-wrapper table {
    border-collapse: collapse;
    width: 100%;
    font-family: Georgia, serif;
    font-size: 1.05em;
}

.scroll-table-wrapper th {
    background-color: #8B0000;
    color: white;
    font-weight: bold;
    position: sticky;
    top: 0;
    z-index: 1;
    padding: 12px 18px;
    border-bottom: 2px solid #ddd;
    text-align: center;
}

.scroll-table-wrapper td {
    padding: 12px 18px;
    border-bottom: 1px solid #eee;
    text-align: center;
}

.scroll-table-wrapper tr:nth-child(even) {
    background-color: #f9f9f9;
}
</style>
""", unsafe_allow_html=True)

# Render the table as scrollable HTML
st.markdown(f"""
<div class="center-table-container">
    <div class="scroll-table-wrapper">
        {df_show.to_html(index=False, escape=False)}
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

# 📊 Bar chart: Number of Plays per Author
author_counts = df_show.groupby("Author").size().reset_index(name="Number of Plays")

fig = px.bar(
    author_counts,
    x="Author",
    y="Number of Plays",
    labels={"Author": "Author", "Number of Plays": "Count of Plays"},
    height=600,
)

st.markdown("""
<h2 style='text-align: center; font-family: Georgia, serif;'>🎭 No of Authors per Play</h2>
""", unsafe_allow_html=True)

# Display the chart
st.plotly_chart(fig, use_container_width=True)