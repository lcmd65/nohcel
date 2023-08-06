import tkinter as tk
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import matplotlib.pyplot as plt

LARGE_FONT = ("Verdana", 12)

class PointSelector():
    """
    classdocs
    """
    def __init__(self, axarr, ax2select, fig, canv, NumRanges, xdat, ydat):
        """
        Constructor
        """
        self.axarr = axarr
        self.ax2select = ax2select
        self.fig = fig
        self.canv = canv
        self.NumRanges = NumRanges
        self.Ranges = []
        self.xdat = xdat
        self.ydat = ydat
        self.Nselected = 0
        self.SelectedL = False
        self.SelectedR = False
        self.LeftArr = []
        self.RightArr = []
        self.cid = canv.mpl_connect('button_press_event', self.onclick)
        print('Done With ALL!')


    def PlotRange(self,rng):
        x = self.xdat[range(rng[0],rng[1]+1)]
        y = self.ydat[range(rng[0],rng[1]+1)]
        self.axarr[self.ax2select].plot(x,y,color='r')

        self.canv.draw()

    def PlotPoint(self,x,y):
        self.axarr[self.ax2select].scatter(x,y,color='r')
        self.canv.draw()

    def onclick(self, event):
        print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' % (event.button, event.x, event.y, event.xdata, event.ydata))

        if event.inaxes == self.axarr[self.ax2select]:

            xval = np.argmin(np.abs(event.xdata-self.xdat))
            if self.SelectedL:
                self.RightArr.append(xval)
                self.SelectedR = True
                self.PlotPoint(self.xdat[xval], self.ydat[xval])
            else:
                self.LeftArr.append(xval)
                self.SelectedL = True
                self.PlotPoint(self.xdat[xval], self.ydat[xval])

            if self.SelectedL and self.SelectedR:
                self.SelectedL = False
                self.SelectedR = False
                self.Nselected += 1
                self.PlotRange([self.LeftArr[-1], self.RightArr[-1]])
                if self.Nselected == self.NumRanges:
                    for i in range(len(self.LeftArr)):
                        self.Ranges.append([self.LeftArr[i], self.RightArr[i]])
                    self.canv.mpl_disconnect(self.cid)
                    print('Done With Selection')

        else:
            print('Outside Window')

class Driver(tk.Tk):
    """
    classdocs
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor
        """
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both",expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = dict()
        F = StartPage
        frame = F(container, self)
        self.frames[F] = frame
        frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(StartPage)
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    """
    classdocs
    """
    def __init__(self, parent, controller):
        """
        Constructor
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        quitButton = tk.Button(self, text="Quit",command=self._quit)
        quitButton.pack(side="bottom")

        NewDataButton = tk.Button(self, text="Get New Data",command=self.GetNewData)
        NewDataButton.pack(side="top")

        menu = tk.Menu(parent)
        controller.config(menu=menu)

        submenuFile = tk.Menu(menu)
        menu.add_cascade(label="File",menu=submenuFile)
        submenuFile.add_command(label='Open File', command=self.onOpen)
        submenuFile.add_command(label='Load Configuration File', command=self.onOpen)
        submenuFile.add_separator()

        submenuFile.add_command(label='Exit', command=self._quit)

        submenuContinuum = tk.Menu(menu)
        menu.add_cascade(label="Continuum",menu=submenuContinuum)

        canvas_width = 100
        canvas_height = 100
        canv = tk.Canvas(self,width=canvas_width,height=canvas_height)
        canv.pack()

        self.x = np.linspace(0.0,4.0*np.pi,100)
        self.fig = plt.figure(figsize=(6,6))
        self.axarr = []
        self.axarr.append(plt.subplot(211))
        self.axarr.append(plt.subplot(212))
        self.canv = FigureCanvasTkAgg(self.fig,master=self)
        self.canv.get_tk_widget().pack()
        self.canv._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand=1)
        self.GetNewData()

        self.txt=tk.Text(self)
        submenuContinuum.add_command(label='Select Continuum', command=self.registerSelector)
        submenuContinuum.add_command(label='Remove Continuum', command=donothing)

    def registerSelector(self):
        self.selector = PointSelector(self.axarr, 0, self.fig, self.canv, 2, self.x, self.y)

    def GetNewData(self):
        rnum = (np.random.rand(1))
        print(rnum)
        self.y = np.sin(self.x)*(np.random.rand(1)*4.0)*(self.x)**rnum
        self.dy = np.gradient(self.y, self.x[1]-self.x[0])
        self.DrawData()
    def DrawData(self):
        self.axarr[0].clear()
        self.axarr[1].clear()
        self.axarr[0].plot(self.x,self.y)
        self.axarr[1].plot(self.x,self.dy)
        self.canv.draw()

    def onOpen(self):
        ftypes = [('Python files', '*.py'), ('All files', '*')]
        dlg = tk.filedialog.Open(self, filetypes=ftypes)
        fl = dlg.show()

        if fl != '':
            text = self.readFile(fl)
            self.txt.insert('end', text)

    def readFile(self, filename):
        f = open(filename, "r")
        text = f.read()
        return text

    def _quit(self):
        self.controller.quit()
        self.controller.destroy()

def donothing():
    print("nothing")

if __name__ == '__main__':
    app = Driver()
    app.mainloop()