#  Cria a classe alunos que permite inserir, atualizar,
#  listar, buscar e deletar alunos no banco de dados.

import psycopg2
from config import config


class Alunos():
    def __init__(self):
        pass

    #  Método para inclusão de alunos.
    def incluir(self, **kwargs):
        """ Insere um aluno na tabela Alunos"""
        p_nome = kwargs.get('nome')
        p_cpf = kwargs.get('cpf')
        p_data_nasc = kwargs.get('data_nasc')
        p_telefone = kwargs.get('telefone')

        sql = f"""
        INSERT INTO public.Alunos(nome_aluno, cpf_aluno, data_nasc_aluno, telefone_aluno)
            VALUES('{p_nome}', '{p_cpf}', '{p_data_nasc}', '{p_telefone}') RETURNING id_aluno;
        """

        conn = None
        id_aluno = None

        try:
            # read database configuration
            params = config(filename=".\database.ini")
            # connect to the PostgreSQL database
            conn = psycopg2.connect(**params)
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql)
            # get the generated id back
            id_aluno = cur.fetchone()[0]
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.close()

            print(f"Aluno {p_nome.upper()} inserido com sucesso!")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

        return id_aluno
    

    #  Método para atualização de alunos.
    def atualizar(self, **kwargs):
        """Atualiza os dados de um aluno"""
        p_id_aluno = kwargs.get('id_aluno')
        p_nome = kwargs.get('nome')
        p_cpf = kwargs.get('cpf')
        p_data_nasc = kwargs.get('data_nasc')
        p_telefone = kwargs.get('telefone')

        sql = f"""
                    UPDATE public.Alunos
                    SET nome_aluno = '{p_nome}',
                    cpf_aluno = '{p_cpf}',
                    data_nasc_aluno = '{p_data_nasc}',
                    telefone_aluno = '{p_telefone}'
                    WHERE id_aluno = '{p_id_aluno}';
                """

        conn = None
        updated_rows = 0

        try:          
            params = config(filename=".\database.ini")
            conn = psycopg2.connect(**params)

            cur = conn.cursor()

            cur.execute(sql)

            deleted_rows = cur.rowcount

            conn.commit()

            cur.close()
            return deleted_rows
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()  


    # Método para exclusão de aluno.
    def excluir(self, id_aluno):
        """Exclui um aluno a partir de seu ID"""
        conn = None
        deleted_rows = 0
        try:
            sql = f"""
                        DELETE FROM public.Alunos
                        WHERE id_aluno = '{id_aluno}';
                    """

            params = config(filename=".\database.ini") #  local do arquivo database.ini
            conn = psycopg2.connect(**params)

            cur = conn.cursor()

            cur.execute(sql)

            deleted_rows = cur.rowcount

            conn.commit()

            cur.close()
            return deleted_rows


        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    #  Método para listar todos os alunos.
    def listar(self):
        """Imprime uma lista com todos os alunos"""
        conn = None

        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute("SELECT id_aluno, nome_aluno, cpf_aluno, data_nasc_aluno, telefone_aluno FROM Alunos")

            # Imprime o número de alunos cadastrados.
            print(f"\nHá {cur.rowcount} aluno(s) cadastrado(s): ")
            row = cur.fetchone()

            while row is not None:
                print(f"\nID: {row[0]}\nNome: {row[1]}\nCPF: {row[2]}\nData de Nascimento: {row[3].strftime('%d/%m/%Y')}\nTelefone: {row[4]}\n")
                row = cur.fetchone()
            
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        finally:
            if conn is not None:
                conn.close()
    

    def isVazia(self):
        """Verifica se a lista está vazia"""
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute("SELECT id_aluno FROM Alunos")

            #  Retorna booleano para ser usado em uma condicional.
            return (cur.rowcount == 0)

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        finally:
            if conn is not None:
                conn.close()


    #  Metódo que deve ser executado quando a lista estiver vazia.
    def listaVazia(self):
        """Pergunta ao usuário se quer incluir um aluno. Caso a resposta seja sim, executa o loop de inclusão"""
        opcao_adicionar = input("A lista está vazia. Deseja incluir um novo aluno? 'S' ou 's' para incluir: ")
        if opcao_adicionar.lower().startswith('s'):
            self.loopIncluir()
    

    #  Método para buscar aluno.
    def buscarAluno(self, nome_pesquisado):
        """Busca alunos a partir de um nome."""
        conn = None
        
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute("SELECT id_aluno, nome_aluno, cpf_aluno, data_nasc_aluno, telefone_aluno FROM Alunos")
            row = cur.fetchone()

            while row is not None:
                if nome_pesquisado in row[1]:
                    print(f"\nID: {row[0]}\nNome: {row[1]}\nCPF: {row[2]}\nData de Nascimento: {row[3].strftime('%d/%m/%Y')}\nTelefone: {row[4]}\n")
                row = cur.fetchone()
            
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        finally:
            if conn is not None:
                conn.close()
    
    #  Método que cria loop de inclusão.
    def loopIncluir(self):
        while True:
            self.incluir(nome=input("Digite o nome do Aluno:\n"),
                            cpf=input("Digite o CPF do Aluno:\n"),
                            data_nasc=input("Digite a data de nascimento do Aluno:\n"),
                            telefone=input("Digite o telefone do Aluno:\n"))

            #  Solicitando a saída para o usuário    
            controle_insert = input("Deseja incluir mais um aluno? Digite 'N' ou 'n' para sair: ")

            #  Verifica se a resposta começa com 'n' ou 'N'.
            if controle_insert.lower().startswith('n'):
                print("Saindo da inclusão de alunos...")
                break

    #  Método que cria loop de atualização.
    def loopAtualizar(self):
        while True:
            input_do_usuario = int(input("Digite um ID para atualizar os dados do aluno: \n"))

            self.atualizar(nome=input("Digite o nome do Aluno:\n"),
                            cpf=input("Digite o CPF do Aluno\n"),
                            data_nasc=input("Digite a data de nascimento do Aluno:\n"),
                            telefone=input("Digite o telefone do Aluno\n"),
                            id_aluno=input_do_usuario)
            
            #  Solicitando a saída para o usuário
            controle_insert = input("Deseja atualizar mais um aluno? Digite 'N' ou 'n' para sair: ")

            #  Verifica se a resposta começa com 'n' ou 'N'.
            if controle_insert.lower().startswith('n'):
                print("Saindo da atualização de dados de alunos...")
                break
    
    #  Método que cria loop de busca.
    def loopBuscar(self):
        while True:
            input_do_usuario = input("Insira o nome do aluno que deseja pesquisar:\n")
            self.buscarAluno(input_do_usuario)

            #  Solicitando a saída para o usuário
            controle_insert = input("Deseja buscar mais um aluno? Digite 'N' ou 'n' para sair: ")

            #  Verifica se a resposta começa com 'n' ou 'N'.
            if controle_insert.lower().startswith('n'):
                print("Saindo da busca de alunos...")
                break

    #  Método que cria loop de exclusão.
    def loopExcluir(self):
        while True:
            input_do_usuario = int(input("Digite um ID para a exclusão do aluno: \n"))

            self.excluir(input_do_usuario)

            #  Caso a lista esteja vazia, informa o usuário e sai do menu exclusão.
            if self.isVazia():
                print("\nNão há outros alunos cadastrados. Saindo de exclusão de alunos...")
                break

            else:
                #  Solicitando a saída para o usuário
                controle_insert = input("Deseja excluir mais um aluno? Digite 'N' ou 'n' para sair: ")

                #  Verifica se a resposta começa com 'n' ou 'N'.
                if controle_insert.lower().startswith('n'):
                    print("Saindo da exclusão de alunos...")
                    break

# Executa este bloco caso o arquivo seja executado a partir dele mesmo.
if __name__ == '__main__':
    aluno = Alunos()
    # Insere um aluno.
    aluno.incluir(nome='Rafaela',
                    cpf='65214587565',
                    data_nasc='12/02/1982',
                    telefone='19952641525')