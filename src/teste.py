import pygtk
pygtk.require('2.0')
import gtk

import gtk.glade 
fname = 'vazio.glade'

gtk.glade.XML(fname)

gtk.main() 
