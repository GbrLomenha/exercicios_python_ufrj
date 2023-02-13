def funcao1(x,y):
    n = 1
    res = x
    while n < y:
        res = res + x
        n = n + 1

    return res

#print(funcao1(8,6))






def funcao2(n):
    x = 1
    somador = 0
    while x <= n:
        somador = somador+(((1+x)*x)/2)
        x = x+1
        
    return somador

#print(funcao2(0))






#QUESTÃO 3

def primFuncao(x):
    if x == 0:
        return 1
    else:
        n = 1
        res = 1
        while n<=x:
            res = res*n
            n = n+1
    return res

def questao3a(n,k):
    arranjo = primFuncao(n)/primFuncao(n-k)
    return arranjo 
#print(questao3a(3,2))
#print(questao3a(3,3))
#print(questao3a(4,2))

def questao3b(n,k):
    combinacao = 1/primFuncao(k)*questao3a(n,k)
    return combinacao

#print(questao3b(3,2))
#print(questao3b(3,3))
#print(questao3b(4,2))






def questao4a(x):
    n = 2
    res = True
    divisor = 2
    if x == 1:
        res = False
    else:
        while n < x:
            div = x%divisor
            if div == 0:
                res = False
                n = x
            else:
                divisor = divisor+1
                n = n+1
    return res

def questao4b(n):
    if questao4a(n) == True:
        return n 
    else:
        while questao4a(n) == False:
            n = n + 1
    return n

#print(questao4b(3))
#print(questao4b(9))
#print(questao4b(12))
#print(questao4b(32))







def funcao5(cxt,watt0):
    cx = 0
    dias = 0
    watt = watt0
    while cx < cxt:
        if dias == 0:
           cx = (cx + watt)/2
           watt = watt + watt*0.2
           dias+=1
        else:
           cx = (cx + watt)/2
           watt = watt + watt*0.2
           dias+=1
    return dias
   
#print(funcao5(100,10)) 