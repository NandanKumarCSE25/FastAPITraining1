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

#Path Parameters
@app.get("/student/{usn}")
def get_result(usn ):
    return{"usn": usn, "Result": "passed"}

#Path Parameters with type Hint
@app.get("/candidate/{roll}")
def get_candidate(roll : int):
    return{"roll": roll, "type":str(type(roll)), "Result": "passed"}
