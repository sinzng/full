from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def healthCheck():
    return "OK"

@app.get('/hello')
async def Hello():
    return "Hello World~!!"

@app.post('/random')
@app.get('/random') # get과 post를 같은 api로, 파라미터가 없어서 가능
async def random(max=None):
    import random

    if max is None:
        max =10
    else :
        max = int(max) 
    random_v = random.randint(1,max)

    return random_v