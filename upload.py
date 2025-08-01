from langchain_community.document_loaders import PyPDFLoader
from langchain_ollama import OllamaEmbeddings
from qdrant_client import QdrantClient
from langchain_qdrant import QdrantVectorStore

embeddings = OllamaEmbeddings(model="llama3.2:3b")

file_path = "D:/Monish/project/ethical hacking.pdf"
loader = PyPDFLoader(file_path)
data=loader.load_and_split()
url=""
api_key=""
qdrant_client = QdrantClient(
    url=url, 
    api_key=api_key,
)

print(qdrant_client.get_collections())


qdrant = QdrantVectorStore.from_documents(
    data,
    embeddings,
    url=url,
    prefer_grpc=True,
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.ZD3kM_ygAAc1Y1VvGSKN8mDxZMXM8ZXoh2r5oZwEdcU",
    collection_name="hacking",
)