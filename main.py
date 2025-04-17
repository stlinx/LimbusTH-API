from fastapi import FastAPI

app = FastAPI()

@app.get("/api/get_version")
def get_version():
    return {
        "version": "0.2.4.7",  # เวอร์ชันล่าสุด
        "download_url": "https://github.com/stlinx/LocalizeLimbusTH/releases/download/0.2.4.6/LimbusTH.zip"  # URL สำหรับดาวน์โหลด
    }
