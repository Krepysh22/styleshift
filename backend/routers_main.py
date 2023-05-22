from typing import List, Optional

from fastapi import APIRouter, Depends

from appeal_dal import AppealDAL, get_appeal_dal
from pydantic_models import Appeal
# from db import Appeal

router = APIRouter()


@router.post("/api/create_appeal")
async def create_appeal(appeal: Appeal, appeal_dal: AppealDAL = Depends(get_appeal_dal)):
    return await appeal_dal.create_appeal(appeal.name, appeal.phone)


@router.put("/api/appeal/{appeal_id}")
async def update_appeal(appeal_id: int, name: Optional[str] = None, phone: Optional[str] = None, completed: Optional[bool] = None, appeal_dal: AppealDAL = Depends(get_appeal_dal)):
    return await appeal_dal.update_appeal(appeal_id, name, phone, completed)


@router.get("/api/appeals")
async def get_all_appeals(appeal_dal: AppealDAL = Depends(get_appeal_dal)) -> List[Appeal]:
    return await appeal_dal.get_all_appeals()
