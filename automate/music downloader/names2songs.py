import requests,json,urlparse
from urllib2 import urlopen
with open("playlist.txt","r") as f:
	playlist = f.read().split("\n")

playlist = map(lambda q: ((q.replace(" ","+")).replace("-","")).replace("++","+"),playlist)
playlist = filter(lambda x: x!="" ,playlist)

#vidinfo_url = "http://youtube.com/get_video_info?video_id="
#https://www.googleapis.com/youtube/v3/search?q={query}&key={key}&part=snippet&type=video&maxResults={0-50}
api_key = "<api_key>"
base_url = "https://www.googleapis.com/youtube/v3/search?q={}&key={}&part=snippet&type=video&maxResults=2"

c=0;
with open("res.txt","a+") as res_file:
	for q in playlist:
		r = requests.get(base_url.format(q,api_key))
		res_file.write(json.loads(r.text)["items"][1]["id"]["videoId"]+"\n")
		c+=1
		print(c)