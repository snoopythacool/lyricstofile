import json
import os

PRIMARY_COLOR = "#D9BF41"
SECONDARY_COLOR = "#3370A6"
ARTIST_NAME = "Concrete Boys"
ALBUM_NAME = "It's Us Vol.1"
ALBUM_ID = "itsusvol1"

TARGET_FOLDER_NAME = "/Users/jihookim/Documents/OmegaT/Documents/target/"
SOURCE_FOLDER_NAME = "/Users/jihookim/Documents/OmegaT/Documents/source/"
RESULT_FOLDER_NAME = f"./final/{ALBUM_ID}/"

class Album():

    def __init__(self) -> None:
        self.title = []
        self.tracks_eng = []
        self.tracks_kor = []
        self.lyrics_eng = []
        self.lyrics_kor = []
    
    def add(self, track:str, lyrics:str):
        self.tracks_eng.append(track.split("\n")[0])
        self.tracks_kor.append(track.split("\n")[1])
        phrases_eng = []
        phrases_kor = []
        for phrase in lyrics.split("\n\n"):
            lines = phrase.split("\n")
            phrases_eng.append(lines[::2])
            phrases_kor.append(lines[1::2])
        pass
        self.lyrics_eng.append(phrases_eng)
        self.lyrics_kor.append(phrases_kor)

    def format(self) -> str:
        fres = ''
        fres += '{%extends "post.html"%}'
        fres += '{%block content%}'

        fres += f'<p style="text-align:center;"><span style="color:{SECONDARY_COLOR};"><strong><span style="font-size:24px;"><span style="background-color:{PRIMARY_COLOR};">{ARTIST_NAME} - {ALBUM_NAME}</span></span></strong></span></p>'
        fres += f'<p style="text-align:center;"><img alt="{ALBUM_NAME}" width=600 src="../static/imgs/{ALBUM_ID}.jpeg" /></p>&nbsp;' + '<hr />' + '<p>&nbsp;</p>'

        for i in range(len(self.tracks_eng)):
            fres += f'<p style="text-align:right;">{i+1}. {self.tracks_eng[i]} ({self.tracks_kor[i]})</p>'
        fres += '<p>&nbsp;</p>'

        # Track
        for i in range(len(self.tracks_eng)):
            fres += f'<hr />' + '<p>&nbsp;</p>'
            fres += f'<p><strong><span style="color:{SECONDARY_COLOR};"><span style="background-color:{PRIMARY_COLOR};">{i+1}. {self.tracks_eng[i]} <u>({self.tracks_kor[i]})</u></strong></p>' + '<p>&nbsp;</p>'
            
            # Phrase
            for j in range(len(self.lyrics_eng[i])):
                fres += '<p>'
                if j != 0:
                    fres += "<br />"

                # Line
                for k in range(len(self.lyrics_kor[i][j])):
                    fres += f'{self.lyrics_eng[i][j][k].replace("-", "&mdash;")}<br />'
                    fres += f'<u><em>{self.lyrics_kor[i][j][k].replace("-", "&mdash;")}</em></u><br />'
                fres += '</p>'
            fres += '<p>&nbsp;</p>'
        fres += '<p>&nbsp;</p>'

        fres = fres.replace("'", "&#39;")
        fres += '{%endblock%}'

        return fres

res = ""
original = ""
target = ""

with open(SOURCE_FOLDER_NAME + ALBUM_ID + ".txt", "r") as fr:
    original = fr.readlines()

with open(TARGET_FOLDER_NAME + ALBUM_ID + ".txt", "r") as fr:
    target = fr.readlines()

target = ["\n"] + target
for i in range(len(original)):
    if original[i] == "\n":
        res += target[i]
    else:
        res += original[i]

try:
    os.mkdir(RESULT_FOLDER_NAME)
except:
    input("Overwriting in process")

res = res.replace("\n\n\n\n", "\n\n\nInstrumental\n인스트루멘탈\n\n\n")

album = Album()
track_lyrics = res.split("\n\n\n")
track_lyrics = track_lyrics[:-1]
for i in range(0, len(track_lyrics), 2):
    if track_lyrics[i+1] == "\n\n":
        print("yup")
        track_lyrics[i+1] = ""
    album.add(track_lyrics[i], track_lyrics[i+1])

f = album.format()
with open(RESULT_FOLDER_NAME + ALBUM_ID + "_wp.html", "w") as fw:
    fw.write(
        f
    )

with open(RESULT_FOLDER_NAME + ALBUM_ID + "_dt.json", "w") as fw:
    json.dump({ALBUM_ID: {"id": ALBUM_ID, "name": ALBUM_NAME, "artist": ARTIST_NAME, "cover": ALBUM_ID + ".jpeg"}}, fw)