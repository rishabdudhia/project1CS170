from random import randint
from array import *

class Board:

    def FindBlank(self): 
        place = "-1"
        for i in range(3):
            for j in range(3):
                if self.boardList[i][j] == '*' or self.boardList[i][j] == '0':
                    place = str(i) + str(j)
                    break
            
        if place == "-1": return "-1"
        return place

    def __init__(self, num1, num2, num3, num4, num5, num6, num7, num8, num9):
        self.boardList = [[],[],[]]
        self.boardList[0].append(num1)
        self.boardList[0].append(num2)
        self.boardList[0].append(num3)
        self.boardList[1].append(num4)
        self.boardList[1].append(num5)
        self.boardList[1].append(num6)
        self.boardList[2].append(num7)
        self.boardList[2].append(num8)
        self.boardList[2].append(num9)

        self.row1 = self.boardList[0][0] + " | " + self.boardList[0][1] + " | " + self.boardList[0][2] + "\n"
        self.row2 = self.boardList[1][0] + " | " + self.boardList[1][1] + " | " + self.boardList[1][2] + "\n"
        self.row3 = self.boardList[2][0] + " | " + self.boardList[2][1] + " | " + self.boardList[2][2] + "\n"
        self.blank = self.FindBlank()
    
    def print_board(self):
        mid1 = "--+---+--\n"
        mid2 = "--+---+--\n"
        
        print (self.row1 + mid1 + self.row2 + mid2+ self.row3)
    
    def setRows(self):
        self.row1 = ""
        self.row1 = self.boardList[0][0] + " | " + self.boardList[0][1] + " | " + self.boardList[0][2] + "\n"
        self.row2 = ""
        self.row2 = self.boardList[1][0] + " | " + self.boardList[1][1] + " | " + self.boardList[1][2] + "\n"
        self.row3 = ""
        self.row3 = self.boardList[2][0] + " | " + self.boardList[2][1] + " | " + self.boardList[2][2] + "\n"
        return self.row1 + self.row2 + self.row3

    def moveBlankUp(self):
        place = self.blank
        if place == "-1": return -1
        x = int(place[0])
        y = int(place[1])
        if x == 0:
            return -1
        xPrime = self.boardList[x-1][y]
        self.boardList[x-1][y] = self.boardList[x][y]
        self.boardList[x][y] = xPrime
        self.setRows()
        self.blank = str(x-1) + str(y)
        return 1

        
    
    def moveBlankDown(self):
        place = self.blank
        if place == "-1": return -1
        x = int(place[0])
        y = int(place[1])
        if x == 2:
            return -1
        xPrime = self.boardList[x+1][y]
        self.boardList[x+1][y] = self.boardList[x][y]
        self.boardList[x][y] = xPrime
        self.setRows()
        self.blank = str(x+1) + str(y)
        return 1

    def moveBlankLeft(self):
        place = self.blank
        if place == "-1": return -1
        x = int(place[0])
        y = int(place[1])
        if y == 0:
            return -1
        xPrime = self.boardList[x][y-1]
        self.boardList[x][y-1] = self.boardList[x][y]
        self.boardList[x][y] = xPrime
        self.setRows()
        self.blank = str(x) + str(y-1)
        return 1

    def moveBlankRight(self):
        place = self.blank
        if place == "-1": return -1
        x = int(place[0])
        y = int(place[1])
        if y == 2:
            return -1
        xPrime = self.boardList[x][y+1]
        self.boardList[x][y+1] = self.boardList[x][y]
        self.boardList[x][y] = xPrime
        self.setRows()
        self.blank = str(x) + str(y+1)
        return 1
    
    def ShuffleBoard(self):
        i = 0
        while i <= 10:
            r = randint(0,3)
            if r == 0:
                v = self.moveBlankUp()
            elif r == 1:
                v = self.moveBlankDown()
            elif r == 2:
                v = self.moveBlankLeft()
            elif r == 3:
                v = self.moveBlankRight()
            
            if v == -1:
                i -= 1
            else:
                i += 1
    
    def getBoard(self):
        return self