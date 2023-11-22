from datetime import datetime

inv_num ="1"
start = 'Jan 16'
until = 'Jan 31'

gst = 1.05
hst = 1.13


clients = [
    { 
      'name' : "Tech Won't Save Us",
      'contact' : '',
      'email': '',
      'rate' : ,
      'tax' : gst
    },
    { 
      'name' : "The Hoser",
      'contact' : '',
      'email': '',
      'rate' : 
      'tax' : hst
    },
    { 
      'name' : "Press Progress",
      'contact' : '',
      'email': '',
      'rate' : 75.00,
      'tax' : hst
    },
    { 
      'name' : "Cited Media",
      'contact' : '',
      'email': '',
      'rate' : 
      'tax'  : hst
    }
]


work = '''<div class="flex-row">
            <div class="flex-item-b">Day</div>
            <div class="flex-item-b">Hours</div>
            <div class="flex-item-b big">Project</div>
            <div class="flex-item-b big">Description</div>
        </div>'
       '''

date_raw = datetime.today()
today_date = datetime.today().strftime("%d %b, %Y")
