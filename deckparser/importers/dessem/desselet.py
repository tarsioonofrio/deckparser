'''
Created on 5 de jul de 2018

@author: Renan
'''
from core.dsFile import dsFile
from core.record import record


class desselet(dsFile):
    def __init__(self, cfg=None):
        dsFile.__init__(self, cfg)
    
    def isComment(self, line):
        return line[0] == '('
    
    def isTableEnd(self, line):
        return record.assertString(line, '9999') or record.assertString(line, '99999')
    
    def readDSFile(self, fileName):
        nRec = 0
        modo = 'BASE'
        with open(fileName, 'r') as f:
            for line in f:
                nRec = nRec + 1
                
                if self.isComment(line) or record.isBlankLine(line):
                    continue
                if self.isTableEnd(line):
                    modo = 'MODIF'
                    continue
                if record.isEOF(line):
                    break
                
                if modo == 'BASE':
                    self.getTable('Base').parseLine(line)
                elif modo == 'MODIF':
                    self.getTable('Modif').parseLine(line)
        f.close()
    