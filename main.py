import fastapi
from dotenv import load_dotenv
load_dotenv()
import os
app = fastapi.FastAPI()
e=os.getenv("TEST_CODE")
e1=os.getenv("TEST_CODE1")
@app.get("/")
def proj_app():
    return {"message":"fastapi test on /"}
@app.get("/emp")
def proj_app():
    return {"message":f"fastapi test on /emp - {e}"}
@app.get("/wmp")
def proj_app2():
    print("MINOR CHANGE")
    return {"message":f"fastapi test on /wmp - {e1}"}