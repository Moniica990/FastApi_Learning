from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def hello():
    return {'message':'Hello world'}


@app.get('/about')
def about():
    return {'message':'I am moniica who studies BE ECE' }