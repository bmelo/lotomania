# -*- coding: cp1252 -*-

pastas = ["janelas","controle","objetos"]
import sys, os
for pasta in pastas:
	sys.path.append(pasta)

import pygtk
pygtk.require('2.0')
import gtk, gtk.glade
import copy
import time

# funcoes feitas por mim
from funcoes import *
from bilhete import *
from manipulador_dados import *

fname = "janelas"+os.sep+"Resultado.glade"

class jResultado:
   def __init__(self,manipulador):
      self.carregaGlade()
      
      #Objetos
      self.manipulador = manipulador
      self.resultado = Bilhete()
      self.bloqueioSinal = False

   # Métodos -----------------------------------------------------------------
   def carregaGlade(self):
      self.arvoreDeWidgets = gtk.glade.XML(fname)

      #Get the Main Window, and connect the 'destroy' event
      self.janela = self.arvoreDeWidgets.get_widget('jAdicionar')
      if (self.janela):
          self.janela.connect('destroy', self.reabre)
      
      #Widgets
      self.chks = list()
      for x in range(0,100):
	      self.chks.append(self.arvoreDeWidgets.get_widget('ck'+str(x).rjust(2,'0')))
      self.lista = self.arvoreDeWidgets.get_widget('lista')
      self.itensLista = self.lista.get_model()
      self.limpar = self.arvoreDeWidgets.get_widget('bLimpar')
      self.salvar = self.arvoreDeWidgets.get_widget('bSalvar')
      self.tNum = self.arvoreDeWidgets.get_widget('tNum')
      self.relatorio = self.arvoreDeWidgets.get_widget('areaTexto')

      #Autoconnect Signals and Callbacks
      self.arvoreDeWidgets.signal_autoconnect(self)

   def marcaResultado(self):
      self.bloqueioSinal = True
      for numero in self.resultado.getListNum():
          self.chks[int(numero)].set_active(True)
      self.bloqueioSinal = False
      self.corrigeTNum()

   def recebeResultado(self,pos):
       self.resultado = copy.deepcopy(self.manipulador.getResultado(pos))
       if not self.bilhete:
          self.bilhete = Bilhete()

   def exibe(self):
       self.itensLista.clear()
       self.itensLista.append([str("VAZIO")])
       #self.lista.items.add("TESTE")
#       self.lista.set_range()
#       self.alteraResultado(self.lista)
       self.janela.show_all()

   def reabre(self, widget=None):
       self.carregaGlade()

   def corrigeTNum(self):
       self.tNum.set_label("( "+str(self.resultado.getNum())+" )")
       self.tNum.set_has_tooltip(True)

   def escondeTNum(self):
       self.tNum.set_label("")
       self.tNum.set_has_tooltip(False)       

   # Callbacks ---------------------------------------------------------------

   def bt_selecao(self, widget=None):
      if self.bloqueioSinal:
          return 0

      numSel = widget.get_name()[-2:]
      if widget.get_active():
          self.resultado.addNum(numSel)
      else:
          self.resultado.delNum(numSel)

      if(self.resultado.getNum()>20):
          self.resultado.delNum(numSel)

      self.bloqueioSinal = True
      if self.resultado.contem(numSel):
          widget.set_active(True)
      else:
          widget.set_active(False)
      self.bloqueioSinal = False
      self.corrigeTNum()

   def exibeRelatorio(self, widget=None):
       self.relatorio.get_buffer().set_text(self.manipulador.getRelatorio(self.resultado.getListNum()))

   def bt_limpar(self, widget=None):
       self.bloqueioSinal = True
       self.resultado.limpa()
       for ck in self.chks:
           ck.set_active(False)
       self.bloqueioSinal = False
       self.corrigeTNum()

   def bt_sair(self, widget=None):
       self.janela.hide_all()

   def bt_salvar(self, widget=None):
      try:
          self.manipulador.addResultado(self.bilhete)
          self.manipulador.salva()

      except:
          print "ERRO AO SALVAR OS DADOS!"

   def alteraResultado(self, widget=None):
       self.bt_limpar()
       self.marcaResultado()
