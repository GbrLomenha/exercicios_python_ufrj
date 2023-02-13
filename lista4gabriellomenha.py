def funcao1(list0,n):
    ind = 0
    lista = []
    x = len(list0)
    while ind < x:
        if list0[ind]%n ==0:
            lista.append(list0[ind])       
            ind+=1
        else:
            ind+=1
    return lista

print(funcao1([-6, -2, 3, 1, 9, 12], 3))








def funcao2(list1,list2):
    x = len(list1)
    ind1 = 0
    ind2 = -1
    lista = []
    while ind1<x:
        lista.append(list1[ind1])
        lista.append(list2[ind2])
        ind1+=1
        ind2+=-1
    return lista
#print(funcao2(['a', -1, 12.5], [52, 'teste', 10.75]))










def funcao3(list1,list2,list3):
    x = len(list1)
    ind1 = 0
    ind2 = 0
    ind3 = 0
    lista = []
    while ind1 < x:
        operacao = (list1[ind1]+list2[ind2])*list3[ind3]
        lista.append(operacao)
        ind1+=1
        ind2+=1
        ind3+=1
    return lista
#print(funcao3([1, 10, 2, 4], [3, 5, 4, 2], [0.5, 0.2, 2, 1]))









def funcao4(list):
    n = len(list)
    indi = 0
    ind = 0
    operacao = 0
    while indi < n:
        while ind < n:
            operacao = operacao + list[indi]*list[ind] 
            ind+=1      
            
        indi+=1
        ind = indi
        
    return operacao        
#print(funcao4([-7, -4, -3, -1, 2, 5, 8, 9]))








def funcao5(list):
    ind = 0
    indi = -1
    lista = True
    x = len(list)
    soma = list[ind]+list[indi]
    while ind < x-1:
        ind+=1
        indi+=-1
        if soma == list[ind] + list[indi]:
            lista = True
        else:
            lista = False   
            ind = x

    return lista

#print(funcao5([2, 1, 9, 13, 12]))








def funcao6(n):
    lista = []
    n