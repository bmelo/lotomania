# -*- coding: cp1252 -*-
import random
import copy

class Bilhete:
    def __init__(self,numeros=list()):
        try:
            if str(type(numeros)) == "<type 'list'>":
                self.numeros=numeros;
            else:
                self.numeros=list();
        except:
            print "Não foi possível inicializar o bilhete."

    def addNum(self,numeros):
        if str(type(numeros)) == "<type 'int'>":
            numeros = [numeros]
        elif str(type(numeros)) != "<type 'list'>":
			numeros = [int(numeros)]
        try:
            for num in numeros:
                if str(type(num)) == "<type 'int'>":
                    if self.numeros.count(num) == 0:
                        self.numeros.append(copy.deepcopy(num))
            self.numeros.sort()
        except:
            print "Tipo inválido, precisa ser lista de inteiros!"

    def contem(self,numero):
        if int(numero) in self.numeros:
            return True
        return False

    def delNum(self,numero):
        if int(numero) in self.numeros:
            self.numeros.remove(int(numero))

    def limpa(self):
        self.numeros = list()

    def getNum(self):
		return len(self.numeros)

    def getListNum(self):
		return self.numeros

    def numAcertos(self,sorteio):
        contAcertos = 0
        for num in sorteio:
            if self.numeros.count(num)>0:
                contAcertos = contAcertos+1
        return contAcertos

    def sorteia(self):
        while len(self.numeros)<50:
            numSort = random.randint(0,99)
            if self.numeros.count(numSort) is 0:
                    self.numeros.append(numSort)
        self.numeros.sort()
