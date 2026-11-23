from PenTile import *
from PenRenderer import PenRenderer as Renderer
from PenGenerator import PenGenerator as Generator

renderer = None
generator = None

def setup():
    global tile_set
    global renderer
    global generator
    size(1000,1000)
    translate(500,500)
    background(255)
    
    # randomSeed(0)
    
    renderer = Renderer()
    generator = Generator()
    
    tile_set = []
    
    for i in range(5):
        angle = 2*i*PI/5
        tile_set.append(PenTile(0, False, False, cos(angle), sin(angle), angle))
        tile_set.append(PenTile(0, False, True, cos(angle), sin(angle), angle))

    # for tile in tile_set:
    #     fill(random(255), random(255), random(255))
    #     drawTile(tile)

    Split(6)
    
    graph_nodes, graph_edges = generator.initGraph(tile_set)
    maze_edges = generator.createMaze()

    for tile in graph_nodes:
        renderer.drawTile(tile)
    for tile_index in range(len(graph_nodes)):
        connect = generator.getConnect(tile_index)
        renderer.drawMazeTile(graph_nodes[tile_index], connect)

    # for t in graph_edges.keys():
    #     for t2 in graph_edges[t]:
    #         if t2 > t:
    #             if random(1)<0.2:
    #                 continue
    #             renderer.drawLine(graph_nodes[t], graph_nodes[t2])
    for t in maze_edges.keys():
        for t2 in maze_edges[t]:
            if t2 > t:
                renderer.drawLine(graph_nodes[t], graph_nodes[t2])
    # print(maze_edges)
    # save("graph.png")

def draw():
    pass

def Split(n=1):
    if n <= 0:
        return
    
    global tile_set
    temp_tile_set = []
    for tile in tile_set:
        for split_tile in tile.split():
            temp_tile_set.append(split_tile)
    tile_set = temp_tile_set
    # print(len(tile_set))
    
    Split(n-1)
