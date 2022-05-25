from uuid import UUID

from prisma import Prisma
from prisma.partials import PeoplePostAndPut


async def create(db: Prisma, people: PeoplePostAndPut):
    return await db.people.create(data={"name": people.name, "age": people.age})


async def find(db: Prisma, id: UUID, with_item: bool):
    return await db.people.find_unique(
        where={"id": str(id)}, include={"items": with_item}
    )


async def update(db: Prisma, id: UUID, people: PeoplePostAndPut):
    return await db.people.update(
        data={"name": people.name, "age": people.age}, where={"id": str(id)}
    )


async def delete(db: Prisma, id: UUID):
    return await db.people.delete(where={"id": str(id)})
