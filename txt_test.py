# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 14:00:33 2018

@author: JES
"""

f = open('test.txt', 'w')
txt = "2010A10,한글,1234".decode('utf-8')
f.write(txt.encode('utf-8'))
f.close()