# youtube_downloader.py
# ✅ Supports video/audio download from any YouTube link
# ✅ Works with livestream, playlist, high-res, etc.

import yt_dlp


def download_video(url):
    # Configuration options
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # choose best quality available
        'outtmpl': '%(title)s.%(ext)s',        # file name = video title
        'noplaylist': False,                   # allow playlists too
        'quiet': False,                        # show progress
        'merge_output_format': 'mp4',          # merge into mp4
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("✅ Download complete!")
    except Exception as e:
        print("❌ Error:", type(e).__name__, "-", e)


if __name__ == "__main__":
    url = input("📺 Enter YouTube video URL (video or playlist): ").strip()
    if url:
        download_video(url)
    else:
        print("❌ No URL provided.")
