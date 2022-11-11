from pydantic import BaseModel
from datetime import  datetime

#data type validation using pydantic
class Item(BaseModel):
    coin_name:str
    coin_add:str
    time_created:datetime