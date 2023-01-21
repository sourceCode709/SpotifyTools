import os
from dotenv import load_dotenv
from spotify import Spotify


def get_top_artists(spotify: Spotify):
    spotify.list_top_artists()


def get_credentials():
    return {
        "ClientId": os.getenv("SPOTIFY_CLIENT_ID"),
        "Secret": os.getenv("SPOTIFY_CLIENT_SECRET")
    }
    
    
def create_playlist(spotify, artists, playlist_name):
    return spotify.create_playlist(artists, playlist_name)


def main():
    playlist_name = input("Enter name of playlist to be created:")
    artists = input("Enter artists:").split(",")

    load_dotenv()
    spotify_credentials = get_credentials()

    spotify = Spotify(spotify_credentials)
    create_playlist(spotify, artists, playlist_name)


main()
