from prisma import Prisma


async def get_db():
    db = Prisma(log_queries=True)
    try:
        await db.connect()
        yield db
    finally:
        await db.disconnect()
