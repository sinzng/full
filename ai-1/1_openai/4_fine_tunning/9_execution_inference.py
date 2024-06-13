from openai import OpenAI
client = OpenAI()

prompt =input( "질문 입력:")
response = client.chat.completions.create(
    model = "ft:gpt-3.5-turbo-0125:personal::9Y47jYv0", 
    messages = [{"role":"user", "content":prompt}],
)

print(response.choices[0].message.content.strip())
