def totals():
    import mysql.connector
    import matplotlib.pyplot as plt
    import plotext
    mydb = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            password="root",
            database ="homebank"
            )

    mycursor = mydb.cursor()

    sqlByMonth = 'select sum(inAmtHST), month(inDate),year(inDate) from invoices where inPaid = 1 group by month(inDate), year(inDate)'
    mycursor.execute(sqlByMonth)

    res = mycursor.fetchall()

    #write the values to arrays to use in plots
    moneyIn = []
    dateIn = []
    lastAmt = 0
    for elem in res: 
        sum = int(elem[0]) + lastAmt
        moneyIn.append(int(elem[0])+lastAmt)
        dateFormat = f'{elem[1]}-{elem[2]}'
        dateIn.append(dateFormat)
        lastAmt = sum
        
    print(moneyIn)
    print(dateIn)
    plt.plot(dateIn, moneyIn)
    plt.xlabel("Month")  # add X-axis label 
    plt.ylabel("Currency")  # add Y-axis label 
    plt.title("Money In Over Time")  # add title 
    plt.show()

    '''
    #breakdown by client
    sqlByClient = 'select sum(inAmtHST),inClient from invoices where inPaid = 1 group by inClient'
    mycursor.execute(sqlByClient)

    res2 = mycursor.fetchall()

    #write the values to arrays to use in plots
    moneyIn = []
    clientName = []
    lastAmt = 0
    for elem in res2: 
        moneyIn.append(int(elem[0]))
        clientName.append(elem[1])
    plt.bar(clientName, moneyIn)
    plt.xlabel("Month")  # add X-axis label 
    plt.ylabel("Money")  # add Y-axis label 
    plt.title("Money In By Client")  # add title 
    plt.show()
'''
