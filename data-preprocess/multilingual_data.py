import os
import re
from tqdm import tqdm
from load import read_json_file,read_file_content
import pandas as pd

DIR_PATH = "2016_txt_data"
text_files = read_json_file("txt.json")
seg_files = read_json_file("seg.json")

LAN = {"french":"FRA","arabic":"PER"}

def get_content(data):
    content_pattern = re.compile(r'\d+\.\d+\|\d+\.\d+\|CC1\|(.*?)\n')
    content = content_pattern.findall(data)
    content = '.'.join(content)
    return content

def get_meta_data(data): 
    metadata_pattern = re.compile(r'LAN\|(.*?)\n')
    metadata = metadata_pattern.findall(data)
    return metadata

def get_arabic_data_from_html(data):
    # from bs4 import BeautifulSoup
    pass

def get_lang_data(text_files,LAN):
    lang_data = []

    for file_name in tqdm(text_files,desc=f"Extracting {LAN} data..."):
        file_path = os.path.join("2016_txt_data",file_name)
        data = read_file_content(file_path)
        meta_data = get_meta_data(data)
        try:
            if LAN in meta_data[0]:
                context = get_content(data)
                if context:
                    lang_data.append(context)
                else:
                    print(file_path)
            else:
                pass # here we need only specific LAN
        except:
            pass # no language detected

    return lang_data

text_french = get_lang_data(text_files,LAN['french'])
print(len(text_french))
seg_french = get_lang_data(seg_files,LAN['french'])
print(len(seg_french))

df = pd.DataFrame(text_french+seg_french, columns=['content'])
df.to_csv("french_data.csv",index=False)
print(df.shape)
"""
text_arabic = get_lang_data(text_files,LAN['arabic'])
print(len(text_arabic))
seg_arabic = get_lang_data(seg_files,LAN['arabic'])
print(len(seg_arabic))

df = pd.DataFrame(text_arabic+seg_arabic, columns=['content'])
df.to_csv("arabic_data.csv",index=False)
print(df.shape)"""