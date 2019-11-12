def moneyPossibilities(grens: int, amount: int, geld: list, matrix: list):
    if matrix[grens][amount] == -1:
        if amount == 0:
            matrix[grens][amount] = 0
        if grens == 0:
            matrix[grens][amount] = 1
        if amount >= geld[grens]:
            matrix[grens][amount] = moneyPossibilities(grens-1, amount, geld, matrix) + moneyPossibilities(grens, amount-geld[grens], geld, matrix)
        if amount < geld[grens]:
            matrix[grens][amount] = moneyPossibilities(grens-1, amount, geld, matrix)
    return matrix[grens][amount]



def main(amount: int):
    geld = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
    matrix = []
    lijst = []

    for i in range(amount+1):
        lijst.append(-1)
    for i in range(len(geld)):
        matrix.append(lijst)

    print(moneyPossibilities(12, amount, geld, matrix))

main(7)

