from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import os
from os import path
import uvicorn
from markdown import markdown

dir = path.dirname(path.abspath(__file__))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hi sweetheart",
            "status": "success",
            "note": "This my declaration of my affection for you."}

@app.get("/details")
def home_page():
    content = ""
    with open(path.join("README.md"), 'r') as f: # join takes path from cwd and appends the file name
        content = f.read()
    details_md = markdown(content)
    return HTMLResponse(details_md)

if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        reload_dirs=[dir],
        reload_excludes=[
            "*/.git/*",
            "*/__pycache__/*",
            "*.pyc",
            "*/.pytest_cache/*",
            "*/.vscode/*",
            "*/.idea/*"
        ],
        reload_delay=1,
        reload_includes=["*.py", "*.html", "*.css", "*.js"]
    )
