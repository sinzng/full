#!/usr/bin/env python

import csv
import json
import requests

# csv 파일 경로
csv_file_path = 'gangnam_park.csv'

# csv 파일 읽어오기

with open(csv_file_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)  # 첫 줄 skip

    # 각 라인마다 딕셔너리 생성 후 리스트에 추가
    data = []
    for line in reader:
        d = {
            'name': line[0],
            'addr': line[1],
            'lat': line[2],
            'lon': line[3]
        }
        data.append(d)
# json string으로 변환
json_string = json.dumps(data, ensure_ascii=False, indent=2)

print(json_string)

# JSON 데이터를 서버에 전송
url = 'http://192.168.1.28:8000/'
response = requests.post(url, json=data)