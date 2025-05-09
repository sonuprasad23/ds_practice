class Playlist:
    def __init__(self, name, creator): self.name, self.creator, self.songs = name, creator, []
    def add_song(self, song_title): self.songs.append(song_title)
    def __len__(self): return len(self.songs)

    def __getitem__(self, index):
        """Allows accessing songs using indexing like my_playlist[index]."""
        print(f"__getitem__ called with index {index}")
        return self.songs[index] 

pl_indexed = Playlist("Indexed Mix", "Indexer")
pl_indexed.add_song("Track 1")
pl_indexed.add_song("Track 2")
pl_indexed.add_song("Track 3")

print(f"First song: {pl_indexed[0]}")   
print(f"Second song: {pl_indexed[1]}")
print(f"Slice [0:2]: {pl_indexed[0:2]}")