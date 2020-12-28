from tkinter import *



#click function for button
def click():
    value1 = name.get()
    output.delete(0.0, END)
    #here 0.0 (clear every thing before the first line and the first character)

    try:
        definition = customers[value1]
    except:
        definition = "sorry there is no customer"
    output.insert(END, definition)    

#exit function
def close_window():
    window.destroy()
    exit()



window = Tk()
window.title("Store Interface")

textformat = "calibri 24 bold"

Label(window, text="Name: ", font= textformat) .grid(row = 0 , column = 0 , sticky=W)
#Label(window, text="Phone: ", font= textformat) .grid(row = 1 , column = 0 , sticky=W)


#entrybox
name = Entry(window, width = 20, font = textformat)
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
customers = {
    'abc': '123',
    'bcd': '234' 
}

#exit label
Label(window, text="Click to exit: ", font= textformat) .grid(row = 4 , column = 0 , sticky=W)

#exit button
Button(window, text = "EXIT", width = 6, command = close_window).grid(row = 5, column = 0, sticky=W)



window.mainloop()