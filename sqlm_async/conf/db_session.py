from pathlib import Path
from typing import Optional

from sqlalchemy.future.engine import Engine

from sqlmodel import Session
from sqlmodel import create_engine as _create_engine
from sqlmodel import SQLModel

__engine: Optional[Engine] = None


def create_engine(sqlite: bool = False) -> Engine:
    global __engine

    if __engine:
        return

    if sqlite:
        arquivo_db = 'db/picoles.sqlite'
        folder = Path(arquivo_db).parent
        folder.mkdir(parents=True, exist_ok=True)

        conn_str = f'sqlite:///{arquivo_db}'
        __engine = _create_engine(url=conn_str, echo=False, connect_args={'check_same_thread': False})
    else:
        conn_str = 'postgresql://anderson:Teste123@localhost:5432/picoles'
        __engine = _create_engine(url=conn_str, echo=False)

    return __engine


def create_session() -> Session:
    global __engine

    if not __engine:
        # create_engine(sqlite=True)
        create_engine()

    session: Session = Session(__engine)

    return session


def create_tables() -> None:
    global __engine

    if not __engine:
        # create_engine(sqlite=True)
        create_engine()

    import sqlm_sync.models
    SQLModel.metadata.drop_all(__engine)
    SQLModel.metadata.create_all(__engine)


if __name__ == '__main__':
    pass
