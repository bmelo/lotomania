# -*- coding: cp1252 -*-
import pygtk
pygtk.require('2.0')
import gtk, gtk.glade
import sys, os
# funcoes feitas por mim
from funcoes import *

local = os.getcwd()+os.sep+"janelas"

if find(sys.path,local)==-1:    
   sys.path.append(local)

fname = "janelas"+os.sep+"Adicionar.glade"

class jAdicionar:
   def __init__(self):
      self.cont = 0
      self.arvoreDeWidgets = gtk.glade.XML(fname)
      #Get the Main Window, and connect the 'destroy' event
      self.janela = self.arvoreDeWidgets.get_widget('jAdicionar')
      if (self.janela):
          self.janela.connect('destroy', gtk.main_quit)
      #Widgets

      #Autoconnect Signals and Callbacks
      self.arvoreDeWidgets.signal_autoconnect(self)
      self.janela.show_all()

   # Callbacks ---------------------------------------------------------------
   def bt_selecao(self, widget):
      if(self.cont<50):
         self.cont = self.cont+1
         print 'numeros selecionados: '+str(self.cont)
         print 'ultimo numero selecionado: '+widget.get_name()

   def teste(self, widget):
       print 'botao_pressionado'

   def on_adicionar_active_item(self, widget):
       print 'botao_pressionado'

if __name__ == '__main__':
    app = jAdicionar()
    gtk.main()
