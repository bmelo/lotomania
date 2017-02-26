#! /usr/bin/env python

import sys
import copy

sys.path.append("../objetos")

import pickle as p
from bilhete import *

class Manipulador:

	def __init__(self,nomeArq="dados.dat"):
		self.nomeArq = nomeArq
		self.dic = dict()

	def add(self,nome,objeto):
		self.dic.update({nome:objeto})

	def rem(self,nome):
		del self.dic[nome]

	def addBilhete(self,bilhete):
		if('bilhete' in self.dic.keys()):
			self.dic['bilhete'].append(copy.deepcopy(bilhete))
		else:
			self.dic.update({'bilhete':[copy.deepcopy(bilhete)]})

	def editaBilhete(self,bilhete,pos):
		if('bilhete' in self.dic.keys()):
			self.dic['bilhete'][int(pos)] = copy.deepcopy(bilhete)

	def getDados(self):
		return self.dic

	def getNumBilhetes(self):
		if 'bilhete' in self.dic.keys():
			return len(self.dic['bilhete'])
		return 0

	def getBilhete(self,pos):
		numBilhetes = self.getNumBilhetes()
		if pos < 0:
			pos += numBilhetes

		if pos < numBilhetes and pos >= 0:
			return self.dic['bilhete'][pos]
		return None

	def getRelatorio(self,listaSorteio):
		resultado = ""
		pos = 0
		for bilhete in self.dic['bilhete']:
			pos+=1
			numAcertos = bilhete.numAcertos(listaSorteio)
			espacamento = str().ljust(35," ")
			if numAcertos>=16 or numAcertos==0:
				resultado += "\n"
				resultado += "Cartela: "+str(pos)+"\n"
				resultado += "Total de Acertos: "+str(numAcertos)+"\n\n"
				resultado += "Numeros da Cartela:\n\n"+espacamento
				cont = 0
				for num in bilhete.getListNum():
					cont+=1
					resultado+=" "+str(num).rjust(2,"0")+" -"
					if cont==10:
						resultado=resultado.strip("-")+"\n"+espacamento
						cont = 0
				resultado=resultado.strip("-")+"\n"
				resultado += str().ljust(87,"-")+"\n"
		return resultado

	def salva(self):
		arquivo = open(self.nomeArq,'w')
		p.dump(self.dic,arquivo)
		arquivo.close()

	def carrega(self):
		try:
			file = open(self.nomeArq,'r')
			self.dic = p.load(file)
			file.close()
			print "Total de Bilhetes Carregados: "+str(len(self.dic['bilhete']))
		except:
			pass
