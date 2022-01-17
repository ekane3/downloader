from pytube import YouTube
import streamlit as st


# Description function
def description_app():
    st.title("Stream Media downer 📈")
    st.markdown("Telecharger des vidéos sur YouTube")
    st.markdown("""
            - Entrer juste le lien de la vidéo et cliquer sur le bouton 🔍 pour commencer le téléchargement
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
    genre = st.sidebar.radio("👇",('App description', 'Download Now'))
    st.sidebar.write(" ")
    st.sidebar.write(" ")
    st.sidebar.markdown("Made by [Emile.E](https://github.com/ekane3)")

if __name__ == "__main__":
    main()