import customtkinter as ctk
from tkinter import ttk
from pytube import YouTube  
import os

def download_video():
    url=entry_url.get()
    # print(url)
    resolution=resolutions_var.get()
    progress_bar.pack(pady=("10p","5p"))
    progress_label.pack(pady=("10p","5p"))
    status_label.pack(pady=("10p","5p"))
    try:
        yt=YouTube(url,on_progress_callback=on_progress)
        stream=yt.streams.filter(res=resolution).first()
        # print(yt.title)

        # download the video to specific path 
        os.path.join("downloads",f"{yt.title}.mp4" )
        stream.download(output_path="downloads")
        status_label.configure(text="Downloaded!",text_color="white",fg_color="green")
    except Exception as e:
        status_label.configure(text=f"Error {str(e)}",text_color="white",fg_color="red")

def on_progress(stream,chunk,bytes_remaning):
    total_size=stream.filesize
    bytes_download=total_size-bytes_remaning
    percentage_completed=bytes_download/total_size *100
    # print(percentage_completed)
    progress_label.configure(text=str(int(percentage_completed))+"%")
    progress_label.update()

    progress_bar.set(float(percentage_completed/100))
# create the root window
root=ctk.CTk()
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# title for window
root.title("Youtube Downloader!")

# set the min and max width and height
root.geometry("720x480")
root.minsize(720,480)
root.maxsize(1080,720)

# create the frame to hold the content
content_frame=ctk.CTkFrame(root)
content_frame.pack(fill=ctk.BOTH,expand=True,padx=10,pady=10)

# create the label and the entry widget for the video url
url_label=ctk.CTkLabel(content_frame,text="Enter the youtube url here:")
entry_url=ctk.CTkEntry(content_frame,width=400,height=40)
url_label.pack(pady=("10p","5p"))
entry_url.pack(pady=("10p","5p"))

# download button
download_button=ctk.CTkButton(content_frame,text="Download",command=download_video)
download_button.pack(pady=("10p","5p"))

# create a resulation box
resolutions=["720p","360p","240p"]
resolutions_var=ctk.StringVar()
resolution_combobox= ttk.Combobox(content_frame,values=resolutions,textvariable=resolutions_var)
resolution_combobox.set("720p")
resolution_combobox.pack(pady=("10p","5p"))

# create the lable and progress bar to display 
progress_label=ctk.CTkLabel(content_frame,text="0%")
# progress_label.pack(pady=("10p","5p"))

progress_bar=ctk.CTkProgressBar(content_frame,width=400)
progress_bar.set(0)
# progress_bar.pack(pady=("10p","5p"))

# create the status label 
status_label=ctk.CTkLabel(content_frame,text="")

# to start the app
root.mainloop()