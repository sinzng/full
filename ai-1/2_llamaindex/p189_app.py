from llama_index import downlad_loader, GPTVectorStoreIndex, ServiceContext, LLMPredictor, LangchainEmbedding
from llama_index.readers import BeautifulSoupReader
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import HuggingFaceEmbeddings
from llama_index import Document

#BeautifulSoupReader 초기화 
loader = BeautifulSoupReader()

# URL에서 문서 로드 
documents = loader.load_data(urls=["https://openai.com/blog/planning-for-agi-and-beyong"])
print("Documents loaded successufully")
print(f"Loaded documents: {documents}")

# Document 객체 생성
Document_objects =[Document(text=doc.text) for doc in documents]

# 임베딩 모델 준비 
embed_model = LangchainEmbedding(HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-V2"
))
print("Embedding Model initialized successfully")

# LLM Predictor 준비
llm_predictor = LLMPredictor(llm=ChatOpenAI(
    temperature=0, model_name="gpt-3.5-turbo" #모델명
))
print("LLM Predictor initialized successfully")

service_context = ServiceContext.from_defaults(
    llm_predictor=llm_predictor,
    embed_model=embed_model
)
print("Service Context initialized successfully")

index = GPTVectorStoreIndex.from_documents(
    Document_objects,
    service_context=service_context
)
print("Index initialized successfully")

query_engine = index.as_query_engine()
print("Query Engine initialized successfully")

query = "이 웹페이지에서 전하고 싶은 말은 무엇인가요? 한국어로 답해주세요"
response = query_engine.query(query)
print(f"query: {query}", end="\n")
print(f"response: {response}", end="\n")