'''
Created on 5 de jul de 2018

@author: Renan
'''
from core.dsFile import dsFile
from core.record import record


class ptoper(dsFile):
    def __init__(self, cfg=None):
        dsFile.__init__(self, cfg)
    
    def readDSFile(self, fileName):
        nRec = 0
        with open(fileName, 'r') as f:
            for line in f:
                nRec = nRec + 1
                
                if record.isComment(line) or record.isBlankLine(line):
                    continue
                self.getTable('PTOPER').parseLine(line)
        f.close()
