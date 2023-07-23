from glob import glob
import os

def write_to_file(file_name, content):
    is_dir_created = os.path.isdir('websites')
    if not is_dir_created:
        os.makedirs("websites")
    file = open('websites/' + file_name, 'w', encoding='utf-8')
    file.writelines(content)
    file.close()

def get_deck_paths():
    return glob("websites/*.html")