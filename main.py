'''
Created on Jul 13, 2018

@author: thanawutth
'''
from datacenter import DataCenter
import time

def runevent(tm):
    
    while True:
        print("DateTime " + time.strftime("%c"))
        time.sleep(tm) # delays for 1 seconds

if __name__ == '__main__':
    dc = DataCenter()
    h = dc.Host()
    runevent(1)