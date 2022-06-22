from sqlalchemy.future import select

from sqla_async.conf.db_session import create_session

from sqla_async.models.sabor import Sabor
from sqla_async.models.picole import Picole


async def atualiza_sabor(id_sabor: int, novo_sabor: str) -> None:
    async with create_session() as session:
        query = select(Sabor).filter(Sabor.id == id_sabor)
        sabor: Sabor = session.execute(query)
        sabor = sabor.scalar_one_or_none()

        if sabor:
            sabor.nome = novo_sabor
            await session.commit()
        else:
            print(f'Não existe sabor com ID {id_sabor}')


async def atualiza_picole(id_picole: int, novo_preco: float, novo_sabor: int = None):
    async with create_session() as session:
        query = select(Picole).filter(Picole.id == id_picole)
        picole: Picole = session.execute(query)
        picole = picole.unique().scalar_one_or_none()

        if picole:
            picole.preco = novo_preco
            if novo_sabor:
                picole.id_sabor = novo_sabor
            await session.commit()
        else:
            print(f'Não existe sabor com ID {id_picole}')


if __name__ == '__main__':
    pass
