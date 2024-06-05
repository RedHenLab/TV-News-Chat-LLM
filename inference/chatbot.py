import os
from getpass import getpass

HF_TOKEN = getpass("HF Access Token:")
os.environ["HUGGINGFACEHUB_API_TOKEN"] = HF_TOKEN

from langchain_community.llms import HuggingFaceHub

model_name = "lucifertrj/redhen-lab-news-chat-7b"

llm = HuggingFaceHub(
    repo_id=model_name,
    model_kwargs={"temperature": 0.5, "max_length": 64,"max_new_tokens":512}
)

print(llm.invoke("Why is Donald Trump not participating in the Fox News Republican debate?"))