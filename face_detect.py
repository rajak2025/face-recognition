import cv2
import numpy as np
import face_recognition
import os
import csv
from datetime import datetime
from tkinter import *
# from PIL import ImageGrab
 
path = 'face-recognition/Images'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)
 
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
 
def markAttendance(name):
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
    
    def click():
        value1 = name.get()
        output.delete(0.0, END)
        #here 0.0 (clear every thing before the first line and the first character)
        try:
            details = customers[value1]
            definition = details[0]
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
    Button(window, text = "SUBMIT", width = 6, command = click).grid(row = 2, column = 0, sticky=W)

    #text box
    output = Text(window, width = 75, height = 6, wrap=WORD)
    output.grid(row = 3, column = 0, columnspan = 3, sticky = W)

    #creating dict
    reader = csv.reader(open('face-recognition/transactions.csv', 'r'))
    customers = {}
    for row in reader:
        cname, phone, date, items = row
        customers[cname] = phone, date, items


    #exit label
    Label(window, text="Click to exit: ", font= textformat) .grid(row = 4 , column = 0 , sticky=W)

    #exit button
    Button(window, text = "EXIT", width = 6, command = close_window).grid(row = 5, column = 0, sticky=W)

    window.mainloop()






#### FOR CAPTURING SCREEN RATHER THAN WEBCAM
# def captureScreen(bbox=(300,300,690+300,530+300)):
#     capScr = np.array(ImageGrab.grab(bbox))
#     capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
#     return capScr
 
encodeListKnown = findEncodings(images)
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

 
    cv2.imshow('Webcam',img)
    cv2.waitKey(1)