from fastapi import FastAPI
import asyncio
from enum import Enum 


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

#example of async vs non async
#async
@app.get("/async_ex")
async def read_result():
    results = await asyncio.sleep(1)
    return results
#non async
@app.get("/non_async_ex")
def results():
    results = asyncio.sleep(1)
    return results

# async param with type 
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
