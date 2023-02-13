def questao1(list):
    list_int = []
    list_float = []
    list_bool = []
    for i in list:
        if type(i) == type(1):
            list_int.append(i)
        if type(i) == type(0.1):
            list_float.append(i)
        if type(i) == type(True):
            list_bool.append(i)
    return list_int,list_float,list_bool
#print(questao1([2, 4.0, True, True, 6.2, 8.5, False, 1]))



def questao2(list):
    lista = []
    for i in list:
        if i in lista:
            continue
        else:
            lista.append(i)
    return lista
#print (questao2([1, 2, 3]))



def questao3(list):
    lista = []
    for i in list:
        if list[i] in list:
            lista.append(list[i])        #PRECISA DA CONDIÇÃO FORA DO RANGE DE INDICE
        else:
            lista.append("False")
        
    return lista
#print(questao3([4, -3, 2, -5])) 



def questao4(list):
    lista = []
    ind = 0
    for i in list:
        if list[0] == i:
            lista.append(list[1]/2)
        elif list[-1] == i:
            lista.append(list[-2]/2)
        else:
           media = (list[ind-1]+list[ind+1])/2
           lista.append(media)
        ind+=1
    return lista
#print(questao4([-1.5, 4.2, 7.7, -3.1, 9.4, 0.6]))





def questao6(list):
    lista = []
    npessoas = len(list)
    idades = []
    alturas =[] 
    pesos =[]
    medidades = 0
    medalturas = 0
    medpesos = 0
    
    for i in list:
        idades.append(i[0])
        alturas.append(i[1])
        pesos.append(i[2])
    for i in idades:
        medidades = medidades+i 
    for i in alturas:
        medalturas = medalturas+i 
    for i in pesos:
        medpesos = medpesos+i 

    lista.append(medidades/npessoas)
    lista.append(medalturas/npessoas)
    lista.append(medpesos/npessoas)
    return lista
#print(questao6([[40, 1.60, 60], [30, 1.80, 75]]))



def questao7(list1,list2):
    lista = []
    newlist = []
    prodt = 0
    for in1 in list1:
        for in2 in list2:
            prodt = in1 * in2
            newlist.append(prodt)
        lista.append(newlist)
        newlist = []   
    return lista
#print(questao7([0.2, 1.3, -7.8], [4.9, -12.1, 8.6]))



def questao8(list):
    primlista = [] 
    lista = []
    for lst in list:
        for i in lst:
            if i < 0:
                i = 0
                primlista.append(i)
            elif i > 10:
                i = 10
                primlista.append(i)
            else:
                primlista.append(i)
        lista.append(primlista)
        primlista=[]
    return lista
#print(questao8([[5, 2, 7, 8, 2], [9, 3, 1, 4, 4], [7, 7, 6, 2, 3]]))