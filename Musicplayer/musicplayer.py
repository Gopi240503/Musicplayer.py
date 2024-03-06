import os
import tkinter as tk
from tkinter import filedialog
from pygame import mixer

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Music Player")
        self.root.geometry("400x200")

        # Initialize Pygame mixer
        mixer.init()

        # Playlist
        self.playlist = []

        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        # Playlist listbox
        self.playlist_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.playlist_listbox.pack(fill=tk.BOTH, expand=True)

        # Buttons
        self.btn_add = tk.Button(self.root, text="Add", command=self.add_to_playlist)
        self.btn_add.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn_remove = tk.Button(self.root, text="Remove", command=self.remove_from_playlist)
        self.btn_remove.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn_play = tk.Button(self.root, text="Play", command=self.play_music)
        self.btn_play.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn_stop = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.btn_stop.pack(side=tk.LEFT, padx=5, pady=5)

    def add_to_playlist(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        if file_path:
            self.playlist.append(file_path)
            self.playlist_listbox.insert(tk.END, os.path.basename(file_path))

    def remove_from_playlist(self):
        selected_index = self.playlist_listbox.curselection()
        if selected_index:
            del self.playlist[selected_index[0]]
            self.playlist_listbox.delete(selected_index)

    def play_music(self):
        selected_index = self.playlist_listbox.curselection()
        if selected_index:
            selected_song = self.playlist[selected_index[0]]
            mixer.music.load(selected_song)
            mixer.music.play()

    def stop_music(self):
        mixer.music.stop()

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
