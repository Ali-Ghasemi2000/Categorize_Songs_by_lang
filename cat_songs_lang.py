import shutil
import os
from langdetect import detect
from mutagen.mp3 import MP3, HeaderNotFoundError

def get_song_language(filename):
    # Read the mp3 file
    audio = MP3(filename)

    # Extract the song title from the file name
    song_title = filename.split('.')[0]

    # Use langdetect to determine the language of the song title
    language = detect(song_title)

    return language

# specify the directory path
path = "D:/آهنگ/mp3/"

# get a list of all the files in the directory
files = os.listdir(path)
files_only = [file for file in files if os.path.isfile(os.path.join(path, file))]

i = 1
tot = len(files)

# print the list of file names
for file in files_only:
    print(f"{i} of {tot}")
    f_path = path + file
    src_path = f_path
    try:
        dest_path = path + get_song_language(f_path)
        os.mkdir(dest_path)
        shutil.move(src_path, dest_path)
    except FileExistsError:
        dest_path = path + get_song_language(f_path)
        shutil.move(src_path, dest_path)
    except HeaderNotFoundError:
        print(f"{file} is not in MP3 format.")
    except Exception as e:
        # handle any other exception
        print(f"An error occurred: {e}")
    i += 1

