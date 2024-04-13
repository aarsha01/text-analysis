import pandas as pd
from bs4 import BeautifulSoup
import requests
import numpy as np
import os
import textwrap
import glob
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context


# Reading the Excel file
df = pd.read_excel('input.xlsx', usecols='A, B')
df = df.iloc[:101]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
}

# Specify the folder name without the leading '/'
# foldername = 'extracted_datas'
# os.makedirs(foldername, exist_ok=True)

# for index, row in df.iterrows():
#     url_id = row['URL_ID']
#     url = row['URL']

#     page = requests.get(url, headers=headers)  # loading text in URL
#     soup = BeautifulSoup(page.content, 'html.parser')  # parsing URL text

#     if page.status_code == 200:
#         # td-post-content tagdiv-type,"tdb-block-inner td-fix-index"
#         title = soup.find('h1',attrs={'class': 'tdb-title-text'})  # extracting title of website

#         if not title:
#             title = soup.find('h1',attrs={'class': 'entry-title'})  # extracting title of website

#         title = title.string

#         # Check if content is present before trying to access it
#         contentParent = soup.find('div',attrs={'class': 'tdb_single_content'})

#         if contentParent:
#             content = contentParent.findChild('div', attrs={'class':'tdb-block-inner'}).find_all(string=True, recursive=True)
#         else:
#             content = soup.find('div', attrs={'class':'td-post-content tagdiv-type'}).find_all(string=True, recursive=True)

#         if content:
#             text = title + '\n'
#             for p_tag in content:
#                 text += textwrap.fill(p_tag.string, width=100)

#             filename = os.path.join(foldername, f"{url_id}.txt")
#             with open(filename, 'w', encoding='utf-8') as file:
#                 file.write(text)
#             print(url_id)
            
#         else:
#             print(f"No content found for URL ID {url_id}")
#     else:
#         print(f"Failed to fetch content for URL ID {url_id}")

# stop_word_dir='StopWords/'
# stop_words=set()
# stopwords_dir=glob.glob(stop_word_dir +'*.txt')
# for file in stopwords_dir:
#     with open(file,'r') as f:
#         text=f.read().splitlines()
#         stop_words.update(set(text))

#loading the text files
textfiles=[]
text_file_dir='extracted_datas/'
textfiles_dir=glob.glob(text_file_dir+'*.txt')
for txt in textfiles_dir:
    with open(txt,'r') as f:
       text=f.read()
       tokens =word_tokenize(text)
       print(tokens)
       break
