import os
import re
from load import read_json_file,read_file_content
from collections import Counter

DIR_PATH = "2016_txt_data"
LAN = list()
text_files = read_json_file("txt.json")
seg_files = read_json_file("seg.json")

def get_meta_data(data): 
    metadata_pattern = re.compile(r'LAN\|(.*?)\n')
    metadata = metadata_pattern.findall(data)
    return metadata

def text_lang_count(text_files):
    for file_name in text_files:
        file_path = os.path.join("2016_txt_data",file_name)
        data = read_file_content(file_path)
        meta_data = get_meta_data(data)
        try:
            LAN.append(meta_data[0])
        except:
            pass #No lang detected or wrong format
    counter = Counter(LAN)
    return counter

#print(text_lang_count(seg_files))
print(text_lang_count(text_files))