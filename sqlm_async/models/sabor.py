from typing import Optional
from sqlmodel import Field, SQLModel
from sqlalchemy import UniqueConstraint
from datetime import datetime


class Sabor(SQLModel, table=True):
    __tablename__: str = 'sabores'
    __table_args__ = (UniqueConstraint('nome'),)

    id: Optional[int] = Field(primary_key=True)
    data_criacao: datetime = Field(default=datetime.now(), index=True)

    nome: str = Field(max_length=45)

    def __repr__(self) -> str:
        return f'<Sabor: {self.nome}>'
