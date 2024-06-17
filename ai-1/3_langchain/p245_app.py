from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter

with open("akazukin_all.txt") as f:
    text_all = f.read()

text_splitter = CharacterTextSplitter(
    separator="\n\n",
    chunk_size=300,
    chunk_overlap=20,
)
texts=text_splitter.split_text(text_all) 

print(len(texts))
for text in texts: 
    print(text[:10], ":", len(text))

docs = [Document(page_content=text) for text in texts]

chain = load_summarize_chain(
    llm = OpenAI(
        model = "gpt-3.5-turbo-instruct", 
        temperature=0
    ), 
    chain_type = "map_reduce", #빅데이터 할때 사용하는 프롬프트, 맵을 줄인다는 의미로 복잡한 문제를 해결할때(빅데이터처리) 문제를 조각조각 내고 각각의 청크를 분석하여 점점 좁혀나가나는 방식
)
print(chain.run(docs))