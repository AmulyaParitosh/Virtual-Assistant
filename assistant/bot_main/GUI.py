import threading
import tkinter
from tkinter import scrolledtext
import json
from PIL import ImageTk,Image
import subprocess as s
import requests



class GUI:

    def __init__(self):
        
        self.kill_code = None

        information = json.loads(open('assistant/bot_main/assistant_info.json').read())

        for info in information["assistant"]:
            self.name = info["name"]
            self.ascii_art = info["ascii"]

        self.gui_done = False

        self.bg = Image.open("assistant/images/background.png")
        self.conn_img = Image.open("assistant/images/connected.png")
        self.disconn_img = Image.open("assistant/images/disconnected.png")

        self.conn_state = False

        gui_thread = threading.Thread(target=self.gui_loop)
        connection_thread = threading.Thread(target=self.check_connection)
        connection_thread.setDaemon(True)
        self.check_conn_event = threading.Event()
        
        gui_thread.start()
        connection_thread.start()

       
    def gui_loop(self):
        self.win = tkinter.Tk()
        self.win.title(f"Assistant {self.name}")
        self.win.resizable(0,0)
        self.bgimage = ImageTk.PhotoImage(self.bg)
        self.conn_img = ImageTk.PhotoImage(self.conn_img)
        self.disconn_img = ImageTk.PhotoImage(self.disconn_img)
        self.win.configure(bg="grey10", relief="solid")

        self.background = tkinter.Label(self.win, image = self.bgimage) 
        self.background.place(relx=0.5, rely=0.5, anchor="center")

        self.title = tkinter.Label(self.win, text=f"{self.name}", bg="grey10", fg="white")
        self.title.config(font=("Freestyle Script", 40, 'bold', 'underline'))
        self.title.pack(padx=20, pady=0)

        self.connection = tkinter.Label(self.win, image=self.disconn_img)
        self.connection.place(x=365,y=8)

        self.display_area = scrolledtext.ScrolledText(self.win, width=52, height=35, bg="grey20", fg="white", bd="4", relief="solid")
        self.display_area.config(font=("Arial", 10))
        self.display_area.pack(padx=20, pady=0)
        
        for line in self.ascii_art:
            self.display_area.insert('end', line)
        
        self.display_area.config(state='disabled')

        self.footer = tkinter.Label(self.win, text="speak to give command...", bg="grey10", fg="white")
        self.footer.place(x=25,y=645)
        self.footer.config(font=("Arial", 12, 'italic'))

        self.clear_button = tkinter.Button(self.win, text="Clear Screen", command=self.clear, relief="solid", bg="grey20", fg="white")
        self.clear_button.config(font=("Arial", 10))
        self.clear_button.pack(side='right', padx=20, pady=10)

        self.gui_done = True
        self.check_conn_event.set()

        self.win.protocol("WM_DELETE_WINDOW", self.stop)

        self.win.mainloop()


    def clear(self):
        self.display_area.config(state='normal')
        self.display_area.delete('1.0', 'end')
        self.display_area.config(state='disabled')

                  
    def stop(self):
        if self.kill_code != None:
            s.Popen(f'taskkill /F /PID {self.kill_code}', shell=True)
        self.win.destroy()
        exit(0)

    def check_connection(self):
        self.check_conn_event.wait()
        while True:
            try:
                requests.get("https://www.google.com")
                self.connection.configure(image=self.conn_img)

            except Exception:
                self.connection.configure(image=self.disconn_img)

    def display(self, message):

        if type(message) == int:
            
            self.kill_code = message
            message = "Ready to GO!\n"

        elif "->>" not in message and "listening..." not in message:
            message = f"{self.name} : {message}\n"

        
        self.display_area.config(state='normal')
        self.display_area.insert('end', message)
        self.display_area.yview('end')
        self.display_area.config(state='disabled')

gui = GUI()