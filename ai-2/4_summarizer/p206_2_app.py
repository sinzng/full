import requests
import os
import textwrap

KAGI_API_KEY = os.environ["KAGI_API_KEY"]

api_url = "https://kagi.com/api/v0/summarize"
contents_url = "https://www.khan.co.kr/opinion/column/article/202304100300035"
headers = {"Authorization": "Bot" + KAGI_API_KEY}
parameters = {"url": contents_url, "target_language": "ko"}

r = requests.get(api_url, headers=headers, params=parameters)

summary = r.json()['data']['output']
shorten_summary = textwrap.shorten(summary,width=150, placeholde=' [...이하 생략...]')
print("요약 내용(축약) : ", shorten_summary)