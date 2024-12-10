"""
## app.api

包含公用與私有 API
"""

# 基本上不需要修改這邊

from fastapi import APIRouter

from app.api import public
from app.api import private

router = APIRouter(prefix="/api", tags=["api"])
router.include_router(public.router)
router.include_router(private.router)
