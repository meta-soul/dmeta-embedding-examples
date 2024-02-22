import sys
import pickle

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.faiss import FAISS
from langchain_community.document_loaders import UnstructuredFileLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from dmeta import DMetaTextEmbeddings
from dotenv import load_dotenv

load_dotenv()

data_path = "../data/movie_desc-1k.txt"
index_path = "./vectorstore_douban_movie-1k.pkl"
hf_model_path = "DMetaSoul/Dmeta-embedding-zh"
api_mode_name = "DMetaSoul/Dmeta-embedding"
model_kwargs = {'device': 'cuda'}

## Load Data
loader = UnstructuredFileLoader(data_path)
text_splitter = RecursiveCharacterTextSplitter(        
    chunk_size=500,
    chunk_overlap=20,
    length_function=len,
)

documents = loader.load_and_split(text_splitter)

print("All documents have been loaded.")

if len(sys.argv) < 2:
    print("Usage: python dump_vec_faiss.py api/local")
    sys.exit(1)

mode = sys.argv[1]

## Load data to vectorstore
if mode == "local":
    emb_model = HuggingFaceEmbeddings(model_name=hf_model_path, model_kwargs=model_kwargs)
    vectorstore = FAISS.from_documents(documents, emb_model)
else:
    emb_model = DMetaTextEmbeddings(model_name=api_mode_name)
    vectorstore = FAISS.from_documents(documents, emb_model)

print("Vectorestore has been built.")

## Save vectorstore
with open(index_path, "wb") as f:
    pickle.dump(vectorstore, f)

print("Vectorestore has been dumped.")
