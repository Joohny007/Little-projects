import pyshorteners
import streamlit as st #para crear la pagina web (runnear como "streamlit run main.py")

def shorten_url(url):
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url)
    return shortened_url

#creamos app web con stremamlit
st.set_page_config(page_title="URL Shortener", page_icon="✏️", layout="centered")
st.image("images/url_image.jpg", use_container_width=True)
st.title("URL Shortener")
url = st.text_input("Enter the URL")
if st.button("Generate new URL"):
    st.write("URL shortened: ", shorten_url(url))