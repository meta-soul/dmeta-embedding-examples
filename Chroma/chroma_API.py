import chromadb
from chromadb import Documents, EmbeddingFunction, Embeddings
from sentence_transformers import SentenceTransformer
from langchain.embeddings import HuggingFaceEmbeddings
import torch
import chromadb.utils.embedding_functions as embedding_functions


# 获取client
client = chromadb.PersistentClient(path="your_path")


# 通过Dmeta-Embedding API推理
dmeta_api_ef = embedding_functions.OpenAIEmbeddingFunction(
                api_key="your_key",
                api_base="https://api.dmetasoul.com/v1",
                model_name="DMetaSoul/Dmeta-embedding"
            )

DE = dmeta_api_ef

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