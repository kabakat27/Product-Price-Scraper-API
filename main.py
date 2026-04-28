from fastapi import FastAPI
from pydantic import BaseModel
from scraper import get_product_price

app = FastAPI()

class ProductRequest(BaseModel):
	product_name: str

@app.get("/retrieve/{product_name}")
def retrieve_product(product_name: str):
	result = get_product_price(product_name)
	if result:
		return result
	return {"message": "Product not found"}