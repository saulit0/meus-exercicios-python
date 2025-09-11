alunos = []

def menu():
    print("\n------ MENU ------")
    print("1. Cadastrar Novo Aluno")
    print("2. Listar Alunos Cadastrados")
    print("3. Buscar Aluno por Matrícula")
    print("4. Sair")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        print("\n- Cadastro de Novo Aluno-")
        nome = input("Nome do aluno: ")
        curso = input("Curso: ")

        try:
            matricula = int(input("Matrícula (apenas números): "))
        except:
            print("Matrícula inválida. Digite apenas números.")
            continue

        if any(aluno["matricula"] == matricula for aluno in alunos):
            print("Matrícula já cadastrada.")
            continue

        aluno = {
            "nome": nome,
            "matricula": matricula,
            "curso": curso
        }
        alunos.append(aluno)
        print("Aluno cadastrado com sucesso.")

    elif opcao == '2':
        print("\n- Lista de Alunos Cadastrados -")
        if not alunos:
            print("Nenhum aluno cadastrado.")
        else:
            for i, aluno in enumerate(alunos, start=1):
                print(f"{i}. Nome: {aluno['nome']} | Matrícula: {aluno['matricula']} | Curso: {aluno['curso']}")

    elif opcao == '3':
        print("\n- Buscar Aluno por Matrícula -")
        try:
            busca_matricula = int(input("Digite a matrícula do aluno: "))
        except:
            print("Matrícula inválida. Digite apenas números.")
            continue

        encontrado = False
        for aluno in alunos:
            if aluno["matricula"] == busca_matricula:
                print(f"Aluno encontrado: Nome: {aluno['nome']} | Curso: {aluno['curso']}")
                encontrado = True
                break

        if not encontrado:
            print("Aluno não encontrado.")

    elif opcao == '4':
        print("Encerrado")
        break

    else:
        print("Opção inválida. Digite outra opção.")