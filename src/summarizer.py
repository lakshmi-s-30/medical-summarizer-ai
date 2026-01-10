from langchain_ollama import ChatOllama
from langchain_classic.chains.summarize import load_summarize_chainfrom langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

class MedicalSummarizer:
    def __init__(self):
        # This connects to the Ollama server running on your machine
        self.llm = ChatOllama(model="llama3.1", temperature=0)
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)

    def summarize(self, file_path):
        loader = PyMuPDFLoader(file_path)
        docs = loader.load_and_split(self.text_splitter)
        
        # Using the same map_reduce logic as before
        chain = load_summarize_chain(self.llm, chain_type="map_reduce")
        return chain.run(docs)