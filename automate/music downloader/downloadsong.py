import os
with open("res.txt") as f:
	a = f.read()
	urls = a.split("\n")

for ext in urls:
	url = "https://www.youtube.com/watch?v="+ext
	command = 'youtube-dl.exe -o "./songs/%(title)s.%(ext)s" --extract-audio --audio-format mp3 {}'.format(url)
	print os.system(command)