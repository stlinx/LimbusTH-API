from fastapi import FastAPI

app = FastAPI()

@app.get("/api/get_version")
def get_version():
    return {
        "version": "1.0.3",
        "download_url": "https://github.com/stlinx/LocalizeLimbusTH/releases/download/1.0.3/LimbusTH.zip"
    }
