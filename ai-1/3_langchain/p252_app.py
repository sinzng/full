from langchain.agents import load_tools
from langchain.chat_models import ChatOpenAI
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.agents import initialize_agent

tools = load_tools(
    tool_names = ['serpapi', 'llm-math'], 
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0 
    )
)

# 메모리 생성
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# 에이전트 생성
agent = initialize_agent(
    agent="conversational-react-description",
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0
    ), 
    tools=tools,
    memory=memory,
    verbose=True
)

print(agent.run("좋은 아침입니다."))
print('-'*50)

print(agent.run("우리집 반려묘 이름은 라푸입니다."))
print('-'*50)

print(agent.run("우리집 반려묘 이름을 불러주세요"))
print('-'*50)

print(agent.run("오늘 한국 서울의 날시를 웹 검색으로 확인하세요."))
print('-'*50)


