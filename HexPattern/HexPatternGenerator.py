from Hex import Hex

#Pattern parameters
radius = 12
hexcount = 1 + 6*radius*(radius+1)/2
pattern_count = 3

hexes = {}
patterns = []
open_indexes = []
seed = 0

#################################
######### MAIN FUNCTIONS
#################################

def Init():
    global hexes
    global patterns
    global open_indexes
    
    randomSeed(seed)
    
    hexes.clear()
    patterns = []
    open_indexes = []
    
    hexes[Hex(0,0,0)] = 0
    
    for i in range(pattern_count):
        initPattern()

def Generate():
    global hexes
    global patterns
    global open_indexes
    Init()
    
    while len(hexes) < hexcount:
        if chooseOpenPattern() == -1:
            print "BIG FAIL"
            return False
        
        if Step():
            if (int(len(hexes)%(0.05*hexcount)) == 0):
                print(str(5*int(len(hexes)*20/hexcount)) + "%")
    
    println("Generated " + str(len(hexes)) + " tiles out of " + str(hexcount) + ".")
    return patterns

def Step(): #returns true if Hex was succesfully added
    global hexes
    global order_lists
    global open_indexes
    
    i = chooseOpenPattern()
    if i == -1:
        return False
    
    h = patterns[i][open_indexes[i]]
    neighbours = h.neighbours()
    
    free_neighbours = []
    for k in range(len(neighbours)):
        neighbours[k].normalize()
        if max(neighbours[k].x, neighbours[k].y, neighbours[k].z) <= radius and not hexes.has_key(neighbours[k]):
            if open_indexes[i] == 0 or patterns[i][open_indexes[i]-1] in neighbours[k].neighbours():
                free_neighbours.append(k)
    
    if len(free_neighbours) == 0:
        open_indexes[i] += 1
        return False
    
    i_neighbour = free_neighbours[int(random(len(free_neighbours)))]
    neighbour = neighbours[i_neighbour]
    
    patterns[i].insert(open_indexes[i], neighbour)
    addWithSymmetry(neighbour,hexes[h] + 1)
    return True


#################################
###### PARAMETER SETTING ########
#################################

def setRadius(r):
    global radius
    radius = r
    global hexcount
    hexcount = 1 + 6*r*(r+1)/2

def newSeed():
    global seed
    randomSeed(millis())
    seed = int(random(1000))

#############################
##### UTILITY FUNCTIONS #####
#############################

def addWithSymmetry(h, val):
    global hexes
    hexes[h] = val
    #3 fold symmetry
    if h != Hex(0,0,0):
        hexes[h.rotated3()] = val
        hexes[h.rotated3().rotated3()] = val

def initPattern():
    global hexes
    global patterns
    global open_indexes
    
    h0 = Hex(int(random(0,radius)),int(random(0,radius)),int(random(0,radius)))
    while h0 in hexes:
        h0 = Hex(int(random(0,radius)),int(random(0,radius)),int(random(0,radius)))
    
    addWithSymmetry(h0,0)
    patterns.append([h0])
    open_indexes.append(0)

def chooseOpenPattern():
    global patterns
    global open_indexes

    free_patterns = []
    for k in range(pattern_count):
        if open_indexes[k] < len(patterns[k]):
            free_patterns.append(k)
    
    if len(free_patterns) == 0:
        return -1
    return free_patterns[int(random(len(free_patterns)))]
