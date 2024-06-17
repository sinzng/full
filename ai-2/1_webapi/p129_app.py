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
json_data = json.dumps(python_dict)
print(type(json_data))
print(json_data)