from tkinter import *
import tkinter.messagebox
q = [	
    "Which is the volatile memory in a computer system?",
    "Which one should  be the first high level programming language?",
    "How many states in India have Legislative Council?",
    "The first person to receive e-passport in India was issued to?",
    "Which is the Capital of india",
    "which is the Capital of Karnataka",
    "which is the Capital of Tamilnadu state",
    "which is the Capital of Madhya pradesh",
    ]
options = [
     ["HardDisk","RAM","ROM","Optical Drive"],
     ["C","COBOL","FORTRAN","C++"],
     ["7","12","15","21"],
     ["Somnath Chatterje","Pranab Mukherjee","Pratibha Patil","Narendra Modi"],  
     ["Delhi","Mumbai","Kolkata","Chennai"],
     ["Delhi","Mumbai","Chennai","Bengalure"],
     ["Bengalure","Dehli","Hyderabad","Chennai"],
     ["Lucknow","Bhopal","Goa","Manipur"],	
     
]
a = [2,3,1,3,1,4,4,2]




class Quiz:
    def __init__(self,master):
        self.opt_selected = IntVar()
        self.qn = 0
        self.correct = 0
        self.ques = self.create_q(master,self.qn)
        self.opts = self.create_options(master, 4)
        self.display_q(self.qn)
        self.status_bar1 = self.create_status_bar1(master)
        self.status_bar = self.create_status_bar(master)
        self.create_nav(master)

    
    def create_status_bar(self,master):
        status_bar = Label(master,text="choose your answer....!!!",bd=1,relief=SUNKEN,anchor=W)
        status_bar.pack(side=BOTTOM,fill=X)
        return status_bar

    def create_status_bar1(self,master):
        status_bar1 = Label(master,text="click on option..!!",bd=1,relief=SUNKEN,anchor=W)
        status_bar1.pack(side=BOTTOM,fill=X)
        return status_bar1
    def create_nav(self,master):    
        self.button = Button(master, text="Back", command=self.back_btn)
        self.button.pack(side=BOTTOM)
        self.button = Button(master, text="Next", command=self.next_btn)
        self.button.pack(side=BOTTOM)
    def create_q(self,master,qn):
        w = Label(master, text=q[qn])
        w.pack(side=TOP)
        return w
    def create_options(self,master,n):
        b_val = 0
        b = []
        while b_val < n:
            btn = Radiobutton(master,text="foo",variable=self.opt_selected,value=b_val+1)
            b.append(btn)
            btn.pack(side=TOP, anchor="w")
            b_val = b_val + 1
        return b
    def display_q(self,qn):
        b_val = 0	
        self.opt_selected.set(0)
        self.ques['text'] = q[qn]
        for op in options[qn]:
            self.opts[b_val]['text'] = op
            b_val = b_val + 1
    def check_q(self,qn):
        if self.opt_selected.get() == a[qn]:
              return True
        return False
    def print_results(self):
        result = "Score:" + str(self.correct) + "/" + str(len(q))
        tkinter.messagebox.showinfo("Final Result", result)
        print("Score",self.correct,"/",len(q))
    def back_btn(self):
        print("go back")
        self.qn =self.qn - 1
        self.display_q(self.qn)
    def next_btn(self):
        if self.check_q(self.qn):
            self.status_bar['text'] = "Correct"
            self.correct += 1
            self.status_bar1['text'] = "Score:",self.correct 
        else:
            self.status_bar['text'] = "Wrong"
            self.status_bar1['text']= "Score:",self.correct
        self.qn =self.qn + 1
        if self.qn >= len(q):
            self.print_results()
        else:
            self.display_q(self.qn)

root = Tk()
root.title("Multiple choose question")
root.geometry("500x300")
app = Quiz(root)
root.mainloop()











