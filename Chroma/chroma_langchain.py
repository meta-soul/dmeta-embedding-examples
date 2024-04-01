import chromadb
from chromadb import Documents, EmbeddingFunction, Embeddings
from sentence_transformers import SentenceTransformer
from langchain.embeddings import HuggingFaceEmbeddings
import torch
import chromadb.utils.embedding_functions as embedding_functions


# 获取client
client = chromadb.PersistentClient(path="your_path")


# 通过 LLM 工具框架 langchain加载推理
class Dmeta_embedding(EmbeddingFunction):
    
    def __call__(self, input: Documents) -> Embeddings:
        model_name = "DMetaSoul/Dmeta-embedding-zh"
        model_kwargs = {'device': 'cuda' if torch.cuda.is_available() else 'cpu'}
        encode_kwargs = {'normalize_embeddings': True}

        model = HuggingFaceEmbeddings(
            model_name=model_name,
            model_kwargs=model_kwargs,
            encode_kwargs=encode_kwargs,
        )    
        embeddings = model.embed_documents(input)
        return embeddings

DE = Dmeta_embedding()


# 创建collection
collection = client.get_or_create_collection("my_collection", embedding_function=DE)

collection.add(
    documents=["胡子长得快怎么办？", "怎样使胡子不浓密！", "香港买手表哪里好", "在杭州手机到哪里买"],
    metadatas=[{"source": "my_source"}, {"source": "my_source"}, {"source": "my_source"},  {"source": "my_source"}],
    ids=["id1", "id2", "id3", "id4"]
)

collection.get()

#{'ids': ['id1', 'id2', 'id3', 'id4'],
# 'embeddings': None,
# 'metadatas': [{'source': 'my_source'},
#  {'source': 'my_source'},
#  {'source': 'my_source'},
#  {'source': 'my_source'}],
# 'documents': ['胡子长得快怎么办？', '怎样使胡子不浓密！', '香港买手表哪里好', '在杭州手机到哪里买'],
# 'uris': None,
# 'data': None}

query_result = collection.query(
        query_texts =["胡子长得太快怎么办？"],
        n_results=2,
    )
print(query_result)

# {'ids': [['id1', 'id2']], 'distances': [[0.09293291344747456, 0.6447157910392011]], 
# 'metadatas': [[{'source': 'my_source'}, {'source': 'my_source'}]], 
# 'embeddings': None, 'documents': [['胡子长得快怎么办？', '怎样使胡子不浓密！']], 
# 'uris': None, 'data': None}