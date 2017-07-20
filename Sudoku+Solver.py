
# coding: utf-8

# In[1]:

import numpy as np
from makelistgrid import makelistgrid 
from nodeclass import node
import DLX
import Sudoku_to_exact_cover


# In[2]:

m = 9
n = 9
links = [[node() for x in range(n) ] for x in range (m)]
columnnode = [node() for x in range(n)]
headnode = node()


# In[3]:

#INPUT THE DATA SPARSE MATRIX
matrix = np.zeros((m,n))
for ix in range(m):
    for iy in range(n):
        matrix[ix][iy] = input()


# In[4]:

sudoku_binary = Sudoku_to_exact_cover.make_sudoku_cover(n=m, sudoku=matrix)
makelistgrid(columnode= columnnode, grid=sudoku_binary, headnode=headnode, links=links, m=m, n=n)


# In[5]:

x = DLX.DLX(headnode)
if x == []:
    print ("No Vertex Exact Cover")
else:
    DLX.printsol(x)

