from datetime import datetime

inv_num ="3"
#start = 'Jan 16'
#until = 'Jan 31'

gst = 1.05
hst = 1.13
none = 1


clients = [
    { 
      'name' : "Tech Won't Save Us",
      'contact' : 'Paris Marx',
      'email': 'paris@parismarx.com',
      'rate' : 45.00,
      'tax' : gst
    },
    { 
      'name' : "System Crash",
      'contact' : 'Paris Marx',
      'email': 'paris@parismarx.com',
      'rate' : 45.00,
      'tax' : gst
    },
    { 
      'name' : "The Hoser",
      'contact' : 'Shannon Carranco',
      'email': 'shannonellycarranco@gmail.com',
      'rate' : 68.25,  #rate takes into account that im collecting 13% hst on the $57 USD
      'tax' : hst
    },
    { 
      'name' : "Press Progress",
      'contact' : 'Stephen Magusiak',
      'email': 'smagusiak@pressprogress.ca',
      'rate' : 75.00,
      'tax' : hst
    },
    { 
      'name' : "Cited Media",
      'contact' : 'Gordon Katic',
      'email': 'gordon@citedmedia.ca',
      'rate' : 39.00, #should be 34.50 to subtract hst which is being added in
      'tax'  : hst
    },
    { 
      'name' : "Unrigged",
      'contact' : 'Andre Goulet',
      'email': 'andremarrgoulet@gmail.com',
      'rate' : 40.00, 
      'tax'  : none
    },
    { 
      'name' : "The Breach",
      'contact' : 'Martin Lukacs',
      'email': 'martin@breachmedia.ca ',
      'rate' : 75.00, 
      'tax'  : gst
    },
    { 
      'name' : "Spacing",
      'contact' : 'Dylan Reid',
      'email': 'dylan@spacing.ca',
      'rate' : 50.00, 
      'tax'  : hst
    },
    { 
      'name' : "Invisible Institutions",
      'contact' : 'Megan Linton',
      'email': 'megan.m.linton@gmail.com',
      'rate' : 50.00, 
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