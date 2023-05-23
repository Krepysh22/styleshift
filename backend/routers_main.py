from typing import List, Optional

from fastapi import APIRouter, Depends
from telethon import TelegramClient
from appeal_dal import AppealDAL, get_appeal_dal
from pydantic_models import Appeal
from tg_settings import settings
# from db import Appeal

router = APIRouter()

bot = TelegramClient('bot', settings.app_id, settings.api_hash)


@router.post("/api/create_appeal")
async def create_appeal(appeal: Appeal, appeal_dal: AppealDAL = Depends(get_appeal_dal)):
    # await bot.send_message(460788585, text='als[fp[')

    await bot.start(bot_token=settings.bot_token)
    async with bot as c:
        for usr in settings.list_of_send_to:
            await c.send_message(usr, f'new appeal, {appeal.name}, {appeal.phone}')
    return await appeal_dal.create_appeal(appeal.name, appeal.phone)


@router.put("/api/appeal/{appeal_id}")
async def update_appeal(appeal_id: int, name: Optional[str] = None, phone: Optional[str] = None, completed: Optional[bool] = None, appeal_dal: AppealDAL = Depends(get_appeal_dal)):
    return await appeal_dal.update_appeal(appeal_id, name, phone, completed)


@router.get("/api/appeals")
async def get_all_appeals(appeal_dal: AppealDAL = Depends(get_appeal_dal)) -> List[Appeal]:
    appeals = await appeal_dal.get_all_appeals()
    return appeals
