from nodeclass import node

def DLX(headnode):
    solution = []
    search(headnode, solution)
    return solution

def search(headnode, solutions):
    if headnode.getRight() == headnode:
        printsol(solutions)
        return 1
    column = choose(headnode)
    cover(column)
    
    row = column.getDown()
    while row != column:
        solutions.append(row)
        rightnode = row.getRight()
        while rightnode != row:
            cover(rightnode)
            rightnode = rightnode.getRight()
        x = search(headnode, solutions)
        if x == 1:
            return 1
        solutions.remove(row)
        
        leftnode = row.getLeft()
        while leftnode != row:
            uncover(leftnode)
            leftnode = leftnode.getLeft()
        row = row.getDown()
    uncover(column)
    return 0

def cover(col):
    column = col.getColumn()
    
    column.getRight().setLeft(column.getLeft())
    column.getLeft().setRight(column.getRight())
    
    row = column.getDown()
    
    while row != column:
        rightnode = row.getRight()
        while rightnode != row:
            rightnode.getUp().setDown(rightnode.getDown())
            rightnode.getDown().setUp(rightnode.getUp())
            
            rightnode = rightnode.getRight()
        row = row.getDown()
        
def uncover(col):
    column = col.getColumn()
    
    row = column.getUp()
    
    while row != column:
        leftnode = row.getLeft()
        while leftnode != row:
            leftnode.getUp().setDown(leftnode)
            leftnode.getDown().setUp(leftnode)
            leftnode = leftnode.getLeft()
        row = row.getUp()
            
    column.getRight().setLeft(column)
    column.getLeft().setRight(column)

def choose(headnode):
    result = node()
    mincnt = 10
    temp = node()
    temp = headnode.getRight()
    while temp != headnode:
        if temp.getSize() < mincnt:
            mincnt = temp.getSize()
            result = temp.getColumn()
        temp = temp.getRight()
    
    return result

def printsol(solution):
    result = []
    for ix in solution:
        temparr = []
        temparr.append(ix.getLocation())
        temp = ix.getRight()
        while temp != ix:
            temparr.append(temp.getLocation())
            temp = temp.getRight()
        result.append(temparr)
    return result
        
            