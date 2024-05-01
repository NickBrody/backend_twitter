from fastapi import FastAPI, Header, HTTPException
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI(title="main")
app_api = FastAPI(title="api")

app.mount("/api/", app_api, name="api")
app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

origins = ["http://127.0.0.1:8000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["origins"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app_api.get("/users/me")
async def read_user_me(api_key: str = "test"):
    if api_key != 'test':
        raise HTTPException(status_code=400, detail="Invalid API Key")

    return {
        "result": "true",
        "user": {
            "id": 1,
            "name": "str",
            "followers": [
                {
                    "id": 2,
                    "name": "str"
                }
            ],
            "following": [
                {
                    "id": 3,
                    "name": "str"
                }
            ]
        }
    }

