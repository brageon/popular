import tldextract
from pytube import YouTube
def Download(video_list):
    for url in video_list:
        youtube = YouTube(url.strip())
        youtube.streams.get_highest_resolution().download()
        print(f'The video {youtube.title} - was downloaded')
video_list = []
run = True
while run == True:
    link = str(input("Enter a YouTube URL or press D to download "))
    domain_name = tldextract.extract(link).domain
    if link.lower() == 'd':
        Download(video_list)
        run = False
    elif domain_name == 'youtube':
        video_list.append(link)