def funcao1(x,y):
    if x>0 and y>0 or x<0 and y<0:
        saida = 1
    elif x>0 and y<0 or x<0 and y>0:
        saida = 0
    else:
        saida = "Digite valores nao nulos"

    return saida

#print(funcao1(16,-8))






def funcao2(x):
    y = x
    if x<-1:
        y = -1
    elif -1<=x<0:
        y = x
    elif 0>x>=1:
        y = x
    elif x>1:
        y = 1
    
    return y

#print(funcao2(2))






def funcao3(temp,sinal):
   convercao = 0,

   if sinal == 1: #Celsius > Fahrenheit
       convercao = (9*temp/5)+32
   elif sinal == 2: #Celsius > Kelvin
       convercao = temp+273
   elif sinal == 3: #Fahrenheit > Celcius
       convercao = 5*(temp-32)/9
   elif sinal == 4: #Fahrenheit > Kelvin
       convercao = (5*(temp-32)/9+273)
   elif sinal == 5: #Kelvin > Celsus
       convercao = temp-273
   elif sinal == 6: #Kelvin > Fahrenheit
       convercao = 9*(temp-273)/5+32

   return convercao
   
#print(funcao3(313,6))







def funcao4(d1,d2,d3,d4,d5,d6,d7,d8,d9):
   #d9 eh bit de paridade
   soma = d1+d2+d3+d4+d5+d6+d7+d8
   res = True

   if d9 == 1 and soma%2 == 0:
       res
   elif d9 == 0 and soma%2 == 1:
       res
   else:
       res = False

   return res

#print(funcao4(0,1,0,1,1,1,0,1,0))





def funcao5(a,b,c):
    bdist = 0
    ab = 0
    ac = 0
    bc = 0



    #Cálculo de distância ab

        #Se ab +/-
    if a<0 and b>0 or a>0 and b<0:
       ab = ((a**2)**(1/2)) + ((b**2)**(1/2))

       #Se ab +/+
    elif a>0 and b>0:
        if a>b:
            ab = a-b
        elif b>a:
            ab = b-a
        elif a==b:
            ab = 0
       
       #Se ab -/-
    elif a<0 and b<0:
      
       if a>b:
            ab = ((a**2)**(1/2)-(b**2)**(1/2))*(-1)
       elif b>a:
            ab = ((b**2)**(1/2)-(a**2)**(1/2))*(-1)
       elif b==a:
            ab = 0




     #Cálculo de distância ac

        #Se ac +/-
    if a<0 and c>0 or a>0 and c<0:
       ac = (a**2)**(1/2) + (c**2)**(1/2)

       #Se ac +/+
    elif a>0 and c>0:
        if a>c:
            ac = a-c
        elif c>a:
            ac = c-a
        elif a==c:
            ac = 0
       
       #Se ac -/-
    elif a<0 and c<0:
       
       if a>c:
            ac = ((a**2)**(1/2)-(c**2)**(1/2))*(-1)
       elif c>a:
            ac = ((c**2)**(1/2)-(a**2)**(1/2))*(-1) 
       elif c==a:
            ac = 0
            



  #Cálculo de distância bc

        #Se bc +/-
    if b<0 and c>0 or b>0 and c<0:
       bc = (b**2)**(1/2) + (c**2)**(1/2)

       #Se bc +/+
    elif b>0 and c>0:
        if b>c:
            bc = b-c
        elif c>b:
            bc = c-b
        elif b==c:
            bc = 0
       
       #Se bc -/-
    elif b<0 and c<0:
       
       if b>c:
            bc = ((b**2)**(1/2)-(c**2)**(1/2))*(-1)
       elif c>b:
            bc = ((c**2)**(1/2)-(b**2)**(1/2))*(-1) 
       elif c==b:
            bc = 0





    #Cálculo da maior distância

    if ab>ac and ab>bc:
        bdist = ab
    elif ac>ab and ac>bc:
        bdist = ac
    elif bc>ab and bc>ac:
        bdist = bc
    elif ab == ac and ab>bc:
        bdist = ab
    elif ac == bc and ac>ab:
        bdist = ac
    elif ab == bc and bc>ac:
        bist = bc
    else:
        bdist = 0
         
    
   
   
    return bdist


#print(funcao5(2,-4,7))








def funcao6(m3):
    #Consumo 15m³ = R$10
    #Consumo 16 - 40m³ = R$ (m³-15).1,2
    #Consumo >=41m³ = R$ (m³-40)
   tx = 10
   conta = 0
   segf = 0
   terf = 0
   if m3<=15:
       conta = tx
       segf = 0
       terf = 0
   elif m3>=16 and m3<=40:
       conta = 10+(m3-15)*1.2
       segf = (m3-15)*1.2
       terf = 0
   elif m3>=41:
       conta = 10 + 25*1.2 + (m3-40)*3
       segf = 25*1.2
       terf = (m3-40)*3

   return conta,segf,terf


#print(funcao6(45))









def funcao7(die1,de1p,dpe2,consumo,lit0,refuel):
    #Condiciones necessárias para função
        #Todos devem seguir a condição
    if type(die1)!=type(1) and type(die1)!=type(0.1):
       return -1
    elif type(de1p)!=type(1) and type(de1p)!=type(0.1):
       return -1
    elif type(dpe2)!=type(1) and type(dpe2)!=type(0.1):
       return -1
    elif die1<=0 or de1p<=0 or dpe2<=0:
       return -1
        #Ao menos um deve seguir a condição
    elif type(consumo)!=type(1) and type(consumo)!=type(0.1):
       return -2
    elif type(lit0)!=type(1) and type(lit0)!=type(0.1):
       return -2
    elif type(refuel)!=type(1) and type(refuel)!=type(0.1):
       return -2
    elif die1<=0 or de1p<=0 or dpe2<=0:
       return -2
           #Tanque inicial não deve ser >60L
    elif lit0>60:
       return -3


    else:
        done = True
        entregas = 0
        restcomb = 0
        tank = lit0
            
        #trajeto até E1 
        if tank < (die1*consumo):
            done = False
            entregas = 0
            restcomb = 0
            return done,entregas,restcomb
        tank = tank - die1*consumo 
                  
        #trajeto até P 
        if tank<de1p*consumo:
            done = False
            entregas = 1
            restcomb = 0
            return done,entregas,restcomb
        tank = tank - de1p*consumo 
        
        tank = tank + refuel
        if tank>60:
            tank = 60        
        #trajeto até E2                  
        elif tank < dpe2*consumo: 
            done = False
            entregas = 1
            restcomb = 0
            return done,entregas,restcomb
        tank = tank - dpe2*consumo 
        
        #trajeto até P volta
        if tank < dpe2*consumo:
            done = False
            entregas = 2
            restcomb = 0
            return done,entregas,restcomb
        tank = tank - dpe2*consumo
        
        tank = tank + refuel
        if tank>60:
            tank = 60
                
        #trajeto até E1 volta    
        elif tank < de1p*consumo: 
            done = False
            entregas = 2
            restcomb = 0
            return done,entregas,restcomb 
        tank = tank - de1p*consumo 
                
        #trajeto até I volta
        if tank < die1*consumo:
            done = False
            entregas = 2
            restcomb = 0
            return done,entregas,restcomb
               
        #trajeto até I volta
        if tank == die1*consumo:
            done = True
            entregas = 2
            restcomb = 0
            return done,entregas,restcomb
        
        #trajeto até I volta
        if tank > die1*consumo:
            done = True
            entregas = 2
            restcomb = tank - die1*consumo
            return done,entregas,restcomb


#print(funcao7('100',-200,35.7,0.05,20,15))
#print(funcao7(200,100,300,-0.003,20,'25'))
#print(funcao7(137.5,42,225.71,0.08,70,20))
#print(funcao7(200,100,100,0.05,20,15))
