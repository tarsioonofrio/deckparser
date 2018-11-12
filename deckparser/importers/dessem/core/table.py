'''
Created on 4 de jul de 2018

@author: Renan
'''
from deckparser.importers.dessem.core.record import record


class table:
    
    def __init__(self, recMap):
        self.rec = record(recMap)
        self.clear()
        
    def isEmpty(self):
        return len(self.dataSet) == 0
     
    def toDict(self, df=True):
        fl = self.rec.recMap
        lst = []
        lines = self.getData(df)
        for ln in lines:
            ds = {}
            for k in fl:
                f = fl[k]
                if f.get('composed'):
                    for kd in self.rec.composedToDict(f, ln):
                        ds[kd] = ln.get(kd)
                else:
                    ds[k] = ln.get(k)
            lst.append(ds)
        return lst
    
    def clear(self):
        self.dataSet = []
        self.lineSet = []
        
    def addField(self, name, cfg):
        self.rec.addField(name, cfg)
        
    def setRange(self, key, r):
        self.rec.setRange(key, r)
        
    def setField(self, key, v):
        self.dataSet[len(self.dataSet)-1][key] = v
        
    def getDataDefault(self):
        ds = []
        for r in self.dataSet:
            ds.append(self.rec.applyDefault(r))
        return ds
        
    def applyDefault(self, r):
        return self.rec.applyDefault(r)
        
    def getData(self, applyDefault=True):
        if applyDefault:
            return self.getDataDefault()
        return self.dataSet
    
    def getField(self, key):
        return self.dataSet[len(self.dataSet)-1][key]
    
    def parseLine(self, line):
        r = self.rec.parse(line)
        self.dataSet.append(r)
        self.lineSet.append(line)
        return r
    