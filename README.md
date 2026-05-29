# Shoe Store — ChromaDB Semantic Search Demo

A minimal demo of vector/semantic search using [ChromaDB](https://www.trychroma.com/). Type a natural-language query and get the best-matching shoes from a small catalog, ranked by semantic similarity.

> Companion article: [ChromaDB Tutorial](https://medium.com/@rajashravan/chromadb-tutorial-cf2cf3e9c676)

## What it does

- Loads 7 shoes (Nike, Adidas, Converse, Vans, etc.) into an in-memory ChromaDB collection
- Each shoe has a text description + metadata (brand, color, price, type)
- Queries the collection with your input and returns the top 3 matches with similarity distances

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python shoe-store.py
```

Example:

```
What kind of shoe are you looking for? waterproof boot for hiking

Results for: "waterproof boot for hiking"

Top 3 matches:

  1. Timberland 6 Inch  (timberland-6-inch)
     timberland · wheat · $198 · boot
     durable, waterproof, leather hiking and work boot with padded collar...
     distance: 0.312  (lower = better match)
  ...
```

## Stack

- [ChromaDB](https://www.trychroma.com/) — embedded vector database
- [sentence-transformers](https://www.sbert.net/) — local embedding model (no API key needed)
