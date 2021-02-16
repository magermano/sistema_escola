#  Cria a classe PROFESSOR que permite inserir, atualizar,
#  listar, buscar e deletar PROFESSOR no banco de dados.

import psycopg2
from datetime import datetime, date
from config import config


class Professores():
    def __init__(self):
        pass

    #  Método para inclusão de PROFESSOR.
    def incluirProfessor(self, **kwargs):
        """ Insere um PROFESSOR na tabela PROFESSORES"""
        p_nome = kwargs.get('nome')
        p_cpf = kwargs.get('cpf')
        p_data_nasc = kwargs.get('data_nasc')
        p_telefone = kwargs.get('telefone')
        p_formacao = kwargs.get('formacao')

        sql = f"""
        INSERT INTO public.Professores(nome_prof, cpf_prof, data_nasc_prof, telefone, formacao)
            VALUES('{p_nome}', '{p_cpf}', '{p_data_nasc}', '{p_telefone}', '{p_formacao}') RETURNING id_professor;
        """

        conn = None
        id_professor = None

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
            id_professores = cur.fetchone()[0]
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.close()

            print(f"Professor {p_nome.upper()} inserido com sucesso!")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

        return id_professor
    

    #  Método para atualização de PROFESSOR.
    def atualizarProfessor(self, **kwargs):
        """Atualiza os dados de um PROFESSOR"""
        p_id_professor = kwargs.get('id_professor')
        p_nome = kwargs.get('nome')
        p_cpf = kwargs.get('cpf')
        p_data_nasc = kwargs.get('data_nasc')
        p_telefone = kwargs.get('telefone')
        p_formacao = kwargs.get('formacao')

        sql = f"""
                    UPDATE public.Professores
                    SET nome_prof = '{p_nome}',
                    cpf_prof = '{p_cpf}',
                    data_nasc_prof = '{p_data_nasc}',
                    telefone = '{p_telefone}',
                    formacao = '{p_formacao}'
                    WHERE id_professor = '{p_id_professor}';
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


    # Método para exclusão de PROFESSOR.
    def excluirProfessor(self, id_professor):
        """Exclui um PROFESSOR a partir de seu ID"""
        conn = None
        deleted_rows = 0
        try:
            sql = f"""
                        DELETE FROM public.Professores
                        WHERE id_professor = '{id_professor}';
                    """

            params = config(filename=".\database.ini") #  local do arquivo database.ini
            conn = psycopg2.connect(**params)

            cur = conn.cursor()

            cur.execute(sql)

            deleted_rows = cur.rowcount

            conn.commit()

            cur.close()
            return deleted_rows

            # TODO: Mostrar ao usuário que o PROFESSOR foi excluído com sucesso.

        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    #  Método para listar todos os PROFESSOR.
    def listarProfessor(self):
        """Imprime uma lista com todos os PROFESSOR"""
        conn = None

        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute("SELECT id_professor, nome_prof, cpf_prof, data_nasc_prof, telefone, formacao FROM Professores")

            # Imprime o número de PROFESSOR cadastrados.
            print(f"\nHá {cur.rowcount} PROFESSOR(Es) cadastrado(s): ")
            row = cur.fetchone()

            while row is not None:
                # TODO: Mostrar idade.
                print(f"\nID: {row[0]}\nNome: {row[1]}\nCPF: {row[2]}\nData de Nascimento: {row[3].strftime('%d/%m/%Y')}\nTelefone: {row[4]}\nFormação: {row[5]}\n")
                row = cur.fetchone()
            
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        finally:
            if conn is not None:
                conn.close()
    

    def isProfessorVazia(self):
        """Verifica se a lista está vazia"""
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute("SELECT id_professor FROM Professores")

            #  Retorna booleano para ser usado em uma condicional.
            return (cur.rowcount == 0)

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        finally:
            if conn is not None:
                conn.close()


    #  Metódo que deve ser executado quando a lista estiver vazia.
    def listaProfessorVazia(self):
        """Pergunta ao usuário se quer incluir um PROFESSOR. Caso a resposta seja sim, executa o loop de inclusão"""
        opcao_adicionar = input("A lista está vazia. Deseja incluir um novo PROFESSOR? 'S' ou 's' para incluir: ")
        if opcao_adicionar.lower().startswith('s'):
            self.loopIncluirProfessor()
    

    #  Método para buscar PROFESSOR.
    def buscarProfessor(self, nome_pesquisado):
        """Busca PROFESSOR a partir de um nome."""
        conn = None
        
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute("SELECT id_professor, nome_prof, cpf_prof, data_nasc_prof, telefone, formacao FROM Professores")
            row = cur.fetchone()

            while row is not None:
                if nome_pesquisado in row[1]:
                    print(f"\nID: {row[0]}\nNome: {row[1]}\nCPF: {row[2]}\nData de Nascimento: {row[3].strftime('%d/%m/%Y')}\nTelefone: {row[4]}\nFormação: {row[5]}\n")
                row = cur.fetchone()
            
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        finally:
            if conn is not None:
                conn.close()
    
    #  Método que cria loop de inclusão.
    def loopIncluirProfessor(self):
        while True:
            self.incluirProfessor(nome=input("Digite o nome do PROFESSOR:\n"),
                            cpf=input("Digite o CPF do PROFESSOR:\n"),
                            data_nasc=input("Digite a data de nascimento do PROFESSOR:\n"),
                            telefone=input("Digite o telefone do PROFESSOR:\n"),
                            tformacao=input("Digite a formação do PROFESSOR:\n")
                            )

            #  Solicitando a saída para o usuário    
            controle_insert = input("Deseja incluir mais um PROFESSOR ? (Digite 'N' ou 'n' para sair: ")

            #  Verifica se a resposta começa com 'n' ou 'N'.
            if controle_insert.lower().startswith('n'):
                print("Saindo da inclusão de PROFESSOR...")
                break

    #  Método que cria loop de atualização.
    def loopAtualizarProfessor(self):
        while True:
            input_do_usuario = int(input("Digite um ID para atualizar os dados do PROFESSOR: \n"))

            self.atualizarProfessor(nome=input("Digite o nome do PROFESSOR:\n"),
                            cpf=input("Digite o CPF do PROFESSOR\n"),
                            data_nasc=input("Digite a data de nascimento do PROFESSOR:\n"),
                            telefone=input("Digite o telefone do PROFESSOR\n"),
                            formacao=input("Digite a formação do PROFESSOR\n"),
                            id_professor=input_do_usuario)
            
            #  Solicitando a saída para o usuário
            controle_insert = input("Deseja atualizar mais um PROFESSOR? (Digite 'N' ou 'n' para sair: ")

            #  Verifica se a resposta começa com 'n' ou 'N'.
            if controle_insert.lower().startswith('n'):
                print("Saindo da atualização de dados de PROFESSOR...")
                break
    
    #  Método que cria loop de busca.
    def loopBuscarProfessor(self):
        while True:
            input_do_usuario = input("Insira o nome do PROFESSOR que deseja pesquisar:\n")
            self.buscarProfessor(input_do_usuario)

            #  Solicitando a saída para o usuário
            controle_insert = input("Deseja buscar mais um PROFESSOR? (Digite 'N' ou 'n' para sair: ")

            #  Verifica se a resposta começa com 'n' ou 'N'.
            if controle_insert.lower().startswith('n'):
                print("Saindo da busca de PROFESSOR...")
                break

    #  Método que cria loop de exclusão.
    def loopExcluirProfessor(self):
        while True:
            input_do_usuario = int(input("Digite um ID para a exclusão do PROFESSOR: \n"))

            self.excluirProfessor(input_do_usuario)

            #  Caso a lista esteja vazia, informa o usuário e sai do menu exclusão.
            if self.isProfessorVazia():
                print("\nNão há outros PROFESSORES cadastrados. Saindo de exclusão de PROFESSOR...")
                break

            else:
                #  Solicitando a saída para o usuário
                controle_insert = input("Deseja excluir mais um PROFESSOR? (Digite 'N' ou 'n' para sair: ")

                #  Verifica se a resposta começa com 'n' ou 'N'.
                if controle_insert.lower().startswith('n'):
                    print("Saindo da exclusão de PROFESSOR...")
                    break
