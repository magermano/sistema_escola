#Cria a classe MATRICULAS que permite matricular alunos e professores em cursos.

import psycopg2
from config import config

from alunos import Alunos
from professores import Professores
from cursos import Cursos


class Matriculas():
    def __init__(self):
        pass

    #  Método para inclusão de matricula.
    def incluirMatriculaAluno(self, **kwargs):
        """ Insere um aluno na tabela Alunos"""
        p_id_aluno = kwargs.get('id_aluno')
        p_id_curso = kwargs.get('id_curso')
        

        sql = f"""
        INSERT INTO public.Matriculas (id_aluno, id_curso)
            VALUES({p_id_aluno}, {p_id_curso}) RETURNING id_matricula;
        """

        conn = None
        id_matricula = None

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
            id_matricula = cur.fetchone()[0]
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.close()

            #TODO: Mostrar ao usuário que o aluno foi inserido com sucesso.
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

        return id_matricula

    #  Faz um join nas tabelas pra poder mostrar pro usuário o nome curso e o nome aluno que está matriculado.
    def listarJoinMatricula(self):
        """Imprime uma lista com todos as matrículas"""
        conn = None

        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute(f"""
                        SELECT public.matriculas.id_aluno,
						id_matricula,
						nome_aluno,
						nome_curso
						from public.matriculas
						INNER JOIN public.alunos 
							on public.alunos.id_aluno = public.matriculas.id_aluno
						INNER JOIN public.cursos
							on public.cursos.id_curso = public.matriculas.id_curso;""")

            # Imprime o número de alunos cadastrados.
            print(f"\nHá {cur.rowcount} mastrícula(s) cadastrada(s): ")
            row = cur.fetchone()

            while row is not None:
                print(f"ID Aluno: {row[0]}\nID Matrícula: {row[1]}\nNome do Aluno: {row[2]}\nCurso : {row[3]}\n")
                row = cur.fetchone()
            
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        finally:
            if conn is not None:
                conn.close() 


    def isMatriculaVazia(self):
        """Verifica se a lista está vazia"""
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute("SELECT id_matricula FROM Matriculas")

            #  Retorna booleano para ser usado em uma condicional.
            return (cur.rowcount == 0)

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        finally:
            if conn is not None:
                conn.close()


    #  Metódo que deve ser executado quando a lista estiver vazia.
    def listaMatriculaVazia(self):
        """Pergunta ao usuário se quer incluir uma MATRÍCULA. Caso a resposta seja sim, executa o loop de inclusão"""
        opcao_adicionar = input("A lista está vazia. Deseja incluir uma nova matrícula? 'S' ou 's' para incluir: ")
        if opcao_adicionar.lower().startswith('s'):
            self.loopIncluirMatriculaAluno()

    ##

    #  Inclui professores lecionando tais cursos, não exibe
    def incluirMatriculaProfessor(self, **kwargs):
        """ Insere um aluno na tabela Alunos"""
        p_id_professor = kwargs.get('id_professor')
        p_id_curso = kwargs.get('id_curso')
        

        sql = f"""
        INSERT INTO public.professores_cursos (id_professor, id_curso)
            VALUES({p_id_professor}, {p_id_curso})
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
            #id_professor = cur.fetchone()[0]
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.close()

            #TODO: Mostrar ao usuário que o aluno foi inserido com sucesso.
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

        return id_professor

    #

    #Faz um Join na tabela pra poder mostrar o id do curso, o professor que leciona e o curso que ele leciona
    #exibe pro usuário
    def listarJoinMatriculaProfessor(self):
        """Imprime uma lista com todas as matrículas e professores."""
        conn = None

        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute(f"""
                        SELECT public.professores_cursos.id_professor
						id_curso,
						nome_prof,
						nome_curso
						from public.professores_cursos
						INNER JOIN public.cursos
							on public.cursos.id_curso = public.professores_cursos.id_curso
						INNER JOIN public.professores
							ON PUBLIC.professores.id_professor = public.professores_cursos.id_professor;""")

            # Imprime o número de matrículas-professores cadastrados.
            print(f"\nHá {cur.rowcount} professores(s) cadastrado(s): ")
            row = cur.fetchone()

            while row is not None:
                print(f"ID Curso: {row[0]}\nNome professor: {row[1]}\nNome do Curso: {row[2]}\n")
                row = cur.fetchone()
            
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        finally:
            if conn is not None:
                conn.close()

    def isMatriculaProfessorVazia(self):
        """Verifica se a lista está vazia"""
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute("SELECT id_professor, id_curso FROM public.professores_cursos")

            #  Retorna booleano para ser usado em uma condicional.
            return (cur.rowcount == 0)

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        finally:
            if conn is not None:
                conn.close()


    def listaMatriculaProfessorVazia(self):
        """Pergunta ao usuário se quer incluir uma MATRÍCULA-PROFESSOR. Caso a resposta seja sim, executa o loop de inclusão"""
        opcao_adicionar = input("A lista está vazia. Deseja incluir uma nova matrícula? 'S' ou 's' para incluir: ")
        if opcao_adicionar.lower().startswith('s'):
            self.loopIncluirMatriculaProfessor()


    def loopIncluirMatriculaAluno(self):
        while True:
            aluno = Alunos()
            curso = Cursos()
            #  Pergunta se o usuário deseja visualizar os alunos cadastrados,
            #  pois pode não saber o ID de cabeça.
            insert_visualizar_alunos = input("Deseja visualizar os alunos cadastrados? Digite 'S' ou 's' para visualizar: ")
            if insert_visualizar_alunos.lower().startswith('s'):
                print("\n-        LISTA DE ALUNOS       - ")
                aluno.listar()
                #  Pede ao usuário que aperte Enter para prosseguir.
                input("Aperte ENTER para continuar.")

            #  Pergunta se o usuário deseja visualizar os cursos cadastrados,
            #  pois pode não saber o ID de cabeça.
            insert_visualizar_cursos = input("Deseja visualizar os cursos cadastrados? Digite 'S' ou 's' para visualizar: ")
            if insert_visualizar_cursos.lower().startswith('s'):
                print("\n-        LISTA DE CURSOS       - ")
                curso.listarCurso()
                #  Pede ao usuário que aperte Enter para prosseguir.
                input("Aperte ENTER para continuar.")

            #  Chama o método de inclusão de matrícula de aluno,
            #  pedindo ao usuário que insira os argumentos.
            self.incluirMatriculaAluno(id_aluno=input("Digite o ID do Aluno:\n"),
                                        id_curso=input("Digite o ID do Curso:\n"))

            #  Solicitando a saída para o usuário    
            controle_insert = input("Deseja incluir mais uma matrícula? Digite 'N' ou 'n' para sair: ")

            #  Verifica se a resposta começa com 'n' ou 'N'.
            if controle_insert.lower().startswith('n'):
                print("Saindo da inclusão de matrículas...")
                break


    def loopIncluirMatriculaProfessor(self):
        while True:
            professor = Professores()
            curso = Cursos()
            #  Pergunta se o usuário deseja visualizar os professores cadastrados,
            #  pois pode não saber o ID de cabeça.
            insert_visualizar_professores = input("Deseja visualizar os PROFESSORES cadastrados? Digite 'S' ou 's' para visualizar: ")
            if insert_visualizar_professores.lower().startswith('s'):
                print("\n-        LISTA DE PROFESSORES       - ")
                professor.listarProfessor()
                #  Pede ao usuário que aperte Enter para prosseguir.
                input("Aperte ENTER para continuar.")

            #  Pergunta se o usuário deseja visualizar os cursos cadastrados,
            #  pois pode não saber o ID de cabeça.
            insert_visualizar_cursos = input("Deseja visualizar os CURSOS cadastrados? Digite 'S' ou 's' para visualizar: ")
            if insert_visualizar_cursos.lower().startswith('s'):
                print("\n-        LISTA DE CURSOS       - ")
                curso.listarCurso()
                #  Pede ao usuário que aperte Enter para prosseguir.
                input("Aperte ENTER para continuar.")

            #  Chama o método de inclusão de matrícula de professor,
            #  pedindo ao usuário que insira os argumentos.            
            self.incluirMatriculaProfessor(id_professor=input("Digite o ID do Professor:\n"),
                                        id_curso=input("Digite o ID do Curso:\n"))

            #  Solicitando a saída para o usuário    
            controle_insert = input("Deseja incluir mais uma matrícula? Digite 'N' ou 'n' para sair: ")

            #  Verifica se a resposta começa com 'n' ou 'N'.
            if controle_insert.lower().startswith('n'):
                print("Saindo da inclusão de matrículas...")
                break


    # ###### 

    def listarJoinMatriculaProfessorAluno(self):
        """Imprime uma lista com dados do curso, matrícula, nome do aluno e nome do professor."""
        conn = None

        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute(f"""
                        SELECT public.matriculas.id_matricula,
                        nome_aluno,
                        nome_curso,
                        nome_prof
                        from public.matriculas

                        INNER JOIN public.alunos 
                            on public.alunos.id_aluno = public.matriculas.id_aluno
                        
                        INNER JOIN public.cursos
                            on public.cursos.id_curso = public.matriculas.id_curso

                        INNER JOIN public.professores_cursos
                            on public.professores_cursos.id_curso = public.cursos.id_curso

                        INNER JOIN public.professores
                            ON PUBLIC.PROFESSORES.id_professor = public.professores_cursos.id_professor;""")

            # Imprime o número de matrículas cadastradas.
            print(f"\nHá {cur.rowcount} relação(ões): ")
            row = cur.fetchone()

            while row is not None:
                print(f"ID Matrícula: {row[0]}\nAluno: {row[1]}\nCurso: {row[2]}\nProfessor: {row[3]}\n")
                row = cur.fetchone()
            
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        finally:
            if conn is not None:
                conn.close()

if __name__ == '__main__':
    matricula = Matriculas()
    matricula.listarJoinMatriculaProfessorAluno()