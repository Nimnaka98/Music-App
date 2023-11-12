import pygame
import time


def _play(song):
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()


class MusicApplication:
    def __init__(self):
        self._songs = []
        pygame.init()

    def add_song(self, song):
        self._songs.append(song)

    def remove_song(self, song):
        if song in self._songs:
            self._songs.remove(song)
            print(f"Removed: {song}")
        else:
            print(f"Error: {song} not found in the playlist.")

    def play_song(self, song):
        if song in self._songs:
            print(f"Now playing: {song}")
            _play(song)
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)  # Adjust the tick value as needed
        else:
            print(f"Error: {song} not found in the playlist.")

    def display_songs(self):
        print("Songs in the playlist:")
        for song in self._songs:
            print(song)

    def get_songs(self):
        return self._songs


# Create a music application instance
app = MusicApplication()

# Add songs to the playlist
app.add_song("Lord Huron The Night We Met Official Audio.mp3")
app.add_song("Please Please Please Let Me Get What I Want 2008 Remaster.mp3")

# Display the songs in the playlist
app.display_songs()

# Play a song
app.play_song("Lord Huron The Night We Met Official Audio.mp3")

# Remove a song from the playlist
app.remove_song("Please Please Please Let Me Get What I Want 2008 Remaster.mp3")

# Display the updated playlist
app.display_songs()

# Allow time for the song to play before the program exits
time.sleep(5)  # Replace with the actual duration of the song
