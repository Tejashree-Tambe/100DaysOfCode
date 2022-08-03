import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id="id",
        client_secret="secret",
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

date = input("Which year you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"{BILLBOARD_URL}{date}")
billboard_html = response.text

soup = BeautifulSoup(billboard_html, "html.parser")

title_tags = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")

song_titles = [tag.getText() for tag in title_tags]

year = date.split("-")[0]
song_uris = []

for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")

    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        # print(f"{song} doesn't exist in Spotify. Skipped.")
        print(".", end="")

# print(song_uris)

playlist_details = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False,
                        description=f"A list of top 100 charts on Billboard in the {date} week.")

playlist_id = playlist_details['id']
# print(playlist_id)

# for song in song_titles:
sp.playlist_add_items(playlist_id=playlist_id, items=song_uris, position=None)

