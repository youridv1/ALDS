def moneyPossibilities(grens: int, amount: int, geld: list, matrix: list):
    if amount < 0:
        return 0
    if matrix[grens][amount] == -1:
        if amount == 0:
            matrix[grens][amount] = 1
        elif grens == 0:
            matrix[grens][amount] = 1
        elif amount >= geld[grens]:
            matrix[grens][amount] = moneyPossibilities(grens-1, amount, geld, matrix) + moneyPossibilities(grens, amount-geld[grens], geld, matrix)
        elif amount < geld[grens]:
            matrix[grens][amount] = moneyPossibilities(grens-1, amount, geld, matrix)
    return matrix[grens][amount]



def main(amount: int):
    geld = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
    matrix = []
    lijst = []

    for _ in range(amount+1):
        lijst.append(-1)
    for _ in range(len(geld)):
        matrix.append(lijst)

    print(moneyPossibilities(12, amount, geld, matrix))

main(-1)

