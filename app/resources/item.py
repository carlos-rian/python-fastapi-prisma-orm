from fastapi import APIRouter, FastAPI


def init_app(app: FastAPI):
    router = APIRouter(prefix="/v1")

    @router.post("/item")
    async def post_item():
        ...

    @router.get("/item")
    async def get_item():
        ...

    @router.put("/item")
    async def put_item():
        ...

    @router.delete("/item")
    async def delete_item():
        ...

    app.include_router(router=router)
