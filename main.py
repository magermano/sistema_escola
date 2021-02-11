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
import sys
import time
from alunos import Alunos
from professores import Professores

#  Inicialização de variáveis e objetos
lista_opcoes = [   "0-) Sair \n"
                  ,"1-) Ver lista de alunos"
                  ,"2-) Incluir um novo aluno"
                  ,"3-) Atualizar dados de um aluno"
                  ,"4-) Excluir um aluno existente"
                  ,"5-) Buscar um aluno"
                  ,"6-) Ver lista de professores"
                  ,"7-) Incluir um novo professor"
                  ,"8-) Atualizar dados de um professor"
                  ,"9-) Excluir um professor existente"
                  ,"10-) Buscar um professor"]

#  Iteração com o usuário e dar as boas vindas
nome_login = input("Olá! Por favor entre com o nome de usuário...\n")

#  Loop para manter na memória
while True:
    #  Mostrar as boas vindas e as opções
    print(f"\nOlá! Seja bem-vinde {nome_login}! Escolha uma opção:")
    for opcao in lista_opcoes:
        print(opcao)
    opcao_selecionada = int(input("Escolha uma opção \n"))
    #  Condicionais para controlar a navegação do programa
    if opcao_selecionada == 0: #Sai do programa
        print("Você saiu do sistema.")
        sys.exit()
    

    #  Imprimir lista de alunos
    elif opcao_selecionada == 1:
        aluno = Alunos()
        aluno.listar()


    #  Incluir um novo aluno
    elif opcao_selecionada == 2: 
        while True:
            nome_aluno = input("Digite o nome do Aluno:\n")
            cpf_aluno = input("Digite o CPF do Aluno:\n")
            data_nascimento_aluno = input("Digite a data de nascimento do Aluno:\n")
            telefone_aluno = input("Digite o telefone do Aluno:\n")

            aluno = Alunos()

            aluno.incluir(nome=nome_aluno,
                            cpf=cpf_aluno,
                            data_nasc=data_nascimento_aluno,
                            telefone=telefone_aluno)
            
            #  Solicitando a saída para o usuário    
            controle_insert = input("Deseja incluir mais um aluno? (Digite 'n' ou 'N' para sair) \n")
            if len(controle_insert) == 1:
                if controle_insert == "n" or controle_insert == "N" or controle_insert == "S" or controle_insert == "s":
                    if controle_insert.upper() == "N":
                        print("Saíndo da inclusão de alunos...")
                        break
    

    #  Atualizar dados de um aluno
    elif opcao_selecionada == 3:
        aluno = Alunos()
        aluno.listar()
        input_do_usuario = int(input("Digite um ID para atualizar os dados do aluno\n"))

        nome_aluno = input("Digite o nome do Aluno:\n")
        cpf_aluno = input("Digite o CPF do Aluno\n")
        data_nascimento_aluno = input("Digite a data de nascimento do Aluno:\n")
        telefone_aluno = input("Digite o telefone do Aluno\n")

        aluno.atualizar(nome=nome_aluno,
                        cpf=cpf_aluno,
                        data_nasc=data_nascimento_aluno,
                        telefone=telefone_aluno,
                        id_aluno=input_do_usuario)


    #  Excluir um aluno existente.
    elif opcao_selecionada == 4:
        #TODO: fazer o loop de exclusão e verificação de input.
        aluno = Alunos()
        aluno.listar()
        input_do_usuario = int(input("Digite um ID para a exclusão do aluno \n"))
        
        aluno.excluir(input_do_usuario)
        aluno.listar()
    

    # Buscar aluno a partir de um nome.
    elif opcao_selecionada == 5:
        input_do_usuario = input("Insira o nome do aluno que deseja pesquisar:\n")

        aluno = Alunos()
        aluno.buscarAluno(input_do_usuario)
        #TODO: fazer o loop e perguntar se quer pesquisar novamente;

    #####################################################################################################################

     #  Imprimir lista de professor
    elif opcao_selecionada == 6:
        professor = Professores()
        professor.listarProfessor()


    #  Incluir um novo professor
    elif opcao_selecionada == 7: 
        while True:
            nome_professor = input("Digite o nome do Professor:\n")
            cpf_professor = input("Digite o CPF do Professor:\n")
            data_nascimento_professor = input("Digite a data de nascimento do Professor:\n")
            telefone_professor = input("Digite o telefone do Professor:\n")
            formacao = input("Digite a formação do Professor:\n")

            professor = Professores()

            professor.incluirProfessor(nome=nome_professor,
                            cpf=cpf_professor,
                            data_nasc=data_nascimento_professor,
                            telefone=telefone_professor,
                            formacao = formacao)
            
            #  Solicitando a saída para o usuário    
            controle_insert = input("Deseja incluir mais um professor? (Digite 'n' ou 'N' para sair) \n")
            if len(controle_insert) == 1:
                if controle_insert == "n" or controle_insert == "N" or controle_insert == "S" or controle_insert == "s":
                    if controle_insert.upper() == "N":
                        print("Saindo da inclusão de professor...")
                        break
    

    #  Atualizar dados de um professor
    elif opcao_selecionada == 8:
        professor = Professores()
        professor.listarProfessor()
        input_do_usuario = int(input("Digite um ID para atualizar os dados do professor\n"))

        nome_professor = input("Digite o nome do Professor:\n")
        cpf_professor = input("Digite o CPF do Professor:\n")
        data_nascimento_professor = input("Digite a data de nascimento do Professor:\n")
        telefone_professor = input("Digite o telefone do Professor:\n")
        formacao = input("Digite a formação do Professor:\n")

        professor.atualizarProfessor(nome=nome_professor,
                        cpf=cpf_professor,
                        data_nasc=data_nascimento_professor,
                        telefone=telefone_professor,
                        formacao = formacao,
                        id_professor=input_do_usuario,)


    #  Excluir um professor existente.
    elif opcao_selecionada == 9:
        #TODO: fazer o loop de exclusão e verificação de input.
        professor = Professores()
        professor.listarProfessor()
        input_do_usuario = int(input("Digite um ID para a exclusão do professor: \n"))
        
        professor.excluirProfessor(input_do_usuario)
        professor.listarProfessor()
    

    # Buscar professor a partir de um nome.
    elif opcao_selecionada == 10:
        input_do_usuario = input("Insira o nome do professor que deseja pesquisar:\n")

        professor = Professores()
        professor.buscarProfessor(input_do_usuario)

        #TODO: fazer o loop e perguntar se quer pesquisar novamente;

    #######################################################################################################

    """PARTE DO CURSO"""

    time.sleep(1)