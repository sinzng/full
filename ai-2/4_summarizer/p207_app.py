import requests
import os
import textwrap

KAGI_API_KEY = os.environ["KAGI_API_TOKEN"]
#engines = ["cecil", "agnes", "daphne", "muriel"]
engines = ["cecil"]

api_url = "https://kagi.com/api/v0/summarize"
#contents_url = "https://www.khan.co.kr/opinion/column/article/202304100300035"
contents_url = "https://arxiv.org/pdf/1910.14296v2"
headers = {"Authorization": "Bot " + KAGI_API_KEY}

for engine in engines:
  parameters = {"url": contents_url, "engine": engine, "target_language": "KO"}
 
  r = requests.get(api_url, headers=headers, params=parameters)
  
  print(r.json())

  summary = r.json()['data']['output']

  shorten_summary = textwrap.shorten(summary, width=150, placeholder=' [...이하 생략...]')

  print("[요약 엔진]", engine)
  print("- 요약 내용(축약) : ", shorten_summary)
