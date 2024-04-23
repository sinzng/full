#!/usr/bin/env python

import json

data = {'age':30, 'name':"홍길동", 'address':"마포구 공덕동",
        'broadcast':{
            'sbs':5, 'kbs':9, 'mbc':11
        }
    }
json_str = json.dumps(data, ensure_ascii=False, indent=5, sort_keys=True) # 덤프를 쓰면 type이 그대로 나옴
print(json_str)
print(type(json_str))
print('-'*50)

json_data = json.loads(json_str) # json loads 썼더니 딕셔너리로 나옴
print(json_data)
print(type(json_data))
print('-'*50)

print(json_data['name'])
print(json_data['age'])
print(json_data['broadcast']['kbs']) # 딕셔너리 안에 딕셔너리, 이중 리스트..?쓰듯이

print('finished..')