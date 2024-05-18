# wget url, cat * | grep mp4?, cdn
import urllib.request as urllib2
dwn_link = 'url'
file_name = 'strike.mp4' 
rsp = urllib2.urlopen(dwn_link)
with open(file_name,'wb') as f:
    f.write(rsp.read())
# melt a{1..9}.mp4 -consumer avformat:jen.mp4 acodec=libmp3lame vcodec=libx264