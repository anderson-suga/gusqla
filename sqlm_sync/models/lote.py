from typing import Optional

from sqlmodel import Field, SQLModel, Relationship

from datetime import datetime

from sqlm_sync.models.tipo_picole import TipoPicole


class Lote(SQLModel, table=True):
    __tablename__: str = 'lotes'

    id: Optional[int] = Field(primary_key=True, autoincrement=True)
    data_criacao: datetime = Field(default=datetime.now, index=True)

    id_tipo_picole: Optional[int] = Field(default=None, foreign_key='tipos_picole.id')
    tipo_picole: TipoPicole = Relationship(back_populates='tipo_picole')

    quantidade: int = Field()

    def __repr__(self) -> int:
        return f'<Lote: {self.id}>'
