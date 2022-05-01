from board import Board
from queue import PriorityQueue
from math import inf


class MisplacedNode:

    def heuristic(self, board: Board):
        count = 0
        if board.boardList[0][0] != '1': count += 1
        if board.boardList[0][1] != '2': count += 1
        if board.boardList[0][2] != '3': count += 1
        if board.boardList[1][0] != '4': count += 1
        if board.boardList[1][1] != '5': count += 1
        if board.boardList[1][2] != '6': count += 1
        if board.boardList[2][0] != '7': count += 1
        if board.boardList[2][1] != '8': count += 1
        # if board.boardList[2][2] == '*' or board.boardList[2][2] == '0': count += 0
        # else: count += 1

        return count
        

    def __init__(self, board: Board, gn, parent, last_move):
        self.board = board
        self.g = gn
        self.h = self.heuristic(board)
        self.f = self.g + self.h
        self.parent = parent
        self.last_move = last_move
        self.children = []

    def __lt__(self, other):
        if self.f <= other.f:
            return True
        return False
    
    def setParent(self, node):
        self.parent = node


class TreeMisplaced:

    def __init__(self):
        self.frontier = PriorityQueue()
        self.root = 0
        self.totalNumNodes = 0
        self.maxFrontierSize = 0
        self.visited = []
    
    def printFrontier(self):
        print("Currently in queue")
        for i in range(self.frontier.qsize()):
            node = self.frontier.queue[i]
            node.board.print_board()
            print("priority: " + str(self.frontier.queue[i].f))
            print("last move: " + str(node.last_move))
        print("done with queue")

    def add(self, node: MisplacedNode):
        curr = node.board.row1 + node.board.row2 + node.board.row3
        for i in range(len(self.visited)):
            if curr == (self.visited[i].board.row1 + self.visited[i].board.row2 + self.visited[i].board.row3):
                if node.last_move == self.visited[i].last_move:
                    return
        if self.root == 0:
            self.root = node
        self.frontier.put(node)
        if self.frontier.qsize() > self.maxFrontierSize:
            self.maxFrontierSize = self.frontier.qsize()
        self.totalNumNodes += 1
        self.visited.append(node)
    
    def checkGoal(self, node: MisplacedNode):
        row1 = "1 | 2 | 3\n"
        row2 = "4 | 5 | 6\n"
        row31 = "7 | 8 | *\n"
        row32 = "7 | 8 | 0\n"
        check1 = row1 + row2 + row31
        check2 = row1 + row2 + row32
        curr = node.board.row1 + node.board.row2 + node.board.row3
        if check1 == curr or check2 == curr:
            return True
        return False

    def remove(self):
        if self.frontier.qsize() == 0: return -1 #solution does not exist
        current = self.frontier.get()
        currentNode: MisplacedNode = current
        found = self.checkGoal(currentNode)
        if found == True: 
            return  (True, currentNode) #solution found
        a = currentNode.board.blank
        x = int(a[0])
        y = int(a[1])
        b = currentNode.board
        print("The best state to expand with g(n) = " + str(currentNode.g) + " and h(n) = " + str(currentNode.h) + " is:")
        b.print_board()
        if x == 0:
            if y == 0:
                if currentNode.last_move != 1:
                    b.moveBlankDown()
                    b1 = Board(b.boardList[0][0], b.boardList[0][1], b.boardList[0][2], b.boardList[1][0], b.boardList[1][1], b.boardList[1][2], b.boardList[2][0], b.boardList[2][1], b.boardList[2][2])
                    b.moveBlankUp()
                    n1 = MisplacedNode(b1, currentNode.g+1, currentNode, 2)
                    self.add(n1)
                    currentNode.children.append(n1)
                if currentNode.last_move != 4:
                    b.moveBlankRight()
                    b2 = Board(b.boardList[0][0], b.boardList[0][1], b.boardList[0][2], b.boardList[1][0], b.boardList[1][1], b.boardList[1][2], b.boardList[2][0], b.boardList[2][1], b.boardList[2][2])
                    n2 = MisplacedNode(b2, currentNode.g+1, currentNode, 3)
                    self.add(n2)
                    currentNode.children.append(n2)
            elif y == 2:
                if currentNode.last_move != 1:
                    b.moveBlankDown()
                    b1 = Board(b.boardList[0][0], b.boardList[0][1], b.boardList[0][2], b.boardList[1][0], b.boardList[1][1], b.boardList[1][2], b.boardList[2][0], b.boardList[2][1], b.boardList[2][2])
                    b.moveBlankUp()
                    n1 = MisplacedNode(b1, (currentNode.g)+1, currentNode, 2)
                    self.add(n1)
                    currentNode.children.append(n1)
                if currentNode.last_move != 3:
                    b.moveBlankLeft()
                    b2 = Board(b.boardList[0][0], b.boardList[0][1], b.boardList[0][2], b.boardList[1][0], b.boardList[1][1], b.boardList[1][2], b.boardList[2][0], b.boardList[2][1], b.boardList[2][2])
                    n2 = MisplacedNode(b2, currentNode.g+1, currentNode, 4)
                    self.add(n2)
                    currentNode.children.append(n2)
            else:
                if currentNode.last_move != 1:
                    b.moveBlankDown()
                    b1 = Board(b.boardList[0][0], b.boardList[0][1], b.boardList[0][2], b.boardList[1][0], b.boardList[1][1], b.boardList[1][2], b.boardList[2][0], b.boardList[2][1], b.boardList[2][2])
                    b.moveBlankUp()
                    n1 = MisplacedNode(b1, currentNode.g+1, currentNode, 2)
                    self.add(n1)
                    currentNode.children.append(n1)
                if currentNode.last_move != 4:
                    b.moveBlankRight()
                    b2 = Board(b.boardList[0][0], b.boardList[0][1], b.boardList[0][2], b.boardList[1][0], b.boardList[1][1], b.boardList[1][2], b.boardList[2][0], b.boardList[2][1], b.boardList[2][2])
                    b.moveBlankLeft()
                    n2 = MisplacedNode(b2, currentNode.g+1, currentNode, 4)
                    self.add(n2)
                    currentNode.children.append(n2)
                if currentNode.last_move != 3:
                    b.moveBlankLeft()
                    b3 = Board(b.boardList[0][0], b.boardList[0][1], b.boardList[0][2], b.boardList[1][0], b.boardList[1][1], b.boardList[1][2], b.boardList[2][0], b.boardList[2][1], b.boardList[2][2])
                    n3 = MisplacedNode(b3, currentNode.g+1, currentNode, 3)
                    self.add(n3)
                    currentNode.children.append(n3)
        elif x == 2:
            if y == 0:
                if currentNode.last_move != 4:
                    b.moveBlankRight()
                    b2 = Board(b.boardList[0][0], b.boardList[0][1], b.boardList[0][2], b.boardList[1][0], b.boardList[1][1], b.boardList[1][2], b.boardList[2][0], b.boardList[2][1], b.boardList[2][2])
                    b.moveBlankLeft()
                    n2 = MisplacedNode(b2, currentNode.g+1, currentNode, 3)
                    self.add(n2)
                    currentNode.children.append(n2)
                if currentNode.last_move != 2:
                    b.moveBlankUp()
                    b1 = Board(b.boardList[0][0], b.boardList[0][1], b.boardList[0][2], b.boardList[1][0], b.boardList[1][1], b.boardList[1][2], b.boardList[2][0], b.boardList[2][1], b.boardList[2][2])
                    b.moveBlankDown()
                    n1 = MisplacedNode(b1, currentNode.g+1, currentNode, 1)
                    self.add(n1)
                    currentNode.children.append(n1)
                
            elif y == 2:
                if currentNode.last_move != 2:
                    b.moveBlankUp()
                    b1 = Board(b.boardList[0][0], b.boardList[0][1], b.boardList[0][2], b.boardList[1][0], b.boardList[1][1], b.boardList[1][2], b.boardList[2][0], b.boardList[2][1], b.boardList[2][2])
                    b.moveBlankDown()
                    n1 = MisplacedNode(b1, currentNode.g+1, currentNode, 1)
                    self.add(n1)
                    currentNode.children.append(n1)
                if currentNode.last_move != 3:
                    b.moveBlankLeft()
                    b2 = Board(b.boardList[0][0], b.boardList[0][1], b.boardList[0][2], b.boardList[1][0], b.boardList[1][1], b.boardList[1][2], b.boardList[2][0], b.boardList[2][1], b.boardList[2][2])
                    n2 = MisplacedNode(b2, currentNode.g+1, currentNode, 4)
                    self.add(n2)
                    currentNode.children.append(n2)
            else:
                if currentNode.last_move != 4:
                    b.moveBlankRight()
                    b3 = Board(b.boardList[0][0], b.boardList[0][1], b.boardList[0][2], b.boardList[1][0], b.boardList[1][1], b.boardList[1][2], b.boardList[2][0], b.boardList[2][1], b.boardList[2][2])
                    b.moveBlankLeft()
                    n3 = MisplacedNode(b3, currentNode.g+1, currentNode, 3)
                    self.add(n3)
                    currentNode.children.append(n3)
                if currentNode.last_move != 2:
                    b.moveBlankUp()
                    b1 = Board(b.boardList[0][0], b.boardList[0][1], b.boardList[0][2], b.boardList[1][0], b.boardList[1][1], b.boardList[1][2], b.boardList[2][0], b.boardList[2][1], b.boardList[2][2])
                    b.moveBlankDown()
                    n1 = MisplacedNode(b1, currentNode.g+1, currentNode, 1)
                    self.add(n1)
                    currentNode.children.append(n1)
                if currentNode.last_move != 3:
                    b.moveBlankLeft()
                    b2 = Board(b.boardList[0][0], b.boardList[0][1], b.boardList[0][2], b.boardList[1][0], b.boardList[1][1], b.boardList[1][2], b.boardList[2][0], b.boardList[2][1], b.boardList[2][2])
                    b.moveBlankRight()
                    n2 = MisplacedNode(b2, currentNode.g+1, currentNode, 4)
                    self.add(n2)
                    n2.setParent(currentNode)
                    currentNode.children.append(n2)
                
        else:
            if y == 0:
                if currentNode.last_move != 4:
                    b.moveBlankRight()
                    b2 = Board(b.boardList[0][0], b.boardList[0][1], b.boardList[0][2], b.boardList[1][0], b.boardList[1][1], b.boardList[1][2], b.boardList[2][0], b.boardList[2][1], b.boardList[2][2])
                    b.moveBlankLeft()
                    n2 = MisplacedNode(b2, currentNode.g+1, currentNode, 3)
                    self.add(n2)
                    currentNode.children.append(n2)
                if currentNode.last_move != 1:
                    b.moveBlankDown()
                    b3 = Board(b.boardList[0][0], b.boardList[0][1], b.boardList[0][2], b.boardList[1][0], b.boardList[1][1], b.boardList[1][2], b.boardList[2][0], b.boardList[2][1], b.boardList[2][2])
                    b.moveBlankUp()
                    n3 = MisplacedNode(b3, currentNode.g+1, currentNode, 2)
                    self.add(n3)
                    currentNode.children.append(n3)
                if currentNode.last_move != 2: 
                    b.moveBlankUp()
                    b1 = Board(b.boardList[0][0], b.boardList[0][1], b.boardList[0][2], b.boardList[1][0], b.boardList[1][1], b.boardList[1][2], b.boardList[2][0], b.boardList[2][1], b.boardList[2][2])
                    b.moveBlankDown()
                    n1 = MisplacedNode(b1, currentNode.g+1, currentNode, 1)
                    self.add(n1)
                    currentNode.children.append(n1)
            elif y == 2:
                if currentNode.last_move != 1:
                    b.moveBlankDown()
                    b3 = Board(b.boardList[0][0], b.boardList[0][1], b.boardList[0][2], b.boardList[1][0], b.boardList[1][1], b.boardList[1][2], b.boardList[2][0], b.boardList[2][1], b.boardList[2][2])
                    b.moveBlankUp()
                    n3 = MisplacedNode(b3, currentNode.g+1, currentNode, 2)
                    self.add(n3)
                    currentNode.children.append(n3)
                if currentNode.last_move != 2:
                    b.moveBlankUp()
                    b1 = Board(b.boardList[0][0], b.boardList[0][1], b.boardList[0][2], b.boardList[1][0], b.boardList[1][1], b.boardList[1][2], b.boardList[2][0], b.boardList[2][1], b.boardList[2][2])
                    b.moveBlankDown()
                    n1 = MisplacedNode(b1, currentNode.g+1, currentNode, 1)
                    self.add(n1)
                    currentNode.children.append(n1)
                    
                if currentNode.last_move != 3:
                    b.moveBlankLeft()
                    b2 = Board(b.boardList[0][0], b.boardList[0][1], b.boardList[0][2], b.boardList[1][0], b.boardList[1][1], b.boardList[1][2], b.boardList[2][0], b.boardList[2][1], b.boardList[2][2])
                    b.moveBlankRight()
                    n2 = MisplacedNode(b2, currentNode.g+1, currentNode, 4)
                    self.add(n2)
                    currentNode.children.append(n2)
                    
            else:
                if currentNode.last_move != 4:
                    b.moveBlankRight()
                    b3 = Board(b.boardList[0][0], b.boardList[0][1], b.boardList[0][2], b.boardList[1][0], b.boardList[1][1], b.boardList[1][2], b.boardList[2][0], b.boardList[2][1], b.boardList[2][2])
                    b.moveBlankLeft()
                    n3 = MisplacedNode(b3, currentNode.g+1, currentNode, 3)
                    self.add(n3)
                    currentNode.children.append(n3)
                if currentNode.last_move != 1:
                    b.moveBlankDown()
                    b4 = Board(b.boardList[0][0], b.boardList[0][1], b.boardList[0][2], b.boardList[1][0], b.boardList[1][1], b.boardList[1][2], b.boardList[2][0], b.boardList[2][1], b.boardList[2][2])
                    b.moveBlankUp()
                    n4 = MisplacedNode(b4, currentNode.g+1, currentNode, 2)
                    self.add(n4)
                    currentNode.children.append(n4)
                if currentNode.last_move != 2:
                    b.moveBlankUp()
                    b1 = Board(b.boardList[0][0], b.boardList[0][1], b.boardList[0][2], b.boardList[1][0], b.boardList[1][1], b.boardList[1][2], b.boardList[2][0], b.boardList[2][1], b.boardList[2][2])
                    b.moveBlankDown()
                    n1 = MisplacedNode(b1, currentNode.g+1, currentNode, 1)
                    self.add(n1)
                    currentNode.children.append(n1)
                    
                if currentNode.last_move != 3:
                    b.moveBlankLeft()
                    b2 = Board(b.boardList[0][0], b.boardList[0][1], b.boardList[0][2], b.boardList[1][0], b.boardList[1][1], b.boardList[1][2], b.boardList[2][0], b.boardList[2][1], b.boardList[2][2])
                    b.moveBlankRight()
                    n2 = MisplacedNode(b2, currentNode.g+1, currentNode, 4)
                    self.add(n2)
                    currentNode.children.append(n2)
        return currentNode

    def print(self):
        for i in range(self.frontier.qsize()):
            node = self.frontier.queue[i]
            print(node.priority)
            node.item.board.print_board()

    def solve(self, initial: MisplacedNode):
        self.add(initial) #adds to frontier
        while self.frontier.qsize() != 0:
            val = self.remove()
            if type(val) == tuple:
                print("GOAL!!!")
                return val[1]
            
            if self.frontier.qsize() == 0:
                return -1
    