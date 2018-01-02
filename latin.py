#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('res/token.sqlite')
con.text_factory = bytes

with con:
    
    cur = con.cursor()    
    cur.execute("SELECT * FROM VOC WHERE key LIKE '" + sys.argv[1] + "%'")
    
    data = cur.fetchall()
    
    for entry in data:
    	print(entry[2].decode('utf-8'))
    	for desc in entry[3].decode('utf-8').split('; '):
    		print('  ', desc)
    	print()