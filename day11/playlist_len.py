class Playlist:
    def __init__(self, name, creator):
        self.name = name
        self.creator = creator
        self.songs = []
    def add_song(self, song_title): self.songs.append(song_title)
    def get_song_count(self): return len(self.songs) 

    def __len__(self): 
        """Returns the number of songs in the playlist."""
        print("__len__ called!")
        return len(self.songs)

pl = Playlist("My Hits", "Me")
pl.add_song("Song A")
pl.add_song("Song B")
print(f"Song count (method): {pl.get_song_count()}")
print(f"Song count (len()): {len(pl)}")