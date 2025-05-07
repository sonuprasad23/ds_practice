# day10/playlist_model.py
class Playlist:
    def __init__(self, name, creator):
        self.name = name
        self.creator = creator
        self.songs = []
        print(f"Playlist '{self.name}' by {self.creator} created.")

    def add_song(self, song_title):
        if song_title not in self.songs:
            self.songs.append(song_title)
            print(f"'{song_title}' added to '{self.name}'.")
        else:
            print(f"'{song_title}' is already in '{self.name}'.")

    def remove_song(self, song_title):
        if song_title in self.songs:
            self.songs.remove(song_title)
            print(f"'{song_title}' removed from '{self.name}'.")
        else:
            print(f"'{song_title}' not found in '{self.name}'.")

    def list_songs(self):
        print(f"\n--- Songs in '{self.name}' ---")
        if not self.songs:
            print("  (No songs yet)")
        else:
            for i, song in enumerate(self.songs, 1):
                print(f"  {i}. {song}")
        print("------------------------")

    def get_song_count(self):
        return len(self.songs)

# Test Playlist
my_playlist = Playlist("Chill Vibes", "DJ Learner")
my_playlist.list_songs()
my_playlist.add_song("Sunset Groove")
my_playlist.add_song("Ocean Drive")
my_playlist.add_song("Starlight")
my_playlist.list_songs()
print(f"Song count: {my_playlist.get_song_count()}")
my_playlist.remove_song("Ocean Drive")
my_playlist.remove_song("Unknown Song")
my_playlist.list_songs()
print(f"Song count: {my_playlist.get_song_count()}")