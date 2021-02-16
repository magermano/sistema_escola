#  Cria a classe CURSO que permite inserir, atualizar,
#  listar, buscar e deletar CURSO no banco de dados.

import psycopg2
from config import config


class Cursos():
    def __init__(self):
        pass

    #  Método para inclusão de CURSO.
    def incluirCurso(self, **kwargs):
        """ Insere um CURSO na tabela Cursos"""
        p_nome = kwargs.get('nome_curso')
        p_periodo = kwargs.get('periodo')
        p_carga_horaria = kwargs.get('carga_horaria')
        p_vagas = kwargs.get('vagas')

        sql = f"""
        INSERT INTO public.Cursos(nome_curso, periodo, carga_horaria, vagas)
            VALUES('{p_nome}', '{p_periodo}', '{p_carga_horaria}', '{p_vagas}') RETURNING id_curso;
        """

        conn = None
        id_curso = None

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
            id_curso = cur.fetchone()[0]
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.close()

            print(f"Curso {p_nome.upper()} inserido com sucesso!")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

        return id_curso
    

    #  Método para atualização de CURSO.
    def atualizarCurso(self, **kwargs):
        """Atualiza os dados de um CURSO"""
        p_id_curso = kwargs.get('id_curso')
        p_nome = kwargs.get('nome_curso')
        p_periodo = kwargs.get('periodo')
        p_carga_horaria = kwargs.get('carga_horaria')
        p_vagas = kwargs.get('vagas')

        sql = f"""
                    UPDATE public.Cursos
                    SET nome_curso = '{p_nome}',
                    periodo = '{p_periodo}',
                    carga_horaria = '{p_carga_horaria}',
                    vagas = '{p_vagas}'
                    WHERE id_curso = '{p_id_curso}';
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


    # Método para exclusão de CURSO.
    def excluirCurso(self, id_curso):
        """Exclui um CURSO a partir de seu ID"""
        conn = None
        deleted_rows = 0
        try:
            sql = f"""
                        DELETE FROM public.Cursos
                        WHERE id_curso = '{id_curso}';
                    """

            params = config(filename=".\database.ini") #  local do arquivo database.ini
            conn = psycopg2.connect(**params)

            cur = conn.cursor()

            cur.execute(sql)

            deleted_rows = cur.rowcount

            conn.commit()

            cur.close()
            return deleted_rows

            # TODO: Mostrar ao usuário que o CURSOS foi excluído com sucesso.

        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    #  Método para listar todos os CURSOS.
    def listarCurso(self):
        """Imprime uma lista com todos os CURSOS"""
        conn = None

        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute("SELECT id_curso, nome_curso, periodo, carga_horaria, vagas FROM Cursos")

            # Imprime o número de CURSOS cadastrados.
            print(f"\nHá {cur.rowcount} cursos(s) cadastrado(s): ")
            row = cur.fetchone()

            while row is not None:
                # TODO: Mostrar idade.
                print(f"\nID: {row[0]}\nCurso: {row[1]}\nPeriodo: {row[2]}\nCarga Horária: {row[3]}\nVagas: {row[4]}\n")
                row = cur.fetchone()
            
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        finally:
            if conn is not None:
                conn.close()
    

    def isCursoVazia(self):
        """Verifica se a lista está vazia"""
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute("SELECT id_curso FROM Cursos")

            #  Retorna booleano para ser usado em uma condicional.
            return (cur.rowcount == 0)

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        finally:
            if conn is not None:
                conn.close()


    #  Metódo que deve ser executado quando a lista estiver vazia.
    def listaCursoVazia(self):
        """Pergunta ao usuário se quer incluir um CURSO. Caso a resposta seja sim, executa o loop de inclusão"""
        opcao_adicionar = input("A lista está vazia. Deseja incluir um novo curso? 'S' ou 's' para incluir: ")
        if opcao_adicionar.lower().startswith('s'):
            self.loopIncluirCurso()
    

    #  Método para buscar CURSO.
    def buscarCurso(self, nome_pesquisado):
        """Busca CURSOS a partir de um nome."""
        conn = None
        
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute("SELECT id_curso, nome_curso, periodo, carga_horaria, vagas FROM Cursos")
            row = cur.fetchone()

            while row is not None:
                if nome_pesquisado in row[1]:
                    print(f"\nID: {row[0]}\nCurso: {row[1]}\nPeriodo: {row[2]}\nCarga Horária: {row[3]}\nVagas: {row[4]}\n")
                row = cur.fetchone()
            
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        finally:
            if conn is not None:
                conn.close()
    
    #  Método que cria loop de inclusão.
    def loopIncluirCurso(self):
        while True:
            self.incluirCurso(nome_curso=input("Digite o nome do Curso:\n"),
                            periodo=input("Digite o periodo do Curso:\n"),
                            carga_horaria=input("Digite a carga horaria do Curso:\n"),
                            vagas=input("Digite a vaga do Curso:\n"))

            #  Solicitando a saída para o usuário    
            controle_insert = input("Deseja incluir mais um curso? Digite 'N' ou 'n' para sair: ")

            #  Verifica se a resposta começa com 'n' ou 'N'.
            if controle_insert.lower().startswith('n'):
                print("Saindo da inclusão de cursos...")
                break

    #  Método que cria loop de atualização.
    def loopAtualizarCurso(self):
        while True:
            input_do_usuario = int(input("Digite um ID para atualizar os dados do CURSO: \n"))

            self.atualizarCurso(nome_curso=input("Digite o nome do CURSO:\n"),
                            periodo=input("Digite o periodo do CURSO\n"),
                            carga_horaria=input("Digite a carga horaria do CURSO:\n"),
                            vagas=input("Digite as vagas do CURSO\n"),
                            id_curso=input_do_usuario)
            
            #  Solicitando a saída para o usuário
            controle_insert = input("Deseja atualizar mais um CURSO? Digite 'N' ou 'n' para sair: ")

            #  Verifica se a resposta começa com 'n' ou 'N'.
            if controle_insert.lower().startswith('n'):
                print("Saindo da atualização de dados de CURSOS...")
                break
    
    #  Método que cria loop de busca.
    def loopBuscarCurso(self):
        while True:
            input_do_usuario = input("Insira o nome do CURSO que deseja pesquisar:\n")
            self.buscarCurso(input_do_usuario)

            #  Solicitando a saída para o usuário
            controle_insert = input("Deseja buscar mais um CURSO? Digite 'N' ou 'n' para sair: ")

            #  Verifica se a resposta começa com 'n' ou 'N'.
            if controle_insert.lower().startswith('n'):
                print("Saindo da busca de CURSO...")
                break

    #  Método que cria loop de exclusão.
    def loopExcluirCurso(self):
        while True:
            input_do_usuario = int(input("Digite um ID para a exclusão do CURSO: \n"))

            self.excluirCurso(input_do_usuario)

            #  Caso a lista esteja vazia, informa o usuário e sai do menu exclusão.
            if self.isCursoVazia():
                print("\nNão há outros CURSOS cadastrados. Saindo de exclusão de CURSOS...")
                break

            else:
                #  Solicitando a saída para o usuário
                controle_insert = input("Deseja excluir mais um CURSO? Digite 'N' ou 'n' para sair: ")

                #  Verifica se a resposta começa com 'n' ou 'N'.
                if controle_insert.lower().startswith('n'):
                    print("Saindo da exclusão de CURSO...")
                    break
