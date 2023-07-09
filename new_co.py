import tkinter
import customtkinter
from pytube import YouTube

def StartDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        quality=optionMenu.get()
        if quality=='audio':
            stream = ytObject.streams.filter(only_audio=True).first()
        elif quality=='video_lowquality':
            video = ytObject.streams.get_lowest_resolution()
        elif quality == 'video_highquality':
            video = ytObject.streams.get_highest_resolution()
        else:
            video = ytObject.streams.first()

        # Adding title to the screen
        title.configure(text=ytObject.title, text_color="white")

        video.download()
        finishLabel.configure(text="Download completed")
    except Exception as e:
        finishLabel.configure(text=f"ERROR: {e}", text_color="red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    print(per)
    pPercentage.configure(text=per + "%")
    pPercentage.update()

    #update progress bar
    progressBar.set(float(per)/100)

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# Adding UI elements
title = customtkinter.CTkLabel(app, text="Insert a YouTube link")
title.pack()

# Link
url = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url)
link.pack()

# Quality selection
qualityLabel = customtkinter.CTkLabel(app, text="Select Quality:")
qualityLabel.pack()

optionMenu=customtkinter.CTkOptionMenu(app,values=["audio","video_lowquality","video_highquality","3gcp"])
optionMenu.pack()

# Finished download
finishLabel = customtkinter.CTkLabel(app, text='')
finishLabel.pack()

# Progress percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Download button
download = customtkinter.CTkButton(app, text="Download", command=StartDownload)
download.pack(padx=10, pady=10)

# Run app
app.mainloop()
