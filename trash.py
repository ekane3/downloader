if url:
        try:
            yt = YouTube(url)
            video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
            st.success("Video downloaded")
        except:
            st.error("Error")