def opcaoUm():
    nomeCliente = input("Digite o nome do cliente: ")
    nomeAnimal = input("Digite o nome do animal: ")
    especieAnimal = input("Digite a especie do animal: ")
    idadeAnimal = input("Digite a idade do animal (anos): ")
    pesoAnimal = input("Digite o peso do animal (Kg): ")
    
    idadeAnimal = int(idadeAnimal)
    pesoAnimal = float(pesoAnimal)
    nomeCliente = nomeCliente.lower()
    especieAnimal = especieAnimal.lower()
    novoCadastro = nomeCliente,nomeAnimal,especieAnimal,idadeAnimal,pesoAnimal

    return novoCadastro


def opcaoDois(clientes):
    if len(clientes) == 0:
        print("Nao ha clientes cadastrados")
    else:
        c = 0
        while c != len(clientes):
            dono = clientes[c][0]
            animal = clientes[c][1]
            especie = clientes[c][2]
            idade = clientes[c][3]
            peso = clientes[c][4]

            print("Dono: {0} ; Animal: {1} ; Especie: {2} ; Idade: {3} ano(s) ; Peso: {4:.2f}Kg".format(dono,animal,especie,idade,peso))
            c+=1


def opcaoTres(clientes):
    if len(clientes) == 0:
        print("Nao ha clientes cadastrados")
    else:
        pesquisa = input("Digite a especie que deseja procurar: ")
        pesquisa = pesquisa.lower()
        finded = False
        for c in clientes:
            if pesquisa == c[2]:
                dono = c[0]
                animal = c[1]
                idade = c[3]
                peso = c[4]
                finded = True
                print("Cliente: {0} ; Animal: {1} ; Idade: {2} ano(s) ; Peso: {3:.2f}Kg".format(dono,animal,idade,peso))
        if finded == False:
            print("Especie nao encontrada")   


def opcaoQuatro(clientes):
    pesquisa = input("Digite o nome do cliente: ")
    pesquisa = pesquisa.lower()
    finded = False
    for c in clientes:
        if pesquisa == c[0]:
            animal = c[1]
            especie = c[2]
            idade = c[3]
            peso = c[4]
            finded = True
            print("Animal: {0} ; Especie: {1} ; Idade: {2} ano(s) ; Peso: {3:.2f}Kg".format(animal,especie,idade,peso))
    if finded == False:
        print("Cliente nao encontrado")


def opcaoCinco(clientes):
    m = 0
    while m == 0:
        pesquisa = input("Digite o nome do cliente: ")  
        pesquisa = pesquisa.lower()

        registros = 0
        for c in clientes:                              
            if pesquisa in c:
                registros+=1
            else:
                continue

        if registros == 0:                              
            print("Cliente nao encontrado")
        else:                                           
            print("{} cliente(s) foram encontrados.".format(registros))  
            for c in clientes:                                     
                cliente = c[0]
                animal = c[1]
                especie = c[2]
                idade = c[3]
                peso = c[4]
                print("Cliente: {0} ; Animal: {1} ; Especie: {2} ; Idade: {3} ano(s) ; Peso: {4:.2f}Kg".format(cliente,animal,especie,idade,peso))
                resposta = input("Deseja excluir esse cliente?(s/n) ")
                if resposta == "s":                               
                    novaTupla = ()                
                    for ind in clientes:            
                        if ind != c:
                            novaTupla += (ind,)
                    cliente = novaTupla
                    break
               
        repetir = input("Deseja excluir outro cliente?(s/n) ")
        if repetir != "s":
            m = 1


                
#PROGRAMA PRINCIPAL
def main1() :
    n = 0
    clientes = ()
    while n == 0:
        print("\
        1 - Inserir um ou mais cliente(s)\n\
        2 - Mostrar a lista de clientes\n\
        3 - Listar clientes de uma espécie\n\
        4 - Listar animais de um cliente\n\
        5 - Remover um ou mais cliente(s)\n\
        6 - Sair")
        opcao = input("Digite uma opção: ")
        opcao = int(opcao)

       
        if opcao == 1:
            um = 1
            while um == 1:
                clientes = clientes + (opcaoUm(),)
                if input("Deseja inserir outro cliente?(s/n): ") == "s":
                    continue
                else:
                    break
                        
        if opcao == 2:
            opcaoDois(clientes)
        elif opcao == 3:
            opcaoTres(clientes)
        elif opcao == 4:
            opcaoQuatro(clientes)
        elif opcao == 5:
            opcaoCinco(clientes)
        elif opcao == 6:
            break
    
    return clientes
            

print(main1())