# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 23:50:02 2019

@author: MastaMoose
"""

import xml.etree.ElementTree as et
tree = et.ElementTree(file="menu.xml")
root = tree.getroot()
root.tag

for child in root:
    print('tag: ', child.tag, 'attributes: ', child.attrib)
    for grandchild in child:
        print('\ttag:', grandchild.tag, 'attributes: ', grandchild.attrib)
        

for i in range(len(root)):
    print(len(root[i]))