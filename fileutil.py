from glob import glob

def write_to_file(file_name, content):
    file = open('websites/' + file_name, 'w', encoding='utf-8')
    file.writelines(content)
    file.close()

def get_deck_paths():
    return glob("websites/*.html")