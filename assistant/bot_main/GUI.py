import threading
import tkinter
from tkinter import scrolledtext
from PIL import ImageTk, Image
import subprocess as s
import requests
from configurations import theme


class GUI:

    def __init__(self):

        self.kill_code = None

        self.name = theme.name

        self.gui_done = False

        self.bg = Image.open(theme.bg_image)
        self.conn_img = Image.open(
            "assistant/configurations/images/connected.png")
        self.disconn_img = Image.open(
            "assistant/configurations/images/disconnected.png")

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
        self.win.resizable(0, 0)
        self.bgimage = ImageTk.PhotoImage(self.bg)
        self.conn_img = ImageTk.PhotoImage(self.conn_img)
        self.disconn_img = ImageTk.PhotoImage(self.disconn_img)
        self.win.configure(bg=theme.label_bg_colour, relief="solid")

        self.background = tkinter.Label(self.win, image=self.bgimage)
        self.background.place(relx=0.5, rely=0.5, anchor="center")

        self.title = tkinter.Label(
            self.win, text=f"{self.name}", bg=theme.label_bg_colour, fg=theme.fg_colour)
        self.title.config(font=(theme.title_font, 40, 'bold', 'underline'))
        self.title.pack(padx=20, pady=0)

        self.connection = tkinter.Label(self.win, image=self.disconn_img)
        self.connection.place(x=365, y=8)

        self.display_area = scrolledtext.ScrolledText(
            self.win, width=52, height=35, bg=theme.scrolltext_bg_colour, fg=theme.fg_colour, bd="4", relief="solid")
        self.display_area.config(font=("theme.base_font", 10))
        self.display_area.pack(padx=20, pady=0)
        self.display_area.config(state='disabled')

        self.footer = tkinter.Label(
            self.win, text="speak to give command...", bg=theme.label_bg_colour, fg=theme.fg_colour)
        self.footer.place(x=25, y=645)
        self.footer.config(font=("theme.base_font", 12, 'italic'))

        self.clear_button = tkinter.Button(
            self.win, text="Clear Screen", command=self.clear, relief="solid", bg=theme.button_colour, fg=theme.fg_colour)
        self.clear_button.config(font=("theme.base_font", 10))
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
            message = "_____________________Ready to GO!___________________\n\n"

        elif "->>" not in message and "listening..." not in message:
            message = f"{self.name} : {message}\n"

        self.display_area.config(state='normal')
        self.display_area.insert('end', message)
        self.display_area.yview('end')
        self.display_area.config(state='disabled')


gui = GUI()
