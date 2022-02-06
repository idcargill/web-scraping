import requests
import re
from os.path import exists
from pathlib import Path
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Lisp_(programming_language)'
file_path = Path('./html_cache/lisp.html')

try:
  if exists(file_path):
    print(f'URL for {file_path} in cache \n\n')
    with open(file_path, 'r') as file:
      text = file.read()
      soup = BeautifulSoup(text, 'html.parser')
  else:
    print(f'Getting HTML from {file_path}\n\n')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    with open(file_path, 'w') as file:
      file.write(soup.prettify())
except Exception as e:
  print(e)
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')


def get_citations_needed_count(url):
  # searches url for citations needed
  # targets wiki citation 'a' tags
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  a_tags = soup.find_all('a')
  citations = [a for a in a_tags if 'citation needed' in a.text]
  print(f'Total Citations needed: {len(citations)}')
  return len(citations)


def get_citations_needed_report(url):

  if get_citations_needed_count(url) <= 0:
    return 'No citations needed here'

  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')

  a_tags = soup.find_all('a')
  citations = [a for a in a_tags if 'citation needed' in a.text]
  citation_needed = [a.find_parent('p') for a in citations]

  output_str = ''
  for item in citation_needed:
    word_list = item.text.split()
    output_str += '\n' + ' '.join(word_list)
  
  print(output_str)
  return output_str
