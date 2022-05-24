import asyncio

import uvloop
from prisma import Prisma

# change event loop to uvloop policy
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


async def main() -> None:
    db = Prisma()
    await db.connect()

    # add user
    user = await db.user.create(data={"name": "carlos rian", "age": 28})

    print(f"\nUser: {user.json(indent=2, sort_keys=True)}\n")

    # add post
    post = await db.post.create(
        data={
            "name": "super",
            "desc": "test",
            "published": True,
            "title": "try",
            "user_id": user.id,
        }
    )
    print(f"\nPost: {post.json(indent=2, sort_keys=True)}\n")

    # get an user with post
    found_user = await db.user.find_unique(
        where={"id": user.id}, include={"posts": True}
    )

    assert found_user is not None
    print(f"found user with post: {found_user.json(indent=2, sort_keys=True)}")

    found_post = await db.post.find_unique(
        where={
            "id": post.id,
        },
        include={"user": True},
    )
    # get a post with user
    print(f"found post with user: {found_post.json(indent=2, sort_keys=True)}")

    await db.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
