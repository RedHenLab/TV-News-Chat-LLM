import os
import json
import pandas as pd
import re
from load import read_json_file,read_file_content

import warnings
warnings.filterwarnings("ignore")

UNIQUE_LAN = []
DIR_PATH = "2016_txt_data"

#seg_files = read_json_file("seg.json")
#seg_data_first = read_file_content(f"2016_txt_data/{seg_files[0]}")

text_files = read_json_file("txt.json")
#text_data_first = read_file_content(f"2016_txt_data/{text_files[0]}")

def get_content(data):
    content_pattern = re.compile(r'\d+\.\d+\|\d+\.\d+\|CC1\|(.*?)\n')
    content = content_pattern.findall(data)
    content = '.'.join(content)
    return content

# currently as per the discussion on May-7 only extracting the text data
def get_meta_data(data): 
    metadata_pattern = re.compile(r'LAN\|(.*?)\n')
    metadata = metadata_pattern.findall(data)
    return metadata

only_text_data = []
for file_name in text_files:
    file_path = os.path.join("2016_txt_data",file_name)
    data = read_file_content(file_path)
    meta_data = get_meta_data(data)
    try:
        if "ENG" in meta_data[0]:
            only_text_data.append(get_content(data))
        else:
            print("Not english")
    except IndexError:
        print("No language detected in the file")

df = pd.DataFrame(only_text_data, columns=['content'])
df.to_csv("text_content.csv",index=False)