# Author: Casey Betts, 2022
# Description: A calculation GUI able to determine the time it takes for two objects to collide when only under the influence of their own gravity
# See README.md for full description and instructions to run

from tkinter import *
from PIL import ImageTk,Image
import math
from tkinter import ttk

# Defining a picture variable
# find spaceRock image at https://www.theverge.com/2018/6/27/17509888/oumuamua-interstellar-comet-asteroid-solar-system-trajectory
image = Image.open("spacerock.jpg")

# Gravitational constant
G = 6.6743e-11 # m3 kg-1 s-2

#Defining the main window class
class Gravity(Tk):
    # This class is a TKinter object and contains all the main elements of the program

    def __init__(self):
        super().__init__()

        self.title("The Gravity Project")                       # Title on title bar
        width, height = 1100, 700                               # Window width and height
        self.geometry(str(width)+"x"+str(height))               # Window size
        self.resizable(False,False)                             # Make window un-resizable

        # Define the image
        self.resized = image.resize((width, height))            # Adjust image size
        self.img = ImageTk.PhotoImage(self.resized)             # Create a TK image object

        # Define Canvas
        self.canvas = Canvas(self, width=width, height=height)  # Create the canvas 


        #Column designations
        self.titleCol = 330                                     # Title column
        self.mass1Col = 65                                      # Mass 1 entry box column
        self.mass2Col = self.mass1Col + 210                     # Mass 2 entry box column
        self.distCol = self.mass2Col + 290                      # Distance entry box column
        self.resultCol = 840                                    # Resutls column

        # Row definitions
        self.titleRow = 20                                      # Title row
        self.labelRow = 90                                      # Column label row (ie. Mass1, Mass2, Distance)
        self.radioStartRow = 130                                # Start row for radio buttons
        self.radioSep = 35                                      # Vertical separation of radio buttons

        # Radio button colors and fonts
        self.radiofont = "Times"                                # Radio button font
        self.radiosize = 12                                     # Radio button size
        self.radiofg = "white"                                  # Radio button forground color
        self.radiobg = "black"                                  # Radio button background color
        self.radioSelect = "grey"                               # Color inside the radio button
        self.radioAn = "nw"                                     # Anchor for the radio buttons
        self.entryRow = self.radioStartRow + self.radioSep*15   # Row for the manual mass entry boxes 

        # Defining radio button options
        # List contains tuples of: object name, mass, approximate radius
        self.OBJLIST = [
            ("Earth",5.97219e24,6.371e6),
            ("Moon",7.34767309e22,1.7374e6),
            ("Ceres",9.1e20,473e3),
            ("Ida", 1e17, 1.57e4),
            ("Bennu", 7.3e10,2.625e2),
            ("AircraftCarrier", 1.046e8,200),
            ("ISS",4.44615e5,109),
            ("Abrams Tank",6e4,2),
            ("Chevy Colorado",1.791e3,2),
            ("Human",7.7e1,0.2),
            ("Gopher", 2e-1, 0.05),
            ("Fly",3e-7,3e-3),
            ("Litheum Molecule", 1.1525801e-26, 1.52e-10),
            ("Custom",1,1)]



        # Defining radio button variables
        # Variables will be used to hold the index associated with the OBJLIST
        self.r_mass1v = IntVar()
        self.r_mass2v = IntVar()

        # Create containing list for radio buttons
        self.radio_button = []

        # Create the Radio buttons
        # Radio buttons associated with an index variable as well as a command to update text in the mass entry fields
        for i in range(len(self.OBJLIST)):
            # Creating the fist column of radio buttons and adding them to the list
            temp_radio_button = Radiobutton(self,
                                            text= self.OBJLIST[i][0], 
                                            variable= self.r_mass1v,
                                            value= i, 
                                            command= lambda: self.rCommand(self.r_mass1v.get(), 1), 
                                            font= (self.radiofont,self.radiosize), 
                                            fg= self.radiofg, 
                                            bg= self.radiobg,
                                            selectcolor= self.radioSelect)
            self.radio_button.append(temp_radio_button)

        for i in range(len(self.OBJLIST)):
            # Creating the second column of radio buttons and adding them to the list
            temp_radio_button = Radiobutton(self,
                                            text= self.OBJLIST[i][0], 
                                            variable= self.r_mass2v,
                                            value= i, 
                                            command= lambda: self.rCommand(self.r_mass2v.get(), 2), 
                                            font= (self.radiofont,self.radiosize), 
                                            fg= self.radiofg, 
                                            bg= self.radiobg,
                                            selectcolor= self.radioSelect)
            self.radio_button.append(temp_radio_button)

        # Creating all text entry boxes
        self.e_mass1 = ttk.Entry(self, width = 19)              # Column one mass text box
        self.e_mass1e = ttk.Entry(self, width= 4)               # Column one mass exponent text box
        self.e_mass2 = ttk.Entry(self, width = 19)              # Column two mass text box
        self.e_mass2e = ttk.Entry(self, width= 4)               # Column two mass exponent text box
        self.e_height = ttk.Entry(self, width = 10)             # Distance text box
        

        # Creating the 'Submit' button
        self.b_submit = Button(self, 
                                text = "        Submit        ", 
                                command =lambda: self.submit(
                                self.e_mass1.get(),
                                self.e_mass1e.get(),
                                self.e_mass2.get(),
                                self.e_mass2e.get(),
                                self.exSplit(self.OBJLIST[self.r_mass1v.get()][2])[0],
                                self.exSplit(self.OBJLIST[self.r_mass1v.get()][2])[1],
                                self.exSplit(self.OBJLIST[self.r_mass2v.get()][2])[0],
                                self.exSplit(self.OBJLIST[self.r_mass2v.get()][2])[1],
                                self.e_height.get()),
                                font=(self.radiofont,self.radiosize),
                                fg=self.radiofg,
                                bg=self.radiobg)

        # Creating the 'Quit' button
        self.b_quit = Button(self, text="Quit", command=self.destroy,font=(self.radiofont,self.radiosize),fg=self.radiofg, bg=self.radiobg)

        # Place the widgets on the window
        self.build()

    def build(self):
        # This function adds the widgets to the canvas

        # Build Canvas
        self.canvas.grid(column=0,row=0, columnspan=7)

        # Place the image on the canvas
        self.canvas.create_image(0,0, image=self.img, anchor="nw")

        # Create the radio button windows for the first column
        for i in range(len(self.OBJLIST)):
            self.canvas.create_window(  self.mass1Col,
                                        self.radioStartRow + self.radioSep*i, 
                                        anchor=self.radioAn, 
                                        window=self.radio_button[i])

        # Create the radio button windows for the second column
        for i in range(len(self.OBJLIST)):
            self.canvas.create_window(  self.mass2Col,
                                        self.radioStartRow + self.radioSep*i, 
                                        anchor=self.radioAn, 
                                        window=self.radio_button[i+14])

        # Defining a lable in a variable to change later
        self.l_result = self.canvas.create_text(self.resultCol,260, text=("...to find time till impact"), font=('Times', 20),fill="white")
        self.l_acc = self.canvas.create_text(self.resultCol, 520, text=(""), font=('Times', '16'),fill="white")

        # Adding text to the canvas
        self.canvas.create_text(130,20, text=("Choose two objects..."), font=('Times', 20),fill="white")
        self.canvas.create_text(self.mass1Col+40,self.labelRow, text=("Mass 1 (kg)"), font=('Times', '14'),fill='white')
        self.canvas.create_text(self.mass1Col+128,self.entryRow, text=("e"), font=('Times', '14'),fill='white')
        self.canvas.create_text(self.mass2Col+40,self.labelRow, text=("Mass 2 (kg)"), font=('Times', '14'),fill='white')
        self.canvas.create_text(self.mass2Col+128,self.entryRow, text=("e"), font=('Times', '14'),fill='white')
        self.canvas.create_text(self.distCol,self.labelRow, text=("Distance (m)"), font=('Times', '14'),fill='white')

        # Placing the entry boxes
        self.canvas.create_window(self.mass1Col+60, self.entryRow, window=self.e_mass1)
        self.canvas.create_window(self.mass1Col+150, self.entryRow, window=self.e_mass1e)
        self.canvas.create_window(self.mass2Col+60, self.entryRow, window=self.e_mass2)
        self.canvas.create_window(self.mass2Col+150, self.entryRow, window=self.e_mass2e)
        self.canvas.create_window(self.distCol, self.radioStartRow, window=self.e_height)

        # Placing the button windows
        self.canvas.create_window(self.resultCol, self.radioStartRow + self.radioSep*12, window=self.b_submit)
        self.canvas.create_window(self.resultCol, self.radioStartRow + self.radioSep*13, window=self.b_quit)

        # Filling the text boxes with defaults
        self.e_height.insert(0,'2') #meters                     # Default value for distance
        self.radio_button[0].invoke()                           # Default for column one mass text box
        self.radio_button[14].invoke()                          # Default for column two mass text box

    def submit(self,m1,m1e,m2,m2e,r1,r1e,r2,r2e,d):
        # Submit button function

        invalid_entry = False           # Flag for an invalid entry        
        
        # Check for an invalid entry and change the color of the text box in that case
        if self.e_mass1.get()=='':
            self.e_mass1.config(bg='red')
            invalid_entry = True
        if self.e_mass1e.get()=='':
            self.e_mass1e.config(bg='red')
            invalid_entry = True
        if self.e_mass2.get()=='':
            self.e_mass2.config(bg='red')
            invalid_entry = True
        if self.e_height.get()=='':
            self.e_height.config(bg='red')
            invalid_entry = True

        # If entry is valid then run and display the calculation
        if invalid_entry == False:
            
            # Reset the entry box background colors in case they were changed due to an invalid entry
            self.e_mass1.config(background='white')
            self.e_mass1e.config(background='white')
            self.e_mass2.config(background='white')
            self.e_height.config(background='white')

            # Set the varaiables to the correct type
            m1 = float(m1)
            m1e = int(m1e)
            m2 = float(m2)
            m2e = int(m2e)
            r1 = float(r1)
            r1e = int(r1e)
            r2 = float(r2)
            r2e = int(r2e)

            # Take the masses to the power of their respective exponent
            m1*=(10**m1e)
            m2*=(10**m2e)
            r1*=(10**r1e)
            r2*=(10**r2e)

            # Run the calcuation function and store in a variable
            result = self.attracting(m1,float(m2),r1,r2,float(d),1000)

            # Display the resuts
            self.canvas.itemconfig(self.l_result,text=str(round(result[0],3))+" "+result[1])
            self.canvas.itemconfig(self.l_acc,text="Acceleration at center of mass 2: "+str(round(result[2],3)))

    def rCommand(self,var,field):
        # This fuction changes the mass value displayed in the entry box when the radio button is changed

        # Break up the mass into base and exponential components
        valu = self.exSplit(float(self.OBJLIST[var][1]))

        if field == 1:

            # Change text box states back to normal
            self.e_mass1.configure(state=["normal"])
            self.e_mass1e.configure(state=["normal"])

            # Delete the current text
            self.e_mass1.delete(0,END)
            self.e_mass1e.delete(0,END)

            # Insert the value based on the radio button selected
            self.e_mass1.insert(0,valu[0])
            self.e_mass1e.insert(0,valu[1])

            # If the selected radio button is not 'Custom' then make it read only 
            if var != 13:
                self.e_mass1.configure(state=["readonly"])
                self.e_mass1e.configure(state=["readonly"])

        elif field == 2:

            # Change text box states back to normal
            self.e_mass2.configure(state=["normal"])
            self.e_mass2e.configure(state=["normal"])

            # Delete the current text
            self.e_mass2.delete(0,END)
            self.e_mass2e.delete(0,END)

            # Insert the value based on the radio button selected
            self.e_mass2.insert(0,valu[0])
            self.e_mass2e.insert(0,valu[1])

            # If the selected radio button is not 'Custom' then make it read only 
            if var != 13:
                self.e_mass2.configure(state=["readonly"])
                self.e_mass2e.configure(state=["readonly"])

    def exSplit(self,num):
        #Convert exponential notation to value and exponent

        count = 0

        # Check for negagive value which is not accepted since the value should be a mass
        if num <= 0:
            return [0,0]

        # For numbers greater than 1, divide the value by 10 until it is less than 10. The number of divisions equals the exponent
        elif num > 1:
            while num > 10:
                num/=10
                count+=1

        # For numbers less than 1, multiply the value by 10 until it's greater than 1. The number of multiplications equals the exponent
        else:
            while num < 1:
                num*=10
                count-=1

        # Returns the value and the exponent in a list
        return [num, count]

    def attracting(self,m1,m2,r1,r2,d,frames):
        # Calculates the time it takes for two masses to collide from a given distance
        
        # The logic of this function is as follows:
            # The distance, d, between the objects's surfaces is divided into segments (number of segments is given by 'frames')
            # The acceleration due to gravity for the objects is calulated from object center to object center
                # wich is calculated by adding the radius of each object to the given distance: r = d + r1 + r2
            # While the distance traveled is less than d (the initial distance between the object's surfaces):
                # Calculate the force due to gravity, acceleration of each object and time it takes to move one segment
                # The new distance between the objects is the segment length plus the distance the larger object traveled
                # The new velocities are calculated by distance over time for each object
                # The total time elapsed is increased by the time taken for the smaller object to travers the segment (calculated above)
        # The function converts the time into more convienient units and returns a list giving: calculated time, units, initial acceleration of mass 2

        # Variable definitions
        segment = d/frames          # Divides the total distance between objects into equal parts
        r = d + r1 + r2             # Total distance from object center to object center
        traveled = 0                # Initalizing distance traveled by the objects
        v1 = v2 = 0                 # Initializing starting velocities for both objects
        total_t = 0                 # Initializing the total time elapsed
        a2i = (G*m1)/(r**2)         # Initial acceleration squared

        # Ensure mass 1 is the larger mass
        if m1 < m2:
            m1, m2 = m2, m1
        
        # While the distance traveled is less than the initial distance between the object's surfaces
        while traveled < d:

            # Calculate the necessary physical attributes
            # This is the equation for force due to gravity (in N): F = (G*m1*m2)/(r**2)  
            a1 = (G*m2)/(r**2)                                  # Acceleration of mass 1: a1 = F/m1
            a2 = (G*m1)/(r**2)                                  # Acceleration of mass 2: a2 = F/m2
            t = (-v2 + math.sqrt((v2**2)+(2*a2*segment)))/a2    # Time for small object to move one segment
            trav1 = ((t**2)*a1*.5) + v1*t                       # Cistance larger object travels in time t
            traveled+= (segment + trav1)                        # Combined distance the objects travel toward eachother

            # Updating variables
            r-=(segment+trav1)              # Updating the center to center distance
            v1 = trav1/t                    # Updating the velocity of object 1: v1 = d1/t
            v2 = segment/t                  # Updating the velocity of object 2: v2 = d2/t
            total_t+=t                      # Updating the total time elapsed

        # Determining the best units to provide the time in and making the conversion form seconds
        if total_t > 31536000:
            total_t/=31536000
            unit = "years"
        elif total_t > 86000:
            total_t/=86400
            unit = "days"
        elif total_t > 14400:
            total_t/=3600
            unit = "hours"
        else:
            unit = "sec"

        # Returning a list giving: calculated time, units, initial acceleration of mass 2
        return [total_t, unit, a2i]



if __name__ == "__main__":

    # Creating the class containing the main program
    grav = Gravity()

    # Running the main loop
    grav.mainloop()
