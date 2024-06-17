import openai

user_input = input("AI와 채팅할 내용을 입력하세요 (종료하려면 end를 입력하세요)\n [나] : ")
messages = [{"role":"system", "content":"You are a helpful assistant"}]

ai_messsage = ""

while user_input != "end":
    messages = [{"role":"system", "content":ai_messsage},
                {"role":"user", "content":user_input}]
    messages.extend(messages)
    
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages , 
        max_tokens = 1000,
        temperature = 0.7,
        n = 1
    )
    ai_messsage = response.choices[0].message["content"]
    print(f"[AI] : {ai_messsage}")
    user_input = input("\n [나] : ")
    
if(user_input == "end"):
    print("AI와 채팅을 종료합니다") 