'''
Created on Jul 16, 2018

@author: thanawutth
'''

class DataCenter:
    nHost       = 0
    sPower      = 0.0
    sUtil       = 0.0
    def __init__(self):
        self.nHost      = 0
        self.sPower     = 0.0
        self.sUtil      = 0.0
    
    class Host:
        nVM         = 0
        nPE         = 0
        nMem        = 0
        nStorage    = 0
        def __init__(self):
            self.nVM        = 0
            self.nPE        = 0
            self.nMem       = 0
            self.nStorage   = 0
        
    class VirtualMachine:
        vMIPS       = 0.0
        vMem        = 0
        def __init__(self):
            self.vMIPS      = 0
            self.vMem       = 0