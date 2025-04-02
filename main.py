from fastapi import FastAPI

app = FastAPI()

@app.get("/api/get_version")
def get_version():
    return {
        "notice": "updated",
        "resource_version": "2025080301",
        "version": "0.2.4.6"
    }
