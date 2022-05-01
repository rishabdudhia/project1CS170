from board import Board
from treeEuclidean import EuclideanNode
from treeUniform import TreeUniform, UniformNode
from treeMisplaced import TreeMisplaced, MisplacedNode
from treeEuclidean import TreeEuclidean, EuclideanNode



print("Welcome to 862141444 8 Puzzle Solver.")
print("Type \"1\" to use a default puzzle, or \"2\" to enter your own:")
choice1 = input()
while choice1:
    if choice1 != '1' and choice1 != '2':
        print("Please enter a valid choice, \"1\" or \"2\": ")
        choice1 = input()
    else:
        if choice1 == '1':
            num1 = '*'
            num2 = '1'
            num3 = '2'
            num4 = '4'
            num5 = '5'
            num6 = '3'
            num7 = '7'
            num8 = '8'
            num9 = '6'
            break
        elif choice1 == '2':
            print("Please enter your puzzle using a \"*\" or \"0\" to represent the blank.")
            print("Please enter the first row, use a space or tab between numbers: ")
            line1 = input()
            print("Please enter the second row, use a space or tab between numbers: ")
            line2 = input()
            print("Please enter the third row, use a space or tab between numbers: ")
            line3 = input()
            count = 1
            for i in range(len(line1)):
                if line1[i] != ' ' and line1[i] != '\t':
                    if count == 1:
                        num1 = line1[i]
                        count += 1
                    elif count == 2:
                        num2 = line1[i]
                        count += 1
                    elif count == 3:
                        num3 = line1[i]
                        break
            count = 1
            for i in range(len(line2)):
                if line2[i] != ' ' and line2[i] != '\t':
                    if count == 1:
                        num4 = line2[i]
                        count += 1
                    elif count == 2:
                        num5 = line2[i]
                        count += 1
                    elif count == 3:
                        num6 = line2[i]
                        break
            
            count = 1
            for i in range(len(line3)):
                if line3[i] != ' ' and line3[i] != '\t':
                    if count == 1:
                        num7 = line3[i]
                        count += 1
                    elif count == 2:
                        num8 = line3[i]
                        count += 1
                    elif count == 3:
                        num9 = line3[i]
                        break
        choice1 = 0

b = Board(num1, num2, num3, num4, num5, num6, num7, num8, num9)
initialB = Board(b.boardList[0][0], b.boardList[0][1], b.boardList[0][2], b.boardList[1][0], b.boardList[1][1], b.boardList[1][2], b.boardList[2][0], b.boardList[2][1], b.boardList[2][2])



print("Enter your choice of algorithm")
print("1. Uniform Cost Search")
print("2. A* with Misplaced Tile Heuristic")
print("3. A* with Euclidean Distance Heuristic")
choice2 = input()
while choice2 != '1' and choice2 != '2' and choice2 != '3':
    choice2 = input()
if choice2 == '1':
    initial = UniformNode(initialB, 0, 0, 0)
    tree = TreeUniform()
    node = tree.solve(initial)
    maxAnyTime = tree.maxFrontierSize
    totalNodes = tree.totalNumNodes
    print("\nTo solve this problem, the search algorithm expanded a total of " + str(totalNodes) + " nodes.")
    print("The maximum number of nodes in the queue at any one time: " + str(maxAnyTime))
    print("The depth of the goal node is: " + str(node.g))
elif choice2 == '2':
    initial = MisplacedNode(initialB, 0, 0, 0)
    tree = TreeMisplaced()
    node = tree.solve(initial)
    maxAnyTime = tree.maxFrontierSize
    totalNodes = tree.totalNumNodes
    print("\nTo solve this problem, the search algorithm expanded a total of " + str(totalNodes) + " nodes.")
    print("The maximum number of nodes in the queue at any one time: " + str(maxAnyTime))
    print("The depth of the goal node is: " + str(node.g))
elif choice2 == '3':
    initial = EuclideanNode(initialB, 0, 0, 0)
    tree = TreeEuclidean()
    node = tree.solve(initial)
    maxAnyTime = tree.maxFrontierSize
    totalNodes = tree.totalNumNodes
    print("\nTo solve this problem, the search algorithm expanded a total of " + str(totalNodes) + " nodes.")
    print("The maximum number of nodes in the queue at any one time: " + str(maxAnyTime))
    print("The depth of the goal node is: " + str(node.g))