# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 21:42:34 2026

@author: Shin
"""

name = "Ryo Shin Mendoza"
file = open("newfile1.txt", 'w')
file.write(f"Hello, {name}\n")
file.write("Isn't this amazing!\n")
file.write("that we can create and write on text files\n")
file.write("using Python.")
file.close()

file = open("newfile2.txt", 'w')
file.write("This message was created using Python!")
file.close()    