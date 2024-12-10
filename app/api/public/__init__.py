"""
## app.api.public

包含所有的公用 API

用法如下
    在 `/app/api/public` 資料夾中建立 python 檔案或新增資料夾後建立 `__init__.py` 檔案
    ``` python
    from fastapi import APIRouter

    router = APIRouter(prefix="/xxx", tags=["xxx"])
    ```
    就可以透過 `router` 建立自己的 API
"""

# 基本上不需要修改這邊

from pathlib import Path

from fastapi import APIRouter

router = APIRouter(prefix="/public", tags=["public"])

for path in Path(__file__).parent.iterdir():
    module_name = ""
    if path.is_file() and path.name.endswith(".py") and path.name != "__init__.py":
        module_name = path.name.removesuffix(".py")
    elif path.is_dir() and any([_path.is_file() and _path.name == "__init__.py" for _path in path.iterdir()]):
        module_name = path.name
    if module_name != "":
        exec(f"""
from app.api.public import {module_name}
router.include_router({module_name}.router)
""")
