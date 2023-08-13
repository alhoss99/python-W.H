
from pytube import YouTube

# أدخل رابط الفيديو هنا
video_url = 'رابط الفيديو'

# تنزيل الفيديو
youtube = YouTube(video_url)
video = youtube.streams.get_highest_resolution()
video.download()