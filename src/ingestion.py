import pandas as pd

def load_and_chunk_data(file_path):
    print("Data load ho raha hai...")
    df = pd.read_csv(file_path)
    
    # ==== SIRF YE LINE CHANGE HUI HAI ====
    df = df.iloc[500:] 
    print(f"Pehli 500 movies skip kar di hain. Ab baqi ki movies upload hongi.")
    # =====================================
    
    # Sirf zaroori columns select karna
    df = df[['id', 'original_title', 'overview', 'genres', 'keywords']]
    
    # Text columns ke missing data ko theek karna
    df.fillna({
        'overview': '', 
        'genres': '', 
        'keywords': ''
    }, inplace=True)
    
    # Chunking Strategy
    def create_chunk(row):
        return f"Title: {row['original_title']}. Overview: {row['overview']} Genres: {row['genres']} Keywords: {row['keywords']}"
    
    # Create a new column named chunk.
    df['chunk'] = df.apply(create_chunk, axis=1)
    
    print(f"Data ready ho gaya hai. Ab upload shuru hoga.")
    return df