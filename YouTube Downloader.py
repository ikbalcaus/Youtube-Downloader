import pytube, os


destination = os.getcwd() + "/downloaded_music"
errors = []


with open("URLs.txt", "r") as file:
	URLs = file.read().splitlines()


for index, URL in enumerate(URLs, 1):
	if URL:
		try:
			yt = pytube.YouTube(URL)

			print(str(index) + '. Downloading "' + yt.title + '"')
		
			yt_video = yt.streams.filter(only_audio=True).first()
			video_file = yt_video.download(output_path=destination)
			audio_file = os.path.splitext(video_file)[0] + ".mp3"

			os.rename(video_file, audio_file)
			print(str(index) + '. Successfully downloaded "' + yt.title + '"\n')

		except:
			errors.append(str(index))
			print(str(index) + '. Failed to download URL "' + URL + '"\n')


if any(URLs) == False:
	input('\nFile "URLs.txt" is empty')
	exit()

if len(errors) == 0:
	with open("URLs.txt", "w") as file:
		file.write("")
	input("\nAll URLs have been successfully downloaded")
	exit()

else:
	print("\nErrors in following lines:", end=" ")
	for error in errors:
		print(error, end=" ")
	input()
	exit()
