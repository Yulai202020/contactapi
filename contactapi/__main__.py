import uvicorn
from main import app
from config import port

def run():
    uvicorn.run(app, host = "0.0.0.0", port = port)

if __name__ == "__main__" :
    run()