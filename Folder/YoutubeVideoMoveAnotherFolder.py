
## This script download videos from Youtube and move into  another folder dest_folder

import os
import shutil
from pytube import *


def move_files(src_folder, dest_folder, file_extension):
    files_to_move = [f for f in os.listdir(src_folder) if f.endswith(file_extension)]
    num_files = len(files_to_move)
    for i, file in enumerate(files_to_move):
        file_path = os.path.join(src_folder, file)
        dest_path = os.path.join(dest_folder, file)
        shutil.move(file_path, dest_path)
        print(f"Moved file {i+1} of {num_files}: {file}")


def YoutubeVideo(link):
    for video in link:
        yt = YouTube(video)
        yt.streams.filter(res="360p").first().download()

if __name__ == '__main__':
    # Add video links in this array videos link should be one or more
    link = []
    src_folder = os.getcwd()
    dest_folder = input("Enter destination folder path: ")
    file_extension = '.mp4'
    YoutubeVideo(link)
    move_files(src_folder, dest_folder, file_extension)

