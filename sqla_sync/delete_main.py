from typing import Optional

from sqla_sync.conf.db_session import create_session

from sqla_sync.models.picole import Picole
from sqla_sync.models.revendedor import Revendedor


def deletar_picole(id_picole: int) -> None:
    with create_session() as session:
        picole: Optional[Picole] = session.query(Picole).filter(Picole.id == id_picole).one_or_none()

        if picole:
            session.delete(picole)
            session.commit()
        else:
            print(f'Não encontrei picole com ID {id_picole}')


def deletar_revendedor(id_revendedor: int) -> None:
    with create_session() as session:
        revendedor: Optional[Revendedor] = session.query(Revendedor).filter(
            Revendedor.id == id_revendedor).one_or_none()

        if revendedor:
            session.delete(revendedor)
            session.commit()
        else:
            print(f'Não encontrei revendedor com ID {id_revendedor}')


if __name__ == '__main__':
    pass
