#!/usr/bin/python
# -*- coding: cp1252 -*-
import pygtk
pygtk.require('2.0')

import copy

pastas = ["janelas","controle","objetos"]
import sys, os
for pasta in pastas:
	sys.path.append(pasta)

from bilhetes import *
from resultado import *
from sobre import *
from manipulador_dados import *

import gtk, gtk.glade 
fname = "janelas"+os.sep+"Loteria.glade"

class appWindow:
   def __init__(self):

       self.programa = gtk.glade.XML(fname)
       #Recebe a janela principal e cria o evento para destruir
       self.window = self.programa.get_widget('jPrincipal')
       if (self.window):
           self.window.connect('destroy', gtk.main_quit)

       #Objetos --------------------------------------------------------------

       self.manipulador = Manipulador("dados.dat")
       self.manipulador.carrega()

       #Widgets --------------------------------------------------------------

       self.jBilhetes = jBilhetes(self.manipulador)
       self.jResultado = jResultado(self.manipulador)
       self.jSobre = jSobre()

       #Autoconnect Signals and Callbacks
       self.programa.signal_autoconnect(self)
       self.window.show_all()

   # Callbacks ---------------------------------------------------------------
   def adicionar(self,*args):
       self.jBilhetes.exibe()

   def resultado(self, *args):
       self.jResultado.exibe()

   def sair(self,*args):
       exit()

   def sobre(self,*args):
       self.jSobre.exibe()

if __name__ == '__main__':
    app = appWindow()
    gtk.main()
