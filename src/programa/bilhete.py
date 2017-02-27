# -*- coding: cp1252 -*-
import random

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
        try:
            for num in numeros:
                if str(type(num)) == "<type 'int'>":
                    if self.numeros.count(num) == 0:
                        self.numeros.append(num)
            self.numeros.sort();
        except:
            print "Tipo inválido, precisa ser lista de inteiros!"

    def delNum(self,numero):
        self.numeros.remove(numero)

    def limpa(self):
        self.numeros = list()

    def numAcerto(self,sorteio):
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
