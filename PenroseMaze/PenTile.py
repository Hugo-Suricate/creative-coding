PHI = (1 + sqrt(5))/2
H = sqrt(3 + 4*PHI)/(2*PHI)

class PenTile:
    id = 0
    type = False #False:acute, True obtuse ### False:kite, True dart
    parity = False
    x, y, rotation = 0,0,0
    neighbours = []
    
    def __init__(self,id, type, parity, x, y, rot):
        self.id = id
        self.type = type
        self.parity = parity
        self.x = x
        self.y = y
        self.rotation = rot
    
    def split(self):
        res = []
        if self.type:
            if self.parity:
                res.append(PenTile(0, True, True, PHI-1, (2*(PHI-1))*H, 6*PI/5))
                res.append(PenTile(0, False, True, 0, 0, 0))
            else:
                res.append(PenTile(0, True, False, PHI-1, -(2*(PHI-1))*H, 4*PI/5))
                res.append(PenTile(0, False, False, 0, 0, 0))
        else:
            if self.parity:
                res.append(PenTile(1, True, False, 0.5-PHI, H*(2-PHI), PI/5))
                res.append(PenTile(1, False, True, 1-0.5*PHI, H*(PHI-1), 7*PI/5))
                res.append(PenTile(1, False, False, 1-0.5*PHI, H*(PHI-1), 7*PI/5))
            else:
                res.append(PenTile(1, True, True, 0.5-PHI, -H*(2-PHI), -PI/5))
                res.append(PenTile(1, False, False, 1-0.5*PHI, -H*(PHI-1), 3*PI/5))
                res.append(PenTile(1, False, True, 1-0.5*PHI, -H*(PHI-1), 3*PI/5))
        
        c, s = cos(self.rotation), sin(self.rotation)
        for tile in res:
            new_x = PHI*self.x + c*tile.x - s*tile.y
            new_y = PHI*self.y + s*tile.x + c*tile.y
            new_rot = self.rotation + tile.rotation
            tile.x, tile.y, tile.rotation = new_x, new_y, new_rot
        return res
