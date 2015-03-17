from Tkinter import Tk, Frame, BOTH
import numgame

class GameBoard(Frame):
    game = numgame.NumGame()

    def __init__(self, parent):
        Frame.__init__(self, parent, background='white')
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Number Guessing Game")
        self.pack(fill=BOTH, expand=1)

def main():
        root = Tk()
        root.geometry("350x250+300+300")
        app = GameBoard(root)
        root.mainloop()

if __name__ =='__main__':
    main()
