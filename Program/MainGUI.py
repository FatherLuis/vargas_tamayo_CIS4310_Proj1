import tkinter as tk
import tkinter.scrolledtext as tkst

from Program.Calculation import Calculation
from Program.Cluster import Cluster
from Program.File_IO import File_IO



# Class name: MainGUI
# Class Author: Luis E. Vargas Tamayo
# Purpose of the class: Creates the GUI for the program to run
# Date: 2/2/2018
# List of changes with dates: none
# Special Notes: none

class MainGUI:

    # Method Name: __btnEnter_click()
    # Purpose: This method is an event handler for a button
    # Parameter: self, event
    # Method used: none
    # Return Value: none
    # Date:  April 2, 2019
    def __btnEnter_click(self, event):

        if self.lbl1.cget('text') != 'No File Selected':
            self.editArea.delete('1.0', tk.END)
            #print("Hello World")
            self.cluster = Cluster(self.calculator.getPoints(), int(self.txtUserInput.get()))
            self.cluster.Clustering()

            self.editArea.insert(tk.INSERT, self.cluster.getInformation())



        else:
            self.lblStatus.config(text= 'No acceptable file has been selected yet.')

    # Method Name: __btnUpLoad_click()
    # Purpose: This method is an event handler for a button
    # Parameter: self, event
    # Method used: none
    # Return Value: none
    # Date:  April 2, 2019
    def __btnUpLoad_click(self, event):

        # USES A CLASS METHOD OT OPEN A TEXT FILE
        self.data.openFile()
        # USES A CLASS METHOD TO READ A TEXT FILE
        self.data.readFile()
        self.calculator = Calculation(self.data.getStates())
        self.calculator.MainCalculation()


        # GUI LABEL1 WILL CONTAIN THE NAME OF THE FILE (IF ANY)
        self.lbl1.config(text=self.data.fileName)
        # LBLSTATUS IS CLEARED
        self.lblStatus.config(text='')

    # Method Name:__INIT__
    # Purpose: Class constructor
    # Parameter: self
    # Method used: __btnEnter(), __btnUpLoad()
    # Return Value: none
    # Date:  April 2, 2019
    def __init__(self):

        # class variable will hold the class object File_IO()
        self.data = File_IO()

        self.calculator = 0
        self.cluster = 0

        # CLASS VARIABLE WILL HOLD THE REFERENCE TO THE GUI WINDOW
        self.MainGUI = tk.Tk()
        # WINDOW TEXT WILL CONTAIN A TEXT
        self.MainGUI.title('K-Mean Cluster')
        # THE INITIAL SIZE OF THE GUI
        self.MainGUI.geometry('600x300')
        # THE MINIMUM SIZE OF THE GUI
        self.MainGUI.minsize(600, 300)

        # CREATES AN OBJECT BUTTON USED ON THE GUI
        btnUpload = tk.Button(self.MainGUI, width=15, height=2, text='Upload File')
        # PLACES THE BUTTON IN THE FOLLOWING COORDINATES ON THE GUI
        btnUpload.place(x=10, y=20)
        # BINDS AN EVENT METHOD TO THE BUTTON
        btnUpload.bind('<ButtonRelease-1>', self.__btnUpLoad_click)
        # CREATES AN OBJECT LABEL

        self.lbl1 = tk.Label(self.MainGUI, height=2, text='No File Selected')
        # PLACES THE LABEL IN THE FOLLOWING COORDINATES ON THE GUI
        self.lbl1.place(x=150, y=22)

        self.lblStatus = tk.Label(self.MainGUI, height=2, text='')
        # PLACES THE LABEL IN THE FOLLOWING COORDINATE ON THE GUI
        self.lblStatus.place(x=120, y=120)

        # CREATES AN OBJECT TEXTBOX
        self.txtUserInput = tk.Entry(self.MainGUI, width=30, )
        # PLACES THE TEXTBOOK IN THE FOLLOWING COORDINATE ON THi GUI
        self.txtUserInput.place(x=120, y=150)

        # CREATES AN OBJECT BUTTON USED ON THE GUI
        btnEnter = tk.Button(self.MainGUI, width=20, height=2, text='Enter')
        # PLACES THE BUTTON IN THE FOLLOWING COORDINATE ON THE GUI
        btnEnter.place(x=120, y=210)
        # BINDS AN EVENT METHOD TO THE BUTTON
        btnEnter.bind('<ButtonRelease-1>', self.__btnEnter_click)

        self.editArea = tkst.ScrolledText(
            master=self.MainGUI,
            wrap=tk.WORD,
            width=20,
            height=15,
            #state = tk.DISABLED
        )
        # Don't use widget.place(), use pack or grid instead, since
        # They behave better on scaling the window -- and you don't
        # have to calculate it manually!
        self.editArea.pack(padx=10, pady=10, fill=tk.NONE, expand=False)
        self.editArea.place(x=350, y=50)


    # Method Name: Run()
    # Purpose: this will allow the the GUI to run (start)
    # Parameter: self
    # Method used: none
    # Return Value: none
    # Date:  April 2, 2019
    def run(self):
        # This is the method used for the gui to be seen on screen
        self.MainGUI.mainloop()