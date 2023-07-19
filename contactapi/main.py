import uvicorn
from router import router
from fastapi import FastAPI
from config import port

app = FastAPI()
app.include_router(router = router)

if __name__ == "__main__" :
    uvicorn.run(app, host = "0.0.0.0", port = port)