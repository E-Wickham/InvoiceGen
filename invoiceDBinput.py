import mysql.connector


def dbInput(clientName, invoiceDate, invoiceAmt, totalHours, rate, filename,inAmtPlusHST):
     # DB information to connect to localhost
        mydb = mysql.connector.connect(
        host="",
        port="",
        user="",
        password="",
        database =""
        )
        #get everything from the listing table
        mycursor = mydb.cursor()
        inputState = "INSERT INTO invoices(inClient, inDate, inAmt, inHours, inRate, inFileName, inAmtHST) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        inputVal = [clientName, invoiceDate, invoiceAmt, totalHours, rate, filename, inAmtPlusHST]
        mycursor.execute(inputState, inputVal)
        mydb.commit()
