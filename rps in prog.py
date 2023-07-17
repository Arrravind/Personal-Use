from tkinter import *
root = Tk()

lab=Label(root, text="Rock / Paper /Scissors : Enter - [r] [p] [s]")
lab.grid(row=0,column=1,padx=15,pady=15)

lab3=Label(root,text="Player 1 :", width=25)
lab3.grid(row=1,column=0)

lab4=Label(root, text="Player 2 :", width=25)
lab4.grid(row=1,column=2)

lab5=Label(root,text="Wins :",width=25)
lab5.grid(row=3,column=0)

lab6=Label(root,text="Wins :",width=25)
lab6.grid(row=3,column=2)

lab7=Label(root,text="Draws :",width=25)
lab7.grid(row=6,column=0)

inpu=Entry(root, width=20, fg="white")
inpu.grid(row=2,column=0)

inp=Entry(root, width=20, fg="white")
inp.grid(row=2,column=2)

def r_p_s():
    a=tkin()
    player1_wins=0
    player2_wins=0
    draws=0

    while a=="Player 1 Won":
        player1_wins+=1
        continue
    while a=="Player 2 Won":
        player2_wins+=1
        continue
    while a=="Draw":
        draws+=1
        continue

    
    draw=Entry(root)
    draw.grid(row=7,column=0)
    draw.insert(0,draws)
        
    wins1=Entry(root)
    wins1.grid(row=4,column=0)
    wins1.insert(0,player1_wins)

    wins2=Entry(root)
    wins2.grid(row=4,column=2)
    wins2.insert(0,player2_wins)

    inpu.delete(0,END)
    inp.delete(0,END)
    
def tkin():
    p1=inpu.get()
    p2=inp.get()
    p1wi=StringVar(root)
    p2wi=StringVar(root)
    drw=StringVar(root)

    p1wi.set("Player 1 Won")
    p2wi.set("Player 2 Won")
    drw.set("Draw")
    if p1==p2:
        lab2=Label(root, textvariable=drw)
        lab2.grid(row=4,column=1)
        return drw
                    
    elif p1=='r' and p2=='s':
        
        lab2=Label(root, textvariable = p1wi.get())
        lab2.grid(row=4,column=1)
        return p1wi
      
                   
    elif p1=='s' and p2=='p':
        lab2=Label(root, textvariable = p1wi)
        lab2.grid(row=4,column=1)
        return p1wi
        
    elif p1=='p' and p2=='r':
        lab2=Label(root, textvariable = p1wi)
        lab2.grid(row=4,column=1)
        return p1wi
        

    elif p1=='s' and p2=='r':
        lab2=Label(root, textvariable = p2wi)
        lab2.grid(row=4,column=1)
        return p2wi
        
    elif p1=='p' and p2=='s':
        lab2=Label(root, textvariable = p2wi)
        lab2.grid(row=4,column=1)
        return p2wi
        
    elif p1=='r' and p2=='p':
        lab2=Label(root, textvariable = p2wi)
        lab2.grid(row=4,column=1)
        return p2wi

def quitf():
    quit()
            
but=Button(root, text="Guess",command=r_p_s,width=10,height=2)
but.grid(row=3,column=1)

but2=Button(root,text="Quit",command=quitf)
but2.grid(row=7,column=2)

root.mainloop

