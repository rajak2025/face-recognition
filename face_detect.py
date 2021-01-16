import cv2
import numpy as np
import face_recognition
import os
import csv
from datetime import datetime
from tkinter import *
# from PIL import ImageGrab

records_folder = 'Transactions'
mainpath = os.listdir(records_folder)
path_to_csv = mainpath[0]

path = 'Images'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)
 
def find_encodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
 
def mark_attendance(name):
    with open('record.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')

def show_gui(name1):
    #click function for button
    
    def append_items():
        newitems = newitem.get()
        success_entry.delete(0.0, END)
        #here 0.0 (clear every thing before the first line and the first character)
        try:
            newname = name1.lower().capitalize()
            details = customers[newname]
            converteddetails = list(details)
            converteddetails[2] = converteddetails[2] + ' '+newitems
            details = tuple(converteddetails)
            customers[newname] = details

            #writing into the file
            with open(f"{records_folder}/{path_to_csv}", 'w') as f:
                for key in customers.keys():
                    f.write("%s,"%(key))
                    internalDetails = customers[key]
                    f.write("%s,%s,%s\n"%(internalDetails[0], internalDetails[1], internalDetails[2]))
            definition = "Items added to list\nAll Items purchased\n" + converteddetails[2]
            success_entry.insert(END, definition)                    
        except:
            definition = "sorry an error occurred"
            success_entry.insert(END, definition)

    
    def click():
        value1 = name.get().capitalize()
        output.delete(0.0, END)
        #here 0.0 (clear every thing before the first line and the first character)
        try:
            details = customers[value1]
            definition = details[0], details[1], details[2]
        except:
            definition = "sorry there is no customer"
        output.insert(END, definition)    

    #exit function
    def close_window():
        window.destroy()
    
    
    window = Tk()
    window.title("Store Interface")

    textformat = "calibri 24 bold"

    Label(window, text="Name: ", font= textformat) .grid(row = 0 , column = 0 , sticky=W)
    #Label(window, text="Phone: ", font= textformat) .grid(row = 1 , column = 0 , sticky=W)


    #entrybox
    name = Entry(window, width = 20, font = textformat)
    name.insert(0,name1)
    name.grid(row = 1, column = 0, sticky=W)

    #phone = Entry(window, width = 10, font = textformat).grid(row = 1, column = 1, sticky=W)
    #creating label
    #Label(window, text="Last Purchase Date: ", font= textformat) .grid(row = 2 , column = 0 , sticky=W)

    #creating button submit
    Button(window, text = "Show old Purchases", width = 6, command = click).grid(row = 2, column = 0, sticky=W)

    #text box
    output = Text(window, width = 75, height = 6, wrap=WORD)
    output.grid(row = 3, column = 0, columnspan = 3, sticky = W)

    #creating dict
    reader = csv.reader(open(f"{records_folder}/{path_to_csv}", 'r'))
    customers = {}
    for row in reader:
        cname, phone, date, items = row
        customers[cname] = phone, date, items

    #creating label
    Label(window, text="Enter Items ", font= textformat) .grid(row = 4 , column = 0 , sticky=W)

    #Creating Entry for new Purchases
    newitem = Entry(window, width = 20 , font = textformat)
    newitem.grid(row = 5, column = 0, sticky = W)

    #creating button submit
    Button(window, text = "Entry New Items", width = 6, command = append_items).grid(row = 6, column = 0, sticky=W)    

    #text box for successful entry
    success_entry = Text(window, width = 75, height = 6, wrap=WORD)
    success_entry.grid(row = 7, column = 0, columnspan = 3, sticky = W)

    #exit label
    Label(window, text="Click to exit: ", font= textformat) .grid(row = 8 , column = 0 , sticky=W)

    #exit button
    Button(window, text = "EXIT", width = 6, command = close_window).grid(row = 9, column = 0, sticky=W)

    window.mainloop()

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
                with open(f"{records_folder}/{path_to_csv}", 'w') as f:
                    for key in customers.keys():
                        f.write("%s,"%(key))
                        internalDetails = customers[key]
                        f.write("%s,%s,%s\n"%(internalDetails[0], internalDetails[1], internalDetails[2]))
                definition = "Customer already exists, Items added to list\nAll Items purchased\n" + converteddetails[2]
                output.insert(END, definition)
            else:
                with open(f"{records_folder}/{path_to_csv}", 'a') as f:
                    f.write("%s,%s,%s,%s\n"%(name1,phone1,get_date(),items1))
                definition = "Customers Details Entered Successfully, Please Press Exit"
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
    reader  = csv.reader(open(f"{records_folder}/{path_to_csv}", 'r'))
    customers = {}
    for row in reader:
        cname, cphone, cdate, citems = row
        customers[cname] = cphone, cdate, citems

    #exit label
    Label(window, text="Click to exit: ", font= textformat) .grid(row = 6 , column = 0 , sticky=W)

    #exit button
    Button(window, text = "EXIT", width = 6, command = close_window).grid(row = 7, column = 0, sticky=W)


    
    window.mainloop()





#### FOR CAPTURING SCREEN RATHER THAN WEBCAM
# def captureScreen(bbox=(300,300,690+300,530+300)):
#     capScr = np.array(ImageGrab.grab(bbox))
#     capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
#     return capScr
 
encodeListKnown = find_encodings(images)
print('Encoding Complete')
 
cap = cv2.VideoCapture(0)
 
while True:
    success, img = cap.read()
    #img = captureScreen()
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
 
    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
 
    for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
        #print(faceDis)
        matchIndex = np.argmin(faceDis)
 
        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            #print(name)
            y1,x2,y2,x1 = faceLoc
            y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            show_gui(name)
        else :
            create_details_gui()
 
    cv2.imshow('Webcam',img)
    cv2.waitKey(1)