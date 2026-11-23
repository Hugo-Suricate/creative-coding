from PenTile import *

tile_set = []
graph_nodes = []
graph_edges = {}
maze_edges = {}

class PenGenerator:
        
    def initGraph(self, tiles):
        global tile_set
        global graph_nodes
        global graph_edges

        for tile in tiles:
            if not tile.parity:
                continue
            graph_nodes.append(tile)
        
        for t in range(len(graph_nodes)):
            tile = graph_nodes[t]
            graph_edges[t] = []
            for t2 in range(len(graph_nodes)):
                tile2 = graph_nodes[t2]
                d = sqrt(sq(tile2.x - tile.x) + sq(tile2.y - tile.y))
                if d > 0.01 and d < 1.5 and not (d > 1.175 and d < 1.176 and tile.type and tile2.type):
                    graph_edges[t].append(t2)
                
            # print(len(graph_edges[t]))
        return graph_nodes, graph_edges
    
    def createMaze(self):
        global graph_nodes
        global graph_edges
        global maze_edges
        
        open_visited = []
        
        # init maze_edges
        for t in range(len(graph_nodes)):
            maze_edges[t] = []
        
        # init with first node
        current = int(random(len(graph_nodes)))
        open_visited.append(current)
        c = 0
    
        while c < len(graph_nodes) -1:
            
            if len(open_visited) < 6:
                current = open_visited[int(random(len(open_visited)))]
            elif random(1) < 0.98:
                current = open_visited[len(open_visited)-1]
            else:
                current = open_visited[int(random(len(open_visited)))]
            neighs = []
            
            for i in self.neighbors(current):
                if len(maze_edges[i]) == 0:
                    neighs.append(i)
            
            if len(neighs) == 0:
                open_visited.remove(current)
                continue
            
            neigh = neighs[int(random(len(neighs)))]
            open_visited.append(neigh)
            maze_edges[current].append(neigh)
            maze_edges[neigh].append(current)
            
            c +=1
        
        return maze_edges
    
    def neighbors(self, tile_index):
        return graph_edges[tile_index]
        
    def getConnect(self, tile_index):
        tile = graph_nodes[tile_index]
        connect = [False, False, False, False]
        for n in maze_edges[tile_index]:
            neigh = graph_nodes[n]
            angle = PVector(neigh.x - tile.x, neigh.y - tile.y).heading() - tile.rotation
            connect[int((10-angle / (PI/2)))%4] = True
        return connect
