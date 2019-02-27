import random


def Mgenerator(row, column):
    matrix = []
    if row >= column:
        for i in range(0, row):
            tmp = []
            for j in range(0,column):
                tmp.append(random.randrange(0,99,3))
            matrix.append(tmp)
        return matrix
    else:
        for i in range(0,column):
            tmp = []
            for j in range(0,row):
                tmp.append(random.randrange(0,99,3))
            matrix.append(tmp)
        return matrix



def prettyPrinter(matrix):
    if matrix == None:
        print("Empty matrix or bad matrix size, make sure to have the good size.")
    elif len(matrix[0]) >= len(matrix):
        print(str(len(matrix[0]))+"x"+str(len(matrix))+":")
        for i in range(0, len(matrix[0])):
            line = ""
            for j in range(0, len(matrix)):
                line += '{:5} {}'.format(str(matrix[i][j])+" ", "")
            length = len(line)
            print(line[0:length-3])
    else:
        print(str(len(matrix))+"x"+str(len(matrix[0]))+":")
        for i in range(0, len(matrix)):
            line = ""
            for j in range(0, len(matrix[0])):
                line += '{:5} {}'.format(str(matrix[i][j])+" ", "")
            length = len(line)
            print(line[0:length-3])



def addM(m1, m2):
    if len(m1[0]) == len(m2[0]) and len(m2) == len(m1) :
        result = Mgenerator(len(m1[0]), len(m1))
        for i in range(0, len(m1[0])-1):
            for j in range(0,len(m1[1])-1):
                result[i][j] = m1[i][j]+ m2[i][j]
        return result
    else:
        print("Nothing to add...")
        return None


def main():
    m1 = Mgenerator(3,5)
    m2 = Mgenerator(3,5)
    prettyPrinter(m1)
    print("\n")
    prettyPrinter(m2)
    print("\n")
    prettyPrinter(addM(m1, m2))

main()
