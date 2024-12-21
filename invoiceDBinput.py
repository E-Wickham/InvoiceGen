import mysql.connector


def dbInput(clientName, invoiceDate, invoiceAmt, totalHours, rate, filename,inAmtPlusHST):
     # DB information to connect to localhost
        mydb = mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="root",
        database ="homebank"
        )
        #get everything from the listing table
        mycursor = mydb.cursor()
        inputState = "INSERT INTO invoices(inClient, inDate, inAmt, inHours, inRate, inFileName, inAmtHST) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        inputVal = [clientName, invoiceDate, invoiceAmt, totalHours, rate, filename, inAmtPlusHST]
        mycursor.execute(inputState, inputVal)
        mydb.commit()

def getInvoiceNum() :
      mydb = mysql.connector.connect(
      host="localhost",
      port="3306",
      user="root",
      password="root",
      database ="homebank"
      )
      #get everything from the listing table
      mycursor = mydb.cursor()
      selState = "select count(*) from invoices"
      mycursor.execute(selState)
      result = mycursor.fetchall()[0][0]
      num = int(result) + 1
      return num

def getExpenses() :
      mydb = mysql.connector.connect(
      host="localhost",
      port="3306",
      user="root",
      password="root",
      database ="homebank"
      )
      #get everything from the listing table
      mycursor = mydb.cursor()
      selState = "select * from bizExp order by expDate limit 10"
      mycursor.execute(selState)
      result = mycursor.fetchall()
      expSummary = result 
      expTotalSel = "select sum(expAmt) from bizExp"
      mycursor.execute(expTotalSel)
      expTotal = mycursor.fetchall()
      expenseList = []
      expenseList.append(expSummary)
      expenseList.append(expTotal)
      return expenseList
