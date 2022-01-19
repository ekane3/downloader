from pytube import YouTube
import streamlit as st
from streamlit_player import st_player


# Description function
def description_app():
    st.title("Stream Media downer 📈")
    st.markdown("Telecharger des vidéos sur YouTube")
    st.markdown("""
            - Entrer juste le lien de la vidéo et cliquer sur le bouton 🔍 pour commencer le téléchargement
                """)

# Download function
def download_video():
    video = " "
    st.markdown(' ')
    st.markdown("### Download video 📥")
    url = st.text_input("Enter the url of the video")
    st_player("https://youtu.be/CmSKVW1v0xM")
    if url:
        try:
            yt = YouTube(url)
            video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
            st.success("Video downloaded")
        except:
            st.error("Error")
    st.download_button(label="Download ",data=video)
# Title bar function
def title_bar():
    project_title = st.sidebar.text_input("You can change the title of this project by input")
    if project_title:
        st.title(project_title)
    else:
        st.title("Demande de valeurs foncières")

# Main function
def main():
    # This streamlit method can only be called once and must be called before any other streamlit method
    st.set_page_config(
        page_title="Stream Media downer 📈",
        page_icon="random",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'https://www.extremelycoolapp.com/help',
            'Report a bug': "https://www.extremelycoolapp.com/bug",
            'About': "# Media downloader "
        }
    )
    st.sidebar.title("Currently streaming with ❤")
    st.sidebar.write(" ")
    st.sidebar.write(" ")
    st.sidebar.markdown("Made by [Emile.E](https://github.com/ekane3)")

    description_app()
    download_video()

if __name__ == "__main__":
    main()