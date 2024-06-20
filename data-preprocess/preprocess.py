import os
import json
from tqdm import tqdm
import pandas as pd
import re
from load import read_json_file,read_file_content

import warnings
warnings.filterwarnings("ignore")

DIR_PATH = "2016_txt_data"

seg_files = read_json_file("seg.json")
#seg_data_first = read_file_content(f"2016_txt_data/{seg_files[0]}")

text_files = read_json_file("txt.json")
#text_data_first = read_file_content(f"2016_txt_data/{text_files[0]}")

def get_content(data):
    content_pattern = re.compile(r'\d+\.\d+\|\d+\.\d+\|CC1\|(.*?)\n')
    content = content_pattern.findall(data)
    content = '.'.join(content)
    return content

def get_meta_data(data): 
    patterns = {
        'lan': re.compile(r'LAN\|(.*?)\n'),
        'src': re.compile(r'SRC\|(.*?)\n'),
        'dur': re.compile(r'DUR\|(.*?)\n'),
        'col': re.compile(r'COL\|(.*?)\n')
    }
    return {key: next((match for match in pattern.findall(data)), None) for key, pattern in patterns.items()}

# for only english
def get_lang_data(text_files):
    page_content = []
    metadata = []
    for file_name in tqdm(text_files,desc=f"Extracting English Language data..."):
        file_path = os.path.join("2016_txt_data",file_name)
        data = read_file_content(file_path)
        info = get_meta_data(data)
        info['path'] = file_name
        try:
            if "ENG" in info['lan']:
                context = get_content(data)
                if context:
                    page_content.append(context)
                    metadata.append(info)
                else:
                    pass
        except:
            pass
    return page_content,metadata

text_eng,metadata = get_lang_data(text_files)
#print(len(text_eng))
#print(len(metadata))
seg_eng,metadata_seg = get_lang_data(seg_files)
#print(len(seg_eng))
#print(len(metadata_seg))

df = pd.DataFrame({"context":text_eng+seg_eng,"metadata":metadata+metadata_seg})
print(df.shape)
df.to_csv("2016_01_english.csv",index=False)