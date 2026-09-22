from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"Message": "HelloWorld","number": 404,"status": "Not Found","is_fun" : True}