import lyricsgenius
import json
import os

SOURCE_FOLDER_NAME = "/Users/jihookim/Documents/OmegaT/Documents/source/"

ARTIST_NAME = "Blur"
ALBUM_NAME = "Parklife"
ALBUM_ID = "parklife"

token = "NU6mwVH_r0WjygRUu4-Vbl1Y2TWUsKsLXJQ881mPBF4DQljDxQV0hK4ZTOd-yOpl"
genius = lyricsgenius.Genius(token)

album = genius.search_album(ALBUM_NAME, ARTIST_NAME)
album.save_lyrics(ALBUM_ID)

with open(ALBUM_ID + ".json", "r") as fr:
    album_data = json.load(fr)

with open(SOURCE_FOLDER_NAME + ALBUM_ID + ".txt", "w") as fw: 
    for t in album_data["tracks"]:
        s = t["song"]
        fw.write(s["title"] + "\n"*2)

        segments = s["lyrics"].split("\n\n")
        for segment in segments:
            if len(segment) > 0:
                if segment[0] == "[":
                    fll = len(segment.split("\n")[0])
                    if len(segment) == fll:
                        segments.remove(segment)
                    else:
                        segment = segment[fll:]
                        segment = segment.replace("\n", "\n\n")
                        fw.write(segment + "\n")
                else:
                    segment = "\n" + segment
                    segment = segment.replace("\n", "\n\n")
                    fw.write(segment + "\n")
        fw.write("\n"*3)

os.remove(ALBUM_ID + ".json")