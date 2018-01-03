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


def get_vok_data_for_id(vok_id):
    cur.execute("SELECT * FROM VOC WHERE vok_id = '" + vok_id + "'")
    data = cur.fetchone()
    return data


def get_form(q):
    d = dict()
    cur.execute("SELECT * FROM FORM WHERE form LIKE '" + sys.argv[1] + "'")
    data = cur.fetchall()
    for e in data:
        vok_id = e[1].decode('utf-8')
        if vok_id in d:
            d[vok_id].append(e[3])
        else:
            d[vok_id] = [e[3]]
    return d



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
    print()
    d = get_form(sys.argv[1])
    for k in d:
        data = get_vok_data_for_id(k)
        pretty_print([data])
        print('  Formen:')
        for form in d[k]:
            f_list = form.decode('utf-8').split(', ')
            for f in f_list:
                print('    ', f)

        print('\______________________________________________________________')
        print()


    if len(d) == 0:
        cur.execute("SELECT * FROM VOC WHERE key LIKE '" + sys.argv[1] + "%'")
        data = cur.fetchall()
        pretty_print(data)
    

    # if len(data) == 0:
    #     cur.execute("SELECT * FROM VOC WHERE key LIKE '%" + sys.argv[1] + "%'")
    #     data = cur.fetchall()
    #     pretty_print(data)





