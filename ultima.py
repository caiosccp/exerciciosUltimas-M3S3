import sqlite3

def criarTodo(cursor):
    descricaoTodo = input("Digite a Descrição -> ")
    categoriaTodo = int(input("Digite sua Categoria -> "))
    dataEvento = input("Digite sua Data e Horário -> ")
    isConcluido = int(input("Digite se está concluído ou não (0 | 1) -> "))

    query = 'insert into TODO(descricao, categoria_id, dataEvento, isConcluido) values(?, ?, ?, ?)'
    valores = [descricaoTodo, categoriaTodo, dataEvento, isConcluido]
    consulta = cursor.execute(query, valores)

    return consulta

def atualizarTodo(cursor):

    idParaAtualizar = int(input("Digite o ID que será atualizado -> "))
    descricaoTodo = input("Digite a Descrição para Atualização-> ")
    categoriaTodo = int(input("Digite sua Categoria para Atualização-> "))
    dataEvento = input("Digite sua Data e Horário para Atualização -> ")
    
    query = 'update TODO set descricao = ?, categoria_id = ?, dataEvento = ? where id = ?'
    valores = [descricaoTodo, categoriaTodo, dataEvento, idParaAtualizar]
    consulta = cursor.execute(query, valores)

    return consulta

def removerTodo(cursor):
    idParaRemover = input("Digite o ID que será removido -> ")

    query = 'delete from TODO where id = ?'
    valores = [idParaRemover]
    consulta = cursor.execute(query, valores)

    return consulta

def criarCategoria(cursor):
    descricaoCategoria = input("Digite a Descrição da Categoria -> ")

    query = 'insert into categoria(descricao) values(?)'
    valores = [descricaoCategoria]
    consulta = cursor.execute(query, valores)

    return consulta

def atualizarCategoria(cursor):
    descricaoParaAtualizar = input("Digite a Nova Descrição -> ")
    idParaAtualizar = int(input("Digite o ID para Atualizar -> "))

    query = 'update categoria set descricao = ? where id = ?'
    valores = [descricaoParaAtualizar, idParaAtualizar]
    consulta = cursor.execute(query, valores)

    return consulta

def removerCategoria(cursor):
    idParaRemover = int(input("Digite o ID da Categoria que será removida -> "))

    query = 'delete from categoria where id = ?'
    valores = [idParaRemover]
    consulta = cursor.execute(query, valores)

    return consulta

def listarAfazeres(cursor):
    dataEspecifica = input("Digite a Data que deseja consultar -> ")
    query = 'select * from TODO where dataEvento = ?'
    valores = [dataEspecifica]
    
    consulta = cursor.execute(query, valores)

    return consulta

def listarTodasCategorias(cursor):

    query = 'select * from categoria'

    consulta = cursor.execute(query)

    return consulta

def concluirEvento(cursor):

    isConcluido = int(input("Digite se está concluído ou não (0 | 1) -> "))
    idParaAtualizar = int(input("Digite o ID para Atualizar -> "))

    query = 'update TODO set isConcluido = ? where id = ?'
    valores = [isConcluido, idParaAtualizar]

    consulta = cursor.execute(query, valores)
    
    return consulta

def realizaConsulta(funcao):

    conexao = sqlite3.connect('ultima')
    cursor = conexao.cursor()
    consulta = funcao(cursor)
    conexao.commit()
    conexao.close

    return consulta

def imprimirConsulta(consulta):
    for resultado in consulta:
        print(resultado)

def menu():

    print('''
            1 - Criar CATEGORIA
            2 - Atualizar CATEGORIA
            3 - Remover CATEGORIA
            4 - Criar TODO
            5 - Atualizar TODO
            6 - Remover TODO
            7 - Listar Todos TODO numa Data Específica
            8 - Listar Todas as Categorias
            9 - Concluir um TODO
            0 - Sair
    ''')

    opcao = int(input("Digite sua Opção -> "))

    if (opcao == 1):
        realizaConsulta(criarCategoria)
    
    elif (opcao == 2):
        realizaConsulta(atualizarCategoria)
    
    elif (opcao == 3):
        realizaConsulta(removerCategoria)

    elif (opcao == 4):
        realizaConsulta(criarTodo)

    elif (opcao == 5):
        realizaConsulta(atualizarTodo)

    elif (opcao == 6):
        realizaConsulta(removerTodo)

    elif (opcao == 7):
        consulta = realizaConsulta(listarAfazeres)
        imprimirConsulta(consulta)

    elif (opcao == 8):
        consulta = realizaConsulta(listarTodasCategorias)
        imprimirConsulta(consulta)

    elif (opcao == 9):
        realizaConsulta(concluirEvento)

    elif (opcao == 0):
        exit

    else:
        print("Opção Inválida")

menu()