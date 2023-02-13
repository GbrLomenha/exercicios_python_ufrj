from random import randint
class personagem():
    def __init__(self):
        self.nome = ''
        self.x = 0
        self.y = 0
        self.experiencia = 2
        self.pokemons = []

    def andar2(self,direcao):
        if direcao == 'cima':
            self.y +=1
        elif direcao == 'baixo':
            self.y -=1
        elif direcao == 'direita':
            self.x +=1
        elif direcao == 'esquerda':
            self.x -=1
        return self.x,self.y
        
    def treino3(self):
        sorteio = randint(0,5)
        if self.experiencia + sorteio > 100:
            self.experiencia = 100
        else:
            self.experiencia += sorteio
    
    def capturar4(self,pokemon,defesa):
        forca = randint(-1,3)
        if self.experiencia + forca > defesa:
            self.pokemons.append(pokemon)
            return 1
        else:
            return 0
    
    def scann5(self,pokemon,defesa,x,y):
        posX = self.x-x
        posY = self.y-y
        if posX >=-1 or posX <=1 and posY >=-1 or posY <=1:
            self.capturar4(pokemon,defesa)
        return posX,posY

class personagem2(personagem):
    def quantidade7(self,pokemon):
        contador = 0
        for p in len(self.pokemons):
            if p == pokemon:
                contador+=1
        return contador
    
    def capturar4(self, pokemon, defesa):
        forcaPers = randint(1,self.experiencia)
        poderDef = randint(1,defesa)
        if forcaPers>poderDef:
            self.pokemons.append(pokemon)
            return 1
        else:
            return 0
