import functools
import operator


def find_lcs(firstWord, secondWord):
    firstWordLength = len(firstWord)
    secondWordLength = len(secondWord)
    table = [[0 for _ in range(secondWordLength + 1)] for _ in range(firstWordLength + 1)]

    for i in range(firstWordLength + 1):
        for j in range(secondWordLength + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif firstWord[i - 1] == secondWord[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    index = table[firstWordLength][secondWordLength]
    result = [""] * index

    i = firstWordLength
    j = secondWordLength
    while i > 0 and j > 0:
        if firstWord[i - 1] == secondWord[j - 1]:
            result[index - 1] = firstWord[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif table[i - 1][j] > table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    try:
        print("Najdłuższy wspólny podciąg " + firstWord + " i " + secondWord + " to " +
              functools.reduce(operator.add, result))
    except TypeError:
        print("Brak podciągu")
    print_table(table)


def print_table(table):
    for line in table:
        print(*line)
