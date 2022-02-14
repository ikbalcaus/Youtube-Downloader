import os


songs = os.listdir("downloaded_music")


for song in songs:
    songModified = song.title().replace("Č", "C").replace("Č","C").replace("č","c").replace("Ć","C").replace("ć","c").replace("Š","S").replace("š","s").replace("Ž","Z").replace("ž","z").replace("Đ","D").replace("đ","d").replace("  ", " ").replace(".Mp3", ".mp3")
    os.rename("downloaded_music/" + song, "downloaded_music/" + songModified)
