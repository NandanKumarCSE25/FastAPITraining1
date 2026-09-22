from fastapi import FastAPI
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
