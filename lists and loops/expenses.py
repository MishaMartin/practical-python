#range() is a function in python and it will loop the range. you can even be specific about (sstart number, when to stop, count by number) for example, range(2, 14, 2) which prints (2, 4, 6, 8, 10)

expenses = [10.50, 8, 5, 15, 20, 5, 3]
sum = 0

for x in expenses:
    sum = sum + x

#comma in a print statement will auto concatenate the values and auto adds a space
#sep='' will denote how you want to separate it
print("You spent $", sum, " on lunch this week.", sep='')

total = 0
expenses = []
num_expenses = int(input("Enter # of expenses:"))
for i in range(num_expenses):
    expenses.append(float(input("Enter an expense:")))

total = sum(expenses)

print(total)