from pydantic import BaseModel

class HotelSchema(BaseModel):
	name: str
	location: str
	price: int
	rating: int