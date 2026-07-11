# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 21:50:03 2026

@author: Shin
"""

file = open("newfile1.txt", 'r')
data = file.read()
print(data)
file.close()

file = open("newfile2.txt", 'r')
data = file.read()
print(data)
file.close()


file = open("newfile2.txt", 'r')
data = file.read(12)
print(data)
file.close()
