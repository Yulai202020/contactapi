import uvicorn
from router import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router = router)

# run by uvicorn
def run(host: str, port: int):
    uvicorn.run(app, host = host, port = port)

if __name__ == "__main__" :
    run(host = "0.0.0.0", port = 8000)