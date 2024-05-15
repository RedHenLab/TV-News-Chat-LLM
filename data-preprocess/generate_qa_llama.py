import os
import json
from getpass import getpass
import time
import pandas as pd
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import ResponseSchema, StructuredOutputParser

def to_lower(x):
  return x.lower()

def divide_string(input_string):
    substring_length = len(input_string) // 6
    substrings = [input_string[i:i+substring_length] for i in range(0, len(input_string), substring_length)]

    return substrings

GROQ_API = getpass("Enter your API key: ")
data = pd.read_csv("text_content.csv")
data.dropna(inplace=True)
data['content'] = data['content'].apply(to_lower)

template = open("prompt.txt","r").read()
Q_A = []
i = 1030

llama3_model = ChatGroq(temperature=0.1, groq_api_key=GROQ_API, model_name="llama3-70b-8192")

for news_data in data.iloc[1030:1100].content:
  substrings = divide_string(news_data)
  i+=1
  print(i)
  for substring in substrings:
    prompt = template.replace("{context}",substring)
    response = llama3_model.invoke(prompt)
    try:
      Q_A.append(json.loads(response.content))
      with open("temp_llama.txt","a") as f:
         f.write(response.content)
    except:
      with open("rejected_llama.txt","a") as f:
         f.write(response.content)
      print("sdmskfnegnrognrgnnfbnfbnfp")
      pass
    time.sleep(60)

with open('data1000_1100.jsonl', 'w') as jsonl_file:
    for item in Q_A:
        for q in item['questions']:
            json.dump({"question": q["question"], "answer": q["answer"]}, jsonl_file)
            jsonl_file.write('\n')