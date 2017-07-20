from nodeclass import node

def makelistgrid(grid):
    
    shape = grid.shape
    m = shape[0]
    n = shape[1]
    links = [[node() for x in range(n) ] for y in range (m)]
    columnode = [node() for x in range(n)]
    headnode = node()
    #INITIALIZING THE INDIVIDUAL NODES
    for ix in range(m):
        for iy in range(n):
            if grid[ix][iy] == 0:
                links[ix][iy] = None;
            else:
                links[ix][iy] = node(loc=(ix,iy))

    #MAKING COLUMNHEAD ROW
    for ix in range(n):
        columnode[ix] = node(loc=(ix,-1), colsize=0, iscolumn=True)

    for ix in range(1,n-1):
        columnode[ix].setRight(columnode[ix+1])
        columnode[ix].setLeft(columnode[ix-1])

    columnode[0].setLeft(headnode)
    columnode[0].setRight(columnode[1])
    columnode[n-1].setRight(headnode)
    columnode[n-1].setLeft(columnode[n-2])

    headnode.setLeft(columnode[n-1])
    headnode.setRight(columnode[0])
    
    head = node()
    temp = node()
    
    #MAKING LINKS IN A ROW FOR ALL ROWS
    for ix in range(m):
        head = None
        temp = None
        for iy in range(n):
            if links[ix][iy] != None:
                if head == None:
                    head = links[ix][iy]
                    temp = links[ix][iy]
                else:
                    temp.setRight(links[ix][iy])
                    links[ix][iy].setLeft(temp)
                    head.setLeft(links[ix][iy])
                    links[ix][iy].setRight(head)
                    temp = temp.getRight()
    
    #MAKING LINKS IN A COL FOR ALL COLS
    for iy in range(n):
        head = None
        temp = None
        for ix in range(m):
            if links[ix][iy] != None:
                if head == None:
                    head = links[ix][iy]
                    temp = links[ix][iy]
                    temp.setUp(columnode[iy])
                    temp.setDown(columnode[iy])
                    temp.setCol(columnode[iy])
                    columnode[iy].setDown(links[ix][iy])
                else:
                    temp.setDown(links[ix][iy])
                    links[ix][iy].setUp(temp)
                    links[ix][iy].setDown(columnode[iy])
                    links[ix][iy].setCol(columnode[iy])
                    temp = temp.getDown()
                columnode[iy].updateSize(1)
        if temp != None:
            columnode[iy].setUp(temp)
    return links,columnode,headnode