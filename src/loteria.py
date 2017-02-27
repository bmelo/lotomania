# -*- coding: cp1252 -*-
import pygtk
pygtk.require('2.0')
import gtk

import gtk.glade 
fname = 'Loteria.glade'

class appWindow:
   def __init__(self):
       self.widgetTree = gtk.glade.XML(fname)
       #Get the Main Window, and connect the 'destroy' event
       self.window = self.widgetTree.get_widget('jPrincipal')
       if (self.window):
           self.window.connect('destroy', gtk.main_quit)
       #Widgets -------

       self.emailEntry = self.widgetTree.get_widget('adicionar')
       self.nomeEntry = self.widgetTree.get_widget('sair')

       #Autoconnect Signals and Callbacks
       self.widgetTree.signal_autoconnect(self)
       self.window.show_all()

   # Callbacks ---------------------------------------------------------------
   def botao_pressionado(self, widget):
       print 'botao_pressionado'

   def teste(self, widget):
       print 'botao_pressionado'

   def on_adicionar_active_item(self, widget):
       print 'botao_pressionado'

if __name__ == '__main__':

    app = appWindow()
    gtk.main()
