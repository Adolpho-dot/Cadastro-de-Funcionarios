lista_funcionario =[]
# Contador global para gerar IDs únicos para cada funcionário
id_global = 4726342 

def cadastrar_funcionario():
    global id_global
    id_global += 1
    print(f"ID do funcionário: {id_global}")

    nome = input("Qual o nome do funcionário?:  ")
    setor = input("Qual o setor do funcionário?:  ").upper()
    
    # Garantindo que o salário é um número válido
    while True:
        try:
            salário = float(input("Qual o salário do funcionário?: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número para o salário.")
 # Garantindo que o salário é um número válido
    funcionario = {
        "id": id_global,
        "nome": nome,
        "setor": setor,
        "salário": salário
    }
 # Adiciona o funcionário à lista e exibe uma mensagem de sucesso
    lista_funcionario.append(funcionario.copy())
    print("Funcionário cadastrado com sucesso!")
	
	
	
 
def consultar_funcionario():
    print("-" * 44)
    print("-------- MENU CONSULTAR FUNCIONÁRIO --------")
    opcao = int(input("Escolha a opção desejada: \n1 - Consultar todos os Funcionários\n2 - Consultar Funcionário por id\n3 - Consultar Funcionário(s) por setor\n4 - Retomar\n>>"))
    if opcao == 1:
        for funcionario in lista_funcionario:
            print(funcionario)
            
    elif opcao == 2:
            id_consulta = int(input("Qual o id do funcionário que você deseja consultar?:   "))
            encontrado = False
            for funcionario in lista_funcionario:
                if funcionario["id"] == id_consulta:#Verifica se o id é de um funcionário cadastrado
                    print(funcionario)
                    encontrado = True
                    break
            if not encontrado:
                print("Funcionário não encontrado.")
            
    elif opcao == 3:
        setor = input("Qual o setor do(s) funcionários?: ").upper()
        for funcionario in lista_funcionario:
            if funcionario["setor"] == setor:
                print(funcionario)
    elif opcao == 4:
        return
    else:
        print('Opção inválida')
            
            
def remover_funcionario():
    id_remover = int(input("Digite o id do funcionário que você deseja remover:\n>>"))
    encontrado = False
    
    for r, funcionario in enumerate(lista_funcionario):
        if funcionario["id"] == id_remover:
            lista_funcionario.pop(r)
            print("Funcionário removido com sucesso!")
            encontrado = True
            break
    
    if not encontrado:
        print("Funcionário não encontrado.")

#Programa Principal (main)
print("Bem vindos a empresa do Adolpho Evaristo Corrêa Neto\n") 
    # Exibe o menu principal e solicita a escolha do usuário
while True:
    opcao = int(input("-------------- Menu Principal -------------- \nEsolha a opção desejada:\n1 - Cadastrar Funcionários\n2 - Consultar Funcionário(s)\n3 - Remover Funcionário\n4 - Sair\n>>"))     
    if opcao == 1:
            cadastrar_funcionario()
    elif opcao == 2:
            consultar_funcionario()
    elif opcao == 3:
            remover_funcionario()
    elif opcao == 4:
            print("Encerrando o programa...")
            break
    else:
        print('Opção inválida')
