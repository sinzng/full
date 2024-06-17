from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain

## 첫번째 체인
# 템플릿 준비
template = """당신은 극작가입니다. 연극 제목이 주어졌을 때, 그 줄거리를 작성하는 것이 당신의 임무입니다.

제목 : {title}
시대 : {era}
시놉시스 :
"""
prompt=PromptTemplate(input_variables=["title", "era"],template=template)
# LLMChain 준비 
chain1=LLMChain(
    llm=OpenAI(
        model="gpt-3.5-turbo-instruct", 
        temperature=0
    ),
    prompt = prompt,
    output_key= "synopsis"
)

## 두번째 체인
# 템플릿 준비
template = """당신은 연극 평론가입니다. 연극의 시놉시스가 주어지면 그 리뷰를 작성하는 것이 당신의 임무입니다.

시놉시스 : {synopsis}
리뷰 :
"""
prompt=PromptTemplate(input_variables=["synopsis"],template=template)
# LLMChain 준비 
chain2=LLMChain(
    llm=OpenAI(
        model="gpt-3.5-turbo-instruct", 
        temperature=0
    ),
    prompt = prompt,
    output_key= "review"
)

## simple sequential chain으로 두 개의 체인 연결

overall_chain = SequentialChain(
    chains=[chain1, chain2],
    input_variables=["title", "era"],
    output_variables=["synopsis", "review"],
    verbose=True
)
print(overall_chain({"title" : "서울 랩소디", "era" : "100년 후의 미래"}))