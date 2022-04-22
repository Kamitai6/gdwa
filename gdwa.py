from tkinter import tk
import json

class HelloWorldApp(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master, width=240, height=240)

        self.master.title('Hello World')
       
        self.label = tk.Label(self, text='Hello World')
        self.label.place(x=20, y=100, width=200, height=40)        

def main():
    file = open("dwa_param.json", 'r')
    json_dict = json.load(file)
    params = json.loads(json_dict)
    
    app= HelloWorldApp()
    app.pack()
    app.mainloop()

if __name__ == '__main__':
    main()