import chromadb
from chromadb.utils import embedding_functions

chroma_client = chromadb.Client()

sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="multi-qa-MiniLM-L6-cos-v1"
)

collection = chroma_client.create_collection(
    name="shoe_store",
    embedding_function=sentence_transformer_ef
)

collection.add(
    ids=[
        "nike-roche",
        "burton-snowboard-boots",
        "adidas-ultraboost",
        "converse-chuck-taylor",
        "new-balance-574",
        "timberland-6-inch",
        "vans-old-skool",
    ],
    documents=[
        "a simple sneaker suitable for walking and jogging. style is streetwear and casual",
        "snowboard boots for beginners and intermediate riders",
        "lightweight running shoe with responsive cushioning for daily training and marathons",
        "classic canvas low-top sneaker with rubber toe cap, timeless casual style",
        "retro heritage sneaker with suede and mesh upper, comfortable for all-day wear",
        "durable, waterproof, leather hiking and work boot with padded collar. Great for hiking and outdoor use",
        "skate shoe with waffle outsole and suede upper, popular in streetwear and skate culture",
    ],
    metadatas=[
        {"brand": "nike", "color": "white", "price": 100, "type": "sneaker", "name": "Nike Roche"},
        {"brand": "burton", "color": "black", "price": 200, "type": "snowboard boots", "name": "Burton Snowboard Boots"},
        {"brand": "adidas", "color": "grey", "price": 180, "type": "running shoe", "name": "Adidas Ultraboost"},
        {"brand": "converse", "color": "red", "price": 65, "type": "sneaker", "name": "Converse Chuck Taylor"},
        {"brand": "new balance", "color": "navy", "price": 90, "type": "sneaker", "name": "New Balance 574"},
        {"brand": "timberland", "color": "wheat", "price": 198, "type": "boot", "name": "Timberland 6 Inch"},
        {"brand": "vans", "color": "black", "price": 70, "type": "skate shoe", "name": "Vans Old Skool"},
    ],
)

def print_results(results):
    for i, ids in enumerate(results["ids"]):
        print(f"Top {len(ids)} matches:\n")
        for rank, shoe_id in enumerate(ids):
            meta = results["metadatas"][i][rank]
            doc = results["documents"][i][rank]
            distance = results["distances"][i][rank]
            print(f"  {rank + 1}. {meta['name']}  ({shoe_id})")
            print(f"     {meta['brand']} · {meta['color']} · ${meta['price']} · {meta['type']}")
            print(f"     {doc}")
            print(f"     distance: {distance:.3f}  (lower = better match)")
            print()


query = input("What kind of shoe are you looking for? ").strip()
if not query:
    print("No query entered. Exiting.")
else:
    results = collection.query(query_texts=[query], n_results=3)
    print(f'\nResults for: "{query}"\n')
    print_results(results)