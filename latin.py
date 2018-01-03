#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import os

def pretty_print(lst):
    for entry in lst:
        print(entry[2].decode('utf-8'))
        for desc in entry[3].decode('utf-8').split('; '):
            print('  ', desc)
        print()


home = os.path.expanduser("~")
dir_path = home + '/latein'
db_path = home + '/latein/dict.sqlite'
zip_path = 'res/dict.zip'

if not os.path.exists(dir_path):
	print('creating directory:', dir_path)
	os.mkdir(dir_path)

if not os.path.isfile(db_path):
	print('On first use of this script the dictionary has to be decompressed.')
	print('Please unzip `dict.zip` and place it in `~/latein`')	
	sys.exit()

if len(sys.argv) < 2:
	print('missing argument.')
	sys.exit()

con = lite.connect(db_path)
con.text_factory = bytes

with con:
    
    cur = con.cursor()    
    cur.execute("SELECT * FROM VOC WHERE key LIKE '" + sys.argv[1] + "%'")
    data = cur.fetchall()
    pretty_print(data)

    if len(data) != 0:
        print('----------------------------------------------------------------', '\n')
    
    cur.execute("SELECT * FROM VOC WHERE key LIKE '%" + sys.argv[1] + "%'")
    data = cur.fetchall()
    pretty_print(data)



