import fastapi
from dotenv import load_dotenv
load_dotenv()
import os
app = fastapi.FastAPI()
e=os.genenv("TEST_CODE")
e1=os.genenv("TEST_CODE1")
@app.get("/")
def proj_app():
    return {"message":"fastapi test on /"}
@app.get("/emp")
def proj_app():
    return {f"message":"fastapi test on /emp - {e}"}
@app.get("/wmp")
def proj_app2():
    return {f"message":"fastapi test on /wmp - {e1}"}