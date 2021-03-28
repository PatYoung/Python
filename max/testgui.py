import easygui as g
import sys
while 1:
        g.msgbox("Hi,welcome to the first page game^_^")
        msg ="What will you wish to learn here?"
        title = "game"
        choices = ["love", "code", "OOXX", "play"]
        
        choice = g.choicebox(msg, title, choices)
        # note that we convert choice to string, in case
        # the user cancelled the choice, and we got None.
        g.msgbox("your choice: " + str(choice), "result")
        msg = "Will start over?"
        title = "Choice"
        
        if g.ccbox(msg, title):     # show a Continue/Cancel dialog
                pass  # user chose Continue
        else:
                sys.exit(0)     # user chose Cancel
				
				
