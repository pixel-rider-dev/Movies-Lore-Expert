import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from sentence_transformers import SentenceTransformer
from ingestion import load_and_chunk_data 

# Load the `.env` file.
load_dotenv('.env') 
PINECONE_KEY = os.getenv("PINECONE_API_KEY")

def main():
    # 1. Pinecone Setup
    print("Pinecone se connect ho raha hai...")
    pc = Pinecone(api_key=PINECONE_KEY)
    
    index_name = "movies-lore-expert" 
    
    if index_name not in pc.list_indexes().names():
        print(f"Naya index '{index_name}' ban raha hai...")
        pc.create_index(
            name=index_name,
            dimension=384, 
            metric='cosine',
            spec=ServerlessSpec(cloud='aws', region='us-east-1')
        )
    
    index = pc.Index(index_name)
    
    # 2. Load the embedding model.
    print("AI Embedding model load ho raha hai...")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # 3.Fetch data from the CSV (the filename has been corrected here).
    # If your file has a different name, correct it here.
    df = load_and_chunk_data('../data/tmdb_5000_movies.xlsx.csv')
    
    # 4.Generate and upload embeddings.
    print("Embeddings ban rahi hain (Is process mein thora time lag sakta hai)...")
    vectors = []
    
    for i, row in df.iterrows():
        # Convert the text chunk into a vector.
        emb = model.encode(row['chunk']).tolist()
        
        vectors.append({
            "id": str(row['id']),
            "values": emb,
            "metadata": {
                "title": row['original_title'], 
                "text": row['chunk']
            }
        })
        
        # Upload in batches of 100.
        if len(vectors) >= 100:
            index.upsert(vectors=vectors)
            vectors = []
            print(f"{i+1} movies upload ho gayin...")
    
    # Upload the remaining vectors.
    if vectors:
        index.upsert(vectors=vectors)
        
    print("Zabardast! Saari embeddings Pinecone par successfully upload ho chuki hain.")

if __name__ == "__main__":
    main()