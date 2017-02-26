# -*- coding: cp1252 -*-

pastas = ["janelas","controle","objetos"]
import sys, os
for pasta in pastas:
	sys.path.append(pasta)

import pygtk
pygtk.require('2.0')
import gtk, gtk.glade

fname = "janelas"+os.sep+"Sobre.glade"

class jSobre:
   def __init__(self):
      self.carregaGlade()

   # Métodos -----------------------------------------------------------------
   def carregaGlade(self):
      self.arvoreDeWidgets = gtk.glade.XML(fname)

      #Get the Main Window, and connect the 'destroy' event
      self.janela = self.arvoreDeWidgets.get_widget('jSobre')
      if (self.janela):
          self.janela.connect('destroy', self.reabre)
          self.janela.connect("response", lambda d, r: d.destroy())

      #Widgets
      self.botoes = self.arvoreDeWidgets.get_widget('botoes')

      #Autoconnect Signals and Callbacks
      self.arvoreDeWidgets.signal_autoconnect(self)

   def exibe(self):
       self.janela.show_all()

   def reabre(self, widget=None):
       self.carregaGlade()
