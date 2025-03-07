from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/api/get_version")
def get_version():
    return {"notice":"อัปเดตแปลไทย","resource_version":20250307,"version":"0.2.4.2"}
