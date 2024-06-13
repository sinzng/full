from llama_index import GPTVectorStoreIndex
from llama_index import Document

texts = ["text1","text2","text3" ]
Documnet = [Document(text) for text in texts]
print("Document: ", Document)

index = GPTVectorStoreIndex.from_documents(Documnet)
print("index: ", index)