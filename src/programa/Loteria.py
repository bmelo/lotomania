# -*- coding: iso-8859-15 -*-
# generated by wxGlade 0.6.3 on Mon Dec 08 18:39:51 2008

import wx
from Adicionar import Adicionar

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
mAdicionar = 1001
mRemover = 1002
mSair = 1003
# end wxGlade

class Loteria(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Loteria.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        
        # Menu Bar
        self.menu = wx.MenuBar()
        self.jogos = wx.Menu()
        self.mAdicionar = wx.MenuItem(self.jogos, mAdicionar, "Adicionar", "Adiciona novo bilhete.", wx.ITEM_NORMAL)
        self.jogos.AppendItem(self.mAdicionar)
        self.mRemover = wx.MenuItem(self.jogos, mRemover, "Remover", "Remove Bilhete.", wx.ITEM_NORMAL)
        self.jogos.AppendItem(self.mRemover)
        self.jogos.AppendSeparator()
        self.mSair = wx.MenuItem(self.jogos, mSair, "Sair", "Encerra Aplicativo.", wx.ITEM_NORMAL)
        self.jogos.AppendItem(self.mSair)
        self.menu.Append(self.jogos, "Jogos")
        self.SetMenuBar(self.menu)
        # Menu Bar end
        self.barrastatus = self.CreateStatusBar(1, 0)
        self.painel = wx.Panel(self, -1)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.Adicionar, self.mAdicionar)
        self.Bind(wx.EVT_MENU, self.Sair, self.mSair)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Loteria.__set_properties
        self.SetTitle("LotoMania")
        _icon = wx.EmptyIcon()
        _icon.CopyFromBitmap(wx.Bitmap("C:\\Users\\Bruno\\Documents\\Trabalhos\\Loteria\\icone.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.barrastatus.SetStatusWidths([-1])
        # statusbar fields
        barrastatus_fields = ["Lotomania"]
        for i in range(len(barrastatus_fields)):
            self.barrastatus.SetStatusText(barrastatus_fields[i], i)
        self.painel.SetMinSize((329, 241))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Loteria.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(self.painel, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        self.Centre()
        # end wxGlade

    def Adicionar(self, event): # wxGlade: Loteria.<event_handler>
        janelaAdicionar = Adicionar(None, -1, "")
        janelaAdicionar.Show()        

    def Sair(self, event): # wxGlade: Loteria.<event_handler>
        self.Close(True)
        exit()

# end of class Loteria

