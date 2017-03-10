# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 06:04:05 2015

@author: user
"""

s=0
def func1():
    global s
    print s
    s=1
    func2()
    print s
    
def func2():
    global s
    s=5
    print s

def func3():
    c=s+1
    print c
        

if __name__ == "__main__":
    func1()
