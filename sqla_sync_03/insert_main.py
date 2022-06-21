from sqla_sync_03.conf.db_session import create_session
from sqla_sync_03.models.aditivo_nutritivo import AditivoNutritivo
from sqla_sync_03.models.conservante import Conservante
from sqla_sync_03.models.ingrediente import Ingrediente
from sqla_sync_03.models.lote import Lote
from sqla_sync_03.models.nota_fiscal import NotaFiscal
from sqla_sync_03.models.picole import Picole
from sqla_sync_03.models.revendedor import Revendedor
from sqla_sync_03.models.sabor import Sabor
from sqla_sync_03.models.tipo_embalagem import TipoEmbalagem
from sqla_sync_03.models.tipo_picole import TipoPicole


# Aditivo Nutritivo
def insert_aditivo_nutritivo() -> None:
    print('Cadastrando Aditivo Nutritivo')

    nome: str = input('Informe o nome do Aditivo Nutritivo: ')
    formula_quimica: str = input('Informe a fórmula química do aditivo: ')

    an: AditivoNutritivo = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)

    with create_session() as session:
        session.add(an)
        session.commit()

    print('Aditivo Nutritivo cadastrado com sucesso')
    print(f'ID: {an.id}')
    print(f'Data: {an.data_criacao}')
    print(f'Nome: {an.nome}')
    print(f'Fórmula Química: {an.formula_quimica}')


# Sabor
def insert_sabor() -> None:
    print('Cadastrando Sabor')

    nome: str = input('Informe o nome do Sabor: ')

    sabor: Sabor = Sabor(nome=nome)

    with create_session() as session:
        session.add(sabor)
        session.commit()

    print('Sabor cadastrado com sucesso')
    print(f'ID: {sabor.id}')
    print(f'Data: {sabor.data_criacao}')
    print(f'Nome: {sabor.nome}')


# Tipo Embalagem
def insert_tipo_embalagem() -> None:
    print('Cadastrando Tipo Embalagem')

    nome: str = input('Informe o nome do Tipo Embalagem: ')

    te: TipoEmbalagem = TipoEmbalagem(nome=nome)

    with create_session() as session:
        session.add(te)
        session.commit()

    print('Tipo Embalagem cadastrado com sucesso')
    print(f'ID: {te.id}')
    print(f'Data: {te.data_criacao}')
    print(f'Nome: {te.nome}')


# Tipo Picole
def insert_tipo_picole() -> None:
    print('Cadastrando Tipo Picole')

    nome: str = input('Informe o nome do Tipo Picole: ')

    tp: TipoPicole = TipoPicole(nome=nome)

    with create_session() as session:
        session.add(tp)
        session.commit()

    print('Tipo Picole cadastrado com sucesso')
    print(f'ID: {tp.id}')
    print(f'Data: {tp.data_criacao}')
    print(f'Nome: {tp.nome}')


# Ingrediente
def insert_ingrediente() -> None:
    print('Cadastrando Ingrediente')

    nome: str = input('Informe o nome do Ingrediente: ')

    ingrediente: Ingrediente = Ingrediente(nome=nome)

    with create_session() as session:
        session.add(ingrediente)
        session.commit()

    print('Ingrediente cadastrado com sucesso')
    print(f'ID: {ingrediente.id}')
    print(f'Data: {ingrediente.data_criacao}')
    print(f'Nome: {ingrediente.nome}')


# Conservante
def insert_conservante() -> None:
    print('Cadastrando Conservante')

    nome: str = input('Informe o nome do Conservante: ')
    descricao: str = input('Informe a descrição do Conservante: ')

    conservante: Conservante = Conservante(nome=nome, descricao=descricao)

    with create_session() as session:
        session.add(conservante)
        session.commit()

    print('Conservante cadastrado com sucesso')
    print(f'ID: {conservante.id}')
    print(f'Data: {conservante.data_criacao}')
    print(f'Nome: {conservante.nome}')
    print(f'Descrição: {conservante.descricao}')


# Revendedor
def insert_revendedor() -> None:
    print('Cadastrando Revendedor')

    nome: str = input('Informe o nome do Revendedor: ')
    razao_social: str = input('Informe a razão social do Revendedor: ')
    contato: str = input('Informe o contato do Revendedor: ')

    revendedor: Revendedor = Revendedor(nome=nome,
                                        razao_social=razao_social,
                                        contato=contato)

    with create_session() as session:
        session.add(revendedor)
        session.commit()

    print('Revendedor cadastrado com sucesso')
    print(f'ID: {revendedor.id}')
    print(f'Data: {revendedor.data_criacao}')
    print(f'Nome: {revendedor.nome}')
    print(f'Razão social: {revendedor.razao_social}')
    print(f'Contato: {revendedor.contato}')


if __name__ == '__main__':
    # insert_aditivo_nutritivo()

    # insert_sabor()

    # insert_tipo_embalagem()

    # insert_tipo_picole()

    # insert_ingrediente()

    # insert_conservante()

    # insert_revendedor()

    pass
