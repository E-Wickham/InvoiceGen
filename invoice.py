import jinja2
import pdfkit
import info as i
from datetime import datetime
import csv
import pandas as pd
import mysql.connector
from decimal import Decimal
from invoiceDBinput import dbInput, getInvoiceNum

def createInv(csvData):
    df = pd.read_csv(csvData)
    input1 = input('''Who are you invoicing? 
                    1) Tech Won't Save Us
                    2) The Hoser
                    3) PressProgress
                    4) Unrigged
                    5) other\n''')
    if input1 == "1":
        clientName = "Tech Won't Save Us"
    elif input1 == '2':
        clientName = "The Hoser"
    elif input1 == '3':
        clientName = "Press Progress"
    elif input1 == '4':
        clientName = "Unrigged"
    elif input1 == '5':
        clientName = "System Crash"
    else: 
        clientName = input("enter the client you are invoicing")

    for elem in i.clients:
        if clientName in elem['name']:
            try:
                print('creating invoice for:' + elem['name'])
                clientInfo = elem
                print(clientInfo)
            except: 
                print('name not input correctly')

    # writing out lines of tasks completed + work done
    with open(csvData) as f:
        # clear this
        i.work = ""
        reader = csv.DictReader(f)
        for row in reader:
            #print(row)
            new_row = '''
                    <div class="flex-row">
                        <div class="flex-item">{day}</div>
                        <div class="flex-item">{hours}</div>
                        <div class="flex-item big">{desc}</div>
                        <div class="flex-item big">{title}</div>
                    </div>'''.format(
                               day = row['day'], 
                               hours = row['Hours'], 
                               desc = row['Description'], 
                               title = row['Title'] 
                               )
            i.work += new_row

    # Additional Fees Block to cover extra costs for non hourly, non-taxable expenses
    addFees = input('Are there additional fees you want to include in this invoice? (y/n?)')
    addFeeList = []
    addFeeTotal = 0
    addFeeRows = ""
    if addFees == "y":
        while addFees == "y":
            addFeeTitle = input ("what is the additional fee for?")
            addFeeNum = float(input('what is the total cost of the additional fee?'))
            addFeeItem = [addFeeTitle, addFeeNum]
            addFeeList.append(addFeeItem)
            addFeeTotal += addFeeNum
            addaddFees = input("are there more additional fees to add to the invoice? (y/n)")
            if addaddFees == "n":
                addFees = "n"
        addFeeRows += '''<div class="flex-row add">
                            <div class="flex-item-b add">Additional Fee</div>
                            <div class="flex-item-b add">Amount</div>
                        </div>'''
        for fee in addFeeList:
            new_fee_row = '''
                        <div class="flex-row">
                            <div class="flex-item add">{title}</div>
                            <div class="flex-item add">${number}</div>
                        </div>'''.format(
                                title = fee[0], 
                                number = "%.2f" % fee[1]
                                )
            addFeeRows += new_fee_row
    #setting values from the csv file            
    try:
        totalHours = df['Hours'].sum()
        startDate = df['day'].iloc[0]
        endDate = df['day'].iloc[-1]
        total = (totalHours*clientInfo['rate']) + addFeeTotal
        hstTotal = (total*clientInfo['tax'])
        rateDisp = "%.2f" % clientInfo['rate']
        subTotalDisp = "%.2f" % total
        hstTotalDisp = "%.2f" % hstTotal
    except:
        totalHours = ""
        startDate = ""
        endDate = ""
        total = ""
        hstTotal = addFeeTotal
        rateDisp = ""
        subTotalDisp = "%.2f" % addFeeTotal
        hstTotalDisp = "%.2f" % addFeeTotal

    print("total hours: ",totalHours)
    print("Sub-total: ", subTotalDisp)
    print("Tax Added: ", (total*(clientInfo['tax']-1)))
    print("Final Total: ", hstTotalDisp)

    if clientInfo['name'] == 'Cited Media' :
        invoiceNum = input('what invoice number is this for Cited Media?')
    else: 
        invoiceNum = getInvoiceNum()

    context = {
           'inv_num': invoiceNum, 
           'date': i.today_date, 
           "work": i.work, 
           "addFees" : addFeeRows,
           "from": startDate, 
           "until": endDate, 
           "hours": totalHours, 
           "total": subTotalDisp,
           "hstTotal": hstTotalDisp,
           "clientRate" : rateDisp,
           "clientName" : clientInfo['name'],
           "clientContact" : clientInfo['contact'],
           "clientEmail" : clientInfo['email'],
          }

    template_loader = jinja2.FileSystemLoader('./')
    template_env = jinja2.Environment(loader=template_loader)

    template = template_env.get_template('placeholder.html')
    output_text = template.render(context)

    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    filename = f"{i.today_date}_{clientInfo['name']}_invoice.pdf"
    pdfkit.from_string(output_text, filename, configuration=config, css='style.css')
    print(f'new pdf created for {clientInfo["name"]}')
    #dbInput(clientInfo['name'], i.today_date, total, totalHours, clientInfo['rate'])
    try:
         dbInput(clientInfo['name'], i.date_raw, Decimal(total), int(totalHours), clientInfo['rate'], filename, Decimal(hstTotalDisp))
         print(f"invoice generated log for {filename}")
    except Exception as e: 
         print('db input failed')
         print(e)
#createInv('timesheet.csv')

    # CLEAR ALL VARS 
    df = None
    context = None
    totalHours = None
    startDate = None
    endDate = None
    total = None
    hstTotal = None