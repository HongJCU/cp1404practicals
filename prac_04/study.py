months = int(input("How many month?"))
incomes = []
total = 0

for month in range(1, months + 1):
    incomeInput = int(input("Enter income for month " + str(month) + "?"))
    total += incomeInput
    incomeStrTmp = "Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, incomeInput, total)
    incomes.append(incomeStrTmp)

print("Income Report")
print("-------------")

for income in incomes:
    print(income)