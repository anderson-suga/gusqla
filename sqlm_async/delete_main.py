from typing import Optional

from sqlm_async.conf.db_session import create_session

from sqlm_async.models.picole import Picole
from sqlm_async.models.revendedor import Revendedor


async def deletar_picole(id_picole: int) -> None:
    async with create_session() as session:
        picole: Optional[Picole] = session.get(Picole, id_picole)

        if picole:
            await session.delete(picole)
            await session.commit()
        else:
            print(f'Não encontrei picole com ID {id_picole}')


async def deletar_revendedor(id_revendedor: int) -> None:
    async with create_session() as session:
        revendedor: Optional[Revendedor] = session.get(Revendedor, id_revendedor)

        if revendedor:
            await session.delete(revendedor)
            await session.commit()
        else:
            print(f'Não encontrei revendedor com ID {id_revendedor}')


if __name__ == '__main__':
    pass
