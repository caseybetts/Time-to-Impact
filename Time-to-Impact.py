from tkinter import *
from PIL import ImageTk,Image
import math
from tkinter import ttk

# Defining a picture variable
# find spaceRock image at https://www.theverge.com/2018/6/27/17509888/oumuamua-interstellar-comet-asteroid-solar-system-trajectory
image = Image.open("spacerock.jpg") #change image here

# gravity constant
G = 6.6743e-11 # m3 kg-1 s-2

#Defining the main window class
class Gravity(Tk):
    def __init__(self):
        super().__init__()

        self.title("The Gravity Project")
        self.geometry("1100x700")
        self.resizable(False,False)

        # Define the image
        self.resized = image.resize((1100,700))
        self.img = ImageTk.PhotoImage(self.resized)

        # Define Canvas
        self.canvas = Canvas(self, width=1100, height=700)

        # Place the image on the canvas
        # self.canvas.create_image(0,0, image=img, anchor="nw")

        #Column designations
        self.titleCol = 330
        self.mass1Col = 65
        self.mass2Col = self.mass1Col + 210
        self.distCol = self.mass2Col + 290
        self.resultCol = 840

        # Row definitions
        self.titleRow = 20
        self.labelRow = 90
        self.radioStartRow = 130
        self.radioSep = 35

        # Radio button colors and fonts
        self.radiofont = "Times"
        self.radiosize = 12
        self.radiofg = "white"
        self.radiobg = "black"
        self.radioSelect = "gray"
        self.radioAn = "nw"
        self.entryRow = self.radioStartRow + self.radioSep*15

        # Defining radio button options
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
        self.r_mass1v = IntVar()
        self.r_mass2v = IntVar()

        # Create the Radio buttons
        self.r_mass1a = Radiobutton(self,text=self.OBJLIST[0][0],variable=self.r_mass1v, value=0, command=lambda: self.rCommand(self.r_mass1v.get(),1),font=(self.radiofont,self.radiosize),fg=self.radiofg, bg=self.radiobg,selectcolor=self.radioSelect)
        self.r_mass1b = Radiobutton(self,text=self.OBJLIST[1][0],variable=self.r_mass1v, value=1, command=lambda: self.rCommand(self.r_mass1v.get(),1),font=(self.radiofont,self.radiosize),fg=self.radiofg, bg=self.radiobg,selectcolor=self.radioSelect)
        self.r_mass1c = Radiobutton(self,text=self.OBJLIST[2][0],variable=self.r_mass1v, value=2, command=lambda: self.rCommand(self.r_mass1v.get(),1),font=(self.radiofont,self.radiosize),fg=self.radiofg, bg=self.radiobg,selectcolor=self.radioSelect)
        self.r_mass1d = Radiobutton(self,text=self.OBJLIST[3][0],variable=self.r_mass1v, value=3, command=lambda: self.rCommand(self.r_mass1v.get(),1),font=(self.radiofont,self.radiosize),fg=self.radiofg, bg=self.radiobg,selectcolor=self.radioSelect)
        self.r_mass1e = Radiobutton(self,text=self.OBJLIST[4][0],variable=self.r_mass1v, value=4, command=lambda: self.rCommand(self.r_mass1v.get(),1),font=(self.radiofont,self.radiosize),fg=self.radiofg, bg=self.radiobg,selectcolor=self.radioSelect)
        self.r_mass1f = Radiobutton(self,text=self.OBJLIST[5][0],variable=self.r_mass1v, value=5, command=lambda: self.rCommand(self.r_mass1v.get(),1),font=(self.radiofont,self.radiosize),fg=self.radiofg, bg=self.radiobg,selectcolor=self.radioSelect)
        self.r_mass1g = Radiobutton(self,text=self.OBJLIST[6][0],variable=self.r_mass1v, value=6, command=lambda: self.rCommand(self.r_mass1v.get(),1),font=(self.radiofont,self.radiosize),fg=self.radiofg, bg=self.radiobg,selectcolor=self.radioSelect)
        self.r_mass1h = Radiobutton(self,text=self.OBJLIST[7][0],variable=self.r_mass1v, value=7, command=lambda: self.rCommand(self.r_mass1v.get(),1),font=(self.radiofont,self.radiosize),fg=self.radiofg, bg=self.radiobg,selectcolor=self.radioSelect)
        self.r_mass1i = Radiobutton(self,text=self.OBJLIST[8][0],variable=self.r_mass1v, value=8, command=lambda: self.rCommand(self.r_mass1v.get(),1),font=(self.radiofont,self.radiosize),fg=self.radiofg, bg=self.radiobg,selectcolor=self.radioSelect)
        self.r_mass1j = Radiobutton(self,text=self.OBJLIST[9][0],variable=self.r_mass1v, value=9, command=lambda: self.rCommand(self.r_mass1v.get(),1),font=(self.radiofont,self.radiosize),fg=self.radiofg, bg=self.radiobg,selectcolor=self.radioSelect)
        self.r_mass1k = Radiobutton(self,text=self.OBJLIST[10][0],variable=self.r_mass1v, value=10, command=lambda: self.rCommand(self.r_mass1v.get(),1),font=(self.radiofont,self.radiosize),fg=self.radiofg, bg=self.radiobg,selectcolor=self.radioSelect)
        self.r_mass1l = Radiobutton(self,text=self.OBJLIST[11][0],variable=self.r_mass1v, value=11, command=lambda: self.rCommand(self.r_mass1v.get(),1),font=(self.radiofont,self.radiosize),fg=self.radiofg, bg=self.radiobg,selectcolor=self.radioSelect)
        self.r_mass1m = Radiobutton(self,text=self.OBJLIST[12][0],variable=self.r_mass1v, value=12, command=lambda: self.rCommand(self.r_mass1v.get(),1),font=(self.radiofont,self.radiosize),fg=self.radiofg, bg=self.radiobg,selectcolor=self.radioSelect)
        self.r_mass1n = Radiobutton(self,text=self.OBJLIST[13][0],variable=self.r_mass1v, value=13, command=lambda: self.rCommand(self.r_mass1v.get(),1),font=(self.radiofont,self.radiosize),fg=self.radiofg, bg=self.radiobg,selectcolor=self.radioSelect)

        self.r_mass2a = Radiobutton(self,text=self.OBJLIST[0][0],variable=self.r_mass2v, value=0, command=lambda: self.rCommand(self.r_mass2v.get(),2),font=(self.radiofont,self.radiosize),fg=self.radiofg, bg=self.radiobg,selectcolor=self.radioSelect)
        self.r_mass2b = Radiobutton(self,text=self.OBJLIST[1][0],variable=self.r_mass2v, value=1, command=lambda: self.rCommand(self.r_mass2v.get(),2),font=(self.radiofont,self.radiosize),fg=self.radiofg, bg=self.radiobg,selectcolor=self.radioSelect)
        self.r_mass2c = Radiobutton(self,text=self.OBJLIST[2][0],variable=self.r_mass2v, value=2, command=lambda: self.rCommand(self.r_mass2v.get(),2),font=(self.radiofont,self.radiosize),fg=self.radiofg, bg=self.radiobg,selectcolor=self.radioSelect)
        self.r_mass2d = Radiobutton(self,text=self.OBJLIST[3][0],variable=self.r_mass2v, value=3, command=lambda: self.rCommand(self.r_mass2v.get(),2),font=(self.radiofont,self.radiosize),fg=self.radiofg, bg=self.radiobg,selectcolor=self.radioSelect)
        self.r_mass2e = Radiobutton(self,text=self.OBJLIST[4][0],variable=self.r_mass2v, value=4, command=lambda: self.rCommand(self.r_mass2v.get(),2),font=(self.radiofont,self.radiosize),fg=self.radiofg, bg=self.radiobg,selectcolor=self.radioSelect)
        self.r_mass2f = Radiobutton(self,text=self.OBJLIST[5][0],variable=self.r_mass2v, value=5, command=lambda: self.rCommand(self.r_mass2v.get(),2),font=(self.radiofont,self.radiosize),fg=self.radiofg, bg=self.radiobg,selectcolor=self.radioSelect)
        self.r_mass2g = Radiobutton(self,text=self.OBJLIST[6][0],variable=self.r_mass2v, value=6, command=lambda: self.rCommand(self.r_mass2v.get(),2),font=(self.radiofont,self.radiosize),fg=self.radiofg, bg=self.radiobg,selectcolor=self.radioSelect)
        self.r_mass2h = Radiobutton(self,text=self.OBJLIST[7][0],variable=self.r_mass2v, value=7, command=lambda: self.rCommand(self.r_mass2v.get(),2),font=(self.radiofont,self.radiosize),fg=self.radiofg, bg=self.radiobg,selectcolor=self.radioSelect)
        self.r_mass2i = Radiobutton(self,text=self.OBJLIST[8][0],variable=self.r_mass2v, value=8, command=lambda: self.rCommand(self.r_mass2v.get(),2),font=(self.radiofont,self.radiosize),fg=self.radiofg, bg=self.radiobg,selectcolor=self.radioSelect)
        self.r_mass2j = Radiobutton(self,text=self.OBJLIST[9][0],variable=self.r_mass2v, value=9, command=lambda: self.rCommand(self.r_mass2v.get(),2),font=(self.radiofont,self.radiosize),fg=self.radiofg, bg=self.radiobg,selectcolor=self.radioSelect)
        self.r_mass2k = Radiobutton(self,text=self.OBJLIST[10][0],variable=self.r_mass2v, value=10, command=lambda: self.rCommand(self.r_mass2v.get(),2),font=(self.radiofont,self.radiosize),fg=self.radiofg, bg=self.radiobg,selectcolor=self.radioSelect)
        self.r_mass2l = Radiobutton(self,text=self.OBJLIST[11][0],variable=self.r_mass2v, value=11, command=lambda: self.rCommand(self.r_mass2v.get(),2),font=(self.radiofont,self.radiosize),fg=self.radiofg, bg=self.radiobg,selectcolor=self.radioSelect)
        self.r_mass2m = Radiobutton(self,text=self.OBJLIST[12][0],variable=self.r_mass2v, value=12, command=lambda: self.rCommand(self.r_mass2v.get(),2),font=(self.radiofont,self.radiosize),fg=self.radiofg, bg=self.radiobg,selectcolor=self.radioSelect)
        self.r_mass2n = Radiobutton(self,text=self.OBJLIST[13][0],variable=self.r_mass2v, value=13, command=lambda: self.rCommand(self.r_mass2v.get(),2),font=(self.radiofont,self.radiosize),fg=self.radiofg, bg=self.radiobg,selectcolor=self.radioSelect)

        # Defining all text entry boxes
        self.e_mass1 = ttk.Entry(self, width = 19)
        self.e_mass1e = ttk.Entry(self, width= 4)
        self.e_mass2 = ttk.Entry(self, width = 19)
        self.e_mass2e = ttk.Entry(self, width= 4)
        self.e_height = ttk.Entry(self, width = 10)
        self.e_height.insert(0,'2') #meters

        # Defining the buttons
        self.b_submit = Button(self, text = "        Submit        ", command =lambda: self.submit(
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
        self.b_quit = Button(self, text="Quit", command=self.destroy,font=(self.radiofont,self.radiosize),fg=self.radiofg, bg=self.radiobg)

    def build(self):

        # Build Canvas
        self.canvas.grid(column=0,row=0, columnspan=7)

        # Place the image on the canvas
        self.canvas.create_image(0,0, image=self.img, anchor="nw")

        # Radio button windows
        self.canvas.create_window(self.mass1Col, self.radioStartRow                  , anchor=self.radioAn, window=self.r_mass1a)
        self.canvas.create_window(self.mass1Col, self.radioStartRow + self.radioSep  , anchor=self.radioAn, window=self.r_mass1b)
        self.canvas.create_window(self.mass1Col, self.radioStartRow + self.radioSep*2, anchor=self.radioAn, window=self.r_mass1c)
        self.canvas.create_window(self.mass1Col, self.radioStartRow + self.radioSep*3, anchor=self.radioAn, window=self.r_mass1d)
        self.canvas.create_window(self.mass1Col, self.radioStartRow + self.radioSep*4, anchor=self.radioAn, window=self.r_mass1e)
        self.canvas.create_window(self.mass1Col, self.radioStartRow + self.radioSep*5, anchor=self.radioAn, window=self.r_mass1f)
        self.canvas.create_window(self.mass1Col, self.radioStartRow + self.radioSep*6, anchor=self.radioAn, window=self.r_mass1g)
        self.canvas.create_window(self.mass1Col, self.radioStartRow + self.radioSep*7, anchor=self.radioAn, window=self.r_mass1h)
        self.canvas.create_window(self.mass1Col, self.radioStartRow + self.radioSep*8, anchor=self.radioAn, window=self.r_mass1i)
        self.canvas.create_window(self.mass1Col, self.radioStartRow + self.radioSep*9, anchor=self.radioAn, window=self.r_mass1j)
        self.canvas.create_window(self.mass1Col, self.radioStartRow + self.radioSep*10, anchor=self.radioAn, window=self.r_mass1k)
        self.canvas.create_window(self.mass1Col, self.radioStartRow + self.radioSep*11, anchor=self.radioAn, window=self.r_mass1l)
        self.canvas.create_window(self.mass1Col, self.radioStartRow + self.radioSep*12, anchor=self.radioAn, window=self.r_mass1m)
        self.canvas.create_window(self.mass1Col, self.radioStartRow + self.radioSep*13, anchor=self.radioAn, window=self.r_mass1n)

        self.canvas.create_window(self.mass2Col, self.radioStartRow                  , anchor=self.radioAn, window=self.r_mass2a)
        self.canvas.create_window(self.mass2Col, self.radioStartRow + self.radioSep  , anchor=self.radioAn, window=self.r_mass2b)
        self.canvas.create_window(self.mass2Col, self.radioStartRow + self.radioSep*2, anchor=self.radioAn, window=self.r_mass2c)
        self.canvas.create_window(self.mass2Col, self.radioStartRow + self.radioSep*3, anchor=self.radioAn, window=self.r_mass2d)
        self.canvas.create_window(self.mass2Col, self.radioStartRow + self.radioSep*4, anchor=self.radioAn, window=self.r_mass2e)
        self.canvas.create_window(self.mass2Col, self.radioStartRow + self.radioSep*5, anchor=self.radioAn, window=self.r_mass2f)
        self.canvas.create_window(self.mass2Col, self.radioStartRow + self.radioSep*6, anchor=self.radioAn, window=self.r_mass2g)
        self.canvas.create_window(self.mass2Col, self.radioStartRow + self.radioSep*7, anchor=self.radioAn, window=self.r_mass2h)
        self.canvas.create_window(self.mass2Col, self.radioStartRow + self.radioSep*8, anchor=self.radioAn, window=self.r_mass2i)
        self.canvas.create_window(self.mass2Col, self.radioStartRow + self.radioSep*9, anchor=self.radioAn, window=self.r_mass2j)
        self.canvas.create_window(self.mass2Col, self.radioStartRow + self.radioSep*10, anchor=self.radioAn, window=self.r_mass2k)
        self.canvas.create_window(self.mass2Col, self.radioStartRow + self.radioSep*11, anchor=self.radioAn, window=self.r_mass2l)
        self.canvas.create_window(self.mass2Col, self.radioStartRow + self.radioSep*12, anchor=self.radioAn, window=self.r_mass2m)
        self.canvas.create_window(self.mass2Col, self.radioStartRow + self.radioSep*13, anchor=self.radioAn, window=self.r_mass2n)

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

    #Submit button function
    def submit(self,m1,m1e,m2,m2e,r1,r1e,r2,r2e,d):
        bad = False
        # print(f"mass1 {m1}^{m1e}, mass2 {m2}^{m2e}, r {r}^{re}, d {d}")
        if self.e_mass1.get()=='':
            self.e_mass1.config(bg='red')
            bad = True
        if self.e_mass1e.get()=='':
            self.e_mass1e.config(bg='red')
            bad = True
        if self.e_mass2.get()=='':
            self.e_mass2.config(bg='red')
            bad = True
        if self.e_height.get()=='':
            self.e_height.config(bg='red')
            bad = True
        if bad == False:
            self.e_mass1.config(background='white')
            self.e_mass1e.config(background='white')
            self.e_mass2.config(background='white')
            self.e_height.config(background='white')
            m1 = float(m1)
            m1e = int(m1e)
            m2 = float(m2)
            m2e = int(m2e)
            r1 = float(r1)
            r1e = int(r1e)
            r2 = float(r2)
            r2e = int(r2e)
            m1*=(10**m1e)
            m2*=(10**m2e)
            r1*=(10**r1e)
            r2*=(10**r2e)
            result = self.attracting(m1,float(m2),r1,r2,float(d),1000)
            self.canvas.itemconfig(self.l_result,text=str(round(result[0],3))+" "+result[1])
            self.canvas.itemconfig(self.l_acc,text="Acceleration at center of mass 2: "+str(round(result[2],3)))

    def rCommand(self,var,field):
        valu = self.exSplit(float(self.OBJLIST[var][1]))
        rad = self.exSplit(float(self.OBJLIST[var][2]))
        if field == 1:
            self.e_mass1.configure(state=["normal"])
            self.e_mass1e.configure(state=["normal"])
            self.e_mass1.delete(0,END)
            self.e_mass1e.delete(0,END)
            self.e_mass1.insert(0,valu[0])
            self.e_mass1e.insert(0,valu[1])
            if var != 13:
                self.e_mass1.configure(state=["readonly"])
                self.e_mass1e.configure(state=["readonly"])
        elif field == 2:
            self.e_mass2.configure(state=["normal"])
            self.e_mass2e.configure(state=["normal"])
            self.e_mass2.delete(0,END)
            self.e_mass2e.delete(0,END)
            self.e_mass2.insert(0,valu[0])
            self.e_mass2e.insert(0,valu[1])
            if var != 13:
                self.e_mass2.configure(state=["readonly"])
                self.e_mass2e.configure(state=["readonly"])

    #Convert exponential notation to value and exponent
    def exSplit(self,num):
        # print("num= ", num)
        count = 0
        if num <= 0:
            return [0,0]
        elif num > 1:
            while num > 10:
                num/=10
                count+=1

        else:
            while num < 1:
                # print(num)
                num*=10
                count-=1
        return [num, count]

    def attracting(self,m1,m2,r1,r2,d,frames):
        segment = d/frames
        #print("segment=", segment)
        r = d + r1 + r2
        traveled = 0
        v1  = v2 = 0
        total_t = 0
        count = 0
        a2i = (G*m1)/(r**2)
        if m1 < m2:
            temp = m1
            m1 = m2
            m2 = temp
        while traveled < d:
            count+=1
            F = (G*m1*m2)/(r**2) # N (force)
            # print("F= ", F)
            # a1 = F/m1
            a1 = (G*m2)/(r**2)
            # print(f"a1{count}= ", a1)
            # a2 = F/m2
            a2 = (G*m1)/(r**2)
            # print(f"a2{count}= ", a2)
            t = (-v2 + math.sqrt((v2**2)+(2*a2*segment)))/a2 #time for small obj to move one segment
            # print(f"t{count}= ", t)
            trav1 = ((t**2)*a1*.5) + v1*t # distance larger object travels in time t
            # print("trav1= ", trav1)
            traveled+= (segment + trav1)
            # print(f"traveled{count}= ", traveled)
            r-=(segment+trav1)
            v1 = trav1/t
            v2 = segment/t
            total_t+=t

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

        return [total_t, unit, a2i]



if __name__ == "__main__":
    grav = Gravity()
    grav.build()

    # Filling the fields with defaults
    grav.r_mass1b.invoke()
    grav.r_mass2b.invoke()

    # Disabling the fields
    grav.e_mass1.configure(state=['readonly'])
    grav.e_mass1e.configure(state=['readonly'])

    # Running the main loop
    grav.mainloop()
