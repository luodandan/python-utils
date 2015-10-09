__author__ = 'x1ang.li'


import os
import codecs

"""
This module is intended for replacing large text file
"""

base = os.path.join(os.environ['USERPROFILE'], 'Desktop') # User's Desktop, for MicroSoft Windows
# base = os.path.dirname(__file__)
fin_name = os.path.join(base, 'Main.asmx.xml')
fout_name = os.path.join(base, 'output.xml')


with codecs.open(fin_name, 'r', 'utf-8') as fin:
    with codecs.open(fout_name, 'w', 'utf-8') as fout:
        for linein in fin:
            lineout = linein.replace('&lt;', '<').replace('&gt;', '>')
            fout.write(lineout)

