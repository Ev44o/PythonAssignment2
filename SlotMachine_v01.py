'''
    Name: Evan Pugh
    Date: 2013, June 6th
    Version: 02
        - quit button functioning
        - methods created for button events (not functional)
        - updated external documentation
        - tried adding background music, cant play file 
        (plays default ding sound when the program starts)
'''
from Tkinter import Tk
from Tkinter import Button
from Tkinter import PhotoImage
from Tkinter import Label
import winsound
import slotmachine_original

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
    
    # create and place all the buttons
    bet1 = Button(window.panel1, text="Bet 1")
    bet1.place(x="220", y="420")
        
    bet10 = Button(window.root, text="Bet 10")
    bet10.place(x="340", y="420")
    
    bet100 = Button(window.root, text="Bet 100")
    bet100.place(x="460", y="420")

    reset = Button(window.root, text="Reset")
    reset.place(x="1", y="470")

    spin = Button(window.root, text="Spin")
    spin.place(x="580", y="420")
    
    quit = Button(window.root, text="Quit")
    quit.place(x="60", y="470")
    

def main():
    
    # methods for initiating button commands
    def quitClick():
        window.root.destroy()
    
    def resetClick():
        print "reset"
    
    def betClick(bets):
        print bets
    
    def spinClick():
        print "spin"
    
    #configure the buttons actions by calling related method
    buttons.quit.config(command=quitClick)
    buttons.reset.config(command=resetClick)
    buttons.bet1.config(command=betClick("1"))
    buttons.bet10.config(command=betClick("10"))
    buttons.bet100.config(command=betClick("100"))
    buttons.spin.config(command=spinClick)
    
    # doesnt like the file i have, plays default sound instead (a ding)
    winsound.PlaySound("\\bkmusic.wav",winsound.SND_FILENAME)
    
    # pack the panel
    window.panel1.pack(side="top", fill="both", expand="yes")
    window.panel2.pack(side="top", fill="both", expand="yes")
    #execute
    window.root.mainloop()
    
    
    
if __name__ == "__main__": main()