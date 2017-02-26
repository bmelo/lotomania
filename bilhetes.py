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

fname = "janelas"+os.sep+"Bilhetes.glade"

class jBilhetes:
   def __init__(self,manipulador):
      self.carregaGlade()
      
      #Objetos
      self.bloqueioCks = False #Libera os botões para serem alterados ao clicar em 'Novo' ou 'Editar'
      self.manipulador = manipulador
      self.bilhete = Bilhete()
      self.bloqueioCks = True #Impede que os botões sejam alterados antes de clicar em 'Novo' ou 'Editar'
      self.editarPressionado = False
      self.ultimaPos = 1 #Indica a última posição antes de clicar em 'Novo' e 'Editar', usado em bt_cancelar
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
      self.limpar = self.arvoreDeWidgets.get_widget('bLimpar')
      self.salvar = self.arvoreDeWidgets.get_widget('bSalvar')
      self.novo = self.arvoreDeWidgets.get_widget('bNovo')
      self.editar = self.arvoreDeWidgets.get_widget('bEditar')
      self.cancelar = self.arvoreDeWidgets.get_widget('bCancelar')
      self.aleatorio = self.arvoreDeWidgets.get_widget('bAleatorio')
      self.tNum = self.arvoreDeWidgets.get_widget('tNum')

      #Autoconnect Signals and Callbacks
      self.arvoreDeWidgets.signal_autoconnect(self)

   def marcaBilhete(self):
      self.bloqueioSinal = True
      print "Numeros do bilhete: "+str(self.bilhete.getListNum())
      for numero in self.bilhete.getListNum():
          self.chks[int(numero)].set_active(True)
      self.bloqueioSinal = False
      self.corrigeTNum()

   def recebeBilhete(self,pos):
       self.bilhete = copy.deepcopy(self.manipulador.getBilhete(pos))
       if not self.bilhete:
          self.bilhete = Bilhete()

   def exibe(self):
       self.janela.show_all()

       #Botões para Esconder
       self.layoutJanela(2)
       self.lista.set_value(1.0)
       self.lista.set_range(1.0,float(self.manipulador.getNumBilhetes()))
       self.alteraBilhete(self.lista)

   def reabre(self, widget=None):
       self.carregaGlade()

   def layoutJanela(self,opcao):
       # 1 - Edição \ 2 - Seleção
       if opcao==1:
           for botao in [self.limpar, self.salvar, self.cancelar, self.aleatorio]:
               botao.show()

           #Esconde
           for botao in [self.novo,self.editar]:
               botao.hide()
           self.bloqueioCks = False
           self.lista.set_range(self.lista.get_value(), self.lista.get_value())

       elif opcao==2:
           if self.manipulador.getNumBilhetes()>0:
               mostra = [self.novo, self.editar]
               esconde = [self.limpar, self.salvar, self.cancelar, self.aleatorio]
           else:
               mostra = [self.novo]
               esconde = [self.limpar, self.salvar, self.cancelar, self.aleatorio, self.editar]
           for botao in mostra:
               botao.show()

           #Esconde
           for botao in esconde:
               botao.hide()
           self.bloqueioCks = True
           self.editarPressionado = False
           self.lista.set_range(1.0,float(self.manipulador.getNumBilhetes()))

   def corrigeTNum(self):
       self.tNum.set_label("( "+str(self.bilhete.getNum())+" )")
       self.tNum.set_has_tooltip(True)

   def escondeTNum(self):
       self.tNum.set_label("")
       self.tNum.set_has_tooltip(False)

   # Callbacks ---------------------------------------------------------------

   def bt_selecao(self, widget=None):
      if self.bloqueioSinal:
          return None
      numSel = widget.get_name()[-2:]
      if not self.bloqueioCks:
          if widget.get_active():
             self.bilhete.addNum(numSel)
          else:
             self.bilhete.delNum(numSel)

          if(self.bilhete.getNum()>50):
             self.bilhete.delNum(numSel)

      self.bloqueioSinal = True
      if self.bilhete.contem(numSel):
          widget.set_active(True)
          print "MARCADO - "+numSel
      else:
          widget.set_active(False)
      self.bloqueioSinal = False
      self.corrigeTNum()

      print self.bilhete.getListNum()

   def bt_novo(self,widget=None):
       self.bloqueioCks = False
       self.ultimaPos = self.lista.get_value()
       max = self.lista.get_range()[1]
       self.lista.set_range(1.0,max+1.0)
       self.lista.set_value(max+1.0)
       self.bt_limpar()
       self.editarPressionado = False

       #LAYOUT BOTÕES
       self.layoutJanela(1)

   def bt_editar(self,widget=None):
       self.bloqueioCks = False
       self.ultimaPos = self.lista.get_value()
       self.editarPressionado = True

       # LAYOUT BOTÕES
       self.layoutJanela(1)

   def bt_limpar(self, widget=None):
       self.bloqueioSinal = True
       self.bilhete.limpa()
       for ck in self.chks:
           ck.set_active(False)
       self.bloqueioSinal = False
       self.corrigeTNum()

   def bt_cancelar(self, widget=None):
       self.lista.set_range(1.0,float(self.manipulador.getNumBilhetes()))
       self.lista.set_value(self.ultimaPos)
       self.alteraBilhete(self.lista)

       # LAYOUT BOTÕES
       self.layoutJanela(2)

   def bt_sair(self, widget=None):
       self.janela.hide_all()

   def bt_aleatorio(self, widget=None):
       #self.bt_limpar()
       self.bilhete.sorteia()
       self.marcaBilhete()

   def bt_salvar(self, widget=None):
      try:
          if self.editarPressionado:
              self.manipulador.editaBilhete(self.bilhete, self.lista.get_value()-1)
              self.manipulador.salva()
          else:
              self.manipulador.addBilhete(self.bilhete)
              self.manipulador.salva()
         
          # LAYOUT BOTÕES
          self.layoutJanela(2)

      except:
          print "ERRO AO SALVAR OS DADOS!"

   def alteraBilhete(self, widget=None):
       self.bt_limpar()
       self.recebeBilhete(int(widget.get_value()-1))
       self.marcaBilhete()
