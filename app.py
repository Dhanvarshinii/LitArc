# app.py
import streamlit as st
from corpus_data import corpus_data, image_urls

st.set_page_config(page_title="LitArc", layout="wide")

st.markdown("""
    <style>
    .decorative-title {
        text-align: center;
        font-family: 'Georgia', serif;
        font-size: 4.2em;
        font-weight: 700;
        letter-spacing: 2px;
        margin-bottom: 40px;
        color: #111;
    }
    .decorative-title span.lit {
        color: #8B0000;
        text-shadow: 1px 1px 2px rgba(139, 0, 0, 0.3);
    }
    .decorative-title span.arc {
        color: #696969;
        text-shadow: 1px 1px 2px rgba(105, 105, 105, 0.3);
    }
    .center-container {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 20px;
        margin-bottom: 40px;
    }
    .link-card {
        width: 320px;
        padding: 25px;
        border-radius: 16px;
        background-color: #f2f2f2;
        border: 2px solid #c0392b;
        box-shadow: 0 4px 12px rgba(192, 57, 43, 0.1);
        transition: transform 0.2s ease-in-out, box-shadow 0.3s ease;
        cursor: pointer;
        min-height: auto;  
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
    }
    .link-card:hover {
        transform: translateY(-4px) scale(1.03);
        box-shadow: 0 8px 20px rgba(192, 57, 43, 0.3);
        background-color: #f9e6e6;
    }
    .link-img {
        width: 100px;
        height: 100px;
        object-fit: cover;
        border-radius: 12px;
        margin-bottom: 12px;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    .link-name {
        font-family: 'Georgia', serif;
        color: #922b21;
        font-size: 1.2em;
        font-weight: 600;
        text-align: center;
        margin-bottom: 10px;
    }
    .description-text {
        font-family: 'Georgia', serif;
        color: #555555;
        font-size: 1em;
        text-align: justify;
        line-height: 1.4em;
        /* Remove min-height */
        min-height: auto; 
        /* Prevent truncation */
        overflow: visible;
        white-space: normal;
    }
    .card-wrapper {
        display: flex;
        justify-content: center;
        margin: 0 15px 20px 15px;
    }
    a {
        text-decoration: none !important;
    }
    </style>

    <div class="decorative-title">
        <span class="lit">Lit</span><span class="arc">Arc</span>
    </div>
""", unsafe_allow_html=True)

cards_per_row = 4

for i in range(0, len(corpus_data), cards_per_row):
    cols = st.columns(cards_per_row)
    for j, (name, short, desc) in enumerate(corpus_data[i:i+cards_per_row]):
        with cols[j]:
            link = f"/{short}"  # Page path for routing
            img_url = image_urls.get(short, "https://via.placeholder.com/100?text=No+Image")
            st.markdown(f"""
            <a href="{link}" target="_self">
                <div class="link-card">
                    <img src="{img_url}" class="link-img"/>
                    <div class="link-name">{name}</div>
                    <div class="description-text">{desc}</div>
                </div>
            </a>
            """, unsafe_allow_html=True)
