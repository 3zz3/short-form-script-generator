# This file will contain functions that generate Streamlit UI components.
import streamlit as st
from streamlit_option_menu import option_menu

def generate_sidebar():
    with st.sidebar:
        with st.sidebar:
            st.image("images/logo-bubble.png", width=250)
            menu_choice = option_menu("Main Menu", ["Script Generator", 'Metrics accuracy'],
                                      icons=['body-text', 'clipboard-data'], menu_icon="cast", default_index=0, orientation="vertical")
    return menu_choice

def display_script(script):
    st.text_area("Generated Voiceover", script, height=250)
