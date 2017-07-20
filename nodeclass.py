class node:
    def __init__(self,loc = (-1,-1), iscolumn = False,  colsize=0):
        self.iscolumnnode = iscolumn
        self.sizeofcolumn = colsize
        self.location = loc
        
        #self-wrapping node
        self.columnode = self
        self.right = self
        self.left = self
        self.up = self
        self.down = self
    
    def getRight(self):
        return self.right
    
    def getLeft(self):
        return self.left
    
    def getUp(self):
        return self.up
    
    def getDown(self):
        return self.down
    
    def getColumn(self):
        return self.columnode
    
    def getSize(self):
        return self.sizeofcolumn
    
    def getLocation(self):
        return self.location
    
    def setRight(self, nextnode):
        self.right = nextnode
        
    def setDown(self, nextnode):
        self.down = nextnode
        
    def setUp(self, nextnode):
        self.up = nextnode
        
    def setLeft(self, nextnode):
        self.left = nextnode
        
    def setCol(self, nextnode):
        self.columnode = nextnode
        
    def updateSize(self, num):
        self.sizeofcolumn += num