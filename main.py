from fastapi import FastAPI
from pydantic import BaseModel
from scraper import get_product_price

app = FastAPI()

class ProductRequest(BaseModel):
	product_name: str

@app.post("/retrieve")
def retrieve_product(data: ProductRequest):
	result = get_product_price(data.product_name)
	if result:
		return result
	return {"message": "Product not found"}
