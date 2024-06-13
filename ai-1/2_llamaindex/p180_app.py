from llama_index import GPTVectorStoreIndex
from llama_index import Document

texts = ["text1","text2","text3" ]
documnets = [Document(text) for text in texts]
print("Document: ", documnets)

index = GPTVectorStoreIndex.from_documents([])
print("index: ", index)

for doc in documents :
    index.insert(doc)