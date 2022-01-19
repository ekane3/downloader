if url:
        try:
            yt = YouTube(url)
            video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
            st.success("Video downloaded")
        except:
            st.error("Error")


DOWNLOAD_FOLDER = "./downloads"
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    video_obj = YouTube(video_url)
    video_stream = video_obj.streams.get_highest_resolution()
    video_stream.download(DOWNLOAD_FOLDER)

    if st.button("Download video"):
        try:
            yt = YouTube(video_url)
            video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(DOWNLOAD_FOLDER)
            st.success("Video downloaded")
        except:
            st.error("Error")