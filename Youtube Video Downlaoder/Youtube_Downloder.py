from pytube import YouTube
import sys

def download_video(url):
    try:
        yt = YouTube(url)
        
        print("Title:", yt.title)
        print("Views:", yt.views)

        # Get the highest resolution stream
        yd = yt.streams.get_highest_resolution()
        
        # Download the video to the current directory
        yd.download()
        
        print("Download complete✅..")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("Enter the YouTube URL: ")
    
    download_video(url)