from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
@app.get("/")
def read_root():
    return {"page": "Home"}
@app.get("/about")
def about():
    return {"page": "About","author": "John Doe"}
@app.get("/health")
def health():
    return {"status": "healthy"}



#POST request
@app.post("/create")
def create_something(item : dict):

    return {"message" : "Item created succesfully", "item" : item  }

#Path Parameters
@app.get("/student/{usn}")
def get_result(usn ):
    return{"usn": usn, "Result": "passed"}

#Path Parameters with type Hint
@app.get("/candidate/{roll}")
def get_candidate(roll : int):
    return{"roll": roll, "type":str(type(roll)), "Result": "passed"}



#Pydantic model
class Item(BaseModel):
    name : str
    price : float
    in_stock : bool = True

@app.post("/items/")

def create_item(item: Item):
        return {"received_item": item, "total_price": item.price * 1.18, "message": "Item created successfully"
        ""}
