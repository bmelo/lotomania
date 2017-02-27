# -*- coding: cp1252 -*-
from bilhete import Bilhete
import random
import pickle

def testaSorte(bilhete):
    premio = [0,16,17,18,19,20]
    quant = 0
    acerto = -1
    while True:
        x=list()
        while len(x)<20:
                numSort = random.randint(0,99)
                if x.count(numSort) is 0:
                        x.append(numSort)
        x.sort()
        acerto = bilhete.numAcerto(x)
        quant = quant+1
        if acerto in premio:
            print "Números sorteados: ",x
            break

    print "Quantidade de Sorteios: ",quant
    print "Quantidade de Acertos: ",bilhete.numAcerto(x)

bilhete = Bilhete()
bilhete.sorteia()
#print "Números do bilhete: ",bilhete.numeros

f = open("teste.ltm", 'wb')
pickle.dump(bilhete, f) # descarrega o objeto em um arquivo
f.close()

del bilhete

f = open("teste.ltm", 'rb')
bilhete = pickle.load(f) # carrega o objeto do arquivo
print(bilhete.numeros)




