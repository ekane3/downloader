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
    st.code("Just enter the link of the video and click on the button 📥 to start the download")

# Download function
def download_video():
    video = " "
    DOWNLOAD_FOLDER = "./downloads"
    st.markdown(' ')
    st.markdown("## Demo ")
    st.markdown(' ')
    st.markdown(' ')
    col1,col2 = st.columns(2)
    
    with col1:
        url = st.text_input("Enter the url of the video","https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        st.markdown("**Title** : " + " " + YouTube(url).title)
        st_player(url) 
        
        #st.download_button(label="Download ",data=video)
        if st.button("Download video 📥"):
            try:
                video_obj = YouTube(url)
                video_stream = video_obj.streams.get_highest_resolution()
                video_stream.download()
                st.success("Video downloaded")
            except:
                st.error("Error")

    with col2:
        url2 = st.text_input("Enter the url of the video ","https://youtu.be/CmSKVW1v0xM")
        st.markdown("**Title** : " + " " + YouTube(url2).title)
        st_player(url2) 
        ideo_obj = YouTube(url2)
        video_stream = ideo_obj.streams.get_highest_resolution()
        video = video_stream.download()
        st.download_button(label="Download2 ",data=video)
        if st.button('Say hello'):
            nam = ideo_obj.streams.filter(file_extension='mp4', res="720p").first().download(DOWNLOAD_FOLDER)
            st.write(nam)
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