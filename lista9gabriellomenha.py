def questao1(list,opcao='media'):
    resultado = 0
    if opcao == 'media':
        num = 0
        den = len(list)
        for n in list:
            num+=n
        media = num/den
        resultado = media

    elif opcao == 'mediana':
        if len(list)%2 == 1:
            ind = int((len(list)/2) - 0.5)
            resultado = list[ind]

        elif len(list)%2 == 0:
            ind1 = len(list)/2 -1
            ind2 = len(list)/2
            resultado = (ind1+ind2)/2

    elif opcao == 'variancia':
        #Cálculo média
        num = 0
        for n in list:
            num+=n
        media = num/len(list)
        #Somatório
        soma = 0
        for n in list:
            soma += (n - media)**2
        #Variancia
        resultado = soma/len(list)    
        return resultado
            
    else :
        return -1

    return resultado
#print(questao1(([-1.1, -0.5, 2.3])))


def questao2(num,den):
    lista = []
    for n in range(len(num)):
        try:
            num[n] = float(num[n])
            den[n] = float(den[n])

        except ValueError:
            return -1
            
        except ZeroDivisionError:
            lista.append('inf')

        except IndexError:
            break
        else:
            razao = num[n]/den[n]
            lista.append(razao)
        
    return lista
#print(questao2([1, 2, 5, 6, 3, 2], [2, 5, 8]))

def questao3(produtos):
    nome = input('Digite o nome do produto: ')
#Inserindo nome e verificando se esta cadastrado
    try:        
        teste = produtos[nome]

        #Produto não cadastrado, iniciando inserção de dados
    except KeyError:                
        print('Inserindo um novo produto')

        preco = 1
        while preco == 1:
            try:                                   #Inserindo preco do produto
                novoPreco = input('Digite o  preço deste produto: ')
                novoPreco = float(novoPreco)
                if novoPreco<=0 or novoPreco>=100: #Verifivação de formato de dado
                    raise ValueError
            except ValueError:  
                print(('Valor invalido, digite um valor maior que 0 e menor que 100.'))
            else:
                preco = 0
                produtos[nome] = [novoPreco,]      #Atribuindo novo preço

                                                   #Inserindo novo Peso
        peso = 1
        while peso == 1:
            try:
                novoPeso = input('Digite o peso: ')
                novoPeso = float(novoPeso)
                if novoPeso < 0:                   #Verificação de formato de dado
                    raise ValueError
            except ValueError:
                print('Valor inválido, digite um númeor nao negativo.')

                                                   #Calculoando valor preco/peso
            else:                                  
                try:
                    precoPorGrama = novoPreco/novoPeso
                except ZeroDivisionError:          #Verificação de valor de dado
                    print('O peso não pode ser igual a zero')
                else:
                    peso = 0
        produtos[nome].append(novoPeso)             #Adicionando dados ao registro
        produtos[nome].append(precoPorGrama)

    #Produto já cadastrado, iniciando alteração de dados(mesmo processo)
    else:
        print(f'Modificando produto {nome}.')
        print(f'Valores cadastrados:\
 preco={produtos[nome][0]}, peso={produtos[nome][1]}, preco/grama={produtos[nome][2]}.')
        preco = 1
        while preco == 1:
            try:
                novoPreco = input('Digite o  preço deste produto: ')
                novoPreco = float(novoPreco)
                if novoPreco<=0 or novoPreco>=100:
                    raise ValueError
            except ValueError:
                print(('Valor invalido, digite um valor maior que 0 e menor que 100.'))
            else:
                preco = 0
                produtos[nome][0] = novoPreco
        peso = 1
        while peso == 1:
            try:
                novoPeso = input('Digite o peso: ')
                novoPeso = float(novoPeso)
                if novoPeso < 0:
                    raise ValueError
            except ValueError:
                print('Valor inválido, digite um númeor nao negativo.')
            else:
                try:
                    precoPorGrama = novoPreco/novoPeso
                except ZeroDivisionError:
                    print('O peso não pode ser igual a zero')
                else:
                    peso = 0
        produtos[nome][1] = novoPeso
        produtos[nome][2] = precoPorGrama

    #Imprimindo registro final 
    finally:
        return produtos   

#print(questao3({'Cookie Bauducco':[3.79, 100, 0.379], 'Oreo':[3.49, 90, 0.038778]}))
        