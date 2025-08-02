import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp
import os

# Main download function


def download_video():
    url = url_entry.get()
    path = path_var.get()

    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL.")
        return
    if not path:
        messagebox.showerror("Error", "Please select a download folder.")
        return

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
        'quiet': False,
        'merge_output_format': 'mp4',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", "Download complete!")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Choose folder function
def choose_folder():
    folder = filedialog.askdirectory()
    path_var.set(folder)


# Setup GUI
root = tk.Tk()
root.title("YouTube Downloader - c0ff33py Edition")
root.geometry("500x200")
root.resizable(False, False)

# URL Input
tk.Label(root, text="YouTube Video URL:").pack(pady=(10, 0))
url_entry = tk.Entry(root, width=60)
url_entry.pack()

# Folder Selection
path_var = tk.StringVar()
tk.Label(root, text="Download Folder:").pack(pady=(10, 0))
tk.Entry(root, textvariable=path_var, width=45).pack(
    side=tk.LEFT, padx=(10, 0))
tk.Button(root, text="Browse", command=choose_folder).pack(
    side=tk.LEFT, padx=5)

# Download Button
tk.Button(root, text="Download", command=download_video,
          bg="green", fg="white").pack(pady=20)

root.mainloop()
