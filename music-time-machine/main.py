from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

CLIENT_ID = ""
CLIENT_SECRET = ""

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# previous_year = str(int(date[:4]) - 1)
# year_range = previous_year + "-" + date[:4]

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

song_list = []

songs = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
for song in songs:
    song_name = song.getText()
    song_list.append(song_name)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False, collaborative=False, description=f"Top Songs in {date}")
playlist_id = playlist["id"]


pp = pprint.PrettyPrinter(indent=4)
url_list = []
for song in song_list:
    try:
        urls = sp.search(q=song, limit=1, offset=0, type="track", market=None)["tracks"]["items"][0][
            "external_urls"]["spotify"]
        # urls = sp.search(q=f"track{song} year:year_range", limit=1, offset=0, type="track", market=None)["tracks"]["items"][0]["external_urls"]["spotify"]
    except IndexError:
        print(f"{song} is not available")
    else:
        url_list.append(urls)
# print(url_list)
sp.playlist_add_items(playlist_id, url_list, None)



