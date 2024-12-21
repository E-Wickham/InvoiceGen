from invoiceDBinput import getExpenses

def expenses() :
    totalExp = getExpenses()
    for exp in totalExp:
        print(exp)

expenses()