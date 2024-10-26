from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncConnection

from app.repositories.interface import StoreInterface
from app.schemas.store import GetStore, GetStores


class StoreServices:
    def __init__(self, store_repo: StoreInterface):
        self.__store_repo = store_repo

    async def get_stores(self, conn: AsyncConnection) -> list[GetStores]:
        stores = await self.__store_repo.get_stores(conn=conn)
        results: list[GetStores] = [GetStores.model_validate(store) for store in stores]
        return results

    async def get_store(self, conn: AsyncConnection, store_uuid: UUID) -> GetStore | None:
        store = await self.__store_repo.get_store_by_uuid(conn=conn, store_uuid=store_uuid)
        if not store:
            return None

        capsters = store.get("capsters")
        if isinstance(capsters, str) and capsters == "[]":
            capsters = []

        result: GetStore = GetStore(
            uuid=store.get("uuid"),
            store_name=store.get("store_name"),
            address=store.get("address"),
            phone_number=store.get("phone_number"),
            opening_hours=store.get("opening_hours"),
            closing_hours=store.get("closing_hours"),
            capsters=capsters,
        )
        return result
