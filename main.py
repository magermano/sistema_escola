'''
Programa de cadastro/exclusão/visualização de cursos/alunos/professores de uma escola.
​
Feito por: Beatriz Ambrósio
           Matheus Germano Dos Santos
           Renato Uccella
​
Facilitador: Jeferson Leal 
​
Campinas Tech Talents 2021
'''

#Programa Principal do Sistema de Matrícula

#  Importa o módulo
import sys

#  Do arquivo importa a classe
from alunos import Alunos
from professores import Professores
from cursos import Cursos
from matriculas import Matriculas

#  Inicialização de variáveis.
menu_principal = ["0-) Sair \n",
                  "1-) Alunos",
                  "2-) Professores",
                  "3-) Cursos",
                  "4-) Matriculas"]

menu_aluno     = ["0-) Voltar ao Menu Principal \n",
                  "1-) Ver lista de alunos",
                  "2-) Incluir um novo aluno",
                  "3-) Atualizar dados de um aluno",
                  "4-) Excluir um aluno existente",
                  "5-) Buscar um aluno"]

menu_professor = ["0-) Voltar ao Menu Principal \n",
                  "1-) Ver lista de professores",
                  "2-) Incluir um novo professor",
                  "3-) Atualizar dados de um professor",
                  "4-) Excluir um professor existente",
                  "5-) Buscar um professor"]

menu_curso     = ["0-) Voltar ao Menu Principal \n",
                  "1-) Ver lista de cursos",
                  "2-) Incluir um novo curso",
                  "3-) Atualizar dados de um curso",
                  "4-) Excluir um curso existente",
                  "5-) Buscar um curso"]

menu_matricula  = ["0-) Voltar ao Menu Principal \n",
                  "1-) Ver lista de matriculas de Alunos",
                  "2-) Incluir uma nova matricula de Aluno",
                  "3-) Ver lista de matriculas de Professor",
                  "4-) Incluir uma nova matricula de Professor",
                  "5-) Imprimir relação Matrícula-Aluno-Professor-Curso"
                  ]


#  Pede o nome do usuário e dá mensagem de boas vindas.
print("\n-    Sistema de Matricula      -\n")
nome_login = input("Olá! Entre com o nome de usuário:\n")
print(f"\nSeja bem-vindo, {nome_login}! Esse é o menu de navegação:")

#  Loop principal.
while True:
    print("\n-        MENU PRINCIPAL       - ")
    #  Loop para mostrar a lista de opções.
    for opcao in menu_principal:
        print(opcao)
    # TODO: validação de seleção de menu.
    #  Pede para o usuário entrar com a opção desejada.
    opcao_menu = int(input("\nEscolha uma opção: "))

    #  Condicionais para controlar a navegação do programa.
    #  Sai do programa.
    if opcao_menu == 0:
        print("Você saiu do sistema.")
        sys.exit()
    

    #  Imprime opções para Alunos.
    elif opcao_menu == 1:
        #  Instancia objeto da classe Alunos.
        aluno = Alunos()

        #  Loop Alunos.
        while True:
            print("\n-        MENU ALUNOS       - ")
            #  Loop para mostrar a lista de opções.
            for opcao in menu_aluno:
                print(opcao)
            #  Pede para o usuário entrar com a opção desejada.
            opcao_aluno = int(input("Escolha uma opção: \n"))
            
            #  Sai do Menu Alunos e retorna ao menu principal.
            if opcao_aluno == 0:
                print("Você saiu do MENU ALUNOS.")
                break

            #  Imprimir lista de alunos.
            elif opcao_aluno == 1:
                if aluno.isVazia():
                    aluno.listaVazia()
                else:
                    print("\n-        LISTA DE ALUNOS       - ")
                    aluno.listar()
                    #  Pede ao usuário que aperte Enter para prosseguir.
                    input("Aperte ENTER para continuar.")

            #  Incluir um novo aluno.
            elif opcao_aluno == 2: 
                aluno.loopIncluir()
            
            #  Atualizar dados de um aluno.
            elif opcao_aluno == 3:
                # Caso a lista esteja vazia, o método retorna True e o método listaVazia() é executado.
                # Caso contrário, apenas faz a listagem.
                if aluno.isVazia():
                    aluno.listaVazia()
                else:
                    aluno.listar()
                    aluno.loopAtualizar()

            #  Excluir um aluno existente.
            elif opcao_aluno == 4:
                if aluno.isVazia():
                    print("Não há alunos cadastrados. Saindo de exclusão de alunos.")
                else:
                    aluno.listar()
                    aluno.loopExcluir()
            
            # Buscar aluno a partir de um nome.
            elif opcao_aluno == 5:
                if aluno.isVazia():
                    print("Não há alunos cadastrados. Saindo de busca de alunos.")
                else:
                    aluno.loopBuscar()

########################################################################################################################

    #  Imprime opções para Professores
    elif opcao_menu == 2:
        #  Instancia objeto da classe Professores.
        professor = Professores()

        #  Loop Professores.
        while True:
            print("\n-        MENU PROFESSORES       - ")
            #  Loop para mostrar a lista de opções.
            for opcao in menu_professor:
                print(opcao)
            #  Pede para o usuário entrar com a opção desejada.
            opcao_professor = int(input("Escolha uma opção: \n"))
            
            #  Sai do Menu Professores e retorna ao Menu Principal.
            if opcao_professor == 0:
                print("Você saiu do MENU PROFESSORES.")
                break

            #  Imprimir lista de professores.
            elif opcao_professor == 1:
                if professor.isProfessorVazia():
                    professor.listaProfessorVazia()
                else:
                    print("\n-        LISTA DE PROFESSORES       - ")
                    professor.listarProfessor()
                    #  Pede ao usuário que aperte Enter para prosseguir.
                    input("Aperte ENTER para continuar.")

            #  Incluir um novo professor
            elif opcao_professor == 2: 
                professor.loopIncluirProfessor()
            
            #  Atualizar dados de um professor
            elif opcao_professor == 3:
                # Caso a lista esteja vazia, o método retorna True e o método listaVazia() é executado.
                # Caso contrário, apenas faz a listagem.
                if professor.isProfessorVazia():
                    professor.listaProfessorVazia()
                else:
                    professor.listarProfessor()
                    professor.loopAtualizarProfessor()

            #  Excluir um professor existente.
            elif opcao_professor == 4:
                if professor.isProfessorVazia():
                    print("Não há professores cadastrados. Saindo de exclusão de professores.")
                else:
                    professor.listarProfessor()
                    professor.loopExcluirProfessor()
            
            # Buscar professor a partir de um nome.
            elif opcao_professor == 5:
                if professor.isProfessorVazia():
                    print("Não há professores cadastrados. Saindo de busca de professores.")
                else:
                    professor.loopBuscarProfessor()

    #######################################################################################################

    #  Imprime opções para CURSOS.
    elif opcao_menu == 3:
        #  Instancia objeto da classe Cursos.
        curso = Cursos()

        #  Loop Cursos.
        while True:
            print("\n-        MENU CURSOS       - ")
            #  Loop para mostrar a lista de opções.
            for opcao in menu_curso:
                print(opcao)
            #  Pede para o usuário entrar com a opção desejada.
            opcao_curso = int(input("Escolha uma opção: \n"))
            
            #  Sai do Menu Cursos e retorna ao Menu Principal.
            if opcao_curso == 0:
                print("Você saiu do MENU CURSOS.")
                break

            #  Imprimir lista de cursos.
            elif opcao_curso == 1:
                if curso.isCursoVazia():
                    curso.listaCursoVazia()
                else:
                    print("\n-        LISTA DE CURSOS       - ")
                    curso.listarCurso()
                    #  Pede ao usuário que aperte Enter para prosseguir.
                    input("Aperte ENTER para continuar.")

            #  Incluir um novo curso.
            elif opcao_curso == 2: 
                curso.loopIncluirCurso()
            
            #  Atualizar dados de um curso.
            elif opcao_curso == 3:
                # Caso a lista esteja vazia, o método retorna True e o método listaCursoVazia() é executado.
                # Caso contrário, apenas faz a listagem.
                if curso.isCursoVazia():
                    curso.listaCursoVazia()
                else:
                    curso.listarCurso()
                    curso.loopAtualizarCurso()

            #  Excluir um curso existente.
            elif opcao_curso == 4:
                if curso.isCursoVazia():
                    print("Não há cursos cadastrados.Saindo de exclusão de cursos.")
                else:
                    curso.listarCurso()
                    curso.loopExcluirCurso()
            
            # Buscar curso a partir de um nome.
            elif opcao_curso == 5:
                if curso.isCursoVazia():
                    print("Não há CURSOS cadastrados. Saindo de busca de CURSOS.")
                else:
                    curso.loopBuscarCurso()

    ##############################################################

    elif opcao_menu == 4:
        #  Instancia objeto da classe Matrícula.
        matricula = Matriculas()

        #  Loop Matrículas.
        while True:
            print("\n-        MENU MATRÍCULAS       - ")
            #  Loop para mostrar a lista de opções.
            for opcao in menu_matricula:
                print(opcao)
            #  Pede para o usuário entrar com a opção desejada.
            opcao_matricula = int(input("Escolha uma opção: \n"))
            
            #  Sai do Menu Matrículas e retorna ao Menu Principal.
            if opcao_matricula == 0:
                print("Você saiu do MENU MATRÍCULAS.")
                break

            #  Imprimir lista de matrículas de alunos.
            elif opcao_matricula == 1:
                if matricula.isMatriculaVazia():
                    matricula.listaMatriculaVazia()
                else:
                    print("\n-        LISTA DE MATRÍCULAS ALUNOS      - ")
                    matricula.listarJoinMatricula()
                    #  Pede ao usuário que aperte Enter para prosseguir.
                    input("Aperte ENTER para continuar.")

            #  Incluir uma nova matrícula de aluno.
            elif opcao_matricula == 2:                   
                    matricula.loopIncluirMatriculaAluno()

            #  Imprimir lista com os professores que lecionam tal matéria.
            elif opcao_matricula == 3:
                if matricula.isMatriculaProfessorVazia():
                    matricula.listaMatriculaProfessorVazia()
                else:
                    print("\n-        LISTA DE MATRÍCULAS PROFESSORES      - ")
                    matricula.listarJoinMatriculaProfessor()
                    #  Pede ao usuário que aperte Enter para prosseguir.
                    input("Aperte ENTER para continuar.")

            #  Incluir um novo professor pra lecionar tal matéria
            elif opcao_matricula == 4:
                    matricula.loopIncluirMatriculaProfessor()

            elif opcao_matricula == 5:
                print("\n-        LISTA DE MATRÍCULAS-ALUNOS-PROFESSORES-CURSOS      - ")
                matricula.listarJoinMatriculaProfessorAluno()
                #  Pede ao usuário que aperte Enter para prosseguir.
                input("Aperte ENTER para continuar.")