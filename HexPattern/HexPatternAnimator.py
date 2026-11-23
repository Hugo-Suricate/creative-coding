from Hex import Hex

#Display
disp_h = 900
disp_w = 900
disp_size = 35;
show_seed = True
seed_color = 0
amount = 1

#Colors
# colors = [color(255,245,230), color(255,245,230), color(255,245,230), color(195,185,220), color(255,40,30)]
colors = [color(255,245,230), color(255,40,30), color(235,210,150), color(255,245,230), color(255,40,30), color(235,210,150)]

#Working variables
vecX = PVector(0    * disp_size, -sqrt(3)/2 * disp_size)
vecY = PVector(0.75  * disp_size, sqrt(3)/4  * disp_size)
vecZ = PVector(-0.75 * disp_size, sqrt(3)/4  * disp_size)

seed = 0

def Render(patterns, seed = 0):
    global colors
    global seed_color
    global amount
    
    amount += 1
    
    background(color(40,40,40))
    translate(disp_h/2,disp_w/2)
    
    for i in range(len(patterns)):
        drawLineWithSymmetry(patterns[i], colors[i])
    
    translate(-disp_h/2,-disp_w/2)
    
    grunge = loadImage("grunge.png")
    tint(0,0,0,80)
    image(grunge, 0, 0)

    
    if show_seed:
        fill(255)
        textSize(20)
        text("#" + format(seed, "03d") + "-" + format(seed_color, "03d"), 0, 0 + 20)

def AnimationInit():
    Animator.setParams()
    Animator.Init()

def AnimationDraw():
    Animator.Step()

#################################
###### PARAMETER SETTING ########
#################################

def newColors(count):
    global colors
    global seed_color
    randomSeed(millis())
    seed_color = int(random(1000))
    randomSeed(seed_color)
    colors = []
    for i in range(count):
        colors.append(color(int(random(256)), int(random(256)), int(random(256))))


#################################
###### UTILITY FUNCTIONS ########
#################################

def orientationToVector(o):
    o = o%6
    res = PVector(0,0)
    if o==5 or o==0 or o==1:
        res += vecX
    if o==1 or o==2 or o==3:
        res += vecY
    if o==3 or o==4 or o==5:
        res += vecZ
    return res

def hexToVector(h):
    return h.x * vecX + h.y * vecY + h.z * vecZ

def colorFromVal(val):
    table = [color(0,0,0), color(64,0,0), color(128,0,0), color(194,0,0), color(255,0,0)]
    #return table[val%5]
    return color((20*val)%255, 0, 0)

def drawHex(h, col):
    pushMatrix()
    translate(h.x * vecX.x + h.y * vecY.x + h.z * vecZ.x, h.x * vecX.y + h.y * vecY.y + h.z * vecZ.y)
    fill(col)
    beginShape()
    noStroke()
    for i in range(6):
        vertex((0.5*disp_size+0.5)*cos(TWO_PI*i/6), (0.5*disp_size+0.5)*sin(TWO_PI*i/6))
    endShape(CLOSE)
    popMatrix()

def drawLine(line, col):
    fill(col)
    beginShape()

    global amount
    line_amount = constrain(amount, 2, len(line))
    line = line[0:line_amount:]
    
    line = [line[1]] + line + line[-2::-1]
    for i in range(1, len(line)-1):
        prev = line[i-1]
        current = line[i]
        next = line[i+1]
        o_start = current.orientationTo(prev)+1
        o_end = current.orientationTo(next)
        if o_end < o_start: 
            o_end += 6
        for k in range(o_start, o_end):
            v = hexToVector(current) + (0.40 + random(-0.06,0.06))*orientationToVector(k)
            vertex(v.x, v.y)
    
    endShape(CLOSE)

def drawLineWithSymmetry(line, col):
    drawLine(line, col)
    for i in range(len(line)):
        line[i] = line[i].rotated3()
    drawLine(line, col)
    for i in range(len(line)):
        line[i] = line[i].rotated3()
    drawLine(line, col)
