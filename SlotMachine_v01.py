'''
    Name: Evan Pugh
    Date: 2013, June 6th
    Version: 01
        - window with background
        - not resizable
        - buttons added: bet 1, 10, 100, reset, quit, spin (no functionality)
        - external documentation included
        - functionality provided by teacher imported
'''
from Tkinter import Tk
from Tkinter import Button
from Tkinter import PhotoImage
from Tkinter import Label

class window():
    
    windowDimensions = "770x540"
    root = Tk()
    # add window title
    root.title("Slot Machine")
    
    # set the size of the window
    root.geometry(windowDimensions)
    # make it so the user cannot resize
    root.resizable(0, 0)
    
    # assign the background image to a variable
    background_image = PhotoImage(file="slotmachine.gif")
    
    # create a panel(like a frame) and add the background to it
    panel1 = Label(root, image=background_image)
    panel2 = Label(root)
   
class buttons():
    
    bet1 = Button(window.panel1, text="Bet 1", command="print")
    bet1.place(x="220", y="420")
        
    bet10 = Button(window.root, text="Bet 10", command="print")
    bet10.place(x="340", y="420")
    
    bet100 = Button(window.root, text="Bet 100")
    bet100.place(x="460", y="420")
    
    spin = Button(window.root, text="Spin")
    spin.place(x="580", y="420")
    
    quit = Button(window.root, text="Quit")
    quit.place(x="60", y="470")
    
    
    def tester(self):
        print "test"

def main():
    
    #mysc
    print "start"
    
    
    # pack the panel
    window.panel1.pack(side="top", fill="both", expand="yes")
    window.panel2.pack(side="top", fill="both", expand="yes")
    #execute
    window.root.mainloop()

    
if __name__ == "__main__": main()