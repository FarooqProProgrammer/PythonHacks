import os
import shutil

def move_files(src_folder, dest_folder, file_extension):
    for file in os.listdir(src_folder):
        if file.endswith(file_extension):
            file_path = os.path.join(src_folder, file)
            shutil.move(file_path, dest_folder)

if __name__ == '__main__':
    src_folder = input("Enter source folder path: ")
    dest_folder = input("Enter destination folder path: ")
    file_extension = input("Enter file extension to move (e.g. '.txt'): ")
    move_files(src_folder, dest_folder, file_extension)
