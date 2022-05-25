from uuid import UUID

from app.controller import people
from app.db import get_db
from fastapi import APIRouter, Depends, FastAPI
from prisma import Prisma
from prisma.models import People
from prisma.partials import PeoplePostAndPut


def init_app(app: FastAPI):
    router = APIRouter(prefix="/v1")

    @router.post("/people", response_model=People)
    async def post_people(data: PeoplePostAndPut, db: Prisma = Depends(get_db)):
        return await people.create(db=db, people=data)

    @router.get("/people/{id}", response_model=People)
    async def get_people(
        id: UUID, with_item: bool = False, db: Prisma = Depends(get_db)
    ):
        return await people.find(db=db, with_item=with_item, id=id)

    @router.put("/people/{id}")
    async def put_people(id: UUID, data: PeoplePostAndPut, db: Prisma = Depends(get_db)):
        return await people.update(db=db, id=id, people=data)

    @router.delete("/people/{id}")
    async def delete_people(id: UUID, db: Prisma = Depends(get_db)):
        return await people.delete(db=db, id=id)

    app.include_router(router=router)
