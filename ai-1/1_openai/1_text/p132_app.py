import openai

# 채팅 메시지 리스트 준비
messages = [
    {"role": "system", "content": "오타를 수정해 주세요."},
    {"role": "user", "content": "집에 준비 갈 완료."},
]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages, 
    temperature=0
)
print(response)
print('-'*50)
print(response["choices"][0]["message"]["content"])