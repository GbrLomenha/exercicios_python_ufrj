def funcao1(i1,i2,i3,i4,i5):
   soma = i1+i2+i3+i4+i5
   gorjeta = soma*10/100
   total = soma+gorjeta 
   
   return total

print(funcao1(10,10,10,10,10))




def funcao2(a,q,n):
   #a = primeiro termo
   #q = razão
   #n = quantidade de termois
   soma = a*(q**n-1)/(q-1)

   return soma

print(funcao2(1,0.5,10))





def funcao3(metros):
   pes = metros/0.3048
   
   return pes
   

print(funcao3(10))




def funcao4(x):
    px1 = ((x**(4/5)+9*x)/3)+7*x**2-100
    px2 = 2*x**3+10*x+3
    px3 = 8*x*(12*x**(2/3)-x**4)
    px4 = 20*x+7

    y = px1/px2-px3/px4

    return y

print(funcao4(1))




def funcao5(nx):
    resto = nx%1000
    centenas = resto//100
   
    return centenas

print (funcao5(3219))





def funcao6(x1,x2,x3,x4):
    m = (x1+x2+x3+x4)/4
    
    v = ((x1-m)**2+(x2-m)**2+(x3-m)**2+(x4-m)**2)/4

    return v

print (funcao6(4.5,1.5,2,3))





def funcao7(x):
     cfat = 5*4*3*2*1
     qfat = 4*3*2*1
     tfat = 3*2*1
     dfat = 2*1
     ufat = 1

     ex = (x**0/1)+(x**1/ufat)+(x**2/dfat)+(x**3/tfat)+(x**4/qfat)+(x**5/cfat)

     return ex

print(funcao7(2))