import app.view.var
import app.environment
import tksheet
import wave
import os
import matplotlib
import matplotlib.pyplot as plt 
import librosa
import librosa.display
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
from tkinter import *
from tkinter.ttk import Style, Button
from tkinter import (
    filedialog,
    ttk,
    messagebox)
from app.func.func import sequence
from functools import partial
from app.model.conversation import Audio


## UI of Laser python CE P3
class Home(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.nodes = dict()
        self.datasource_path = None
        self.radio_value = IntVar()
        self.initUI()

    def insert_node(self, parent, text, abspath):
        node = self.tree.insert(parent, 'end', text=text, open=True)
        if os.path.isdir(abspath):
            self.nodes[node] = abspath
            self.tree.insert(node, 'end')

    def open_node(self, event):
        node = self.tree.focus()
        abspath = self.nodes.pop(node, None)
        if abspath:
            self.tree.delete(self.tree.get_children(node))
            for p in os.listdir(abspath):
                self.insert_node(node, p, os.path.join(abspath, p))
                
    def processDirectory(self, parent, path):
        for p in os.listdir(path):
            abspath = os.path.join(path, p)
            isdir = os.path.isdir(abspath)
            oid = self.tree.insert(parent, 'end', text=p, open = False)
            if isdir:
                self.processDirectory(oid, abspath)
    
    def eventButtonClickChangeDataSource(self):
        """
        Button click in data source tree
        """
        self.datasource_path = filedialog.askdirectory()
        
        
    def eventButtonClickPushData(self, tree):
        """ 
        Click to exit to login
        """
        tree['selectmode'] = "browse"
    
    def eventButtonClickExit(self):
        """ 
        Click to Exit 
        """
        try:
            from app.view.view import loginView
            app.tkinter.environment.root_main.destroy()
            loginView()
        except Exception as e:
            messagebox.showerror(title= "Error", message = e)
        
    def eventButtonClickEdit(self):
        """ 
        Click to Edit software environment
        """
        try:
            from app.view.view import editView
            editView()
        except Exception as e:
            messagebox.showerror(title= "Error", message = e)
        return
    
    def eventButtonClickHelp(self):
        try:
            from app.view.view import helpView
            helpView()
        except Exception as e:
            messagebox.showerror(title= "Error", message = e)
        
    def eventButtonClickProcessingLabel(self):
        """ 
        Main function of this tool 
        """
        
        return
        
    def eventButtonClickStartFunction(self):
        """ 
        Click to Start labeling
        """
        return
        
    def eventButtonClickEndFunction(self):
        """
        Click to end labeling
        """
        
        return
        
    def audioPlot(self, audio_path):
        obj = wave.open(audio_path, 'rb')
        sample_freq = obj.getframerate()
        n_samples = obj.getnframes()
        signal_wave = obj.readframes(-1)
        duration = n_samples/sample_freq
        signal_array = np.frombuffer(signal_wave, dtype=np.int16)
        time = np.linspace(0, duration, num = n_samples)
        fig = plt.figure(figsize=(4, 1.5))
        plt.rc('font', size = 2)  # controls default text sizes
        plt.rc('axes', titlesize = 2)     # fontsize of the axes title
        plt.rc('axes', labelsize= 2)    # fontsize of the x and y labels
        plt.rc('xtick', labelsize = 2)    # fontsize of the tick labels
        plt.rc('ytick', labelsize = 2)    # fontsize of the tick labels
        plt.rc('legend', fontsize = 2)    # legend fontsize
        plt.rc('figure', titlesize = 2) 
        plt.rcParams["font.size"] = "2"
        plt.xlabel('Time (seconds)')
        plt.ylabel('Amplitude')
        plt.tight_layout()
        plt.axvline(x= 0, color='r', linestyle='--')
        plt.axvline(x= 30, color='r', linestyle='--')
        plt.tick_params(direction='in')
        plt.plot(time, signal_array, color='black')
        
        if any(duration > t for t in time):
            plt.xlim(0, duration)
        return fig
        
    def eventProcessingAudio(self, audio, frame):
        """
        Processing Canvas Audio Visualize (Frequency)
        """
        fig = self.audioPlot(audio)
        canvas = FigureCanvasTkAgg(fig, frame)
        return
        
        
    def initUI(self):
        self.parent.title("VinBigdata LLM")
        self.pack(fill=BOTH, expand = True, side = BOTTOM)
        
        self.label_root = Label(self.parent, i= app.view.var.background_view, bg = None)
        self.label_root.pack(fill = BOTH, side = TOP)
        
        self.label_privacy = Label(self, text = "VinBigdata Privacy @2023")
        self.label_privacy.pack(fill = X, side = LEFT, padx = 10)
        
        self.logo_menu = Label(self, i = app.view.var.logo_view)
        self.logo_menu.pack(side = RIGHT, padx = 10)  
        
        self.home_menu = Menu(self.parent)
        
        """
        File menu
        """
        file_menu = Menu(self.home_menu)
        file_menu.add_command(label="New", command = None)
        file_menu.add_command(label="Open", command = None)
        file_menu.add_separator()
        file_menu.add_command(label= "Exit", command = partial(self.eventButtonClickExit))
        
        """ 
        Edit menu 
        """
        edit_menu = Menu(self.home_menu)
        edit_menu.add_command(label="Edit environment", command = partial(self.eventButtonClickEdit))
        
        """ 
        Help menu 
        """
        help_menu = Menu(self.home_menu)
        help_menu.add_command(label = "Help", command = partial(self.eventButtonClickHelp))
        
        for index, label_text, commands in zip(range(1, 4), ["File", "Edit", "Help"], [file_menu, edit_menu, help_menu]):
            self.home_menu.add_cascade(label= label_text, menu = commands)
        
        # Notebook include tab home, laser P3A to C
        self.notebook_control = ttk.Notebook(self.label_root)
        self.notebook_control.pack(expand= True, fill=BOTH, padx=10, pady= 0)
        self.noteStyle = ttk.Style()
        self.noteStyle.configure('TNotebook', tabposition='wn')
        self.noteStyle.theme_use('default')
        self.noteStyle.configure("TNotebook", background= "#001c54", borderwidth = 0)
        self.noteStyle.configure("TNotebook.Tab", background = "#001c54", foreground = "#ececec", borderwidth = 0)
        self.noteStyle.map("TNotebook", background= [("selected", "#ececec")] )
        self.noteStyle.map("TNotebook.Tab", foreground = [("selected", "black")])
        
        buttonStyle = Style()
        buttonStyle.configure('W.TButton', background = "#ececec", foreground = 'black')
        
        # init tab control 
        self.tab_controls = [None for _ in range(2)]
        self.body_controls = [None for _ in range(2)]
        self.button_controls = [None for _ in range(2)]
        self.text_controls = [None for _ in range(2)]
        self.sheet_controls = [None for _ in range(2)]
        
        for index, label_text in zip(range(2), ['           Audio Labeling          ', '      Speech to Text      ']):
            """ 
            Speech to Text tab
            """
            self.tab_controls[index] = Frame(self.notebook_control, bg=None)
            self.tab_controls[index].pack(side= LEFT, padx=0, pady=5)
            self.notebook_control.add(self.tab_controls[index], text = label_text)
            if index != 0: # except home tab
                self.body_controls[index] = [None for _ in range(3)]
                self.button_controls[index] =[None for _ in range(3)]
                for se_index in range(3):
                    self.body_controls[index][se_index] = Frame(self.tab_controls[index])
                    self.body_controls[index][se_index].pack(fill =X)
                
                # sheet view of each laser tab
                self.sheet_controls[index] = tksheet.Sheet(self.body_controls[index][2], data = [[]], height = 800, width = 1500)
                self.sheet_controls[index].pack(fill=BOTH, pady=10, padx=5, expand=True)
                self.sheet_controls[index].grid(row =20, column = 20, sticky="nswe")
                self.sheet_controls[index].enable_bindings()
                
                # text information view of each laser tab
                self.text_controls[index] =  Text(self.body_controls[index][1], bg ="#fcfcfc", height= 2)
                self.text_controls[index].pack(fill=BOTH, pady=0, padx=5, expand=True)
                
                # get type of machine data connect: A, B, C
                commands = [
                    partial(self.eventButtonClickProcessingLabel),
                    partial(self.eventButtonClickStartFunction),
                    partial(self.eventButtonClickEndFunction),
                ]
                for se_index, button_text, command_ in zip(range(3), ["Import Audio", "Start", "End"], commands):
                    self.button_controls[index][se_index] = Button(self.body_controls[index][0], text= button_text, width= 15, style = 'W.TButton', command = command_)
                    self.button_controls[index][se_index].pack(side=LEFT, padx=5, pady=5)
            
            elif index == 0:
                """ 
                UI 2 monitor: tree view and processing
                """
                self.body_controls[index] = [None for _ in range(3)]
                """ 
                Tree view for open and browse data
                """
                self.body_controls[index][0] = Frame(self.tab_controls[index])
                self.body_controls[index][0].pack(fill= Y, padx = 0 ,pady = 5, side = LEFT)
                """ 
                Tree view for open and browse segment
                """
                self.body_controls[index][2] = Frame(self.tab_controls[index])
                self.body_controls[index][2].pack(fill= Y, padx = 0 ,pady = 5, side = RIGHT)
                """
                View for processing data 
                """
                self.body_controls[index][1] = Frame(self.tab_controls[index])
                self.body_controls[index][1].pack(fill= BOTH, padx = 0 ,pady = 5, side = TOP)
                
                
                self.body_control_processing = [None for _ in range(3)]
                for second_index in range(3):
                    self.body_control_processing[second_index] = Frame(self.body_controls[index][1])
                    self.body_control_processing[second_index].pack(fill= BOTH, padx = 0 ,pady = 5)
                    
                self.tree = ttk.Treeview(self.body_controls[index][0])
                ysb = ttk.Scrollbar(self.body_controls[index][0], orient='vertical', command=self.tree.yview)
                xsb = ttk.Scrollbar(self.body_controls[index][0], orient='horizontal', command=self.tree.xview)
                self.tree.configure(yscroll = ysb.set, xscroll = xsb.set, height= 37)
                self.tree.heading('#0', text='Data Source', anchor='n', command= partial(self.eventButtonClickChangeDataSource))
                
                abspath = os.path.abspath("dataset/wav")
                root_node = self.tree.insert("", 'end', text = abspath, open = True)
                self.processDirectory(root_node, abspath)
                # self.insert_node('', abspath, abspath)
                # self.tree.bind('<<TreeviewOpen>>', self.open_node)
                xsb.pack(fill = X, side = BOTTOM)
                ysb.pack(fill = Y, side = RIGHT)
                self.tree.pack(fill = Y)
                
                self.segment_tab = ttk.Treeview(self.body_controls[index][2])
                self.segment_tab.heading('#0', text='Segment', anchor='n')
                self.segment_tab.pack(fill = Y, side = BOTTOM)
                
                self.segment_param_tab = ttk.Treeview(self.body_controls[index][2])
                self.segment_param_tab.heading('#0', text='Segment Paramater', anchor='n')
                self.segment_param_tab.configure(height= 30)
                self.segment_param_tab.pack(fill = Y, side = TOP)
                
                canvas = FigureCanvasTkAgg(self.audioPlot('dataset/wav/FPTOpenSpeechData_Set001_V0.1_000024.wav'), master = self.body_control_processing[0])
                canvas.draw()
                canvas.get_tk_widget().pack(fill= BOTH, expand = False)
                
                self.label_text = Entry(self.body_control_processing[0], text = "Nhập nhãn tại đây")
                self.label_text.pack(fill = X, pady = 15)
                
                self.radio_list = [None for _ in range(3)]
                for second_index, text_ in zip(range(3), ["Tổng đài viên", "Khách hàng", "Nhiều người nói"]):
                    self.radio_list[second_index] = Radiobutton(self.body_control_processing[1], text= text_, variable = self.radio_value, value = second_index)
                    self.radio_list[second_index].pack(fill = X, side = TOP)
                
                self.button_controls[index] = Button(self.body_controls[index][0], text="Browse",style = 'W.TButton', width= 15, command = partial(self.eventButtonClickChangeDataSource))
                self.button_controls[index].pack(side = BOTTOM, padx = 0, pady = 0, fill = BOTH)
        
                

