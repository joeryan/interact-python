#! /usr/bin/env python
import Tkinter as tk

class PongGame(tk.Frame):
    FLD_H = 650
    FLD_W = 1150
    PAD_H = 80
    PAD_W = 20

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text = 'Quit',
                                    command=self.quit)
        self.fld = tk.Canvas(bg='black', height=self.FLD_H, 
                                  width = self.FLD_W)
        self.fld.grid(padx=25, pady=15)
        self.quitButton.grid()
        l_gut = self.fld.create_line(self.PAD_W, 0, self.PAD_W, self.FLD_H, 
                                     width = 2, fill  = 'white')
        r_gut = self.fld.create_line((self.FLD_W - self.PAD_W), 0,
                                     (self.FLD_W - self.PAD_W), 
                                     self.FLD_H, width = 2, fill  = 'white')
        c_line = self.fld.create_line((self.FLD_W/2), 0,
                                      (self.FLD_W/2), self.FLD_H, 
                                      width = 2, fill  = 'white')
        l_pad = self.fld.create_rectangle(0, self.FLD_H/2+self.PAD_H/2, 
                                          self.PAD_W, self.FLD_H/2-self.PAD_H/2,
                                          outline="white", fill="white",width = 2)
        r_pad = self.fld.create_rectangle(self.FLD_W, self.FLD_H/2+self.PAD_H/2, 
                                          self.FLD_W - self.PAD_W, self.FLD_H/2 -
                                          self.PAD_H/2, outline ="white", 
                                          fill="white", width = 2)
def main():
    pong = PongGame()
    pong.master.geometry("1240x820+300+300")
    pong.master.title('Game of Pong')
    pong.mainloop()

if __name__ == '__main__':
    main()
#online submission url - http://www.codeskulptor.org/#user39_wJkf7WYddA_17.py
