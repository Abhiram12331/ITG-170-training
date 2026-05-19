from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def base_url():
    return {'status':200,
            'message':"Hello World"}


@app.get('/hello/{name}')
def hello_world(name:str):
    return f'Hello {name}'