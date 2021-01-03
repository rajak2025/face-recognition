import csv
from datetime import datetime

def get_date():
    # datetime object containing current date and time
    now = datetime.now()
 
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    return dt_string

reader  = csv.reader(open('C:/Users/USER/Desktop/rajashekar/face-recognition/face-recognition/transactions.csv', 'r'))
customers = {}
for row in reader:
    cname, phone, date, items = row
    customers[cname] = phone, date, items



items1 = "bat"
phone1 = "12345"
name1 = "Ricky"



if name1 in customers:
    #mutating the tuple, appending new items
    details = customers[name1]
    convertedDetails = list(details)
    convertedDetails[2] = convertedDetails[2] + ' '+items1
    details = tuple(convertedDetails)
    customers[name1] = details

    #writing into the file
    with open('C:/Users/USER/Desktop/rajashekar/face-recognition/face-recognition/transactions1.csv', 'w') as f:
        for key in customers.keys():
            f.write("%s,"%(key))
            internalDetails = customers[key]
            f.write("%s,%s,%s\n"%(internalDetails[0], internalDetails[1], internalDetails[2]))
    definition = "Customer already exists, Items added to list\nAll Items purchased\n" + convertedDetails[2]
    print(definition)
else:
    with open('C:/Users/USER/Desktop/rajashekar/face-recognition/face-recognition/transactions1.csv', 'a') as f:
        f.write("%s,%s,%s,%s\n"%(name1,phone1,get_date(),items1))    




