# -*- coding: utf-8 -*-  
## setup_win32.py (run me as python setup_win32.py py2exe -O2)  
##  
## Copyright (C) 2003-2006 Yann Le Boulanger <asterix@lagaule.org>  
## Copyright (C) 2005-2006 Nikos Kouremenos <kourem@gmail.com>  
## Copyright (C) 2007 Marcelo Lira dos Santos <setanta@gmail.com>  
##  
## This program is free software; you can redistribute it and/or modify  
## it under the terms of the GNU General Public License as published  
## by the Free Software Foundation; version 2 only.  
##  
## This program is distributed in the hope that it will be useful,  
## but WITHOUT ANY WARRANTY; without even the implied warranty of  
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the  
## GNU General Public License for more details.  
##  
  
from distutils.core import setup
import py2exe  

setup(console=['doLink.py'])
