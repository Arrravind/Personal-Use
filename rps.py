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

player1_wins=0
player2_wins=0
draws=0

def r_p_s():
    p1=inpu.get()
    p2=inp.get()
    global player1_wins
    global player2_wins
    global draws

    
    if p1==p2:
        lab2=Label(root, text="Draw")
        lab2.grid(row=4,column=1)
        draws+=1
            
    elif p1=='r' and p2=='s':
        player1_wins+=1
        lab2=Label(root, text="Player 1 Won")
        lab2.grid(row=4,column=1)        
                   
    elif p1=='s' and p2=='p':
        lab2=Label(root, text="Player 1 Won")
        lab2.grid(row=4,column=1)
        player1_wins+=1
        
    elif p1=='p' and p2=='r':
        lab2=Label(root, text="Player 1 Won")
        lab2.grid(row=4,column=1)
        player1_wins+=1
        

    elif p1=='s' and p2=='r':
        lab2=Label(root, text="Player 2 Won")
        lab2.grid(row=4,column=1)
        player2_wins+=1
        
    elif p1=='p' and p2=='s':
        lab2=Label(root, text="Player 2 Won")
        lab2.grid(row=4,column=1)
        player2_wins+=1
        
    elif p1=='r' and p2=='p':
        lab2=Label(root, text="Player 2 Won")
        lab2.grid(row=4,column=1)
        player2_wins+=1
        
    wins1=Entry(root)
    wins1.grid(row=4,column=0)
    wins1.insert(0,player1_wins)

    wins2=Entry(root)
    wins2.grid(row=4,column=2)
    wins2.insert(0,player2_wins)

    draw=Entry(root)
    draw.grid(row=7,column=0)
    draw.insert(0,draws)

    inpu.delete(0,END)
    inp.delete(0,END)

def quitf():
    quit()

def endf():
    final=Entry(root,justify="center")
    final.grid(row=7,column=1)
    if player1_wins>player2_wins:
        final.insert(0,"Player 1 Wins The Game !!")
    elif player2_wins>player1_wins:
        final.insert(0,"Player 2 Wins The Game !!")
    else:
        final.insert(0,"Its a Tie")
    
    
    
            
but=Button(root, text="Guess",command=r_p_s,width=10,height=2)
but.grid(row=3,column=1)

but2=Button(root,text="Quit",command=quitf)
but2.grid(row=8,column=2)

but3=Button(root, text="End Game",command=endf)
but3.grid(row=8,column=1)

root.mainloop
