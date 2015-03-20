#! /usr/bin/env python
import Tkinter as tk

class PongGame(tk.Frame):
    FIELD_HEIGHT = 650
    FIELD_WIDTH = 1150
    PAD_HEIGHT = 80
    PAD_WIDTH = 20

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text = 'Quit',
                                    command=self.quit)
        self.playArea = tk.Canvas(bg='black', height=self.FIELD_HEIGHT, 
                                  width = self.FIELD_WIDTH)
        self.playArea.grid(padx=25, pady=15)
        self.quitButton.grid()

def main():
    pong = PongGame()
    pong.master.geometry("1240x820+300+300")
    pong.master.title('Game of Pong')
    pong.mainloop()

if __name__ == '__main__':
    main()
#online submission url - http://www.codeskulptor.org/#user39_wJkf7WYddA_17.py
