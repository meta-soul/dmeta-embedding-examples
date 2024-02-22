# Reference: https://github.com/langchain-ai/langchain/blob/master/libs/community/langchain_community/embeddings/baichuan.py

from typing import Any, Dict, List, Optional

import requests
from langchain_core.embeddings import Embeddings
from langchain_core.pydantic_v1 import BaseModel, SecretStr, root_validator
from langchain_core.utils import convert_to_secret_str, get_from_dict_or_env

DMETA_API_URL: str = "https://api.dmetasoul.com/v1/embeddings"

class DMetaTextEmbeddings(BaseModel, Embeddings):
    """DMeta Text Embedding models."""

    session: Any
    model_name: str = "DMetaSoul/Dmeta-embedding"
    dmeta_api_key: Optional[SecretStr] = None
    batch_size: int = 5

    @root_validator(allow_reuse=True)
    def validate_environment(cls, values: Dict) -> Dict:
        """Validate that auth token exists in environment."""
        dmeta_api_key = convert_to_secret_str(
            get_from_dict_or_env(values, "dmeta_api_key", "DMETA_API_KEY")
        )
        if not dmeta_api_key:
            raise ValueError("DMeta API key must be provided")
        session = requests.Session()
        session.headers.update(
            {
                "Authorization": f"Bearer {dmeta_api_key.get_secret_value()}",
                "Accept-Encoding": "identity",
                "Content-type": "application/json",
            }
        )
        values["session"] = session
        return values

    def _embed(self, texts: List[str]) -> Optional[List[List[float]]]:
        """Internal method to call DMeta Embedding API and return embeddings.

        Args:
            texts: A list of texts to embed.

        Returns:
            A list of list of floats representing the embeddings, or None if an
            error occurs.
        """
        try:
            response = self.session.post(
                DMETA_API_URL, json={"input": texts, "model": self.model_name}
            )

            if response.status_code == 200:
                resp = response.json()
                embeddings = resp.get("data", [])
                sorted_embeddings = sorted(embeddings, key=lambda e: e.get("index", 0))
                return [result.get("embedding", []) for result in sorted_embeddings]
            else:
                print(f"Error: Received status code {response.status_code} from embedding API")
                return None
        except Exception as e:
            print(f"Exception occurred while trying to get embeddings: {str(e)}")
            return None
        
    def _embed_batched(self, texts: List[str]) -> Optional[List[List[float]]]:
        """Embed texts in batches."""
        all_embeddings = []
        
        # Split texts into batches
        for i in range(0, len(texts), self.batch_size):
            batch_texts = texts[i:i + self.batch_size]
            # Call the original _embed method for each batch
            batch_embeddings = self._embed(batch_texts)
            
            if batch_embeddings is None:
                print(f"Error occurred in batch {i // self.batch_size}")
                return None
            
            all_embeddings.extend(batch_embeddings)
            
        return all_embeddings

    def embed_documents(self, texts: List[str]) -> Optional[List[List[float]]]:
        """Public method to get embeddings for a list of documents.

        Args:
            texts: The list of texts to embed.

        Returns:
            A list of embeddings, one for each text, or None if an error occurs.
        """
        return self._embed_batched(texts)

    def embed_query(self, text: str) -> Optional[List[float]]:
        """Public method to get embedding for a single query text.

        Args:
            text: The text to embed.

        Returns:
            Embeddings for the text, or None if an error occurs.
        """
        result = self._embed([text])
        return result[0] if result is not None else None
