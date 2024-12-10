"""
## app

使用
```bash
uvicorn app:app
```
或
```bash
fastapi run app
```
運行伺服器。

常用參數
- --port [int]： 為 app 指定使用的 port。
- --reload： 當資料夾中的檔案更新時，伺服器自動重載，通常用於開發階段。
"""

# 基本上不需要修改這邊

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app import api

app = FastAPI()
app.mount("/", StaticFiles(directory="static"), name="static")
app.include_router(api.router)
