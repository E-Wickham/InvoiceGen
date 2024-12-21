import invoice as inv
import totals as t
import expenses as exp

while True:
    print('''Welcome to the Invoice App.
          \n 1 => New Invoice
          \n x => New Client
          \n 3 => Check Totals
          \n x => Expenses
          \n 0 => Exit
          
          
          ''')
    appChoice = input("")
    appChoiceClean = appChoice.strip()
    if appChoiceClean == "1":
        inv.createInv('timesheet.csv')
    elif appChoiceClean == "3":
        t.totals()
    elif appChoiceClean == "4":
        exp.expenses()
    elif appChoiceClean == "0":
        break