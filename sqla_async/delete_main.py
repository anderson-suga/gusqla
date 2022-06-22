from typing import Optional

from sqlalchemy.future import select
from sqla_async.conf.db_session import create_session

from sqla_async.models.picole import Picole
from sqla_async.models.revendedor import Revendedor


async def deletar_picole(id_picole: int) -> None:
    async with create_session() as session:
        query = select(Picole).filter(Picole.id == id_picole)
        picole: Optional[Picole] = await session.execute(query)
        picole = picole.unique().scalar_one_or_none()

        if picole:
            session.delete(picole)
            session.commit()
        else:
            print(f'Não encontrei picole com ID {id_picole}')


async def deletar_revendedor(id_revendedor: int) -> None:
    async with create_session() as session:
        query = select(Revendedor).filter(Revendedor.id == id_revendedor)
        revendedor: Optional[Revendedor] = await session.execute(query)
        revendedor = revendedor.scalar_one_or_none()

        if revendedor:
            session.delete(revendedor)
            session.commit()
        else:
            print(f'Não encontrei revendedor com ID {id_revendedor}')


if __name__ == '__main__':
    pass
