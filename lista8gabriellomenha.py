import random
def questao1(x):
    alg = {1:"I", 2:"II",3:"III",4:"IV",5:"V",\
        6:"VI",7:"VII",8:"VIII",9:"IX",10:"X"}

    if x in alg:
        rom = alg[x]
        return rom
    if x not in alg:
        rom = ""
        return rom



def questao2(list):
    unitarios = []
    repetidos = []
    for ind in list:
        if ind not in unitarios:
            unitarios.append(ind)
        else:
            if ind in repetidos:
                continue
            else:
                repetidos.append(ind)
        
    return repetidos





def questao3(qntq,letras):
    gabarito = {}
    questao = 1
    while questao <= qntq:
        gabarito[questao] = random.choice(letras)
        questao+=1

    return gabarito



def questao4(perso1,perso2):
    ptsHP1 = perso1[0]
    danMin1 = perso1[1]
    danMax1 = perso1[2]
    armor1 = perso1[3]
    crita1 = perso1[4]

    ptsHP2 = perso2[0]
    danMin2 = perso2[1]
    danMax2 = perso2[2]
    armor2 = perso2[3]
    crita2 = perso2[4]

    
    turno = 0
    vez = 1
    while ptsHP1 > 0 and ptsHP2 > 0:
        turno+=1
        if vez == 1:
            #Cáluclo de DanoBase1
            danoBase1 = random.randint(danMin1,danMax1)
            acertoCrit1 = random.randint(0,100)
            if acertoCrit1 <= crita1:
                danoBase1 *= 2
            #Cálculo de Dano Causado1
            if danoBase1 <= armor2:
                danoCausado1 = 0
            else:
                danoCausado1 = danoBase1 - armor2
            #Dreno de Vida 2
            ptsHP2 -= danoCausado1

            #TROCA DE TURNO?
            if ptsHP1 > 0 and ptsHP2 > 0:
                vez = 2

        if vez == 2:
            #Cáluclo de DanoBase2
            danoBase2 = random.randint(danMin2,danMax2)
            acertoCrit2 = random.randint(0,100)
            if acertoCrit2 <= crita2:
                danoBase2 *= 2
            #Cálculo de Dano Causado2
            if danoBase2 <= armor1:
                danoCausado2 = 0
            else:
                danoCausado2 = danoBase2 - armor1
            #Dreno de Vida 1
            ptsHP1 -= danoCausado2

            #TROCA DE TURNO?
            if ptsHP1 > 0 and ptsHP2 > 0:
                vez = 1
    if ptsHP1 > 0:
        vencedor = 1
    if ptsHP2 > 0:
        vencedor = 2 
    if vencedor == 1:
        hpRestante = ptsHP1
    if vencedor == 2:
        hpRestante = ptsHP2
    resultado = vencedor,hpRestante,turno

    return resultado






