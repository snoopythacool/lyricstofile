import os

PRIMARY_COLOR = "#F2D027"
SECONDARY_COLOR = "#262223"
ARTIST_NAME = "Blur"
ALBUM_NAME = "Parklife"
ALBUM_ID = "parklife"
COVER_URL = "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/8a/71/66/8a71664b-3baa-537b-e008-b32d86da27bc/5099997227755.jpg/600x600bb.jpg"

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
        fres = ""

        fres += f'<p style="text-align:center;"><span style="color:{SECONDARY_COLOR};"><strong><span style="font-size:24px;"><span style="background-color:{PRIMARY_COLOR};">{ARTIST_NAME} - {ALBUM_NAME}</span></span></strong></span></p>'
        fres += f'<p style="text-align:center;"><img alt="{ALBUM_NAME}.jpeg" editor_component="image_link" src="{COVER_URL}" /></p>' + '<p style="text-align:center;">유튜브 -&nbsp;</p>' + '<p style="text-align:center;">&nbsp;</p>' + '<hr />' + '<p>&nbsp;</p>'

        for i in range(len(self.tracks_eng)):
            fres += f'<p style="text-align:right;"><span style="color:{SECONDARY_COLOR};"><span style="background-color:{PRIMARY_COLOR};">{i+1}. {self.tracks_eng[i]} <u>({self.tracks_kor[i]})</u></p>'
        fres += '<p>&nbsp;</p>'

        # Track
        for i in range(len(self.tracks_eng)):
            fres += f'<hr />' + '<p>&nbsp;</p>'
            fres += f'<p><strong><span style="color:{SECONDARY_COLOR};"><span style="background-color:{PRIMARY_COLOR};">{i+1}. {self.tracks_eng[i]} <u>({self.tracks_kor[i]})</u></strong></p>' + '<p>&nbsp;</p>' + '<p>https://www.youtube.com/watch?v=</p>' + '<p>&nbsp;</p>'
            
            # Phrase
            for j in range(len(self.lyrics_eng[i])):
                fres += '<p>'
                if j != 0:
                    fres += "<br />"

                # Line
                for k in range(len(self.lyrics_kor[i][j])):
                    fres += f'{self.lyrics_eng[i][j][k].replace("-", "&mdash;")}<br />'
                    fres += f'<u>{self.lyrics_kor[i][j][k].replace("-", "&mdash;")}</u><br />'
                fres += '</p>'
            fres += '<p>&nbsp;</p>'
        fres += '<p>&nbsp;</p>'

        fres = fres.replace("'", "&#39;")

        return fres

res = ""
original = ""
target = ""

with open(SOURCE_FOLDER_NAME + ALBUM_ID + ".txt", "r") as fr:
    original = fr.readlines()

with open(TARGET_FOLDER_NAME + ALBUM_ID + ".txt", "r") as fr:
    target = fr.readlines()

target = ["\n"] + target

try:
    os.mkdir(RESULT_FOLDER_NAME)
except:
    input("Overwriting in process")

with open(RESULT_FOLDER_NAME + ALBUM_ID + ".txt", "w") as fw:
    for i in range(len(original)):
        if original[i] == "\n":
            res += target[i]
        else:
            res += original[i]
    fw.write(res)

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
with open(RESULT_FOLDER_NAME + ALBUM_ID + "_le.txt", "w") as fw:
    fw.write(
        f
    )