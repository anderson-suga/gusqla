from sqla_sync.conf.db_session import create_session

from sqla_sync.models.sabor import Sabor
from sqla_sync.models.picole import Picole


def atualiza_sabor(id_sabor: int, novo_sabor: str) -> None:
    with create_session() as session:
        sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one_or_none()

        if sabor:
            sabor.nome = novo_sabor
            session.commit()
        else:
            print(f'Não existe sabor com ID {id_sabor}')


def atualiza_picole(id_picole: int, novo_preco: float, novo_sabor: int = None):
    with create_session() as session:
        picole: Picole = session.query(Picole).filter(Picole.id == id_picole).one_or_none()

        if picole:
            picole.preco = novo_preco
            if novo_sabor:
                picole.id_sabor = novo_sabor
            session.commit()
        else:
            print(f'Não existe sabor com ID {id_picole}')


if __name__ == '__main__':
    pass
