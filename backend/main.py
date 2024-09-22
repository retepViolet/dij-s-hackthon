from fastapi import FastAPI, File, UploadFile, Query, Form, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from contextlib import asynccontextmanager
from datetime import datetime, timezone
from urllib.parse import quote
from prisma import Prisma
from typing import List
import os


db = Prisma()
path =  os.path.join(os.path.expanduser('~'), 'Desktop') + '\\Altomic\\'

@asynccontextmanager
async def lifespan(_app: FastAPI):
    await db.connect()
    yield
    await db.disconnect()

app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory=path), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源，生产环境中请更加谨慎地配置
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有 HTTP 方法
    allow_headers=["*"],  # 允许所有 HTTP 头
)


@app.get("/")
async def index_page():
    return FileResponse(path+'index/index.html', media_type="text/html")


@app.get("/prompt")
async def index_page():
    return FileResponse(path+'prompt/prompt.html', media_type="text/html")


@app.get("/task")
async def index_page():
    return FileResponse(path+'task/task.html', media_type="text/html")