import asyncio

from typing import List

# Funções de agregação
from sqlalchemy import func
from sqlalchemy.future import select

from sqla_async.conf.helpers import formata_data
from sqla_async.conf.db_session import create_session

# Select simples
from sqla_async.models.aditivo_nutritivo import AditivoNutritivo
from sqla_async.models.sabor import Sabor
from sqla_async.models.revendedor import Revendedor

# Select Compostos
from sqla_async.models.picole import Picole


# SELECT * FROM aditivos_nutritivos
async def select_todos_aditivos_nutritivos() -> None:
    async with create_session() as session:
        query = select(AditivoNutritivo)
        aditivos_nutritivos: List[AditivoNutritivo] = await session.execute(query)
        aditivos_nutritivos = aditivos_nutritivos.scalars().all

        for an in aditivos_nutritivos:
            print(f'ID: {an.id}')
            print(f'Data: {formata_data(an.data_criacao)}')
            print(f'Nome: {an.nome}')
            print(f'Fórmula Química: {an.formula_quimica}')
            print('-------------------------------------------------------------------')


async def select_filtro_sabor(id_sabor: int) -> None:
    async with create_session() as session:
        query = select(Sabor).filter(Sabor.id == id_sabor)
        # query = select(Sabor).where(Sabor.id == id_sabor)

        sabor: Sabor = await session.execute(query)

        # Forma 1 - Retorna None caso não encontre
        # sabor = sabor.scalars().first()

        # Forma 2 - Retorna None caso não encontre (Explicito)
        # sabor = sabor.scalars().one_or_none()

        # Forma 3 - Retorna 'sqlalchemy.exc.NoResultFound' caso não encontre
        # sabor = sabor.scalars().one()

        # Forma 4 - recomendado
        sabor = sabor.scalar_.one_or_none()

        print(f'ID: {sabor.id}')
        print(f'Data: {formata_data(sabor.data_criacao)}')
        print(f'Nome: {sabor.nome}')


async def select_complexo_picole() -> None:
    async with create_session() as session:
        query = select(Picole)
        picoles: List[Picole] = await session.execute(query)
        picoles = picoles.scalars().unique().all()

        for picole in picoles:
            print(f'ID: {picole.id}')
            print(f'Data: {picole.data_criacao}')
            print(f'Preço: {picole.preco}')
            print(f'Sabor: {picole.sabor.nome}')
            print(f'Tipo Picole: {picole.tipo_picole.nome}')
            print(f'Tipo Embalagem: {picole.tipo_embalagem.nome}')
            print(f'Ingredientes: {picole.ingredientes}')
            print(f'Conservantes: {picole.conservantes}')
            print(f'Aditivos Nutritivos: {picole.aditivos_nutritivos}')
            print('-------------------------------------------------------------------')


async def select_order_by_sabor() -> None:
    async with create_session() as session:
        query = select(Sabor).order_by(Sabor.data_criacao.desc())
        sabores: List[Sabor] = await session.execute(query)
        sabores = sabores.scalars().all()

        for sabor in sabores:
            print(f'ID: {sabor.id}')
            print(f'Data: {sabor.data_criacao}')
            print(f'Nome: {sabor.nome}')
            print('-------------------------------------------------------------------')


async def select_group_by_picole() -> None:
    async with create_session() as session:
        query = select(Picole).group_by(Picole.id, Picole.id_tipo_picole)
        picoles: List[Picole] = session.execute(query)
        picoles = picoles.scalars().unique().all()

        for picole in picoles:
            print(f'ID: {picole.id}')
            print(f'Tipo Picole: {picole.tipo_picole.nome}')
            print(f'Data: {picole.data_criacao}')
            print(f'Preço: {picole.preco}')
            print(f'Sabor: {picole.sabor.nome}')
            print('-------------------------------------------------------------------')


async def select_limit() -> None:
    async with create_session() as session:
        query = select(Sabor).limit(25)
        sabores: List[Sabor] = await session.execute(query)
        sabores = sabores.scalars()

        for sabor in sabores:
            print(f'ID: {sabor.id}')
            print(f'Data: {sabor.data_criacao}')
            print(f'Nome: {sabor.nome}')
            print('-------------------------------------------------------------------')


async def select_count_revendedor() -> None:
    async with create_session() as session:
        query = select(func.count(Revendedor.id))
        resultado = await session.execute(query)
        quantidade: int = resultado.scalar()

        print(f'Quantidade de revendedores: {quantidade}')


async def select_agregacao() -> None:
    async with create_session() as session:
        query = select(
            func.sum(Picole.preco).label('soma'),
            func.avg(Picole.preco).label('media'),
            func.min(Picole.preco).label('mais_barato'),
            func.max(Picole.preco).label('mais_caro')
        )
        resultado = await session.execute(query)
        resultado = resultado.all()

        print(f'Resultado: {resultado}')

        print(f'A soma de todos os picolés é: {resultado[0][0]}')
        print(f'A média de todos os picolés é: {resultado[0][1]}')
        print(f'O picolé mais barato é: {resultado[0][2]}')
        print(f'O picolé mais caro é: {resultado[0][3]}')


if __name__ == '__main__':
    # asyncio.run(select_todos_aditivos_nutritivos())

    # asyncio.run(select_filtro_sabor(21))

    # asyncio.run(select_complexo_picole())

    # asyncio.run(select_order_by_sabor())

    # asyncio.run(select_group_by_picole())

    # asyncio.run(select_limit())

    # asyncio.run(select_count_revendedor())

    asyncio.run(select_agregacao())

    pass
