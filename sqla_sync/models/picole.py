import sqlalchemy as sa
import sqlalchemy.orm as orm

from datetime import datetime
from typing import List, Optional

from sqla_sync.models.model_base import ModelBase
from sqla_sync.models.sabor import Sabor
from sqla_sync.models.tipo_embalagem import TipoEmbalagem
from sqla_sync.models.tipo_picole import TipoPicole
from sqla_sync.models.ingrediente import Ingrediente
from sqla_sync.models.conservante import Conservante
from sqla_sync.models.aditivo_nutritivo import AditivoNutritivo

# Picolé pode ter vários ingredientes
ingredientes_picole = sa.Table(
    'ingredientes_picole',
    ModelBase.metadata,
    sa.Column('id_picole', sa.Integer, sa.ForeignKey('picoles.id')),
    sa.Column('id_ingrediente', sa.Integer, sa.ForeignKey('ingredientes.id'))
)

# Picolé pode ter vários conservantes
conservantes_picole = sa.Table(
    'conservantes_picole',
    ModelBase.metadata,
    sa.Column('id_picole', sa.Integer, sa.ForeignKey('picoles.id')),
    sa.Column('id_conservante', sa.Integer, sa.ForeignKey('conservantes.id'))
)

# Picolé pode ter vários aditivos nutritivos
aditivos_nutritivos_picole = sa.Table(
    'aditivos_nutritivos_picole',
    ModelBase.metadata,
    sa.Column('id_picole', sa.Integer, sa.ForeignKey('picoles.id')),
    sa.Column('id_aditivo_nutritivo', sa.Integer, sa.ForeignKey('aditivos_nutritivos.id'))
)


class Picole(ModelBase):
    __tablename__: str = 'picoles'

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)

    preco: float = sa.Column(sa.DECIMAL(8, 2), nullable=False)

    id_sabor: int = sa.Column(sa.Integer, sa.ForeignKey('sabores.id'))
    sabor: Sabor = orm.relationship('Sabor', lazy='joined')

    id_tipo_embalagem: int = sa.Column(sa.Integer, sa.ForeignKey('tipos_embalagem.id'))
    tipo_embalagem: TipoEmbalagem = orm.relationship('TipoEmbalagem', lazy='joined')

    id_tipo_picole: int = sa.Column(sa.Integer, sa.ForeignKey('tipos_picole.id'))
    tipo_picole: TipoPicole = orm.relationship('TipoPicole', lazy='joined')

    # Um picolé pode ter vários ingredientes
    ingredientes: List[Ingrediente] = orm.relationship('Ingrediente',
                                                       secondary=ingredientes_picole,
                                                       backref='ingrediente',
                                                       lazy='joined')

    # Um picolé pode ter vários conservantes ou mesmo nenhum
    conservantes: Optional[List[Conservante]] = orm.relationship('Conservante',
                                                                 secondary=conservantes_picole,
                                                                 backref='conservante',
                                                                 lazy='joined')

    # Um picolé pode ter vários aditivos nutritivos ou mesmo nenhum
    aditivos_nutritivos: Optional[List[AditivoNutritivo]] = orm.relationship('AditivoNutritivo',
                                                                             secondary=aditivos_nutritivos_picole,
                                                                             backref='aditivo_nutritivo',
                                                                             lazy='joined')

    def __repr__(self) -> str:
        return f'<Picole: {self.tipo_picole.nome} com sabor {self.sabor.nome} e preço {self.preco}>'
