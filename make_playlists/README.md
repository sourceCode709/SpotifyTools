## Automated Spotify Playlist Generation
Problem:
- tired of listening to the same music
- tough to find new music that suit personal tastes
- countless hours spent manually creating new playlists to listen to while coding


Solution:
- tool that automatically generates Spotify playlists
- playlists compromised of top songs from artists of your choice
- massive playlists generated in under a minute


How to run:
- Setup a [Spotify Developer Account](https://developer.spotify.com/documentation/web-api/quick-start/)
- Create the file ".env" in the SpotifyTools/make_playlists directory with the following contents that can be found in your Spotify Developer Account:
    SPOTIFY_CLIENT_ID="yours_goes_here"
    SPOTIFY_CLIENT_SECRET="yours_goes_here"

- Run the following commands in the /SpotifyTools/make_playlists directory from your terminal:
```
pip install spotipy
pip install python-dotenv
python make_playlist.py
```

**Note: Developed with Python 3.8.10**
