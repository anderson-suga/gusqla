from typing import Optional

from sqlm_async.conf.db_session import create_session

from sqlm_async.models.picole import Picole
from sqlm_async.models.revendedor import Revendedor


def deletar_picole(id_picole: int) -> None:
    with create_session() as session:
        picole: Optional[Picole] = session.get(Picole, id_picole)

        if picole:
            session.delete(picole)
            session.commit()
        else:
            print(f'Não encontrei picole com ID {id_picole}')


def deletar_revendedor(id_revendedor: int) -> None:
    with create_session() as session:
        revendedor: Optional[Revendedor] = session.get(Revendedor, id_revendedor)

        if revendedor:
            session.delete(revendedor)
            session.commit()
        else:
            print(f'Não encontrei revendedor com ID {id_revendedor}')


if __name__ == '__main__':
    pass
