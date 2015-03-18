#! /usr/bin/env python
import Tkinter as tk

class PongGame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        

    def createWidgets(self):
        self.quitButton = tk.Button(self, text = 'Quit',
                                    command=self.quit)
        self.playArea = tk.Canvas(bg='white', height=850, width = 1150)
        self.playArea.grid(padx=25, pady=15)
        self.quitButton.grid()

pong = PongGame()
pong.master.geometry("1200x900+300+300")
pong.master.title('Game of Pong')
pong.mainloop()
