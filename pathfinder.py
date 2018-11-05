from dllist import *

class Precondition(Exception):
    def typeCheck(v,t):
        if(type(v)!=t): raise Precondition
    def precondition(b):
        if(not b): raise Precondition


class Waypoint:
    def __init__(self, x, y,distance, prevWaypoint):
        Precondition.typeCheck(x,int)
        Precondition.typeCheck(y,int)
        self.x = x
        self.y = y
        self.prev = prevWaypoint
        self.distance = distance
    
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"
    def toTuple(self):
        return (self.x,self.y)

# A path finder object isolates the logic to perform a path-finding
# problem on:
# 
#   - An underlying `board` object.
# 
#   - A `player` object, which holds the player's current position and
#   other relevant information about the player.
class PathFinder:
    def __init__(self, board, player):
        # The underlying game board on which tiles live
        self.board   = board
        
        # The underlying player object
        self.player  = player
        # The starting coordinates
        self.startX  = player.getX()
        self.startY  = player.getY()
        
        # The width / height of the board
        self.width   = self.board.width
        self.height  = self.board.height

        # A two-dimensional array to store whether or not the tile has
        # been visited.
        self.visited = [[False for x in range(board.width)]
                        for y in range(board.height)]

        #the list of waypoints that should be investigated next
        # XXX
        self.winning = False

    # Check whether `path` is a valid path
    def checkValidPath(self,path):
        return False

    # Check whether or not there is a wall (or other solid object) at
    # the coordinates (x,y)
    def wallAt(self,x,y):
        Precondition.precondition(x>=0 and x<self.width)
        Precondition.precondition(y>=0 and y<self.height)
        return self.board.higherPriorityObjectAt(self.player,x,y)
   
    def withinBounds(self,x,y):
        return (x>=0 and x<self.width and y>=0 and y<self.height)


    # Check whether or not we can move to (x,y) I.e., is there a wall
    # there, or is it out of bounds?
    def canMoveTo(self,tx,ty):
        return (self.withinBounds(tx,ty) and not self.wallAt(tx,ty))
   
   #the algorithm should never return to a tile that has already been visited. this will prevent that from happening.
    def shouldMoveTo(self,tx,ty):
        return self.canMoveTo(tx,ty) and not self.visited[tx][ty]

    def canSolve(self, toCoordinate):
        print("looking for ",toCoordinate)
        self.visited[self.startX][self.startY]=True
        return self.findNextFrontier([Waypoint(self.startX,self.startY,0,None)],toCoordinate)

    def findPath(self, toCoordinate):
        return False

    def findNextFrontier(self,frontier,toCoordinate):
        newFrontier = []
        print(frontier)
        if(frontier==[]):
            print ("frontier exhausted")
            return False #we have exhausted the frontier and have no more places to go.
        else: #in this case we are going to iterate through all of the frontier points to find new ones. 
            for o in frontier:
                #We've found the path if this is true
                print(o)
                if(o.x==toCoordinate[0] and o.y==toCoordinate[1]):
                    print("destination found at ",o.x,",",o.y)
                    return True
                
                if(self.shouldMoveTo(o.x+1,o.y)):
                    #we have now added this point to the frontier and it should be makred as such
                    self.visited[o.x+1][o.y]=True
                    newFrontier.append(Waypoint(o.x+1,o.y,o.distance+1,o))
                #repeated for each of the four possible additional accessable points
                if(self.shouldMoveTo(o.x-1,o.y)):
                    self.visited[o.x-1][o.y]=True
                    newFrontier.append(Waypoint(o.x-1,o.y,o.distance+1,o))

                if(self.shouldMoveTo(o.x,o.y+1)):
                    self.visited[o.x][o.y+1]=True
                    newFrontier.append(Waypoint(o.x,o.y+1,o.distance+1,o))

                if(self.shouldMoveTo(o.x,o.y-1)):
                    self.visited[o.x][o.y-1]=True
                    newFrontier.append(Waypoint(o.x,o.y-1,o.distance+1,o))

                print("the additional points added by frontier point ",o,"are")
                for e in newFrontier:
                    print(e)
            print ("new frontier found.")
            print(newFrontier)
            self.findNextFrontier(newFrontier,toCoordinate)
        
