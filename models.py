import pydantic
from pydantic import BaseModel

class ProductRequest(BaseModel):
	product_name: str

class ProductResponse(BaseModel):
	product: str
	price: str

class NotFoundResponse(BaseModel):
	message: str
