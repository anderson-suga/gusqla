from sqlm_async.conf.db_session import create_session
from sqlm_async.models.aditivo_nutritivo import AditivoNutritivo
from sqlm_async.models.conservante import Conservante
from sqlm_async.models.ingrediente import Ingrediente
from sqlm_async.models.lote import Lote
from sqlm_async.models.nota_fiscal import NotaFiscal
from sqlm_async.models.picole import Picole
from sqlm_async.models.revendedor import Revendedor
from sqlm_async.models.sabor import Sabor
from sqlm_async.models.tipo_embalagem import TipoEmbalagem
from sqlm_async.models.tipo_picole import TipoPicole


# Aditivo Nutritivo
def insert_aditivo_nutritivo() -> AditivoNutritivo:
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

        return an


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
def insert_ingrediente() -> Ingrediente:
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

        return ingrediente


# Conservante
def insert_conservante() -> Conservante:
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

        return conservante


# Revendedor
def insert_revendedor() -> Revendedor:
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

        return revendedor


# Lote
def insert_lote() -> Lote:
    print('Cadastrando Lote')

    id_tipo_picole: int = int(input('Informe o ID do tipo do picole: '))
    quantidade: int = int(input('Informe a quantidade do picole: '))

    lote: Lote = Lote(id_tipo_picole=id_tipo_picole,
                      quantidade=quantidade)

    with create_session() as session:
        session.add(lote)
        session.commit()

        print('Lote cadastrado com sucesso')
        print(f'ID: {lote.id}')
        print(f'Data: {lote.data_criacao}')
        print(f'ID do tipo do picole: {lote.id_tipo_picole}')
        print(f'Quantidade: {lote.quantidade}')

        return lote


# Nota Fiscal
def insert_nota_fiscal() -> None:
    print('Cadastrando Nota Fiscal')

    valor: float = float(input('Informe o valor da nota fiscal: '))
    numero_serie: str = input('Informe o número da série: ')
    descricao: str = input('Informe a descrição da nota fiscal: ')

    rev = insert_revendedor()
    id_revendedor = rev.id

    nf: NotaFiscal = NotaFiscal(valor=valor,
                                numero_serie=numero_serie,
                                descricao=descricao,
                                id_revendedor=id_revendedor)

    lote1 = insert_lote()
    nf.lotes.append(lote1)

    lote2 = insert_lote()
    nf.lotes.append(lote2)

    with create_session() as session:
        session.add(nf)
        session.commit()

        print('Nota Fiscal cadastrada com sucesso')
        print(f'ID: {nf.id}')
        print(f'Data: {nf.data_criacao}')
        print(f'Valor: {nf.valor}')
        print(f'Número da Série: {nf.numero_serie}')
        print(f'Descrição: {nf.descricao}')
        print(f'ID Revendedor: {nf.id_revendedor}')
        print(f'Revendedor: {nf.revendedor.razao_social}')


# Picole
def insert_picole() -> None:
    print('Cadastrando Picole')

    preco: float = float(input('Informe o preço do picole: '))
    id_sabor: int = int(input('Informe o ID do sabor: '))
    id_tipo_picole: int = int(input('Informe o ID do tipo do picole: '))
    id_tipo_embalagem: int = int(input('Informe o ID do tipo da embalagem: '))

    picole: Picole = Picole(preco=preco,
                            id_sabor=id_sabor,
                            id_tipo_picole=id_tipo_picole,
                            id_tipo_embalagem=id_tipo_embalagem)

    ingrediente1 = insert_ingrediente()
    picole.ingredientes.append(ingrediente1)

    ingrediente2 = insert_ingrediente()
    picole.ingredientes.append(ingrediente2)

    conservante = insert_conservante()
    picole.conservantes.append(conservante)

    aditivo_nutritivo = insert_aditivo_nutritivo()
    picole.aditivos_nutritivos.append(aditivo_nutritivo)

    with create_session() as session:
        session.add(picole)
        session.commit()

        print('Picole cadastrado com sucesso')
        print(f'ID: {picole.id}')
        print(f'Data: {picole.data_criacao}')
        print(f'Preço: {picole.preco}')
        print(f'Sabor: {picole.sabor.nome}')
        print(f'Tipo Picole: {picole.tipo_picole.nome}')
        print(f'Tipo Embalagem: {picole.tipo_embalagem.nome}')
        print(f'Ingredientes: {picole.ingredientes}')
        print(f'Conservantes: {picole.conservantes}')
        print(f'Aditivos Nutritivos: {picole.aditivos_nutritivos}')


if __name__ == '__main__':
    # insert_aditivo_nutritivo()

    # insert_sabor()

    # insert_tipo_embalagem()

    # insert_tipo_picole()

    # insert_ingrediente()

    # insert_conservante()

    # insert_revendedor()

    # insert_lote()

    # insert_nota_fiscal()

    # insert_picole()

    pass
