import os
from fastapi import FastAPI, HTTPException
from supabase import create_client, Client
from pydantic import BaseModel

app = FastAPI()

# Supabase setup
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

class Item(BaseModel):
    name: str

@app.get("/")
def read_root():
    return {"status": "FastAPI is running on Cloud Run"}

@app.post("/items")
def create_item(item: Item):
    response = supabase.table("items").insert({"name": item.name}).execute()
    return response.data

@app.get("/items")
def get_items():
    response = supabase.table("items").select("*").execute()
    return response.data
