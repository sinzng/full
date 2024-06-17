from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

template = """{subject}를 주제로 {target}을 작성해주세요."""

prompt=PromptTemplate(template=template, 
    input_variables=["subject","target"]
)
llm_chain=LLMChain(
    llm=OpenAI(
        model="gpt-3.5-turbo-instruct", 
        temperature=0
    ),
    prompt=prompt,
    verbose = True
)

print(llm_chain.predict(subject="고양이", target="시"))
