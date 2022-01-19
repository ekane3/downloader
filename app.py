from datetime import date, datetime
from pytube import YouTube
import streamlit as st
from streamlit_player import st_player


# Date and Time of the day function 
def get_date_time():
    today = datetime.now()
    # create 3 columns
    col1,col2,col3 = st.columns(3)
    with col2:
        st.markdown(' ')
        st.markdown(' ')
        st.markdown(' ')
        st.markdown(' ')
        #st.markdown("### Date and Time 📆")
        st.markdown("##### 📆" +" "+ today.strftime("%d %B %Y "))
        st.markdown("# "+today.strftime(" %H:%M:%S"))
    
# Description function
def description_app():
    st.title("Stream Media downer 📈")
    st.markdown("Télécharger des vidéos sur YouTube")
    st.code("Entrer juste le lien de la vidéo et cliquer sur le bouton 🔍 pour commencer le téléchargement")

# Download function
def download_video():
    video = " "
    DOWNLOAD_FOLDER = "./downloads"
    st.markdown(' ')
    st.markdown("### Download video 📥")
    st.markdown(' ')
    st.markdown(' ')
    col1,col2 = st.columns(2)
    
    with col1:
        url = st.text_input("Enter the url of the video","https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        st_player(url) 
        
        #st.download_button(label="Download ",data=video)
        if st.button("Download video"):
            try:
                video_obj = YouTube(url)
                video_stream = video_obj.streams.get_highest_resolution()
                video_stream.download(DOWNLOAD_FOLDER)
            except:
                st.error("Error")

    with col2:
        url2 = st.text_input("Enter the url of the video ","https://youtu.be/CmSKVW1v0xM")
        st_player(url2) 
        st.download_button(label="Download2 ",data=video)
        if st.button('Say hello'):
            st.write('Why hello there')

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
    get_date_time()

if __name__ == "__main__":
    main()