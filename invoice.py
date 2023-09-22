import jinja2
import pdfkit
import info as i
from datetime import datetime
import csv
import pandas as pd
import mysql.connector
from decimal import Decimal
from invoiceDBinput import dbInput

def createInv(csvData):
    df = pd.read_csv(csvData)
    clientName = input("Who are you invoicing?")
    for elem in i.clients:
        if clientName in elem['name']:
            try:
                print('creating invoice for:' + elem['name'])
                clientInfo = elem
                print(clientInfo)
            except: 
                print('name not input correctly')

    with open(csvData) as f:
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

    totalHours = df['Hours'].sum()
    startDate = df['day'].iloc[0]
    endDate = df['day'].iloc[-1]
    total = totalHours*clientInfo['rate']
    hstTotal = (total*clientInfo['tax'])

    rateDisp = "%.2f" % clientInfo['rate']
    subTotalDisp = "%.2f" % total
    hstTotalDisp = "%.2f" % hstTotal
    print("total hours: ",totalHours)
    print("Sub-total: ", subTotalDisp)
    print("Tax Added: ", (total*(clientInfo['tax']-1)))
    print("Final Total: ", hstTotalDisp)
    context = {
           'inv_num': i.inv_num, 
           'date': i.today_date, 
           "work": i.work, 
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
createInv('timesheet.csv')