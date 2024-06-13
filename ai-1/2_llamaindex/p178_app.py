from llama_index import SimpleDirectoryReader


# 문서 로드 (data폴더에 문서를 넣어두세요)
documents= SimpleDirectoryReader("data").load_data()
print("documents:", documents)
