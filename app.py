from pytube import YouTube
import streamlit as st

DOWNLOAD_PATH = "./downloads"
video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
video_obj = YouTube(video_url)

#stream = video_obj.streams.first()
stream = video_obj.streams.get_highest_resolution()

stream.download(DOWNLOAD_PATH)

st.write("Downloaded video to:", DOWNLOAD_PATH)

# Description function
def description_app():
    st.title("Description analysis 📈")
    st.markdown("Les données sont recueillies pour chaque année fiscale, nous avons donc 5 jeux de données, comptabilisant plusieurs millions de transactions, constitués d'après la documentation fournie auprès du fournisseur des données des variables suivantes, nous allons juste nous interesser aux données de l'année 2020 :")
    st.markdown("""
            -terrain : Surface du terrain
                
                """)
# Title bar function
def title_bar():
    project_title = st.sidebar.text_input("You can change the title of this project by input")
    if project_title:
        st.title(project_title)
    else:
        st.title("Demande de valeurs foncières")

# Main function
def main():
    st.set_page_config(
        page_title="App valeurs foncieres",
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
    genre = st.sidebar.radio("👇",('Analysis description', 'Lookup Analysis'))
    st.sidebar.write(" ")
    st.sidebar.write(" ")
    st.sidebar.markdown("Made by [Emile.E](https://github.com/ekane3)")
    
    if genre == 'Analysis description':
        st.balloons()
        description_analysis()
    else:
        title_bar()

if __name__ == "__main__":
    main()