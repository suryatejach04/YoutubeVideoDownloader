import ssl
import urllib.request

# Disable SSL certificate verification
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE


url = "https://www.youtube.com/watch?v=aTGaGSuNw3o"
data = None
timeout = 10
# Now use this context in your request
opener = urllib.request.build_opener(urllib.request.HTTPSHandler(context=context))
response = opener.open(url, data, timeout)





import tkinter as Tk
# import all Tkinter libraries from the module
from tkinter import *
# From the  installed Pytube module, import the youtube library
from pytube import YouTube 

root = Tk()
root.geometry("700x300") # Size of the window
root.title("youtube downloader")

def download():
    url = YouTube(str(link.get())) #This captures the link(url) and locates it from YouTube.
    video = url.streams.get_highest_resolution() # This captures the streams available for downloaded for the video i.e. 360p, 720p, 1080p. etc.
    video.download() # This is the method with the instruction to download the video.
    Label(root, text="Downloaded ", font="arial 15") #Once the video is downloaded, this label `downloaded` is displayed to show dowload completion.

Label(root, text="Paste the link to download Youtube Videos!", font='san-serif 14 bold').pack()
link = StringVar() # Specifying the variable type
Label(root, text="Paste your link here", font='san-serif 15 bold')
link_enter = Entry(root, width=70, textvariable=link).place(x=30, y=85)
Button(root, text='Download', font='san-serif 16 bold', bg='red', padx=2, command=download).place(x=290, y=150)

root.mainloop()