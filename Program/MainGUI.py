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
    # Date:  April 2, 2018
    def __btnEnter_click(self, event):

        self.lblStatus.config(text='')

        #IF NO FILE IS SELECTED, THEN THERE THE CODE IS NOT EXECUTED
        if self.lbl1.cget('text') != 'No File Selected':
            #DELETE ANY TEXT FOUND IN THE TEXTAREA
            self.editArea.delete('1.0', tk.END)

            if (self.Is_Integer(self.txtUserInput.get())):
                #CREATES CLUSTERS BY SENDING IN THE DATA POINTS AND THE NUMBER OF CLUSTERS CREATED
                self.cluster = Cluster(self.calculator.getPoints(), int(float(self.txtUserInput.get())))
                #THIS LINE OF CODE CREATES THE CLUSTERS
                self.cluster.Clustering()
                # AFTER THE STATES ARE CLUSTERED IN, THE INFORMATION IS POSTED ON THE TEXTAREA
                self.editArea.insert(tk.INSERT, self.cluster.getInformation())

        else:
            self.lblStatus.config(text= 'No acceptable file has been selected yet.')

    # Method Name: __btnUpLoad_click()
    # Purpose: This method is an event handler for a button
    # Parameter: self, event
    # Method used: none
    # Return Value: none
    # Date:  April 2, 2018
    def __btnUpLoad_click(self, event):

        # class variable will hold the class object File_IO()
        self.data = File_IO()

        self.calculator = 0
        self.cluster = 0

        try:
            # USES A CLASS METHOD OT OPEN A TEXT FILE
            self.data.openFile()
            # USES A CLASS METHOD TO READ A TEXT FILE
            self.data.readFile()
            # GUI LABEL1 WILL CONTAIN THE NAME OF THE FILE (IF ANY)
            self.lbl1.config(text=self.data.fileName)
        except:
            self.lbl1.config(text= 'No File Selected')


        #SENDS IN THE STATE LIST OBJECTS TO THE PARAMENETER
        # OF CALCULATOR AND FINDS NECESSARY INFORMATION FOR COMPUTATION
        self.calculator = Calculation(self.data.getStates())
        #MAKES NECESSARY CALCULATIONS FROM THE DATA GIVEN
        self.calculator.MainCalculation()


        # LBLSTATUS IS CLEARED
        self.lblStatus.config(text='Enter number of Clusters')

    # Method Name: Is_Integer()
    # Purpose: checks if string/number is an integer
    # Parameter: self, num
    # Method used: none
    # Return Value: boolean
    # Date:  April 2, 2018
    def Is_Integer(self,num):

        try:
            if float(num).is_integer():

                if not(float(num) > 0 and float(num) < 50):

                    self.lblStatus.config(text='Input must be an integer between 0 and 50,\n exclusive')
                    return False
                return True
            else:
                self.lblStatus.config(text='Input must be an integer')
                return False
        except:
            return False


    # Method Name:__INIT__
    # Purpose: Class constructor
    # Parameter: self
    # Method used: __btnEnter(), __btnUpLoad()
    # Return Value: none
    # Date:  April 2, 2018
    def __init__(self):



        # CLASS VARIABLE WILL HOLD THE REFERENCE TO THE GUI WINDOW
        self.MainGUI = tk.Tk()
        # WINDOW TEXT WILL CONTAIN A TEXT
        self.MainGUI.title('K-Mean Cluster')
        # THE INITIAL SIZE OF THE GUI
        self.MainGUI.geometry('600x300')
        # THE MINIMUM SIZE OF THE GUI
        self.MainGUI.minsize(600, 310)

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
        self.lblStatus.place(x=120, y=110)
        self.lblStatus.config(text='Enter number of Clusters')

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

        #CREATES A TEXTAREA
        self.editArea = tkst.ScrolledText(
            master=self.MainGUI,
            wrap=tk.WORD,
            width=20,
            height=15,
            #state = tk.DISABLED
        )
        #SETS THE PLACEMENT OF OBJECT
        self.editArea.pack(padx=10, pady=10, fill=tk.NONE, expand=False)
        self.editArea.place(x=370, y=50)


    # Method Name: Run()
    # Purpose: this will allow the the GUI to run (start)
    # Parameter: self
    # Method used: none
    # Return Value: none
    # Date:  April 2, 2018
    def run(self):
        # This is the method used for the gui to be seen on screen
        self.MainGUI.mainloop()
