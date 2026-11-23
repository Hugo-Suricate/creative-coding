class Hex:
    
    x = 0
    y = 0
    z = 0
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def neighbours(self):
        n = [0,0,0,0,0,0]
        n[0] = Hex(self.x+1, self.y  , self.z  )
        n[1] = Hex(self.x+1, self.y+1, self.z  )
        n[2] = Hex(self.x  , self.y+1, self.z  )
        n[3] = Hex(self.x  , self.y+1, self.z+1)
        n[4] = Hex(self.x  , self.y  , self.z+1)
        n[5] = Hex(self.x+1, self.y  , self.z+1)
        return n
    
    def neighboursRotated(self):
        n = [0,0,0,0,0,0]
        shift = (6-getQuadrant())
        n[(0+shift)%6] = Hex(self.x+1, self.y  , self.z  )
        n[(1+shift)%6] = Hex(self.x+1, self.y+1, self.z  )
        n[(2+shift)%6] = Hex(self.x  , self.y+1, self.z+1)
        n[(4+shift)%6] = Hex(self.x  , self.y  , self.z+1)
        n[(5+shift)%6] = Hex(self.x+1, self.y  , self.z+1)
        return n
    
    def getQuadrant(self):
        if self.x > self.y and self.y >= self.z:
            return 0
        elif self.y >= self.x and self.x > self.z:
            return 1
        elif self.y > self.z and self.z >= self.x:
            return 2
        elif self.z >= self.y and self.y > self.x:
            return 3
        elif self.z > self.x and self.x >= self.y:
            return 4
        else:
            return 5
    
    def normalize(self):
        if self.x <= self.y and self.x <= self.z:
            self.y -= self.x
            self.z -= self.x
            self.x = 0
        elif self.y <= self.x and self.y <= self.z:
            self.x -= self.y
            self.z -= self.y
            self.y = 0
        elif self.z <= self.x and self.z <= self.y:
            self.x -= self.z
            self.y -= self.z
            self.z = 0
    
    def rotated3(self):
        return Hex(self.y,self.z,self.x)
    
    def orientationTo(self, other):
        return Hex(other.x-self.x, other.y-self.y, other.z-self.z).getQuadrant()
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.x-self.y == other.x-other.y) and (self.y-self.z == other.y-other.z) and (self.z-self.x == other.z-other.x)
        else:
            return False

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ")"
    
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        self.normalize()
        return self.x + self.y*256 + self.z*65536
