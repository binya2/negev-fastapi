from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; background-color: #f0f0f0; }
                h1 { color: #007acc; font-size: 3em; }
                .card { background: white; padding: 20px; border-radius: 10px; display: inline-block; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>שלום כיתת נגב! 🌵</h1>
                <p>האתר הזה רץ על OpenShift בפרויקט ה-DevOps שלנו.</p>
            </div>
        </body>
    </html>
    """