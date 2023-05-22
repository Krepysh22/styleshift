from typing import List, Optional

from sqlalchemy import update
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from db import async_session, Appeal


class AppealDAL:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def create_appeal(self, name: str, phone: str):
        new_book = Appeal(name=name, phone=phone)
        self.db_session.add(new_book)
        print(new_book)
        await self.db_session.flush()

    async def get_all_appeals(self) -> List[Appeal]:
        q = await self.db_session.execute(select(Appeal).order_by(Appeal.id))
        return q.scalars().all()

    async def update_appeal(self, appeal_id: int, name: Optional[str], phone: Optional[str], completed: Optional[bool]):
        q = update(Appeal).where(Appeal.id == appeal_id)
        if name:
            q = q.values(name=name)
        if phone:
            q = q.values(phone=phone)
        if completed:
            q = q.values(completed=completed)
        q.execution_options(synchronize_session="fetch")
        await self.db_session.execute(q)


async def get_appeal_dal():
    async with async_session() as session:
        async with session.begin():
            yield AppealDAL(session)