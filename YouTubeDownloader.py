import os
import yt_dlp


# Set default save path to YouTubeVids folder on the Desktop
save_path = os.path.expanduser("~/Desktop/YouTubeVids")

# Ensure the folder exists
os.makedirs(save_path, exist_ok=True)

# Ask for the YouTube video URL
url = input("Paste the YouTube video URL: ").strip()

# Check if the user entered a URL
if not url:
    print("Error: No URL provided. Please enter a valid YouTube video URL.")
    exit(1)

# Download options for yt-dlp
ydl_opts = {
    'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),  # Save as title.extension
    'format': 'bestvideo+bestaudio/best',  # Get best quality
    'postprocessors': [{
        'key': 'FFmpegMerger',
        'preferredformat': 'mp4'  # Convert to MP4 after merging
    }]
}

# Download video
try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print(f"\n✅ Download completed successfully!\n📁 Video saved to: {save_path}\n")
except yt_dlp.utils.DownloadError as e:
    print(f"\n❌ Download failed: {e}\nPlease check the URL and try again.")
except Exception as e:
    print(f"\n❌ An unexpected error occurred: {e}\n")

