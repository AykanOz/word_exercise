from asyncio.windows_events import NULL
from multiprocessing import Value
from threading import local
from tkinter import *
import random
from tkinter.messagebox import QUESTION
from matplotlib.pyplot import text
from data_ import word_easy,question_easy,question_hard,word_hard,question_middle,word_middle
from numpy import var


def easy_():

    
    root1.destroy()
    global word
    word = random.choice(question_easy)
    options =[]
    options.append(word_easy[word])
    x = 3
    while x>0:
        option=random.choice(question_easy)
        if word_easy[option] not in options:
            options.append(word_easy[option])
            x -=1
        else:
            continue    
    
    random.shuffle(options)
    
    def answer_btn1_():
        if answer_btn1["text"] == word_easy[word]:
            answer_btn1["bg"] = "green"
        else:
            
            if answer_btn2["text"] == word_easy[word]:
                answer_btn1["bg"] = "red"
                answer_btn2["bg"] = "green"
            elif answer_btn3["text"] == word_easy[word]:
                answer_btn1["bg"] = "red"
                answer_btn3["bg"] = "green"
            elif answer_btn4["text"] == word_easy[word]:
                answer_btn1["bg"] = "red"
                answer_btn4["bg"] = "green"
    def answer_btn2_():
        if answer_btn2["text"] == word_easy[word]:
            answer_btn2["bg"] = "green"
        else:
            
            if answer_btn1["text"] == word_easy[word]:
                answer_btn2["bg"] = "red"
                answer_btn1["bg"] = "green"
            elif answer_btn3["text"] == word_easy[word]:
                answer_btn2["bg"] = "red"
                answer_btn3["bg"] = "green"
            elif answer_btn4["text"] == word_easy[word]:
                answer_btn2["bg"] = "red"
                answer_btn4["bg"] = "green"
    def answer_btn3_():
        if answer_btn3["text"] == word_easy[word]:
            answer_btn3["bg"] = "green"
        else:
            
            if answer_btn1["text"] == word_easy[word]:
                answer_btn3["bg"] = "red"
                answer_btn1["bg"] = "green"
            elif answer_btn2["text"] == word_easy[word]:
                answer_btn3["bg"] = "red"
                answer_btn2["bg"] = "green"
            elif answer_btn4["text"] == word_easy[word]:
                answer_btn3["bg"] = "red"
                answer_btn4["bg"] = "green"
    def answer_btn4_():
        if answer_btn4["text"] == word_easy[word]:
            answer_btn4["bg"] = "green"
        else:
            
            if answer_btn1["text"] == word_easy[word]:
                answer_btn4["bg"] = "red"
                answer_btn1["bg"] = "green"
            elif answer_btn2["text"] == word_easy[word]:
                answer_btn4["bg"] = "red"
                answer_btn2["bg"] = "green"
            elif answer_btn3["text"] == word_easy[word]:
                answer_btn4["bg"] = "red"
                answer_btn3["bg"] = "green"
    def next_():
        global word
        
        word = random.choice(question_easy)
        options =[]
        options.append(word_easy[word])
        x = 3
        while x>0:
            option=random.choice(question_easy)
            if word_easy[option] not in options:
                options.append(word_easy[option])
                x -=1
            else:
                continue    
        
        random.shuffle(options)
        
        question_lbl["text"] = (f"What is the Turkish meaning of '{word}'?")
        answer_btn1["text"] = options[0]
        answer_btn2["text"] = options[1]
        answer_btn3["text"] = options[2]
        answer_btn4["text"] = options[3]
        answer_btn1["bg"] = "light grey"
        answer_btn2["bg"] = "light grey"
        answer_btn3["bg"] = "light grey"
        answer_btn4["bg"] = "light grey"

    root = Tk()
    root.geometry("500x350+300+300")
    root.title("English Exercise")
    question_lbl = Label(root,text=f"What is the Turkish meaning of '{word}'?",font=("Verdana",12))
    question_lbl.pack(pady=35)
    answer_btn1= Button(root,height=3,text=options[0],command=answer_btn1_,width=20,font=("Verdana",12),bg="light grey")
    answer_btn1.place(relx=0.08,rely=0.22)
    answer_btn2= Button(root,height=3,text=options[1],command=answer_btn2_,width=20,font=("Verdana",12),bg="light grey")
    answer_btn2.place(relx=0.48,rely=0.22)
    answer_btn3= Button(root,height=3,text=options[2],command=answer_btn3_,width=20,font=("Verdana",12),bg="light grey")
    answer_btn3.place(relx=0.08,rely=0.48)
    answer_btn4= Button(root,height=3,text=options[3],command=answer_btn4_,width=20,font=("Verdana",12),bg="light grey")
    answer_btn4.place(relx=0.48,rely=0.48)
    btn_next = Button(root,text="Next",height=2,width=8,command=next_,font=("Verdana",10),bg="light grey")
    btn_next.place(relx=0.40,rely=0.75)

    root.mainloop()
    

        
def middle_():
    root1.destroy()
    global word
    word = random.choice(question_middle)
    options =[]
    options.append(word_middle[word])
    x = 3
    while x>0:
        option=random.choice(question_middle)
        if word_middle[option] not in options:
            options.append(word_middle[option])
            x -=1
        else:
            continue    
    
    random.shuffle(options)
    
    def answer_btn1_():
        if answer_btn1["text"] == word_middle[word]:
            answer_btn1["bg"] = "green"
        else:
            
            if answer_btn2["text"] == word_middle[word]:
                answer_btn1["bg"] = "red"
                answer_btn2["bg"] = "green"
            elif answer_btn3["text"] == word_middle[word]:
                answer_btn1["bg"] = "red"
                answer_btn3["bg"] = "green"
            elif answer_btn4["text"] == word_middle[word]:
                answer_btn1["bg"] = "red"
                answer_btn4["bg"] = "green"
    def answer_btn2_():
        if answer_btn2["text"] == word_middle[word]:
            answer_btn2["bg"] = "green"
        else:
            
            if answer_btn1["text"] == word_middle[word]:
                answer_btn2["bg"] = "red"
                answer_btn1["bg"] = "green"
            elif answer_btn3["text"] == word_middle[word]:
                answer_btn2["bg"] = "red"
                answer_btn3["bg"] = "green"
            elif answer_btn4["text"] == word_middle[word]:
                answer_btn2["bg"] = "red"
                answer_btn4["bg"] = "green"
    def answer_btn3_():
        if answer_btn3["text"] == word_middle[word]:
            answer_btn3["bg"] = "green"
        else:
            
            if answer_btn1["text"] == word_middle[word]:
                answer_btn3["bg"] = "red"
                answer_btn1["bg"] = "green"
            elif answer_btn2["text"] == word_middle[word]:
                answer_btn3["bg"] = "red"
                answer_btn2["bg"] = "green"
            elif answer_btn4["text"] == word_middle[word]:
                answer_btn3["bg"] = "red"
                answer_btn4["bg"] = "green"
    def answer_btn4_():
        if answer_btn4["text"] == word_middle[word]:
            answer_btn4["bg"] = "green"
        else:
            
            if answer_btn1["text"] == word_middle[word]:
                answer_btn4["bg"] = "red"
                answer_btn1["bg"] = "green"
            elif answer_btn2["text"] == word_middle[word]:
                answer_btn4["bg"] = "red"
                answer_btn2["bg"] = "green"
            elif answer_btn3["text"] == word_middle[word]:
                answer_btn4["bg"] = "red"
                answer_btn3["bg"] = "green"
    def next_():
        global word
        
        word = random.choice(question_middle)
        options =[]
        options.append(word_middle[word])
        x = 3
        while x>0:
            option=random.choice(question_middle)
            if word_middle[option] not in options:
                options.append(word_middle[option])
                x -=1
            else:
                continue    
        
        random.shuffle(options)
        
        question_lbl["text"] = (f"What is the Turkish meaning of '{word}'?")
        answer_btn1["text"] = options[0]
        answer_btn2["text"] = options[1]
        answer_btn3["text"] = options[2]
        answer_btn4["text"] = options[3]
        answer_btn1["bg"] = "light grey"
        answer_btn2["bg"] = "light grey"
        answer_btn3["bg"] = "light grey"
        answer_btn4["bg"] = "light grey"

    root = Tk()
    root.geometry("500x350+300+300")
    root.title("English Exercise")
    question_lbl = Label(root,text=f"What is the Turkish meaning of '{word}'?",font=("Verdana",12))
    question_lbl.pack(pady=35)
    answer_btn1= Button(root,height=3,text=options[0],command=answer_btn1_,width=20,font=("Verdana",12),bg="light grey")
    answer_btn1.place(relx=0.08,rely=0.22)
    answer_btn2= Button(root,height=3,text=options[1],command=answer_btn2_,width=20,font=("Verdana",12),bg="light grey")
    answer_btn2.place(relx=0.48,rely=0.22)
    answer_btn3= Button(root,height=3,text=options[2],command=answer_btn3_,width=20,font=("Verdana",12),bg="light grey")
    answer_btn3.place(relx=0.08,rely=0.48)
    answer_btn4= Button(root,height=3,text=options[3],command=answer_btn4_,width=20,font=("Verdana",12),bg="light grey")
    answer_btn4.place(relx=0.48,rely=0.48)
    btn_next = Button(root,text="Next",height=2,width=8,command=next_,font=("Verdana",10),bg="light grey")
    btn_next.place(relx=0.40,rely=0.75)

    root.mainloop()
    
def hard_():
    root1.destroy()
    global word
    word = random.choice(question_hard)
    options =[]
    options.append(word_hard[word])
    x = 3
    while x>0:
        option=random.choice(question_hard)
        if word_hard[option] not in options:
            options.append(word_hard[option])
            x -=1
        else:
            continue    
    
    random.shuffle(options)
    
    def answer_btn1_():
        if answer_btn1["text"] == word_hard[word]:
            answer_btn1["bg"] = "green"
        else:
            
            if answer_btn2["text"] == word_hard[word]:
                answer_btn1["bg"] = "red"
                answer_btn2["bg"] = "green"
            elif answer_btn3["text"] == word_hard[word]:
                answer_btn1["bg"] = "red"
                answer_btn3["bg"] = "green"
            elif answer_btn4["text"] == word_hard[word]:
                answer_btn1["bg"] = "red"
                answer_btn4["bg"] = "green"
    def answer_btn2_():
        if answer_btn2["text"] == word_hard[word]:
            answer_btn2["bg"] = "green"
        else:
            
            if answer_btn1["text"] == word_hard[word]:
                answer_btn2["bg"] = "red"
                answer_btn1["bg"] = "green"
            elif answer_btn3["text"] == word_hard[word]:
                answer_btn2["bg"] = "red"
                answer_btn3["bg"] = "green"
            elif answer_btn4["text"] == word_hard[word]:
                answer_btn2["bg"] = "red"
                answer_btn4["bg"] = "green"
    def answer_btn3_():
        if answer_btn3["text"] == word_hard[word]:
            answer_btn3["bg"] = "green"
        else:
            
            if answer_btn1["text"] == word_hard[word]:
                answer_btn3["bg"] = "red"
                answer_btn1["bg"] = "green"
            elif answer_btn2["text"] == word_hard[word]:
                answer_btn3["bg"] = "red"
                answer_btn2["bg"] = "green"
            elif answer_btn4["text"] == word_hard[word]:
                answer_btn3["bg"] = "red"
                answer_btn4["bg"] = "green"
    def answer_btn4_():
        if answer_btn4["text"] == word_hard[word]:
            answer_btn4["bg"] = "green"
        else:
            
            if answer_btn1["text"] == word_hard[word]:
                answer_btn4["bg"] = "red"
                answer_btn1["bg"] = "green"
            elif answer_btn2["text"] == word_hard[word]:
                answer_btn4["bg"] = "red"
                answer_btn2["bg"] = "green"
            elif answer_btn3["text"] == word_hard[word]:
                answer_btn4["bg"] = "red"
                answer_btn3["bg"] = "green"
    def next_():
        global word
        
        word = random.choice(question_hard)
        options =[]
        options.append(word_hard[word])
        x = 3
        while x>0:
            option=random.choice(question_hard)
            if word_hard[option] not in options:
                options.append(word_hard[option])
                x -=1
            else:
                continue    
        
        random.shuffle(options)
        
        question_lbl["text"] = (f"What is the Turkish meaning of '{word}'?")
        answer_btn1["text"] = options[0]
        answer_btn2["text"] = options[1]
        answer_btn3["text"] = options[2]
        answer_btn4["text"] = options[3]
        answer_btn1["bg"] = "light grey"
        answer_btn2["bg"] = "light grey"
        answer_btn3["bg"] = "light grey"
        answer_btn4["bg"] = "light grey"

    root = Tk()
    root.geometry("500x350+300+300")
    root.title("English Exercise")
    question_lbl = Label(root,text=f"What is the Turkish meaning of '{word}'?",font=("Verdana",12))
    question_lbl.pack(pady=35)
    answer_btn1= Button(root,height=3,text=options[0],command=answer_btn1_,width=20,font=("Verdana",12),bg="light grey")
    answer_btn1.place(relx=0.08,rely=0.22)
    answer_btn2= Button(root,height=3,text=options[1],command=answer_btn2_,width=20,font=("Verdana",12),bg="light grey")
    answer_btn2.place(relx=0.48,rely=0.22)
    answer_btn3= Button(root,height=3,text=options[2],command=answer_btn3_,width=20,font=("Verdana",12),bg="light grey")
    answer_btn3.place(relx=0.08,rely=0.48)
    answer_btn4= Button(root,height=3,text=options[3],command=answer_btn4_,width=20,font=("Verdana",12),bg="light grey")
    answer_btn4.place(relx=0.48,rely=0.48)
    btn_next = Button(root,text="Next",height=2,width=8,command=next_,font=("Verdana",10),bg="light grey")
    btn_next.place(relx=0.40,rely=0.75)

    root.mainloop()
    
    
root1 = Tk()
root1.geometry("500x300+300+300")
root1.title("English Exercise")
lbl = Label(root1,text="Hangi seviye kelimelerle çalışmak istiyorsunuz?",font=("Verdana",12))
lbl.place(relx=0.1,rely=0.2)

btn1 = Button(root1,text="Basit",command=easy_,font=("Verdana",16))
btn1.place(relx=0.2,rely=0.5)
btn2 = Button(root1,text="Orta",command=middle_,font=("Verdana",16))
btn2.place(relx=0.4,rely=0.5)
btn3 = Button(root1,text="İleri",command=hard_,font=("Verdana",16))
btn3.place(relx=0.6,rely=0.5)


root1.mainloop()









