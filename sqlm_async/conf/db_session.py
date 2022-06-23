from pathlib import Path
from typing import Optional

from sqlmodel import create_engine as _create_engine
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession, AsyncEngine

__async_engine: Optional[AsyncEngine] = None


def create_engine(sqlite: bool = False) -> AsyncEngine:
    global __async_engine

    if __async_engine:
        return

    if sqlite:
        arquivo_db = 'db/picoles.sqlite'
        folder = Path(arquivo_db).parent
        folder.mkdir(parents=True, exist_ok=True)

        conn_str = f'sqlite+aiosqlite:///{arquivo_db}'
        __async_engine = AsyncEngine(
            _create_engine(url=conn_str, echo=False, connect_args={'check_same_thread': False}))
    else:
        conn_str = 'postgresql+asyncpg://anderson:Teste123@localhost:5432/picoles'
        __async_engine = AsyncEngine(_create_engine(url=conn_str, echo=False))

    return __async_engine


def create_session() -> AsyncSession:
    global __async_engine

    if not __async_engine:
        # create_engine(sqlite=True)
        create_engine()

    session: AsyncSession = AsyncSession(__async_engine)

    return session


def create_tables() -> None:
    global __async_engine

    if not __async_engine:
        # create_engine(sqlite=True)
        create_engine()

    import sqlm_async.models
    async with __async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)


if __name__ == '__main__':
    pass
