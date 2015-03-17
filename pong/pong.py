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
        self.quitButton.grid()

pong = PongGame()
pong.master.title('Game of Pong')
pong.mainloop()
