import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import PINECONE_API_KEY, PINECONE_INDEX_NAME
from pinecone import Pinecone

pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(PINECONE_INDEX_NAME)

# Here, we have changed `top_k=3` to `top_k=10`.
def query_pinecone(vector, top_k=10):
    results = index.query(vector=vector, top_k=top_k, include_metadata=True)
    contexts = [match['metadata']['text'] for match in results['matches']]
    return "\n".join(contexts)