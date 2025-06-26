import streamlit as st
import pandas as pd
import plotly.express as px
from corpus_data import corpus_data, image_urls

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
short = "als"
data = next((c for c in corpus_data if c[1] == short), None)

# Sample detailed corpus data for table (you can extend this with real data)
# Using dummy numbers matching your original message:
corpus_stats = {
    'Plays': 30,
    'Characters': 375,
    'Male Characters': 232,
    'Female Characters': 110,
    'Text Units': 30,
    'Sp Units': 15092,
    'Stage Units': 7958,
    'Word Count Text': 329985,
    'Word Count Sp': 312184,
    'Word Count Stage': 44647
}

if data:
    name, _, desc = data
    st.set_page_config(page_title=name, layout="centered")

    # Title
    st.markdown(f"<h1>{name}</h1>", unsafe_allow_html=True)

    # Image
    st.image(image_urls.get(short))

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
    

# Sample data
data = [
    ["William Shakespeare", "Hamlet", "Prince of Denmark", 1603, 12, 3],
    ["Christopher Marlowe", "Doctor Faustus", "The Tragical History", 1604, 9, 2],
    ["Aphra Behn", "The Rover", "The Banish'd Cavaliers", 1677, 6, 4],
    ["John Webster", "The Duchess of Malfi", "", 1623, 7, 2],
    ["Ben Jonson", "Volpone", "The Fox", 1606, 10, 1],
    ["Susanna Centlivre", "The Busy Body", "", 1709, 4, 5],
    ["Thomas Middleton", "Women Beware Women", "", 1657, 5, 6],
    ["George Etherege", "The Man of Mode", "Sir Fopling Flutter", 1676, 7, 3],
    ["John Ford", "'Tis Pity She's a Whore", "", 1633, 8, 3],
    ["Elizabeth Inchbald", "Lovers' Vows", "", 1798, 4, 4],
    ["Oscar Wilde", "The Importance of Being Earnest", "", 1895, 5, 3],
    ["Henrik Ibsen", "A Doll's House", "", 1879, 3, 4],
    ["George Bernard Shaw", "Pygmalion", "", 1913, 4, 4],
    ["Lorraine Hansberry", "A Raisin in the Sun", "", 1959, 3, 4],
    ["Tennessee Williams", "A Streetcar Named Desire", "", 1947, 4, 5],
    ["Arthur Miller", "Death of a Salesman", "", 1949, 6, 1],
    ["Caryl Churchill", "Top Girls", "", 1982, 2, 7],
    ["Sarah Kane", "Blasted", "", 1995, 3, 2],
    ["Harold Pinter", "The Homecoming", "", 1965, 5, 1],
    ["Marina Carr", "By the Bog of Cats", "", 1998, 3, 4]
]

columns = ["Author", "Title", "Subtitle", "Year Printed", "Male Speakers", "Female Speakers"]
df = pd.DataFrame(data, columns=columns)

# Inject custom scrollable style and display the table
st.markdown("""
<style>
.scroll-table-wrapper {
    max-height: 400px;
    overflow-y: auto;
    border-radius: 12px;
    box-shadow: 0 0 12px rgba(0,0,0,0.1);
    margin: 30px auto;
    width: 130%;
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
<div class="scroll-table-wrapper">
{df.to_html(index=False, escape=False)}
</div>
""", unsafe_allow_html=True)

