import json 

python_dict = {
    "이름" : "홍길동", 
    "나이" : 25, 
    "거주지" : "서울", 
    "신체정보" : {
        "키" : 176.7, 
        "몸무게" : 71.2 
    }, 
    "취미" : [
        "등산", 
        "자건거 타기",
        "독서" 
    ]
}

json_data = json.dumps(python_dict, indent=3, sort_keys=True, ensure_ascii=False)
print(type(json_data))
dict_data = json.loads(json_data) # 타입이 딕셔너리로 바뀜
print(type(dict_data))
print(dict_data)