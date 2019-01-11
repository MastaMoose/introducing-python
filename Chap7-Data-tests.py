# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 22:25:50 2018

@author: Mustafa
"""

def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value="%s" , name = "%s", value2="%s"' %(value, name, value2))
    
def sencap(pattern, source):
    import re
    m = re.match(pattern,source)
    if m:
        print(m.group())
    else:
        print('not in there')
    return m.group()

import struct
valid_png_header = b'\x89PNG\r\n\x1a\n'
