import os

def delete_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            os.remove(file_path)

if __name__ == '__main__':
    folder_path = input("Enter folder path: ")
    delete_files(folder_path)
