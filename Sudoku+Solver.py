
# coding: utf-8

# In[39]:


import numpy as np
import pandas as pd
from DancingLinksBundle.makelistgrid import makelistgrid as makeListGrid
from DancingLinksBundle.nodeclass import node
import DancingLinksBundle.DLX as DLX
import DancingLinksBundle.Sudoku_to_exact_cover as sudokuToExactCover


# In[8]:


n = 9
m = n


# In[37]:


#INPUT THE DATA SPARSE MATRIX
matrix = np.zeros((m,n))
f = open("./Sample Sudoku Inputs/easy.txt")
data = f.read()
print (len(data))
boards = []
#print (board.shape)
break_point = data[n*n]
temp = np.zeros((n*n,))
index = 0
for ix in range(len(data)):
    if data[ix] == break_point:
        boards.append(temp)
        temp = np.zeros((n*n,))
        index = 0
        continue
    if data[ix] != ".":
        temp[index] = int(data[ix])
    index += 1
#print (boards)
#print (data)


# In[35]:


print (boards[0])


# In[48]:


for ix in range(len(boards)):
    sudoku = boards[ix]
    sudoku_binary = sudokuToExactCover.make_sudoku_cover(n=n, sudoku=sudoku)
    
    #we may need to make columnode, headnode and links separately for all boards but lets just skip it for now and test wether we need to or not
    linksmatrix, columnodearray, headnode = makeListGrid(grid=sudoku_binary)
    x = DLX.DLX(headnode)
    solution = []
    if x == []:
        print ("No Solution Possible")
    else:
        solution = DLX.printsol(x)
    answer = []
    for ix in range(len(solution)):
        for iy in solution[ix]:
            if iy[1]<n*n: #basically a cell is represented by four constraints and we can get our original cell info in (row,col,num)format by just looking at the cell-number constraint, so basically we chose that constraint out of the four and built the usable infodatatype
                col = iy[1]%n
                row = int(iy[1]/n)
                value = iy[0]%n + 1
                answer.append((row,col,value))
                break
    answer.sort(key = lambda x: (x[0],x[1]))
    columncount=0
    for iy in answer:
        print (iy[2]),
        columncount = columncount + 1
        if (columncount == 9):
            columncount = 0
            print 
    print


# In[ ]:




