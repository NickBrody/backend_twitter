from fastapi import FastAPI, Header, HTTPException
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from database import engine, session

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


# async def startup() -> None:
#     async with engine.begin() as conn:
#         await conn.run_sync(models.Base.metadata.create_all)
#         await session.commit()


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):

    return templates.TemplateResponse("index.html", {"request": request})

@app_api.get("/users/me")
async def read_user_me(api_key: str = Header(None)):
    if api_key != 'test':
        raise HTTPException(status_code=400, detail="Invalid API Key")

    return {
        "result": "true",
        "user": {
            "id": 1,
            "name": "Джон",
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

@app_api.get("/tweets")
async def read_user_me(api_key: str = Header(None)):
    if api_key != 'test':
        raise HTTPException(status_code=400, detail="Invalid API Key")

    return {
        "result": "true",
        "tweets": [
            {
                "id": 123,
                "content": "Пример текста твита",
                "attachments": [
                    "link_1",
                    "link_2"
                ],
                "author": {
                    "id": 456,
                    "name": "Имя Автора"
                },
                "likes": [
                    {
                        "user_id": 789,
                        "name": "Имя пользователя"
                    }
                ]
            },
            {
                "id": 456,
                "content": "Еще один твит",
                "attachments": [
                    "link_3",
                    "link_4"
                ],
                "author": {
                    "id": 789,
                    "name": "Другой автор"
                },
                "likes": [
                    {
                        "user_id": 101112,
                        "name": "Понравилось пользователю"
                    }
                ]
            }
        ]
    }



