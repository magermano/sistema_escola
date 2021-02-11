#  Cria a classe alunos que permite inserir, atualizar,
#  listar, buscar e deletar alunos no banco de dados.

import psycopg2
from datetime import datetime, date
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
            params = config(filename=".\database.ini") # TODO: POSSÍVEL OTIMIZAÇÃO.
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

            # TODO: Mostrar ao usuário que o aluno foi inserido com sucesso.
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

            params = config(filename=".\database.ini") #local do arquivo database.ini
            conn = psycopg2.connect(**params)

            cur = conn.cursor()

            cur.execute(sql)

            deleted_rows = cur.rowcount

            conn.commit()

            cur.close()
            return deleted_rows

            # TODO: Mostrar ao usuário que o aluno foi excluído com sucesso.

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
            print(f"Há {cur.rowcount} aluno(s) cadastrado(s): ")
            row = cur.fetchone()

            while row is not None:
                # TODO: Mostrar idade.
                print(f"\nID: {row[0]}\nNome: {row[1]}\nCPF: {row[2]}\nData de Nascimento: {row[3].strftime('%d/%m/%Y')}\nTelefone: {row[4]}\n")
                row = cur.fetchone()
            
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        finally:
            if conn is not None:
                conn.close()


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