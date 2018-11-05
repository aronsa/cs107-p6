# Doubly-linked list implementation

# 
# Modify this file
#

class PostconditionException(Exception):
    pass

class NoSuchLink(Exception):
    pass

# A double link has three fields
#  - data <-- The underlying data the link is storing
#  - back <-- A reference to the previous element
#             (possibly None)
#  - next <-- A reference to the next element
#             (possibly None)
class DoubleLink:
    def __init__(self,data,back,nxt):
        self.data    = data
        self.prevLnk = back
        self.nextLnk = nxt

    # Make this object work with "deep" equality. See this
    # StackOverflow post:
    #     https://stackoverflow.com/questions/1227121/compare-object-instances-for-equality-by-their-attributes-in-python
    def __eq__(self, other): 
        if (other):
            return self.__dict__ == other.__dict__
        return False
    def __str__(self):
        return str(self.data)
    def hasNext(self):
        return (self.nextLnk != None)
    
    def hasPrev(self):
        return (self.prevLnk != None)

    def getData(self):
        return self.data

    def getNext(self):
        return self.nextLnk

    def getPrev(self):
        return self.prevLnk

    def setNext(self, n):
        self.nextLnk = n

    def setPrev(self, n):
        self.prevLnk = n


#A doubly-linked list
# 15 points
class DLList:
    # Constructor for empty doubly-linked list
    def __init__(self):
        self.first = None

    # Calculate the size of the list
    #  1 points
    def size(self):
        #edge case handled
        link = self.first
        i=0
        while(link != None):
            link = link.getNext()
            i+=1
        return i
        

    # Check whether this doubly-linked list is equal to another
    # list. Two lists should be equal when they contain exactly the
    # same sequence of elements, where the comparison of each object
    # happens using the == operator.
    # 
    # I.e., two lists (e.g., created using distinct calls to the
    # DoublyLinkedList constructor and subsequent calls to add)
    # containing the sequence of elements: 
    # 
    #   (1,1), (0,1), (1,0)
    # 
    # Should be equal
    #   2 points
    def __eq__(self, other):

        if(self.size()!=other.size()):
            return False
        i = 0
        a = self.first
        b = other.first
        if(a == None): return True
        while(i<self.size()):
            if(self.first.getData() != other.first.getData()): return False
            a = a.getNext()
            b = b.getNext()
            i+=1
        return True

    # Add some data at the head of a doubly-linked list This should
    # take O(1) time
    #   2 points
    def add(self, data):
        #this will set the new data as the head and link the previoushead back to the new head.
        previousHead = self.first
        self.first = DoubleLink(data,None,previousHead)
        if(previousHead != None): previousHead.setPrev(self.first)
        if(self.first.getData() != data or self.first.getNext() != previousHead): raise PostconditionException

    # Remove some piece of data from the list. Compare for equality of
    # data using ==
    #   2 points
    def remove(self,data):
        d = self.first
        isFound = False
        while(not isFound):
            if(d.getData() == data): isFound = True
            if(not d.hasNext()): raise NoSuchElementException
            d = d.getNext()
        #once the element is found, it will be eliminated by referencing the next and previous elements instead.
        if(d.hasNext()):
            d.getNext().setPrev(d.getPrev())
        if(d.hasPrev()):
            d.getPrev().setNext(d.getNext())
    # Check whether the list contains `data`
    #   2 points
    def contains(self, data):
        d = self.first
        isFound= False
        if(self.first==None):return self.first==data #to handle nones
        while(not isFound):
            if(d.getData()==data):return True
            elif(not d.hasNext()): return False #we have iterated through th elist
            else: d=d.getNext()

    # Reverse this linked-list in place. After a call to reverse, the
    # last element of the list should become the first, etc...
    #   2 points
    def reverse(self):
        def reverseHelper(d):
            print(d.getData())
            oldNext = d.getNext()
            oldPrev = d.getPrev()
            d.setNext(oldPrev)
            d.setPrev(oldNext)
            if(d.hasPrev()): reverseHelper(d.getPrev())
            return d 
        
        data= self.first
        if(data==None): return None #we're done and should escape at this point.
        self.first = reverseHelper(data)
        
        print(self.toArray())
    # Convert the elements of this list to an array
    #  2 points
    
    def toArray(self):
        def toArrayHelper(a,e):
            a.append(e.getData())
            if(e.hasNext()):
                toArrayHelper(a,e.getNext())

        arr = []
        d=self.first
        if(self.first==None): return arr
        toArrayHelper(arr,d)
        return arr
    # Get the `i`th element of the list
    # Precondition: i < self.size()
    # Otherwise, raise NoSuchElementException
    #  2 points
    def getIth(self, i):
        return
