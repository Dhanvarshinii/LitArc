import streamlit as st
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
short = "am"
data = next((c for c in corpus_data if c[1] == short), None)

# Sample detailed corpus data for table (you can extend this with real data)
# Using dummy numbers matching your original message:
corpus_stats = {
    'Plays': 40,
    'Characters': 759,
    'Male Characters': 439,
    'Female Characters': 214,
    'Spoken Segments': 21990,
    'Stage Directions': 11019,
    'Total Word Count': 645014,
    'Word Count (Spoken Segments)': 578222,
    'Word Count (Stage Directions)': 79805
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
