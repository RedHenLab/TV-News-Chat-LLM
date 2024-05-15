import os
from tqdm import tqdm
import json

def get_files_ext(folder_path):
    seg_files = []
    txt_files = []
    all_files = os.listdir(folder_path)

    for filename in tqdm(all_files, desc="Splitting Files", unit="files"):
        if filename.endswith('.seg'):
            seg_files.append(filename)
        elif filename.endswith('.txt'):
            txt_files.append(filename)

    with open('seg.json', 'w') as f:
        json.dump(seg_files, f, indent=4)

    with open('txt.json', 'w') as f:
        json.dump(txt_files, f, indent=4)

    return seg_files, txt_files

def read_json_file(json_path):
    with open(json_path, 'r') as file:
        data = json.load(file)
    return data

def load_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File not found {file_path}")
        return None
    
def read_first_line_of_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read().strip() 
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return None

if __name__ == "__main__":
    print(load_file_content("seg.json"))