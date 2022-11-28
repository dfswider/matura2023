filename = "/home/wiercik/szkola/Przedmioty/Informatyka/Matura2023/Dane_2203/szachy_przyklad.txt"
print(filename)
file = open(filename)
b = file.readlines()


def emptyColumns(boards):  # zad 1.1
    boardsWithEmptyColumns = 0
    maxEmptyColumns = 0

    def empty_columns(brds, boardno):
        emptyColumns = 0
        for i in range(8):
            emptyPlaces = 0
            for j in range(8):
                if brds[boardno * 9 + j][i] == '.':
                    emptyPlaces += 1
            if emptyPlaces == 8:  # column is empty
                emptyColumns += 1
        return emptyColumns

    howManyBoards = (len(boards) // 9) + 1

    for i in range(howManyBoards):
        ec = empty_columns(boards, i)
        if ec > 0:
            boardsWithEmptyColumns += 1
            if ec > maxEmptyColumns:
                maxEmptyColumns = ec
    print("Boards: ", howManyBoards)
    print("Boards with empty columns: ", boardsWithEmptyColumns)
    print("Max empty columns in one board: ", maxEmptyColumns)


def balance(boards):  # Zad 1.2
    balancedBoards = 0
    minFigures = 32

    def isBalance(brds, brdno):
        figures = {'p': 0, 'w': 0, 's': 0, 'g': 0, 'h': 0, 'k': 0, 'P': 0, 'W': 0, 'S': 0, 'G': 0, 'H': 0, 'K': 0}
        for i in range(8):
            for j in range(8):
                if brds[brdno * 9 + i][j] != '.':
                    x = figures.get(brds[brdno * 9 + i][j]) + 1
                    figures.update({brds[brdno * 9 + i][j]: x})
        if figures.get('p') == figures.get('P') and figures.get('w') == figures.get('W') and \
                figures.get('s') == figures.get('S') and figures.get('g') == figures.get('G') and \
                figures.get('h') == figures.get('H'):
            return (figures.get('p') + figures.get('s') + figures.get('w') + figures.get('g') + figures.get(
                'h') + figures.get('k')) * 2
        else:
            return 0

    for i in range((len(boards) // 9) + 1):
        f = isBalance(boards, i)
        if f > 0:
            balancedBoards += 1
            if minFigures > f:
                minFigures = f

    print("Balanced boards: ", balancedBoards)
    print("Minimum number of figures on one balanced board: ", minFigures)


def rookCheck(boards):  # zad 1.3
    whiteKingChecks = 0
    blackKingChecks = 0
    # minFigures = 32

    def findFigure(brds, boardnumber, king):
        figurePos = []
        for i in range(8):
            for j in range(8):
                if brds[boardnumber * 9 + i][j] == king:
                    figurePos.append((i, j))
                    return figurePos
        return figurePos

    """
    def countFigures(bords, bordno):
        figures = 0
        for i in range(8):
            for j in range(8):
                if bords[bordno*9+i][j] =='.':
                    figures += 1
        return figures
    """

    def isCheck(bords, bordno, kk, ww):
        if kk[0] == ww[0]:  # row check?
            distance = abs(kk[1] - ww[1])
            dots = 0
            for j in range(kk[1], ww[1]):
                if bords[bordno * 9 + kk[0]][j] == '.':
                    dots += 1
            if dots == distance - 1:
                return True
        if kk[1] == ww[1]:
            distance = abs(kk[0] - ww[0])
            dots = 0
            for i in range(kk[0], ww[0]):
                if bords[bordno * 9 + i][kk[0]] == '.':
                    dots += 1
            if dots == distance - 1:
                return True
        return False

    for i in range(len(boards) // 9 + 1):
        k = findFigure(boards, i, 'k')
        K = findFigure(boards, i, 'K')
        w = findFigure(boards, i, 'w')
        W = findFigure(boards, i, 'W')

        if len(w) > 0:
            for j in range(len(w)):
                if isCheck(boards, i, K[0], w[j]):
                    whiteKingChecks += 1;
        if len(W) > 0:
            for j in range(len(W)):
                if isCheck(boards, i, k[0],  W[j]):
                    blackKingChecks += 1
    print("Black king checked: ", blackKingChecks, "White king checked: ", whiteKingChecks )


emptyColumns(b)
balance(b)
rookCheck(b)
