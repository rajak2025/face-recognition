from tkinter import *
import csv

from datetime import datetime

def get_date():
    # datetime object containing current date and time
    now = datetime.now()
 
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    return dt_string


def create_details_gui():
    
    #to be implemented
    def click():
        name1 = name.get()
        phone1 = phone.get()
        items1 = item.get()
        output.delete(0.0, END)
        #here 0.0 (clear every thing before the first line and the first character)
        
        try:
            if name1 in customers:
                #mutating the tuple, appending new items
                details = customers[name1]
                converteddetails = list(details)
                converteddetails[2] = converteddetails[2] + ' '+items1
                details = tuple(converteddetails)
                customers[name1] = details

                #writing into the file
                with open('C:/Users/USER/Desktop/rajashekar/face-recognition/face-recognition/transactions1.csv', 'w') as f:
                    for key in customers.keys():
                        f.write("%s,"%(key))
                        internalDetails = customers[key]
                        f.write("%s,%s,%s\n"%(internalDetails[0], internalDetails[1], internalDetails[2]))
                definition = "Customer already exists, Items added to list\nAll Items purchased\n" + converteddetails[2]
                output.insert(END, definition)
            else:
                with open('C:/Users/USER/Desktop/rajashekar/face-recognition/face-recognition/transactions1.csv', 'a') as f:
                    f.write("%s,%s,%s,%s\n"%(name1,phone1,get_date(),items1))
        except:
            definition = "Could not load details"
            output.insert(END, definition)

        

    #To be implemented
    def close_window():
        window.destroy()


    window = Tk()
    window.title("Create Details")

    textformat = "calibri 24 bold"

    #Name Label
    Label(window, text="Name: ", font = textformat) .grid(row =0 , column = 0, sticky=W)
    
    #Name textbox
    name = Entry(window, width = 20, font = textformat)
    name.grid(row = 0, column = 1, sticky = W)

    #Phone Label
    Label(window, text = "Phone: ", font = textformat) .grid(row = 1, column = 0, sticky=W)

    #Phone Textbox
    phone = Entry(window, width = 20, font = textformat)
    phone.grid(row = 1, column = 1, sticky = W)

    #Items Label
    Label(window, text = "Enter Items: ", font = textformat) .grid(row = 2, column = 0, sticky=W)

    #Transaction Textbox
    item = Entry(window, width = 20, font = textformat)
    item.grid(row = 3, column = 0, sticky = W)

    #creating button submit
    Button(window, text = "SUBMIT", width = 6, command = click).grid(row = 4, column = 0, sticky=W)

    #text box for success
    output = Text(window, width = 20, height = 2, font = "calibri 16",wrap=WORD)
    output.grid(row = 5, column = 0, columnspan = 3, sticky = W)

    #creating dict of customers
    reader  = csv.reader(open('C:/Users/USER/Desktop/rajashekar/face-recognition/face-recognition/transactions.csv', 'r'))
    customers = {}
    for row in reader:
        cname, cphone, cdate, citems = row
        customers[cname] = cphone, cdate, citems

    #exit label
    Label(window, text="Click to exit: ", font= textformat) .grid(row = 6 , column = 0 , sticky=W)

    #exit button
    Button(window, text = "EXIT", width = 6, command = close_window).grid(row = 7, column = 0, sticky=W)


    
    window.mainloop()


if __name__ == "__main__":
    create_details_gui()