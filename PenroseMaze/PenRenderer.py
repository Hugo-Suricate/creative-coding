from PenTile import *
t_scale = 16

class PenRenderer:
    
    def drawTile(self, tile):
        if not tile.parity:
            return
        
        stroke(220,220,255)
        strokeWeight(2)
        noFill()
        
        pushMatrix()
        translate(t_scale*tile.x,t_scale*tile.y)
        rotate(tile.rotation)
        if tile.type:
            # fill(130,150,0)
            quad(t_scale*(1-PHI), 0, t_scale*0.5*(3-PHI), t_scale*H, t_scale*(2-PHI), 0, t_scale*0.5*(3-PHI), t_scale*-H)
            # if tile.parity:
            #     triangle(t_scale*(1-PHI), 0, t_scale*0.5*(3-PHI), t_scale*H, t_scale*(2-PHI), 0)
            # else:
            #     triangle(t_scale*(1-PHI), 0, t_scale*0.5*(3-PHI), t_scale*-H, t_scale*(2-PHI), 0)
        else:
            # fill(100,170,0)
            quad(t_scale*-1, 0, t_scale*0.5*(PHI-1), t_scale*H, t_scale*(PHI-1), 0, t_scale*0.5*(PHI-1), t_scale*-H)
            # if tile.parity:
            #     triangle(t_scale*-1, 0, t_scale*0.5*(PHI-1), t_scale*H, t_scale*(PHI-1), 0)
            # else:
            #     triangle(t_scale*-1, 0, t_scale*0.5*(PHI-1), t_scale*-H, t_scale*(PHI-1), 0)
        popMatrix()
        
    def drawMazeTile(self, tile, connect = [False, False, True, False]):
        if not tile.parity:
            return
        
        pathWidth = 0.3
        p, p2 = (1-pathWidth)/2, (PHI-pathWidth)/(2*PHI)
        q, q2 = 1-p, 1-p2
        
        fill(255,0,0)
        
        pushMatrix()
        translate(t_scale*tile.x,t_scale*tile.y)
        rotate(tile.rotation)
        
        if tile.type:
            poly = [ t_scale*PVector(1-PHI, 0), t_scale*PVector(0.5*(3-PHI), H), t_scale*PVector(2-PHI, 0), t_scale*PVector(0.5*(3-PHI), -H)]
            inter1 = [p2*poly[0] + q2*poly[1] + 0.04*(poly[0]-poly[1]).rotate(PI/2), p*poly[1] + q*poly[2] + 0.2*(poly[1]-poly[2]).rotate(PI/2), p*poly[2] + q*poly[3] + 0.28*(poly[2]-poly[3]).rotate(PI/2), p2*poly[3] + q2*poly[0] + 0.2*(poly[3]-poly[0]).rotate(PI/2)]
            inter2 = [p2*poly[1] + q2*poly[0] + 0.2*(poly[0]-poly[1]).rotate(PI/2), q*poly[1] + p*poly[2] + 0.28*(poly[1]-poly[2]).rotate(PI/2), q*poly[2] + p*poly[3] + 0.2*(poly[2]-poly[3]).rotate(PI/2), p2*poly[0] + q2*poly[3] + 0.04*(poly[3]-poly[0]).rotate(PI/2)]
            
        else:
            poly = [ t_scale*PVector(-1, 0), t_scale*PVector(0.5*(PHI-1), H), t_scale*PVector(PHI-1, 0), t_scale*PVector(0.5*(PHI-1), -H)]
            inter1 = [p2*poly[0] + q2*poly[1] + 0.4*(poly[0]-poly[1]).rotate(PI/2), p*poly[1] + q*poly[2] + 0.4*(poly[1]-poly[2]).rotate(PI/2), p*poly[2] + q*poly[3] + 0.6*(poly[2]-poly[3]).rotate(PI/2), p2*poly[3] + q2*poly[0] + 0.4*(poly[3]-poly[0]).rotate(PI/2)]
            inter2 = [p2*poly[1] + q2*poly[0] + 0.4*(poly[0]-poly[1]).rotate(PI/2), q*poly[1] + p*poly[2] + 0.6*(poly[1]-poly[2]).rotate(PI/2), q*poly[2] + p*poly[3] + 0.4*(poly[2]-poly[3]).rotate(PI/2), p2*poly[0] + q2*poly[3] + 0.4*(poly[3]-poly[0]).rotate(PI/2)]
        
        pl,ql = [p2,p,p,p2], [q2,q,q,q2]
        
        beginShape()
        noStroke()
        i = 0
        j = i+1
        while i<4:
            if not connect[i]:
                i = i+1
                j = (i+1) % 4
                continue
            if not connect[j]:
                j = (j+1) % 4
                continue
            
            A1 = poly[i]
            A2 = poly[(i+1)%4]
            B1 = poly[j]
            B2 = poly[(j+1)%4]
            
            vertex(pl[i]*A1.x+ql[i]*A2.x, pl[i]*A1.y+ql[i]*A2.y)
            bezierVertex(inter1[i].x, inter1[i].y, inter2[j].x, inter2[j].y, pl[j]*B2.x+ql[j]*B1.x, pl[j]*B2.y+ql[j]*B1.y)
            
            if j <= i:
                break
            i = j
            j = (i+1) % 4

        endShape(CLOSE)
        
        popMatrix()
    
    def drawCenter(self, tile):
        fill(255,0,0)
        circle(t_scale*tile.x, t_scale*tile.y, 5)
    
    def drawLine(self, tile, tile2):
        stroke(0)
        strokeWeight(4)
        line(t_scale*tile.x, t_scale*tile.y, t_scale*tile2.x, t_scale*tile2.y)

# if tile.type:
#     poly = [ t_scale*PVector(1-PHI, 0), t_scale*PVector(0.5*(3-PHI), H), t_scale*PVector(2-PHI, 0), t_scale*PVector(0.5*(3-PHI), -H)]
#     inter1 = [p2*poly[0] + q2*poly[1] + 0.04*(poly[0]-poly[1]).rotate(PI/2), p*poly[1] + q*poly[2] + 0.2*(poly[1]-poly[2]).rotate(PI/2), p*poly[2] + q*poly[3] + 0.28*(poly[2]-poly[3]).rotate(PI/2), p2*poly[3] + q2*poly[0] + 0.2*(poly[3]-poly[0]).rotate(PI/2)]
#     inter2 = [q*poly[1] + p*poly[2] + 0.28*(poly[1]-poly[2]).rotate(PI/2), q*poly[2] + p*poly[3] + 0.2*(poly[2]-poly[3]).rotate(PI/2), p2*poly[0] + q2*poly[3] + 0.04*(poly[3]-poly[0]).rotate(PI/2), p2*poly[1] + q2*poly[0] + 0.2*(poly[0]-poly[1]).rotate(PI/2)]
    
# else:
#     poly = [ t_scale*PVector(-1, 0), t_scale*PVector(0.5*(PHI-1), H), t_scale*PVector(PHI-1, 0), t_scale*PVector(0.5*(PHI-1), -H)]
#     inter1 = [p2*poly[0] + q2*poly[1] + 0.4*(poly[0]-poly[1]).rotate(PI/2), p*poly[1] + q*poly[2] + 0.4*(poly[1]-poly[2]).rotate(PI/2), p*poly[2] + q*poly[3] + 0.6*(poly[2]-poly[3]).rotate(PI/2), p2*poly[3] + q2*poly[0] + 0.4*(poly[3]-poly[0]).rotate(PI/2)]
#     inte
