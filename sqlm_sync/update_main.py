from sqlm_sync.conf.db_session import create_session

from sqlmodel import select

from sqlm_sync.models.sabor import Sabor
from sqlm_sync.models.picole import Picole


def atualiza_sabor(id_sabor: int, novo_sabor: str) -> None:
    with create_session() as session:
        sabor: Sabor = session.get(Sabor, id_sabor)

        if sabor:
            sabor.nome = novo_sabor
            session.commit()
        else:
            print(f'Não existe sabor com ID {id_sabor}')


def atualiza_picole(id_picole: int, novo_preco: float, novo_sabor: int = None):
    with create_session() as session:
        picole: Picole = session.get(Picole, id_picole)

        if picole:
            picole.preco = novo_preco
            if novo_sabor:
                picole.id_sabor = novo_sabor
            session.commit()
        else:
            print(f'Não existe sabor com ID {id_picole}')


if __name__ == '__main__':
    pass
