import requests
from bs4 import BeautifulSoup
API="http://www.billboard.com/"
response=requests.get("https://www.americantop40.com/music/top-songs/")
data=response.text
soup=BeautifulSoup(data,"html.parser")
list1=soup.select(selector="a span")
song_names=[]
for element in list1:
    song_names.append(element.getText())
CLIENT_DI1="a1fcbbc80e1a421b846799d0e3937bc2"
CLIENT_SECRET1="88a2473c9c4443fa83bfed6add8125ee"
import spotipy
from spotipy.oauth2 import  SpotifyOAuth
sp=spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id=CLIENT_DI1,
        client_secret=CLIENT_SECRET1,
        show_dialog=True,
        cache_path="token.txt"

    )
)
user_id=sp.current_user()["id"]
print(user_id)
print(song_names)
song_uris=[]
for song in song_names:
    result=sp.search(q=f"track:{song} year:{2023}",type="track")
    try:
        uri=result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} does not exist in spotify.Skipped :)")
play_list=sp.user_playlist_create(user=user_id, name="The top 40 songs of 2023",public=False)
sp.playlist_add_items(playlist_id=play_list["id"],items=song_uris)
#idk how I have created and completed this project :) Funny!