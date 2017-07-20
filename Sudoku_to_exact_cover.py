import numpy as np

def basic_exact_grid(n):
    grid = np.zeros((n*n*n,n*n*4))
    colno = 0
    #CELL-NUMBER CONSTRAINT
    for ix in range(n):
        for iy in range(n):   #basically ix iy represent all the cells in a grid
            for num in range(1,n+1):
                id = getrowid(ix,iy,num,n)
                grid[id][colno] = 1
            colno += 1    
            
    #ROW-NUMBER CONSTRAINT
    for ix in range(n):
        for iy in range(n):
            for num in range(1,n+1):
                id = getrowid(ix,iy,num,n)
                grid[id][colno] = 1
                colno += 1
            colno -= n
        colno += n
        
    #COL-NUMBER CONSTRAINT
    for ix in range(n):
        for iy in range(n):
            for num in range(1,n+1):
                id = getrowid(ix,iy,num,n)
                grid[id][colno] = 1
                colno += 1
        colno -= n*n
    colno += n*n
                
    #BLOCK-NUMBER CONSTRAINT
    block_offset = n*n*3
    sqrt_n = int(n**0.5)
    for iv in range(sqrt_n):
        for iw in range(sqrt_n):
            for ix in range(sqrt_n):
                for iy in range(n):
                    for iz in range(sqrt_n):
                        x = iv*n*n*sqrt_n + iw*n*n + ix*n*sqrt_n + iz*n + iy
                        y = block_offset + iv*n*sqrt_n + ix*n + iy
                        grid[x][y] = 1 
                
    return grid

#sudoku grid is assumed to be a numpy array of shape (n*n,)
def make_sudoku_cover(sudoku,n):
    sudoku = sudoku.reshape((n,n))
    
    grid = basic_exact_grid(n)
    for ix in range(n):
        for iy in range(n):
            num = sudoku[ix][iy]
            if num != 0:      #if it is 0 , then it means it is blank which we have to fill
                for iz in range(1,n+1):
                    if num != iz:   #while making the basic exact grid, we considered all possibilities but now since the given cell
                                    #in the sudoku grid is a constant so we remove all the other possibilities considered while making the 
                                    #basic grid
                                    
                        id = getrowid(ix,iy,iz,n)
                        fillrow(grid,id,0)
    
    return grid
                
def getrowid(ix,iy,num,n):
    return (ix*n*n + iy*n + num - 1)

def fillrow(grid, rowno, value):
    cols = grid.shape[1]
    for ix in range(cols):
        grid[rowno][ix] = value
    