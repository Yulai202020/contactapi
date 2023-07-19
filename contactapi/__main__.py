import uvicorn
from main import app
import os

def run():
    uvicorn.run(app, host = "0.0.0.0", port = os.environ.get("PORT"))

if __name__ == "__main__" :
    run(host = "0.0.0.0", port = 8000)