'''
Created on 23 de jul de 2018

@author: Renan
'''
import operator
import os.path
import re

from areacont import areacont
from cotasr11 import cotasr11
from curvtviag import curvtviag
from dadvaz import dadvaz
from deflant import deflant
from desselet import desselet
from dessem import dessem
from eletbase import eletbase
from entdados import entdados
from ils_tri import ils_tri
from infofcf import infofcf
from operuh import operuh
from operut import operut
from ptoper import ptoper
from respot import respot
from termdat import termdat
from tolperd import tolperd


def listCases(reFile='.*'):
    cl = ['dessem', 'dadvaz', 'infofcf', 'operuh', 'deflant', 'termdat', 'operut', 
          'ptoper', 'areacont', 'respot', 'desselet', 'eletbase', 'eletmodif', 'entdados', 
          'ils_tri', 'cotasr11', 'tolperd', 'curvtviag']
    
    pattern = re.compile(reFile)
    fcl = []
    for c in cl:
        if pattern.match(c) is not None:
            fcl.append(c)
    return fcl

def case(opt):
    xmlFile = 'cfg/{:s}.xml'.format(opt)
    cfg = {'xml': xmlFile}
    
    if opt == 'dessem':
        return [dessem(cfg), 'dessem.arq']
    if opt == 'dadvaz':
        return [dadvaz(cfg), 'dadvaz.dat']
    if opt == 'infofcf':
        return [infofcf(cfg), 'infofcf.dat']
    if opt == 'operuh':
        return [operuh(cfg), 'operuh.dat']
    if opt == 'deflant':
        return [deflant(cfg), 'deflant.dat']
    if opt == 'termdat':
        return [termdat(cfg), 'termdat.dat']
    if opt == 'operut':
        return [operut(cfg), 'operut.dat']
    if opt == 'ptoper':
        return [ptoper(cfg), 'ptoper.dat']
    if opt == 'areacont':
        return [areacont(cfg), 'areacont.dat']
    if opt == 'respot':
        return [respot(cfg), 'respot.dat']
    if opt == 'desselet':
        return [desselet(cfg), 'desselet.dat']
    if opt == 'eletbase':
        return [eletbase(cfg), 'leve.pwf']
    if opt == 'eletmodif':
        return [eletbase(cfg, muda=True), 'pat01.afp']
    if opt == 'entdados':
        return [entdados(cfg), 'entdados.dat']
    if opt == 'ils_tri':
        return [ils_tri(cfg), 'ils_tri.dat']
    if opt == 'cotasr11':
        return [cotasr11(cfg), 'cotasr11.dat']
    if opt == 'tolperd':
        return [tolperd(cfg), 'tolperd.dat']
    if opt == 'curvtviag':
        return [curvtviag(cfg), 'curvtviag.dat']
    
    raise ValueError

def showHeader(opt):
    cs = case(opt)
    print('*'*50 + '\nHeader for case "{:s}"\n'.format(opt) + '*'*50)
    cs[0].showHeader()
    
def dsFileTest(dirDS, opt):
    cs = case(opt)
    dsFile = cs[0]
    fileName = cs[1]
    fullPath = dirDS + fileName
    
    print('-'*50 + '\nTest reading "{:s}"'.format(opt))
    if fileName is None:
        print('Missing file name')
    elif not os.path.isfile(fullPath):
        print('Missing file "{:s}"'.format(fileName)) 
    else:
        dsFile.test(fullPath, maxLines=5)

def fieldSearch(reField='.*', reRec='.*', reFile='.*'):
    fields = dict()
    for opt in listCases(reFile):
        cs = case(opt)
        fd = cs[0].listFields(reField, reRec)
        for f in fd:
            if f not in fields:
                fields[f] = []
            for r in fd[f]:
                fields[f].append('{:s}.{:s}'.format(opt, r))
        
    capt = 'List fields "{:s}" in "{:s}\\{:s}" (total: {:d})\n'.format(reField, reFile, reRec, len(fields))
    print(capt + '-'*50)
    sortedF = sorted(fields.items(), key=operator.itemgetter(0))
    for f in sortedF:
        spc = '\t\t' if len(f[0]) < 7 else '\t'
        print('{:s}:{:s}[{:s}]'.format(f[0], spc, ', '.join(f[1])))
    print('-'*50)
