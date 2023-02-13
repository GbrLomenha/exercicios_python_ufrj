def questao1(x,y):
    if x == y:
        return 0
    if x < y:
        return x
    if x > y:
        return questao1(x-y,y)

#print(questao1(2,5))
#print(questao1(10,3))
#print(questao1(10,4))
#print(questao1(10,5))


def questao2(valorI,taxa,meses):
    if meses == 0:
        return valorI
    else:
        return questao2(valorI,taxa,meses-1) + taxa/100*questao2(valorI,taxa,meses-1)

#print(questao2(400,5,4))

def questao3(n):
    if n == 0:
        return 1
    num = (2*n-1)*questao3(n-1)
    den = n+1
    return 2*num/den

#print(questao3(0))
#print(questao3(1))
#print(questao3(2))
#print(questao3(3))
#print(questao3(9))

    