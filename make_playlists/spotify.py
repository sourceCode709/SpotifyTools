import spotipy
from spotipy.oauth2 import SpotifyOAuth

class Spotify:
    def __init__(self, credentials: dict):
        self.credentials =  credentials
        self.client = self.__authenticate()
    
    def __authenticate(self):
        return spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=self.credentials["ClientId"],
                client_secret=self.credentials["Secret"],
                scope=[
                    "playlist-read-private", 
                    "user-library-read", 
                    "user-follow-read", 
                    "user-top-read",
                    "playlist-modify-private"
                ],
                redirect_uri="http://localhost",
                open_browser=False
        )
    )
        
    def __get_user_id(self):
        return self.client.current_user()["id"]
        
    def __get_results(self, data):
        results = data
        results_list = results["items"]
        
        while "next" in results:
            results = self.client.next(results)

            if "items" in results:
                results_list.extend(results["items"])
            
        return results_list
    
    def __get_artist_id(self, artist):
        results = self.client.search(
            q=f"artist: {artist}",
            type="artist"
        )
        artists = self.__get_results(results["artists"])
        
        return artists[0]["id"]
    
    def __get_artist_top_tracks(self, artist):
        tracks =  self.client.artist_top_tracks(artist_id=artist)["tracks"]
        
        return [track["id"] for track in tracks]
        
    
    def create_playlist(self, artists, playlist_name):
        playlist_tracks = []
        uid = self.__get_user_id()
        
        for artist in artists:
            artist_id = self.__get_artist_id(artist)
            top_tracks = self.__get_artist_top_tracks(artist_id)
            playlist_tracks.extend(top_tracks)
        
        playlist = self.client.user_playlist_create(
            user=uid,
            public=False,
            name=playlist_name
        )["id"]
        
        created = self.client.user_playlist_add_tracks(
            user=uid,
            playlist_id=playlist,
            tracks=playlist_tracks
        )
        
        return "snapshot_id" in created
    
    def list_top_artists(self):
        data = self.client.current_user_top_tracks()
        
        artists = self.__get_results(data)

        for artist in artists:
            print(artist["name"])
