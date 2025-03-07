from fastapi import FastAPI

app = FastAPI()

@app.get("/api/get_version")
def get_version():
    return {
        "notice": "อัปเดตแปลไทย",
        "resource_version": "03072025",
        "version": "0.2.4.2"
    }
