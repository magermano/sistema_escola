#  Cria a classe alunos que permite inserir, atualizar,
#  listar, buscar e deletar professor no banco de dados.

import psycopg2
from datetime import datetime, date
from config import config


class Professores():
    def __init__(self):
        pass

    #  Método para inclusão de professor.
    def incluirProfessor(self, **kwargs):
        """ Insere um professor na tabela Professores"""
        p_nome = kwargs.get('nome')
        p_cpf = kwargs.get('cpf')
        p_data_nasc = kwargs.get('data_nasc')
        p_telefone = kwargs.get('telefone')
        p_formacao = kwargs.get('formacao')

        sql = f"""
        INSERT INTO public.Professores(nome_prof, cpf_prof, data_nasc_prof, telefone, formacao)
            VALUES('{p_nome}', '{p_cpf}', '{p_data_nasc}', '{p_telefone}','{p_formacao}') RETURNING id_professor;
        """

        conn = None
        id_professor = None

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
    

    #  Método para atualização de professor.
    def atualizarProfessor(self, **kwargs):
        """Atualiza os dados de um professor"""
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


    # Método para exclusão de professor.
    def excluirProfessor(self, id_professor):
        """Exclui um aluno a partir de seu ID"""
        conn = None
        deleted_rows = 0
        try:
            sql = f"""
                        DELETE FROM public.Professores
                        WHERE id_professor = '{id_professor}';
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

    #  Método para listar todos os professores.
    def listarProfessor(self):
        """Imprime uma lista com todos os professores"""
        conn = None
        
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute("SELECT id_professor, nome_prof, cpf_prof, data_nasc_prof, telefone, formacao FROM Professores")
            print(f"Há {cur.rowcount} professor(es) cadastrado(s): ")
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


    #  Método para buscar professor.
    def buscarProfessor(self, nome_pesquisado):
        """Busca professor a partir de um nome."""
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